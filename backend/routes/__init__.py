"""
Backend routes package

Contains Flask blueprints for modular API structure organized by domain:
- courses: Course management endpoints
- units: Unit endpoints (units contain Habits & Foundational Concepts)
- concepts: HC (Habits & Foundational Concepts) endpoints
- quiz: Quiz card and answer submission endpoints
- users: User profile and progress endpoints

Each blueprint follows separation of concerns:
- Route handlers: HTTP request/response logic
- Serialization: Data transformation (model → JSON)
- Error handling: Consistent error responses
"""
