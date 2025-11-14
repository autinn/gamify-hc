"""
Seed data package for populating the database with course content.
"""

from .seed import populate_database

# Export only populate_database - this is what database.py imports
# The course data files (CX50_DATA, etc.) are internal implementation details
__all__ = ['populate_database']
