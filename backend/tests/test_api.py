"""
Pytest tests for API endpoints
"""

import pytest
import json


class TestHealthEndpoint:
    """Tests for health check endpoint"""
    
    def test_health_check(self, test_client):
        """Test health check endpoint"""
        response = test_client.get('/api/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'ok'
        assert 'message' in data


class TestCourseEndpoints:
    """Tests for course-related endpoints"""
    
    def test_get_courses(self, test_client, populated_test_data):
        """Test getting all courses"""
        response = test_client.get('/api/courses')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) >= 2
        
        # Check structure
        course = data[0]
        assert 'id' in course
        assert 'code' in course
        assert 'name' in course
        assert 'description' in course
    
    def test_get_course_by_id(self, test_client, populated_test_data):
        """Test getting a specific course"""
        course_id = populated_test_data['courses'][0].course_id
        response = test_client.get(f'/api/courses/{course_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == course_id
        assert 'code' in data
        assert 'name' in data
        assert 'description' in data
    
    def test_get_course_units(self, test_client, populated_test_data):
        """Test getting units for a course"""
        course_id = populated_test_data['courses'][0].course_id
        response = test_client.get(f'/api/courses/{course_id}/units')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) >= 2
        
        # Check structure
        unit = data[0]
        assert 'id' in unit
        assert 'course_id' in unit
        assert 'name' in unit
        assert 'description' in unit
        assert 'order_index' in unit


class TestUnitEndpoints:
    """Tests for unit-related endpoints"""
    
    def test_get_unit_by_id(self, test_client, populated_test_data):
        """Test getting a specific unit"""
        unit_id = populated_test_data['units'][0].unit_id
        response = test_client.get(f'/api/units/{unit_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == unit_id
        assert 'course_id' in data
        assert 'name' in data
        assert 'description' in data
    
    def test_get_unit_concepts(self, test_client, populated_test_data):
        """Test getting concepts for a unit"""
        unit_id = populated_test_data['units'][0].unit_id
        response = test_client.get(f'/api/units/{unit_id}/concepts')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        
        if len(data) > 0:
            concept = data[0]
            assert 'id' in concept
            assert 'unit_id' in concept
            assert 'name' in concept
            assert 'definition' in concept


class TestConceptEndpoints:
    """Tests for concept endpoints"""
    
    def test_get_concept_by_id(self, test_client, populated_test_data):
        """Test getting a specific concept"""
        concept_id = populated_test_data['concepts'][0].concept_id
        response = test_client.get(f'/api/concepts/{concept_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == concept_id
        assert 'unit_id' in data
        assert 'name' in data
        assert 'definition' in data
    
    def test_get_concept_quiz_cards(self, test_client, populated_test_data):
        """Test getting quiz cards for a concept"""
        concept_id = populated_test_data['concepts'][0].concept_id
        response = test_client.get(f'/api/concepts/{concept_id}/quiz-cards')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        
        if len(data) > 0:
            quiz = data[0]
            assert 'id' in quiz
            assert 'concept_id' in quiz
            assert 'question' in quiz
            assert 'answers' in quiz


class TestQuizEndpoints:
    """Tests for quiz-related endpoints"""
    
    def test_get_quiz_card(self, test_client, populated_test_data, sample_quiz_answers):
        """Test getting a quiz card with answers"""
        quiz_card_id = populated_test_data['quiz_cards'][0].quiz_card_id
        response = test_client.get(f'/api/quiz-cards/{quiz_card_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == quiz_card_id
        assert 'concept_id' in data
        assert 'question' in data
        assert 'answers' in data
        assert isinstance(data['answers'], list)
        assert len(data['answers']) > 0
        
        # Check answer structure
        answer = data['answers'][0]
        assert 'id' in answer
        assert 'answer_text' in answer
        assert 'is_correct' in answer
    
    def test_submit_quiz_answer(self, test_client, populated_test_data, sample_quiz_answers):
        """Test submitting a quiz answer"""
        user = populated_test_data['user']
        quiz_card = populated_test_data['quiz_cards'][0]
        answer = sample_quiz_answers[0]
        
        response = test_client.post(
            '/api/quiz-submit',
            json={
                'user_id': user.user_id,
                'quiz_card_id': quiz_card.quiz_card_id,
                'answer_id': answer.answer_id
            }
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'is_correct' in data
        assert 'explanation' in data


class TestUserEndpoints:
    """Tests for user-related endpoints"""
    
    def test_get_user_by_id(self, test_client, populated_test_data):
        """Test getting a specific user"""
        user_id = populated_test_data['user'].user_id
        response = test_client.get(f'/api/users/{user_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['user_id'] == user_id
        assert 'username' in data
        assert 'email' in data
    
    def test_get_user_progress(self, test_client, populated_test_data):
        """Test getting user progress"""
        user_id = populated_test_data['user'].user_id
        response = test_client.get(f'/api/users/{user_id}/progress')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)

