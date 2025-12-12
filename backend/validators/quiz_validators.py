"""
Quiz Validators - Input validation for quiz operations
Validates quiz submissions and answer selections
"""

from backend.validators.auth_validators import ValidationError


def validate_quiz_submission(data: dict) -> None:
    """
    Validate quiz submission data.
    
    Rules:
    - quiz_card_id is required and must be an integer
    - answer_id is required and must be an integer
    - is_first_attempt is optional and must be a boolean
    
    Args:
        data: Quiz submission data dictionary
        
    Raises:
        ValidationError: If validation fails
        
    Example:
        >>> data = {
        ...     'quiz_card_id': 42,
        ...     'answer_id': 105,
        ...     'is_first_attempt': True
        ... }
        >>> validate_quiz_submission(data)  # OK
    """
    if not isinstance(data, dict):
        raise ValidationError('Request data must be a JSON object')
    
    # Validate quiz_card_id
    if 'quiz_card_id' not in data:
        raise ValidationError('Missing required field: quiz_card_id')
    
    if not isinstance(data['quiz_card_id'], int):
        raise ValidationError('quiz_card_id must be an integer')
    
    if data['quiz_card_id'] <= 0:
        raise ValidationError('quiz_card_id must be positive')
    
    # Validate answer_id
    if 'answer_id' not in data:
        raise ValidationError('Missing required field: answer_id')
    
    if not isinstance(data['answer_id'], int):
        raise ValidationError('answer_id must be an integer')
    
    if data['answer_id'] <= 0:
        raise ValidationError('answer_id must be positive')
    
    # Validate is_first_attempt (optional)
    if 'is_first_attempt' in data:
        if not isinstance(data['is_first_attempt'], bool):
            raise ValidationError('is_first_attempt must be a boolean')


def validate_positive_id(id_value: int, field_name: str = 'id') -> None:
    """
    Validate that an ID is a positive integer.
    
    Args:
        id_value: ID value to validate
        field_name: Name of the field (for error messages)
        
    Raises:
        ValidationError: If validation fails
        
    Example:
        >>> validate_positive_id(42, 'course_id')  # OK
        >>> validate_positive_id(-1, 'user_id')  # Raises ValidationError
    """
    if not isinstance(id_value, int):
        raise ValidationError(f'{field_name} must be an integer')
    
    if id_value <= 0:
        raise ValidationError(f'{field_name} must be positive')
