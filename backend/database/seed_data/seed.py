"""
Seed data functions for populating the database with course content.

This module contains functions to populate the database with initial quiz data
from the course data files (cx50.py, ea50.py, fa50.py, mc50.py). The data
is structured hierarchically:

    Course
      └── Unit
            └── Concept (Habit of Mind)
                  └── QuizCard (Question)
                        └── QuizAnswer (Answer options)

It is intended that populate_database() is called automatically by
create_database() in database.py when the database is empty, ensuring new
databases are automatically populated with quiz content.
"""
# Handle imports for both module import and direct execution
try:
    # Try relative imports first (when imported as module)
    from ..database import Course, Unit, Concept, QuizCard, QuizAnswer
    from .cx50 import CX50_DATA
    from .ea50 import EA50_DATA
    from .fa50 import FA50_DATA
    from .mc50 import MC50_DATA
except ImportError:
    # Fall back to absolute imports (when run from database directory)
    from database import Course, Unit, Concept, QuizCard, QuizAnswer
    from seed_data.cx50 import CX50_DATA
    from seed_data.ea50 import EA50_DATA
    from seed_data.fa50 import FA50_DATA
    from seed_data.mc50 import MC50_DATA


# Aggregate all course data for easy iteration
SEED_DATA = {
    'CX50': CX50_DATA,  # Complex Systems course
    'EA50': EA50_DATA,  # Empirical Analysis course
    'FA50': FA50_DATA,  # Formal Analysis course
    'MC50': MC50_DATA,  # Meaningful Communication course
}


def get_or_create(session, model, **filters):
    """
    Get an existing database record or create a new one if it doesn't exist.

    This is a common ORM pattern that makes database operations idempotent
    (safe to run multiple times). It checks if a record matching the given
    filters already exists in the database. If it exists, returns that record.
    If not, creates a new record with the filter values and returns it.

    Args:
        session: SQLAlchemy database session
        model: SQLAlchemy model class (e.g., Course, Unit, Concept)
        **filters: Keyword arguments used to filter/search for existing
                  records. These same arguments are used to create a new
                  record if none exists. Examples: title='CX50', course_id=1.

    Returns:
        SQLAlchemy model instance: Either the existing record or a newly
        created one. The new record is added to the session and flushed
        (saved to get its auto-generated ID).

    Example:
        # Get or create a course
        course = get_or_create(
            session, Course, title='CX50', description='...'
        )
        # If CX50 exists, returns it. Otherwise creates new one.
    """
    instance = session.query(model).filter_by(**filters).first()
    if not instance:
        instance = model(**filters)
        session.add(instance)
        # Flush to get auto-generated ID for foreign keys
        session.flush()
    return instance


def populate_database(session):
    """
    Populate the database with quiz data from the seed data files.

    This function iterates through the hierarchical data structure and creates
    database records for all courses, units, concepts, questions, and answers.
    It uses get_or_create() to ensure idempotency - running it multiple times
    won't create duplicate records.

    The function processes data in this order to maintain foreign key
    relationships:
    1. Courses (no dependencies)
    2. Units (depend on Courses)
    3. Concepts (depend on Units)
    4. QuizCards/Questions (depend on Concepts)
    5. QuizAnswers (depend on QuizCards)

    Args:
        session: SQLAlchemy database session. Must be an active session
                 that can be committed.

    Raises:
        SQLAlchemy exceptions: If database operations fail (e.g., constraint
                                violations, connection errors).

    Note:
        This function commits the session at the end. If called within a
        transaction, the caller should handle rollback on errors.
    """
    for course_data in SEED_DATA.values():
        # Create course (top-level, no dependencies)
        course = get_or_create(
            session, Course,
            title=course_data['title'],
            description=course_data['description']
        )

        # Create units for this course
        for unit_data in course_data['units']:
            unit = get_or_create(
                session, Unit,
                course_id=course.course_id,
                title=unit_data['title'],
                description=unit_data['description'],
                order_index=unit_data['order_index']
            )

            # Create concepts for this unit
            for concept_data in unit_data['concepts']:
                concept = get_or_create(
                    session, Concept,
                    unit_id=unit.unit_id,
                    title=concept_data['title'],
                    definition=concept_data['definition']
                )

                # Create questions for this concept
                for question_data in concept_data['questions']:
                    quiz_card = get_or_create(
                        session, QuizCard,
                        concept_id=concept.concept_id,
                        question=question_data['question']
                    )

                    # Create answer options for this question
                    for answer_data in question_data['answers']:
                        get_or_create(
                            session, QuizAnswer,
                            quiz_card_id=quiz_card.quiz_card_id,
                            answer_text=answer_data['text'],
                            is_correct=answer_data['correct'],
                            explanation=question_data['explanation']
                        )

    session.commit()
