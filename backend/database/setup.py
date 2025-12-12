"""
Database setup utilities for Gamify-HC
Configuration and database initialization functions with side effects
"""

import os
from typing import Optional, Union
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.database.models import (
    Base, Course, Unit, Concept, QuizCard, QuizAnswer
)
from backend.utils.logger import get_logger

logger = get_logger(__name__)


def _str_to_bool(value: Optional[str], default: bool = False) -> bool:
    """Convert common string representations to boolean values."""
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y"}


# PostgreSQL is required - no SQLite fallback
DEFAULT_DATABASE_URL = os.getenv("DATABASE_URL")
DEFAULT_SQLALCHEMY_ECHO = _str_to_bool(
    os.getenv("SQLALCHEMY_ECHO"),
    default=False,
)


def _resolve_database_url(database_url: Optional[str]) -> str:
    """Resolve the database URL.

    Prefers explicit arguments to environment defaults.
    Raises an error if no database URL is configured.
    """
    url = database_url or DEFAULT_DATABASE_URL
    if not url:
        raise ValueError(
            "DATABASE_URL environment variable is required. "
            "Start PostgreSQL with: docker compose up postgres -d\n"
            "Then set: DATABASE_URL=postgresql://"
            "gamify:gamify_secret@localhost:5432/gamify_hc"
        )
    return url


def _resolve_echo(echo: Union[bool, str, None]) -> bool:
    """Resolve SQLAlchemy's echo flag from parameters or environment."""
    if isinstance(echo, bool):
        return echo
    if isinstance(echo, str):
        return _str_to_bool(echo)
    return DEFAULT_SQLALCHEMY_ECHO


# ===============================
# DATABASE SETUP UTILITIES
# ===============================

def create_database(
    database_url: Optional[str] = None,
    echo: Union[bool, str, None] = None,
    auto_seed: bool = True,
):
    """
    Create the database engine and all tables.

    Args:
        database_url: Explicit database connection string. When omitted, the
            value of the ``DATABASE_URL`` environment variable is used.
            PostgreSQL is required.
        echo: Whether to log SQL statements. Accepts bools or truthy strings.
            When omitted, the ``SQLALCHEMY_ECHO`` environment variable is used.
        auto_seed: If True, automatically seed database with initial data if
            it's empty. Default: True.

    Returns:
        tuple: (engine, Session class)

    Raises:
        ValueError: If DATABASE_URL is not set.
    """
    database_url = _resolve_database_url(database_url)
    echo_flag = _resolve_echo(echo)
    
    # PostgreSQL connection pool configuration
    engine = create_engine(
        database_url,
        echo=echo_flag,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        pool_recycle=300,  # Recycle connections after 5 min
    )
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Auto-seed if database is empty
    if auto_seed:
        session = Session()
        try:
            # Check if database is empty (no courses)
            course_count = session.query(Course).count()
            if course_count == 0:
                logger.info("Database is empty. Seeding initial data...")
                # Import seed function - works as module or direct execution
                try:
                    # Relative import (works when imported as module)
                    from .seed_data.seed import populate_database
                except ImportError:
                    # Absolute import (works when run directly)
                    from seed_data.seed import populate_database
                populate_database(session)
                logger.info("Seeding complete!")
        except Exception as e:
            logger.error(f"Failed to seed database: {e}", exc_info=True)
            session.rollback()
        finally:
            session.close()

    return engine, Session


def get_session(database_url: Optional[str] = None):
    """
    Get a database session.

    Args:
        database_url: Optional database connection string overriding the
            ``DATABASE_URL`` environment value.

    Returns:
        Session instance

    Raises:
        ValueError: If DATABASE_URL is not set.
    """
    database_url = _resolve_database_url(database_url)
    echo_flag = _resolve_echo(None)
    
    engine = create_engine(
        database_url,
        echo=echo_flag,
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    # Create the database and tables
    logger.info("Creating database...")
    engine, Session = create_database()
    logger.info("Database created successfully!")

    # Display database content
    session = Session()
    try:
        # Summary statistics
        logger.info("=" * 80)
        logger.info("DATABASE SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Total Courses: {session.query(Course).count()}")
        logger.info(f"Total Units: {session.query(Unit).count()}")
        logger.info(f"Total Concepts: {session.query(Concept).count()}")
        logger.info(f"Total Quiz Cards: {session.query(QuizCard).count()}")
        logger.info(f"Total Answers: {session.query(QuizAnswer).count()}")
        logger.info("=" * 80)

        # Display all courses with their content
        courses = session.query(Course).order_by(Course.course_id).all()
        for course in courses:
            logger.info(f"\n{'=' * 80}")
            logger.info(f"COURSE: {course.title}")
            logger.info(f"Description: {course.description}")
            logger.info(f"Units: {len(course.units)}")
            logger.info(f"{'=' * 80}")

            # Display units
            for unit in sorted(course.units, key=lambda u: u.order_index or 0):
                logger.info(f"\n  UNIT {unit.order_index}: {unit.title}")
                logger.info(f"  Description: {unit.description}")
                logger.info(f"  Concepts: {len(unit.concepts)}")

                # Display concepts
                for concept in unit.concepts:
                    logger.info(f"\n    CONCEPT: {concept.title}")
                    logger.info(f"    Definition: {concept.definition}")
                    logger.info(f"    Questions: {len(concept.quiz_cards)}")

                    # Display quiz cards/questions
                    for quiz_card in concept.quiz_cards:
                        logger.info("\n      QUESTION:")
                        logger.info(f"      {quiz_card.question}")
                        logger.info(f"      Answers: {len(quiz_card.answers)}")

                        # Display answers
                        for answer in quiz_card.answers:
                            correct_marker = "✓" if answer.is_correct else " "
                            logger.info(
                                f"        [{correct_marker}] "
                                f"{answer.answer_text}"
                            )
                        if quiz_card.answers:
                            explanation = quiz_card.answers[0].explanation
                            if explanation:
                                logger.info(
                                    f"      Explanation: {explanation}"
                                )
                            else:
                                logger.info(
                                    "      Explanation: (none provided)"
                                )
                        else:
                            logger.info("      Explanation: N/A")

        logger.info(f"\n{'=' * 80}")
        logger.info("END OF DATABASE CONTENT")
        logger.info(f"{'=' * 80}\n")

    finally:
        session.close()
