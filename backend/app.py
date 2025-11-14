"""
Flask API for Gamify-HC
Simple REST API to connect React frontend with SQLAlchemy database
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.database.database import (
    Base, DEFAULT_DATABASE_URL,
    Course, Unit, Concept, QuizCard, QuizAnswer,
    User, UserCard
)
from datetime import datetime


def create_app(database_url=None):
    """Create and configure Flask app"""
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Setup database
    db_url = database_url or DEFAULT_DATABASE_URL
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    
    def get_db() -> Session:
        return SessionLocal()
    
    # ========================================
    # COURSE ENDPOINTS
    # ========================================
    
    @app.route('/api/courses', methods=['GET'])
    def get_courses():
        """Get all courses"""
        db = get_db()
        try:
            courses = db.query(Course).all()
            return jsonify([{
                'course_id': c.course_id,
                'title': c.title,
                'description': c.description
            } for c in courses])
        finally:
            db.close()
    
    @app.route('/api/courses/<int:course_id>', methods=['GET'])
    def get_course(course_id):
        """Get a specific course"""
        db = get_db()
        try:
            course = db.query(Course).filter(
                Course.course_id == course_id
            ).first()
            if not course:
                return jsonify({'error': 'Course not found'}), 404
            
            return jsonify({
                'course_id': course.course_id,
                'title': course.title,
                'description': course.description
            })
        finally:
            db.close()
    
    # ========================================
    # UNIT ENDPOINTS
    # ========================================
    
    @app.route('/api/courses/<int:course_id>/units', methods=['GET'])
    def get_course_units(course_id):
        """Get all units for a course"""
        db = get_db()
        try:
            units = db.query(Unit).filter(
                Unit.course_id == course_id
            ).order_by(Unit.order_index).all()
            
            return jsonify([{
                'unit_id': u.unit_id,
                'course_id': u.course_id,
                'title': u.title,
                'description': u.description,
                'order_index': u.order_index
            } for u in units])
        finally:
            db.close()
    
    @app.route('/api/units/<int:unit_id>', methods=['GET'])
    def get_unit(unit_id):
        """Get a specific unit"""
        db = get_db()
        try:
            unit = db.query(Unit).filter(Unit.unit_id == unit_id).first()
            if not unit:
                return jsonify({'error': 'Unit not found'}), 404
            
            return jsonify({
                'unit_id': unit.unit_id,
                'course_id': unit.course_id,
                'title': unit.title,
                'description': unit.description,
                'order_index': unit.order_index
            })
        finally:
            db.close()
    
    # ========================================
    # CONCEPT ENDPOINTS
    # ========================================
    
    @app.route('/api/units/<int:unit_id>/concepts', methods=['GET'])
    def get_unit_concepts(unit_id):
        """Get all concepts for a unit"""
        db = get_db()
        try:
            concepts = db.query(Concept).filter(
                Concept.unit_id == unit_id
            ).order_by(Concept.order_index).all()
            
            return jsonify([{
                'concept_id': c.concept_id,
                'unit_id': c.unit_id,
                'title': c.title,
                'description': c.description,
                'content': c.content,
                'order_index': c.order_index
            } for c in concepts])
        finally:
            db.close()
    
    @app.route('/api/concepts/<int:concept_id>', methods=['GET'])
    def get_concept(concept_id):
        """Get a specific concept with its quiz cards"""
        db = get_db()
        try:
            concept = db.query(Concept).filter(
                Concept.concept_id == concept_id
            ).first()
            if not concept:
                return jsonify({'error': 'Concept not found'}), 404
            
            # Get quiz cards for this concept
            quiz_cards = db.query(QuizCard).filter(
                QuizCard.concept_id == concept_id
            ).all()
            
            return jsonify({
                'concept_id': concept.concept_id,
                'unit_id': concept.unit_id,
                'title': concept.title,
                'description': concept.description,
                'content': concept.content,
                'order_index': concept.order_index,
                'quiz_cards': [{
                    'quiz_card_id': q.quiz_card_id,
                    'question': q.question
                } for q in quiz_cards]
            })
        finally:
            db.close()
    
    # ========================================
    # QUIZ CARD ENDPOINTS
    # ========================================
    
    @app.route('/api/quiz-cards/<int:quiz_card_id>', methods=['GET'])
    def get_quiz_card(quiz_card_id):
        """Get a quiz card with its answers"""
        db = get_db()
        try:
            quiz_card = db.query(QuizCard).filter(
                QuizCard.quiz_card_id == quiz_card_id
            ).first()
            if not quiz_card:
                return jsonify({'error': 'Quiz card not found'}), 404
            
            # Get answers
            answers = db.query(QuizAnswer).filter(
                QuizAnswer.quiz_card_id == quiz_card_id
            ).all()
            
            return jsonify({
                'quiz_card_id': quiz_card.quiz_card_id,
                'concept_id': quiz_card.concept_id,
                'question': quiz_card.question,
                'answers': [{
                    'answer_id': a.answer_id,
                    'answer_text': a.answer_text,
                    'is_correct': a.is_correct,
                    'explanation': a.explanation
                } for a in answers]
            })
        finally:
            db.close()
    
    @app.route('/api/concepts/<int:concept_id>/quiz-cards', methods=['GET'])
    def get_concept_quiz_cards(concept_id):
        """Get all quiz cards for a concept"""
        db = get_db()
        try:
            quiz_cards = db.query(QuizCard).filter(
                QuizCard.concept_id == concept_id
            ).all()
            
            result = []
            for q in quiz_cards:
                answers = db.query(QuizAnswer).filter(
                    QuizAnswer.quiz_card_id == q.quiz_card_id
                ).all()
                
                result.append({
                    'quiz_card_id': q.quiz_card_id,
                    'question': q.question,
                    'answers': [{
                        'answer_id': a.answer_id,
                        'answer_text': a.answer_text,
                        'is_correct': a.is_correct,
                        'explanation': a.explanation
                    } for a in answers]
                })
            
            return jsonify(result)
        finally:
            db.close()
    
    # ========================================
    # QUIZ SUBMISSION
    # ========================================
    
    @app.route('/api/quiz-submit', methods=['POST'])
    def submit_quiz_answer():
        """Submit a quiz answer"""
        db = get_db()
        try:
            data = request.get_json()
            
            user_id = data.get('user_id')
            quiz_card_id = data.get('quiz_card_id')
            answer_id = data.get('answer_id')
            
            if not all([user_id, quiz_card_id, answer_id]):
                return jsonify({'error': 'Missing required fields'}), 400
            
            # Check if answer is correct
            answer = db.query(QuizAnswer).filter(
                QuizAnswer.answer_id == answer_id
            ).first()
            
            if not answer:
                return jsonify({'error': 'Invalid answer_id'}), 400
            
            is_correct = answer.is_correct
            
            # Update or create UserCard
            user_card = db.query(UserCard).filter(
                UserCard.user_id == user_id,
                UserCard.quiz_card_id == quiz_card_id
            ).first()
            
            if user_card:
                # Update existing record
                user_card.times_seen = (user_card.times_seen or 0) + 1
                if is_correct:
                    user_card.times_correct = (
                        user_card.times_correct or 0
                    ) + 1
                user_card.last_seen = datetime.utcnow()
            else:
                # Create new record
                user_card = UserCard(
                    user_id=user_id,
                    quiz_card_id=quiz_card_id,
                    times_seen=1,
                    times_correct=1 if is_correct else 0,
                    last_seen=datetime.utcnow()
                )
                db.add(user_card)
            
            db.commit()
            
            return jsonify({
                'is_correct': is_correct,
                'explanation': answer.explanation,
                'times_seen': user_card.times_seen,
                'times_correct': user_card.times_correct
            })
        except Exception as e:
            db.rollback()
            return jsonify({'error': str(e)}), 500
        finally:
            db.close()
    
    # ========================================
    # USER ENDPOINTS
    # ========================================
    
    @app.route('/api/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        """Get user information"""
        db = get_db()
        try:
            user = db.query(User).filter(
                User.user_id == user_id
            ).first()
            if not user:
                return jsonify({'error': 'User not found'}), 404
            
            return jsonify({
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email,
                'created_at': user.created_at.isoformat() if user.created_at else None
            })
        finally:
            db.close()
    
    @app.route('/api/users/<int:user_id>/progress', methods=['GET'])
    def get_user_progress(user_id):
        """Get user's quiz card progress"""
        db = get_db()
        try:
            user_cards = db.query(UserCard).filter(
                UserCard.user_id == user_id
            ).all()
            
            return jsonify([{
                'quiz_card_id': uc.quiz_card_id,
                'times_seen': uc.times_seen,
                'times_correct': uc.times_correct,
                'last_seen': uc.last_seen.isoformat() if uc.last_seen else None
            } for uc in user_cards])
        finally:
            db.close()
    
    # ========================================
    # HEALTH CHECK
    # ========================================
    
    @app.route('/api/health', methods=['GET'])
    def health_check():
        """Check if API is running"""
        return jsonify({
            'status': 'ok',
            'message': 'Gamify-HC API is running'
        })
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
