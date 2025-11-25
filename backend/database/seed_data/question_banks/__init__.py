"""Question Banks Module
Centralized repository of HC-related MCQ items for all courses.
Each course module exports a dictionary of HC tags mapped to question lists.
"""

from .cx50 import CX50_HC_QUESTIONS
from .ea50 import EA50_HC_QUESTIONS
from .fa50 import FA50_HC_QUESTIONS
from .mc50 import MC50_HC_QUESTIONS

__all__ = [
    'CX50_HC_QUESTIONS',
    'EA50_HC_QUESTIONS',
    'FA50_HC_QUESTIONS',
    'MC50_HC_QUESTIONS',
]
