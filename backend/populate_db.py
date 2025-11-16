#!/usr/bin/env python3
"""
Populate the database with test data for API testing
This script uses the test fixtures from tests/fixtures.py
"""

from backend.database.setup import create_database
from backend.database.models import Course, Unit, Concept, QuizCard, QuizAnswer, User
from backend.tests.fixtures import populate_test_data


def main():
    """Main function to populate test database"""
    print("Creating database and adding test data...")
    engine, Session = create_database()
    session = Session()
    
    try:
        result = populate_test_data(session)
        
        # Summary
        print("\n" + "="*60)
        print("DATABASE POPULATED SUCCESSFULLY!")
        print("="*60)
        print(f"Courses: {session.query(Course).count()}")
        print(f"Units: {session.query(Unit).count()}")
        print(f"Concepts (HCs): {session.query(Concept).count()}")
        print(f"Quiz Cards: {session.query(QuizCard).count()}")
        print(f"Quiz Answers: {session.query(QuizAnswer).count()}")
        print(f"Users: {session.query(User).count()}")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == '__main__':
    main()
