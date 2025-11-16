"""
Pytest configuration and fixtures for backend tests
"""

import pytest
import os
import sys
import tempfile
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from backend.app import create_app
from backend.database.setup import create_database
from backend.database.models import Course, Unit, Concept, QuizCard, QuizAnswer, User
from sqlalchemy.orm import Session


@pytest.fixture(scope='session')
def test_database_url():
    """Create a temporary test database URL"""
    # Use in-memory SQLite for faster tests
    return "sqlite:///:memory:"


@pytest.fixture(scope='session')
def db_session(test_database_url):
    """Create a test database session"""
    engine, Session = create_database(
        database_url=test_database_url,
        echo=False,
        auto_seed=False  # We'll seed manually in fixtures
    )
    session = Session()
    yield session
    session.close()


@pytest.fixture(scope='function')
def clean_db(db_session):
    """Clean database before each test"""
    # Delete in reverse order of dependencies
    db_session.query(QuizAnswer).delete()
    db_session.query(QuizCard).delete()
    db_session.query(Concept).delete()
    db_session.query(Unit).delete()
    db_session.query(Course).delete()
    db_session.query(User).delete()
    db_session.commit()
    yield db_session
    # Cleanup after test
    db_session.query(QuizAnswer).delete()
    db_session.query(QuizCard).delete()
    db_session.query(Concept).delete()
    db_session.query(Unit).delete()
    db_session.query(Course).delete()
    db_session.query(User).delete()
    db_session.commit()


@pytest.fixture
def test_client(test_database_url):
    """Create a test Flask client"""
    app = create_app(database_url=test_database_url)
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    with app.test_client() as client:
        yield client


@pytest.fixture
def sample_course(clean_db):
    """Create a sample course for testing"""
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
    """Create a sample unit for testing"""
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
    """Create a sample concept for testing"""
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
def sample_quiz_card(clean_db, sample_concept):
    """Create a sample quiz card for testing"""
    quiz_card = QuizCard(
        concept_id=sample_concept.concept_id,
        question="Which visualization is best for showing proportions of a whole?"
    )
    clean_db.add(quiz_card)
    clean_db.commit()
    clean_db.refresh(quiz_card)
    return quiz_card


@pytest.fixture
def sample_quiz_answers(clean_db, sample_quiz_card):
    """Create sample quiz answers for testing"""
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
    """Create a sample user for testing"""
    user = User(
        username="test_user",
        email="test@example.com",
        password_hash="dummy_hash_for_testing"
    )
    clean_db.add(user)
    clean_db.commit()
    clean_db.refresh(user)
    return user


@pytest.fixture
def populated_test_data(clean_db):
    """Populate database with comprehensive test data"""
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
        question="Which visualization is best for showing proportions of a whole?"
    )
    quiz2 = QuizCard(
        concept_id=concept3.concept_id,
        question="What is the availability heuristic?"
    )
    quiz3 = QuizCard(
        concept_id=concept4.concept_id,
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
    user = User(
        username="test_user",
        email="test@example.com",
        password_hash="dummy_hash_for_testing"
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

