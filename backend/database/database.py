"""
SQLAlchemy Database Models for Gamify-HC
Implements the database schema defined in backend_database.sql
"""

from datetime import datetime
import os
from pathlib import Path
from typing import Optional, Union
from sqlalchemy import (
    Boolean, CheckConstraint, Column, DateTime, Float, ForeignKey,
    Integer, Text, create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


def _str_to_bool(value: Optional[str], default: bool = False) -> bool:
    """Convert common string representations to boolean values."""
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y"}


_DATABASE_DIR = Path(__file__).resolve().parent
_DEFAULT_SQLITE_PATH = _DATABASE_DIR / "test.db"
DEFAULT_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{_DEFAULT_SQLITE_PATH}"
)
DEFAULT_SQLALCHEMY_ECHO = _str_to_bool(
    os.getenv("SQLALCHEMY_ECHO"),
    default=False,
)


def _resolve_database_url(database_url: Optional[str]) -> str:
    """Resolve the database URL.

    Prefers explicit arguments to environment defaults.
    """
    return database_url or DEFAULT_DATABASE_URL


def _resolve_echo(echo: Union[bool, str, None]) -> bool:
    """Resolve SQLAlchemy's echo flag from parameters or environment."""
    if isinstance(echo, bool):
        return echo
    if isinstance(echo, str):
        return _str_to_bool(echo)
    return DEFAULT_SQLALCHEMY_ECHO


# ===============================
# 1. CONTENT TABLES (Courses, Units, Habits of Mind)
# ===============================

class Course(Base):
    """A course is a collection of units."""
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text, nullable=False)
    description = Column(Text)

    # Relationships
    units = relationship(
        'Unit', back_populates='course', cascade='all, delete-orphan'
    )

    # Constraints
    __table_args__ = (
        CheckConstraint(
            'length(title) > 0', name='check_title_length'
        ),
        CheckConstraint(
            'length(description) > 0', name='check_description_length'
        ),
    )

    def __repr__(self):
        return (f"<Course(course_id={self.course_id}, "
                f"title='{self.title}')>")


class Unit(Base):
    """A unit is a collection of concepts."""
    __tablename__ = 'units'

    unit_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(
        Integer,
        ForeignKey('courses.course_id', ondelete='CASCADE'),
        nullable=False
    )
    title = Column(Text, nullable=False)
    description = Column(Text)
    order_index = Column(Integer)

    # Relationships
    course = relationship('Course', back_populates='units')
    concepts = relationship(
        'Concept', back_populates='unit', cascade='all, delete-orphan'
    )

    # Constraints
    __table_args__ = (
        CheckConstraint(
            'length(title) > 0', name='check_title_length'
        ),
        CheckConstraint(
            'length(description) > 0', name='check_description_length'
        ),
        CheckConstraint(
            'order_index >= 0', name='check_order_index_non_negative'
        ),
    )

    def __repr__(self):
        return (f"<Unit(unit_id={self.unit_id}, "
                f"title='{self.title}')>")


class Concept(Base):
    """A concept is an HC. Terminology was borrowed from frontend team."""
    __tablename__ = 'concepts'

    concept_id = Column(Integer, primary_key=True, autoincrement=True)
    unit_id = Column(
        Integer,
        ForeignKey('units.unit_id', ondelete='CASCADE'),
        nullable=False
    )
    title = Column(Text, nullable=False)
    definition = Column(Text)

    # Relationships
    unit = relationship('Unit', back_populates='concepts')
    quiz_cards = relationship(
        'QuizCard', back_populates='concept', cascade='all, delete-orphan'
    )

    # Constraints
    __table_args__ = (
        CheckConstraint(
            'length(title) > 0', name='check_title_length'
        ),
        CheckConstraint(
            'length(definition) > 0', name='check_definition_length'
        ),
    )

    def __repr__(self):
        return (f"<Concept(concept_id={self.concept_id}, "
                f"title='{self.title}')>")


# ===============================
# 2. LEARNING TABLES (Quizzes)
# ===============================

class QuizCard(Base):
    """Each concept has a set of quiz cards associated with it."""
    __tablename__ = 'quiz_cards'

    quiz_card_id = Column(Integer, primary_key=True, autoincrement=True)
    concept_id = Column(
        Integer,
        ForeignKey('concepts.concept_id', ondelete='CASCADE'),
        nullable=False
    )
    question = Column(Text, nullable=False)

    # Relationships
    concept = relationship('Concept', back_populates='quiz_cards')
    answers = relationship(
        'QuizAnswer',
        back_populates='quiz_card',
        cascade='all, delete-orphan'
    )
    user_cards = relationship(
        'UserCard',
        back_populates='quiz_card',
        cascade='all, delete-orphan'
    )

    # Constraints
    __table_args__ = (
        CheckConstraint(
            'length(question) > 0', name='check_question_length'
        ),
    )

    def __repr__(self):
        question_preview = self.question[:50]
        return (f"<QuizCard(quiz_card_id={self.quiz_card_id}, "
                f"question='{question_preview}...')>")


