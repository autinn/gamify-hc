#!/usr/bin/env python3
"""
Populate the database with test data for API testing
"""

from backend.database.setup import create_database
from backend.database.models import Course, Unit, Concept, QuizCard, QuizAnswer, User


def populate_test_data():
    """Add test data to the database"""
    print("Creating database and adding test data...")
    engine, Session = create_database()
    session = Session()
    
    try:
        # Clear existing data (optional)
        print("Clearing existing data...")
        session.query(QuizAnswer).delete()
        session.query(QuizCard).delete()
        session.query(Concept).delete()
        session.query(Unit).delete()
        session.query(Course).delete()
        session.query(User).delete()
        session.commit()
        
        # Create courses
        print("\nCreating courses...")
        course1 = Course(
            title="EA50 - Empirical Analyses",
            description="Empirical analysis and data-driven reasoning"
        )
        course2 = Course(
            title="FA50 - Formal Analyses",
            description="Logic, deduction, and formal reasoning"
        )
        session.add_all([course1, course2])
        session.commit()
        print(f"✅ Created courses: {course1.title}, {course2.title}")
        
        # Create units for EA50
        print("\nCreating units...")
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
        session.add_all([unit1, unit2, unit3])
        session.commit()
        print(f"✅ Created units: {unit1.title}, {unit2.title}, {unit3.title}")
        
        # Create concepts (HCs)
        print("\nCreating concepts (HCs)...")
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
        session.add_all([concept1, concept2, concept3, concept4])
        session.commit()
        print(f"✅ Created concepts: {concept1.title}, {concept2.title}, {concept3.title}, {concept4.title}")
        
        # Create quiz cards
        print("\nCreating quiz cards...")
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
        session.add_all([quiz1, quiz2, quiz3])
        session.commit()
        print(f"✅ Created quiz cards")
        
        # Create quiz answers
        print("\nCreating quiz answers...")
        answers = [
            # For quiz 1 (data viz)
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
                quiz_card_id=quiz1.quiz_card_id,
                answer_text="Scatter plot",
                is_correct=False,
                explanation="Scatter plots show relationships between two variables"
            ),
            # For quiz 2 (heuristics)
            QuizAnswer(
                quiz_card_id=quiz2.quiz_card_id,
                answer_text="Judging likelihood based on how easily examples come to mind",
                is_correct=True,
                explanation="The availability heuristic relies on immediate examples that come to mind"
            ),
            QuizAnswer(
                quiz_card_id=quiz2.quiz_card_id,
                answer_text="Always choosing the first option",
                is_correct=False,
                explanation="This describes a different bias"
            ),
            # For quiz 3 (deduction)
            QuizAnswer(
                quiz_card_id=quiz3.quiz_card_id,
                answer_text="All mammals have hearts. Dogs are mammals. Therefore, dogs have hearts.",
                is_correct=True,
                explanation="This is deductive reasoning from general to specific"
            ),
            QuizAnswer(
                quiz_card_id=quiz3.quiz_card_id,
                answer_text="I saw three black crows, so all crows must be black",
                is_correct=False,
                explanation="This is inductive reasoning, not deductive"
            ),
        ]
        session.add_all(answers)
        session.commit()
        print(f"✅ Created quiz answers")
        
        # Create a test user
        print("\nCreating test user...")
        user = User(
            username="test_user",
            email="test@example.com",
            password_hash="dummy_hash_for_testing"
        )
        session.add(user)
        session.commit()
        print(f"✅ Created user: {user.username}")
        
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
    populate_test_data()
