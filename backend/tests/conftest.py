"""
Pytest configuration and fixtures for backend tests

Uses testcontainers to automatically spin up a PostgreSQL container for testing.
No manual database setup required - just run pytest.
"""

import pytest
import sys
from pathlib import Path

from testcontainers.postgres import PostgresContainer

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from backend.app import create_app
from backend.database.setup import create_database
from backend.database.models import Base, Course, Unit, Concept, QuizCard, QuizAnswer, User


@pytest.fixture(scope='session')
def postgres_container():
    """Spin up a PostgreSQL container for the test session."""
    with PostgresContainer("postgres:16-alpine") as postgres:
        yield postgres


@pytest.fixture(scope='session')
def test_database_url(postgres_container):
    """Get connection URL from the container."""
    return postgres_container.get_connection_url()


@pytest.fixture(scope='session')
def test_engine(test_database_url):
    """Create a shared test database engine."""
    engine, _ = create_database(
        database_url=test_database_url,
        echo=False,
        auto_seed=False  # We'll seed manually in fixtures
    )
    yield engine
    engine.dispose()


@pytest.fixture(scope='session')
def test_session_factory(test_engine):
    """Create a session factory from the shared test engine."""
    from sqlalchemy.orm import sessionmaker
    return sessionmaker(bind=test_engine)


@pytest.fixture(scope='function')
def db_session(test_session_factory):
    """Create a test database session."""
    session = test_session_factory()
    yield session
    session.close()


@pytest.fixture(scope='function')
def clean_db(db_session):
    """Clean database before each test."""
    from backend.database.models import UserCard
    # Rollback any pending transactions
    db_session.rollback()
    # Delete in reverse order of dependencies
    db_session.query(QuizAnswer).delete()
    db_session.query(UserCard).delete()
    db_session.query(QuizCard).delete()
    db_session.query(Concept).delete()
    db_session.query(Unit).delete()
    db_session.query(Course).delete()
    db_session.query(User).delete()
    db_session.commit()
    yield db_session
    # Cleanup after test
    db_session.rollback()
    db_session.query(QuizAnswer).delete()
    db_session.query(UserCard).delete()
    db_session.query(QuizCard).delete()
    db_session.query(Concept).delete()
    db_session.query(Unit).delete()
    db_session.query(Course).delete()
    db_session.query(User).delete()
    db_session.commit()


@pytest.fixture
def test_client(test_engine, test_session_factory, test_database_url, monkeypatch):
    """Create a test Flask client with shared database engine."""
    from backend.utils.database_manager import DatabaseManager
    
    # Set DATABASE_URL environment variable for Settings to work
    monkeypatch.setenv("DATABASE_URL", test_database_url)
    monkeypatch.setenv("FLASK_ENV", "testing")
    
    # Create DatabaseManager with shared engine
    db_manager = DatabaseManager(
        engine=test_engine,
        SessionLocal=test_session_factory
    )
    
    # Create app with test database URL, disable auto_seed for tests
    app = create_app(database_url=test_database_url, auto_seed=False)
    # Replace the app's db_session with our shared one to ensure
    # all sessions use the same engine
    app.db_session = db_manager.get_session
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    
    # Ensure database tables exist
    Base.metadata.create_all(bind=test_engine)
    
    with app.test_client() as client:
        yield client


@pytest.fixture
def sample_course(clean_db):
    """Create a sample course for testing."""
    course = Course(
        title="EA50 - Empirical Analyses",
        description="Empirical analysis and data-driven reasoning"
    )
    clean_db.add(course)
    clean_db.commit()
    clean_db.refresh(course)
    return course


@pytest.fixture
def sample_unit(clean_db, sample_course):
    """Create a sample unit for testing."""
    unit = Unit(
        course_id=sample_course.course_id,
        title="Data Visualization",
        description="Understanding and creating effective visualizations",
        order_index=1
    )
    clean_db.add(unit)
    clean_db.commit()
    clean_db.refresh(unit)
    return unit


@pytest.fixture
def sample_concept(clean_db, sample_unit):
    """Create a sample concept for testing."""
    concept = Concept(
        unit_id=sample_unit.unit_id,
        title="#dataviz",
        definition="The practice of translating data into visual representations"
    )
    clean_db.add(concept)
    clean_db.commit()
    clean_db.refresh(concept)
    return concept


@pytest.fixture
def sample_quiz_card(clean_db, sample_concept, sample_unit, sample_course):
    """Create a sample quiz card for testing."""
    quiz_card = QuizCard(
        concept_id=sample_concept.concept_id,
        unit_id=sample_unit.unit_id,
        course_id=sample_course.course_id,
        question="Which visualization is best for showing proportions of a whole?"
    )
    clean_db.add(quiz_card)
    clean_db.commit()
    clean_db.refresh(quiz_card)
    return quiz_card


@pytest.fixture
def sample_quiz_answers(clean_db, sample_quiz_card):
    """Create sample quiz answers for testing."""
    answers = [
        QuizAnswer(
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_text="Pie chart",
            is_correct=True,
            explanation="Pie charts effectively show parts of a whole as percentages"
        ),
        QuizAnswer(
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_text="Line graph",
            is_correct=False,
            explanation="Line graphs are better for showing trends over time"
        ),
    ]
    clean_db.add_all(answers)
    clean_db.commit()
    return answers


@pytest.fixture
def sample_user(clean_db):
    """Create a sample user for testing."""
    from werkzeug.security import generate_password_hash
    user = User(
        username="test_user",
        email="test@minerva.edu",
        password_hash=generate_password_hash(
            "test_password", method='pbkdf2:sha256'
        )
    )
    clean_db.add(user)
    clean_db.commit()
    clean_db.refresh(user)
    return user