class QuizAnswer(Base):
    """
    A quiz card has a question, a topic concept, an arbitrary number
    of answers, arbitrary number of explanations, and correct answer(s).
    """
    __tablename__ = 'quiz_answers'

    # Unique across all answers
    answer_id = Column(Integer, primary_key=True, autoincrement=True)
    # Links to quiz card
    quiz_card_id = Column(
        Integer,
        ForeignKey('quiz_cards.quiz_card_id', ondelete='CASCADE'),
        nullable=False
    )
    answer_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    explanation = Column(Text, nullable=False)

    # Relationships
    quiz_card = relationship('QuizCard', back_populates='answers')

    # Constraints
    __table_args__ = (
        CheckConstraint(
            'length(answer_text) > 0', name='check_answer_text_length'
        ),
        CheckConstraint(
            'length(explanation) > 0', name='check_explanation_length'
        ),
    )

    def __repr__(self):
        return (f"<QuizAnswer(answer_id={self.answer_id}, "
                f"is_correct={self.is_correct})>")


# ===============================
# 3. USER TABLES
# ===============================

class User(Base):
    """
    User implementation, has major security flaws, but is a good
    starting point for the MVP.
    """
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Text, unique=True, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user_cards = relationship(
        'UserCard', back_populates='user', cascade='all, delete-orphan'
    )

    # Constraints
    __table_args__ = (
        CheckConstraint(
            'length(username) >= 3 AND length(username) <= 50',
            name='check_username_length'
        ),
        CheckConstraint(
            "email LIKE '%_@_%._%'",
            name='check_email_format'
        ),
        CheckConstraint(
            'length(password_hash) >= 60',
            name='check_password_hash_length'
        ),
    )

    def __repr__(self):
        return (f"<User(user_id={self.user_id}, "
                f"username='{self.username}')>")


class UserCard(Base):
    """
    Keeps track of user's aptitude for any given quiz card.
    Uses user_id and quiz_card_id as composite primary key.
    """
    __tablename__ = 'user_card'

    # Composite primary key: user_id and quiz_card_id
    user_id = Column(
        Integer,
        ForeignKey('users.user_id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False
    )
    quiz_card_id = Column(
        Integer,
        ForeignKey('quiz_cards.quiz_card_id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False
    )
    ease_factor = Column(Float, default=2.5)
    interval_days = Column(Integer, default=0)
    due_date = Column(DateTime)
    last_reviewed = Column(DateTime)
    repetitions = Column(Integer, default=0)
    success_count = Column(Integer, default=0)
    failure_count = Column(Integer, default=0)

    # Relationships
    user = relationship('User', back_populates='user_cards')
    quiz_card = relationship('QuizCard', back_populates='user_cards')

    # Constraints
    __table_args__ = (
        CheckConstraint(
            'ease_factor >= 1.3 AND ease_factor <= 3.0',
            name='check_ease_factor_range'
        ),
        CheckConstraint(
            'interval_days >= 0',
            name='check_interval_days_non_negative'
        ),
        CheckConstraint(
            'repetitions >= 0',
            name='check_repetitions_non_negative'
        ),
        CheckConstraint(
            'success_count >= 0',
            name='check_success_count_non_negative'
        ),
        CheckConstraint(
            'failure_count >= 0',
            name='check_failure_count_non_negative'
        ),
    )

    @property
    def success_rate(self) -> float:
        """Return the success rate derived from success and failure counts."""
        total_reviews = self.success_count + self.failure_count
        return self.success_count / total_reviews if total_reviews else 0.0

    def __repr__(self):
        return (f"<UserCard(user_id={self.user_id}, "
                f"quiz_card_id={self.quiz_card_id}, "
                f"ease_factor={self.ease_factor}, "
                f"successes={self.success_count}, "
                f"failures={self.failure_count})>")


# ===============================
# DATABASE SETUP UTILITIES
# ===============================

def create_database(
    database_url: Optional[str] = None,
    echo: Union[bool, str, None] = None,
):
    """
    Create the database engine and all tables.

    Args:
        database_url: Explicit database connection string. When omitted, the
            value of the ``DATABASE_URL`` environment variable is used, falling
            back to a bundled SQLite file.
        echo: Whether to log SQL statements. Accepts bools or truthy strings.
            When omitted, the ``SQLALCHEMY_ECHO`` environment variable is used.

    Returns:
        tuple: (engine, Session class)
    """
    database_url = _resolve_database_url(database_url)
    echo_flag = _resolve_echo(echo)
    engine = create_engine(database_url, echo=echo_flag)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return engine, Session


def get_session(database_url: Optional[str] = None):
    """
    Get a database session.

    Args:
        database_url: Optional database connection string overriding the
            ``DATABASE_URL`` environment value.

    Returns:
        Session instance
    """
    database_url = _resolve_database_url(database_url)
    echo_flag = _resolve_echo(None)
    engine = create_engine(database_url, echo=echo_flag)
    Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    # Create the database and tables
    print("Creating database...")
    engine, Session = create_database()
    print("Database created successfully!")

    # Example usage
    session = Session()

    # Create a sample course
    course = Course(
        title="Introduction to Habits of Mind",
        description="Learn the fundamental habits of mind"
    )
    session.add(course)
    session.commit()

    print(f"Created sample course: {course}")
    session.close()
