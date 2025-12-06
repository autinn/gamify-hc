"""
Tests for database index usage.

This module verifies that indices are created and used in query execution
plans. Tests are based on common query patterns used in the application routes.
"""

import pytest
from sqlalchemy import text


class TestIndexExistence:
    """Tests to verify all expected indices exist in the database."""

    @pytest.fixture
    def expected_indices(self):
        """Define all expected indices."""
        return [
            ('units', 'idx_units_course'),
            ('concepts', 'idx_concepts_unit'),
            ('quiz_cards', 'idx_quiz_cards_concept'),
            ('quiz_cards', 'idx_quiz_cards_unit'),
            ('quiz_cards', 'idx_quiz_cards_course'),
            ('quiz_cards', 'idx_quiz_cards_unit_concept'),
            ('quiz_answers', 'idx_quiz_answers_quiz'),
            ('user_card', 'idx_user_card_user'),
            ('user_card', 'idx_user_card_quiz'),
        ]

    def test_all_indices_exist(self, db_session, expected_indices):
        """Verify all expected indices are created in the database."""
        for table_name, index_name in expected_indices:
            query = text("""
                SELECT name FROM sqlite_master
                WHERE type = 'index'
                AND tbl_name = :table_name
                AND name = :index_name
            """)
            result = db_session.execute(
                query,
                {"table_name": table_name, "index_name": index_name}
            )
            assert result.fetchone() is not None, (
                f"Index {index_name} should exist on table {table_name}"
            )


class TestIndexUsage:
    """Tests to verify indices are used in query execution plans."""

    @pytest.fixture
    def test_queries(self):
        """Define queries that should use specific indices."""
        return [
            {
                'name': 'user_card_by_user',
                'query': "SELECT * FROM user_card WHERE user_id = 1",
                'index': 'idx_user_card_user'
            },
            {
                'name': 'quiz_cards_by_concept',
                'query': "SELECT * FROM quiz_cards WHERE concept_id = 1",
                'index': 'idx_quiz_cards_concept'
            },
            {
                'name': 'concepts_by_unit',
                'query': "SELECT * FROM concepts WHERE unit_id = 1",
                'index': 'idx_concepts_unit'
            },
            {
                'name': 'units_by_course',
                'query': "SELECT * FROM units WHERE course_id = 1",
                'index': 'idx_units_course'
            },
            {
                'name': 'quiz_answers_by_quiz_card',
                'query': "SELECT * FROM quiz_answers WHERE quiz_card_id = 1",
                'index': 'idx_quiz_answers_quiz'
            },
            {
                'name': 'quiz_cards_by_unit',
                'query': "SELECT * FROM quiz_cards WHERE unit_id = 1",
                'index': 'idx_quiz_cards_unit'
            },
            {
                'name': 'quiz_cards_by_course',
                'query': "SELECT * FROM quiz_cards WHERE course_id = 1",
                'index': 'idx_quiz_cards_course'
            },
        ]

    def test_indices_used_in_queries(
        self, db_session, test_queries, populated_test_data
    ):
        """Verify each query uses its expected index."""
        for test_case in test_queries:
            explain_query = text(
                f"EXPLAIN QUERY PLAN {test_case['query']}"
            )
            result = db_session.execute(explain_query)

            # Collect all plan lines into a single string
            plan_lines = []
            for row in result:
                plan_str = ' '.join(str(cell) for cell in row)
                plan_lines.append(plan_str)

            # Check if index name appears in query plan
            plan_text = ' '.join(plan_lines).upper()
            expected_index = test_case['index'].upper()

            assert expected_index in plan_text, (
                f"Query '{test_case['name']}' should use "
                f"index '{test_case['index']}'. "
                f"Query plan: {plan_lines}"
            )
