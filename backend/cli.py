"""
Admin CLI tool for Gamify-HC.

Implements 12-Factor App Factor XII: Admin Processes.
Run administrative tasks as one-off processes, separate from the web app.

Usage:
    python -m backend.cli seed          # Seed database with course data
    python -m backend.cli create-user   # Create a new user
    python -m backend.cli reset-db      # Reset database (danger!)
    python -m backend.cli db-info       # Display database info
"""

import sys

import click
from sqlalchemy import text

from backend.config.settings import get_settings
from backend.database.models import (
    Base,
    Course,
    Unit,
    Concept,
    QuizCard,
    QuizAnswer,
    User,
)
from backend.database.seed_data.seed import populate_database
from backend.database.setup import create_database
from backend.utils.logger import get_logger

logger = get_logger(__name__)


@click.group()
def cli():
    """
    Gamify-HC Admin CLI Tool.
    
    Administrative commands for database management, user creation,
    and other operational tasks.
    """
    pass


@cli.command()
@click.option(
    '--force',
    is_flag=True,
    help='Force re-seeding even if data exists'
)
def seed(force):
    """
    Seed database with course data.
    
    Populates the database with initial courses, units, concepts,
    and quiz cards from the seed data files.
    """
    try:
        settings = get_settings()
        logger.info(f"Connecting to database: {settings.DATABASE_URL}")
        
        engine, Session = create_database(auto_seed=False)
        session = Session()
        
        try:
            # Check if database already has data
            course_count = session.query(Course).count()
            
            if course_count > 0 and not force:
                logger.warning(
                    f"Database already contains {course_count} courses. "
                    f"Use --force to re-seed."
                )
                click.echo(
                    f"⚠️  Database already has {course_count} courses. "
                    f"Use --force to re-seed."
                )
                sys.exit(1)
            
            if force and course_count > 0:
                logger.warning("Force flag set. Clearing existing data...")
                click.echo("🗑️  Clearing existing course data...")
                
                # Delete in reverse dependency order
                session.query(QuizAnswer).delete()
                session.query(QuizCard).delete()
                session.query(Concept).delete()
                session.query(Unit).delete()
                session.query(Course).delete()
                session.commit()
            
            logger.info("Seeding database...")
            click.echo("🌱 Seeding database with course data...")
            
            populate_database(session)
            
            # Get counts
            courses = session.query(Course).count()
            units = session.query(Unit).count()
            concepts = session.query(Concept).count()
            quiz_cards = session.query(QuizCard).count()
            answers = session.query(QuizAnswer).count()
            
            logger.info(
                f"Seeding complete: {courses} courses, {units} units, "
                f"{concepts} concepts, {quiz_cards} quiz cards, "
                f"{answers} answers"
            )
            
            click.echo("✅ Database seeded successfully!")
            click.echo(f"   📚 Courses: {courses}")
            click.echo(f"   📖 Units: {units}")
            click.echo(f"   💡 Concepts: {concepts}")
            click.echo(f"   ❓ Quiz Cards: {quiz_cards}")
            click.echo(f"   ✏️  Answers: {answers}")
            
        except Exception as e:
            session.rollback()
            logger.error(f"Seeding failed: {e}", exc_info=True)
            click.echo(f"❌ Error: {e}", err=True)
            sys.exit(1)
        finally:
            session.close()
            
    except Exception as e:
        logger.error(f"Database connection failed: {e}", exc_info=True)
        click.echo(f"❌ Database connection failed: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--username', prompt=True, help='Username for login')
@click.option('--email', prompt=True, help='User email address')
@click.option(
    '--password',
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
    help='User password'
)
def create_user(username, email, password):
    """
    Create a new user account.
    
    Prompts for username, email, and password.
    Useful for creating test accounts or admin users.
    """
    try:
        settings = get_settings()
        logger.info("Creating new user...")
        
        engine, Session = create_database(auto_seed=False)
        session = Session()
        
        try:
            # Check if user already exists
            existing_user = (
                session.query(User)
                .filter(
                    (User.username == username) | (User.email == email)
                )
                .first()
            )
            
            if existing_user:
                if existing_user.username == username:
                    click.echo(
                        f"❌ Error: Username '{username}' already exists",
                        err=True
                    )
                else:
                    click.echo(
                        f"❌ Error: Email '{email}' already exists",
                        err=True
                    )
                sys.exit(1)
            
            # Create new user
            from werkzeug.security import generate_password_hash
            
            new_user = User(
                username=username,
                email=email,
                password_hash=generate_password_hash(password)
            )
            
            session.add(new_user)
            session.commit()
            
            logger.info(
                f"User created: {username} (ID: {new_user.user_id})"
            )
            click.echo(f"✅ User created successfully!")
            click.echo(f"   👤 Username: {username}")
            click.echo(f"   📧 Email: {email}")
            click.echo(f"   🆔 User ID: {new_user.user_id}")
            
        except Exception as e:
            session.rollback()
            logger.error(f"User creation failed: {e}", exc_info=True)
            click.echo(f"❌ Error creating user: {e}", err=True)
            sys.exit(1)
        finally:
            session.close()
            
    except Exception as e:
        logger.error(f"Database connection failed: {e}", exc_info=True)
        click.echo(f"❌ Database connection failed: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.confirmation_option(
    prompt='⚠️  This will DELETE ALL DATA! Are you sure?'
)
def reset_db():
    """
    Reset database (DROP and recreate all tables).
    
    ⚠️  DANGER: This deletes ALL data including users and progress!
    Use with caution. Requires confirmation.
    """
    try:
        logger.warning("RESETTING DATABASE - ALL DATA WILL BE LOST")
        click.echo("🗑️  Resetting database...")
        
        engine, Session = create_database(auto_seed=False)
        
        # Drop all tables
        click.echo("   Dropping all tables...")
        Base.metadata.drop_all(engine)
        
        # Recreate all tables
        click.echo("   Creating fresh tables...")
        Base.metadata.create_all(engine)
        
        logger.info("Database reset complete")
        click.echo("✅ Database reset successfully!")
        click.echo("   Run 'python -m backend.cli seed' to populate data")
        
    except Exception as e:
        logger.error(f"Database reset failed: {e}", exc_info=True)
        click.echo(f"❌ Error resetting database: {e}", err=True)
        sys.exit(1)


@cli.command()
def db_info():
    """
    Display database information and statistics.
    
    Shows table counts, connection info, and database health.
    """
    try:
        settings = get_settings()
        
        click.echo("=" * 60)
        click.echo("📊 DATABASE INFORMATION")
        click.echo("=" * 60)
        click.echo(f"Environment: {settings.FLASK_ENV}")
        click.echo(f"Database URL: {settings.DATABASE_URL}")
        click.echo()
        
        engine, Session = create_database(auto_seed=False)
        session = Session()
        
        try:
            # Get counts
            courses = session.query(Course).count()
            units = session.query(Unit).count()
            concepts = session.query(Concept).count()
            quiz_cards = session.query(QuizCard).count()
            answers = session.query(QuizAnswer).count()
            users = session.query(User).count()
            
            click.echo("📈 TABLE STATISTICS:")
            click.echo(f"   📚 Courses: {courses}")
            click.echo(f"   📖 Units: {units}")
            click.echo(f"   💡 Concepts: {concepts}")
            click.echo(f"   ❓ Quiz Cards: {quiz_cards}")
            click.echo(f"   ✏️  Answers: {answers}")
            click.echo(f"   👥 Users: {users}")
            click.echo()
            
            # Test database connectivity
            click.echo("🔌 DATABASE HEALTH:")
            result = session.execute(text("SELECT version()"))
            version = result.scalar()
            click.echo("   ✅ Connection: OK")
            click.echo(f"   🗄️  PostgreSQL: {version.split(',')[0]}")
            
            click.echo("=" * 60)
            
        except Exception as e:
            logger.error(f"Failed to get database info: {e}", exc_info=True)
            click.echo(f"❌ Error: {e}", err=True)
            sys.exit(1)
        finally:
            session.close()
            
    except Exception as e:
        logger.error(f"Database connection failed: {e}", exc_info=True)
        click.echo(f"❌ Database connection failed: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    cli()