@pytest.fixture
def populated_test_data(clean_db):
    """Populate database with comprehensive test data."""
    # Create courses
    course1 = Course(
        title="EA50 - Empirical Analyses",
        description="Empirical analysis and data-driven reasoning"
    )
    course2 = Course(
        title="FA50 - Formal Analyses",
        description="Logic, deduction, and formal reasoning"
    )
    clean_db.add_all([course1, course2])
    clean_db.commit()
    clean_db.refresh(course1)
    clean_db.refresh(course2)
    
    # Create units
    unit1 = Unit(
        course_id=course1.course_id,
        title="Data Visualization",
        description="Understanding and creating effective visualizations",
        order_index=1
    )
    unit2 = Unit(
        course_id=course1.course_id,
        title="Heuristics & Biases",
        description="Cognitive shortcuts and common thinking errors",
        order_index=2
    )
    unit3 = Unit(
        course_id=course2.course_id,
        title="Logical Reasoning",
        description="Formal logic and valid arguments",
        order_index=1
    )
    clean_db.add_all([unit1, unit2, unit3])
    clean_db.commit()
    clean_db.refresh(unit1)
    clean_db.refresh(unit2)
    clean_db.refresh(unit3)
    
    # Create concepts
    concept1 = Concept(
        unit_id=unit1.unit_id,
        title="#dataviz",
        definition="The practice of translating data into visual representations"
    )
    concept2 = Concept(
        unit_id=unit1.unit_id,
        title="#systemmapping",
        definition="Creating visual representations of system components and relationships"
    )
    concept3 = Concept(
        unit_id=unit2.unit_id,
        title="#heuristics",
        definition="Mental shortcuts that simplify complex problem-solving"
    )
    concept4 = Concept(
        unit_id=unit3.unit_id,
        title="#deduction",
        definition="Drawing specific conclusions from general principles"
    )
    clean_db.add_all([concept1, concept2, concept3, concept4])
    clean_db.commit()
    clean_db.refresh(concept1)
    clean_db.refresh(concept2)
    clean_db.refresh(concept3)
    clean_db.refresh(concept4)
    
    # Create quiz cards
    quiz1 = QuizCard(
        concept_id=concept1.concept_id,
        unit_id=unit1.unit_id,
        course_id=course1.course_id,
        question="Which visualization is best for showing proportions of a whole?"
    )
    quiz2 = QuizCard(
        concept_id=concept3.concept_id,
        unit_id=unit2.unit_id,
        course_id=course1.course_id,
        question="What is the availability heuristic?"
    )
    quiz3 = QuizCard(
        concept_id=concept4.concept_id,
        unit_id=unit3.unit_id,
        course_id=course2.course_id,
        question="Which of the following is an example of deductive reasoning?"
    )
    clean_db.add_all([quiz1, quiz2, quiz3])
    clean_db.commit()
    clean_db.refresh(quiz1)
    clean_db.refresh(quiz2)
    clean_db.refresh(quiz3)
    
    # Create quiz answers
    answers = [
        QuizAnswer(
            quiz_card_id=quiz1.quiz_card_id,
            answer_text="Pie chart",
            is_correct=True,
            explanation="Pie charts effectively show parts of a whole as percentages"
        ),
        QuizAnswer(
            quiz_card_id=quiz1.quiz_card_id,
            answer_text="Line graph",
            is_correct=False,
            explanation="Line graphs are better for showing trends over time"
        ),
        QuizAnswer(
            quiz_card_id=quiz2.quiz_card_id,
            answer_text="Judging likelihood based on how easily examples come to mind",
            is_correct=True,
            explanation="The availability heuristic relies on immediate examples that come to mind"
        ),
        QuizAnswer(
            quiz_card_id=quiz3.quiz_card_id,
            answer_text="All mammals have hearts. Dogs are mammals. Therefore, dogs have hearts.",
            is_correct=True,
            explanation="This is deductive reasoning from general to specific"
        ),
    ]
    clean_db.add_all(answers)
    clean_db.commit()
    
    # Create test user
    from werkzeug.security import generate_password_hash
    user = User(
        username="populated_user",
        email="populated@minerva.edu",
        password_hash=generate_password_hash(
            "test_password", method='pbkdf2:sha256'
        )
    )
    clean_db.add(user)
    clean_db.commit()
    clean_db.refresh(user)
    
    return {
        'courses': [course1, course2],
        'units': [unit1, unit2, unit3],
        'concepts': [concept1, concept2, concept3, concept4],
        'quiz_cards': [quiz1, quiz2, quiz3],
        'answers': answers,
        'user': user
    }


@pytest.fixture
def auth_token(sample_user):
    """Create a JWT token for the sample user."""
    import jwt
    from datetime import datetime, timedelta
    
    payload = {
        'user_id': sample_user.user_id,
        'exp': datetime.utcnow() + timedelta(hours=24),
        'iat': datetime.utcnow()
    }
    return jwt.encode(
        payload,
        'dev-secret-key-change-in-production',
        algorithm='HS256'
    )


def create_auth_token(user_id):
    """Helper function to create a JWT token for a user."""
    import jwt
    from datetime import datetime, timedelta
    
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=24),
        'iat': datetime.utcnow()
    }
    return jwt.encode(
        payload,
        'dev-secret-key-change-in-production',
        algorithm='HS256'
    )
