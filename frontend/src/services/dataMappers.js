/**
 * Data Mappers - Shared field mapping utilities for API transformations
 *
 * Transforms API response formats to component-expected data structures.
 * Centralizes field mappings to reduce duplication and improve maintainability.
 * API field names often differ from component conventions, so these mappers
 * provide a single source of truth for data shape conversions.
 *
 * @module dataMappers
 */

// ============================================================================
// COURSE MAPPERS
// ============================================================================

/**
 * Transforms individual course from API format to component format
 *
 * Maps API course fields to frontend naming conventions:
 * - id → course_id
 * - name/code → title (prefers 'name' with 'code' as fallback)
 *
 * @param {Object} course - Course object from API
 * @param {number} course.id - Course identifier
 * @param {string} [course.name] - Course name (preferred field)
 * @param {string} [course.code] - Course code (fallback if no name)
 * @param {string} course.description - Course description
 * @returns {Object} Mapped course object for components
 * @returns {number} result.course_id - Unique course identifier
 * @returns {string} result.title - Course display name
 * @returns {string} result.description - Course description
 *
 * @example
 * const apiCourse = { id: 1, name: 'CS 101', description: 'Intro to CS' };
 * const mappedCourse = mapCourseData(apiCourse);
 * // Returns: { course_id: 1, title: 'CS 101', description: 'Intro to CS' }
 */
export function mapCourseData(course) {
  return {
    course_id: course.id,
    title: course.name || course.code,
    description: course.description
  };
}

/**
 * Transforms array of courses from API format to component format
 *
 * @param {Array<Object>} courses - Array of course objects from API
 * @returns {Array<Object>} Array of mapped course objects
 *
 * @see mapCourseData
 */
export function mapCoursesArray(courses) {
  return courses.map(mapCourseData);
}

// ============================================================================
// UNIT MAPPERS
// ============================================================================

/**
 * Transforms individual unit from API format to component format
 *
 * Maps API unit fields to frontend naming conventions and preserves
 * hierarchical relationships:
 * - id → unit_id
 * - name → title
 * - Maintains course_id and order_index for navigation
 *
 * @param {Object} unit - Unit object from API
 * @param {number} unit.id - Unit identifier
 * @param {number} unit.course_id - Parent course identifier
 * @param {string} unit.name - Unit name
 * @param {string} unit.description - Unit description
 * @param {number} unit.order_index - Sequential position within course
 * @returns {Object} Mapped unit object for components
 * @returns {number} result.unit_id - Unique unit identifier
 * @returns {number} result.course_id - Parent course identifier
 * @returns {string} result.title - Unit display name
 * @returns {string} result.description - Unit description
 * @returns {number} result.order_index - Position in sequence
 */
export function mapUnitData(unit) {
  return {
    unit_id: unit.id,
    course_id: unit.course_id,
    title: unit.name,
    description: unit.description,
    order_index: unit.order_index
  };
}

/**
 * Transforms array of units from API format to component format
 *
 * @param {Array<Object>} units - Array of unit objects from API
 * @returns {Array<Object>} Array of mapped unit objects
 *
 * @see mapUnitData
 */
export function mapUnitsArray(units) {
  return units.map(mapUnitData);
}

// ============================================================================
// CONCEPT MAPPERS
// ============================================================================

/**
 * Transforms individual concept from API format to component format
 *
 * Maps API concept fields to frontend naming conventions:
 * - id → concept_id
 * - name/tag → title (prefers 'name' with 'tag' as fallback)
 * - Maintains unit relationship for hierarchy
 *
 * @param {Object} concept - Concept object from API
 * @param {number} concept.id - Concept identifier
 * @param {number} concept.unit_id - Parent unit identifier
 * @param {string} [concept.name] - Concept name (preferred field)
 * @param {string} [concept.tag] - Concept tag (fallback if no name)
 * @param {string} concept.definition - Concept definition
 * @returns {Object} Mapped concept object for components
 * @returns {number} result.concept_id - Unique concept identifier
 * @returns {number} result.unit_id - Parent unit identifier
 * @returns {string} result.title - Concept display name
 * @returns {string} result.definition - Concept definition
 */
export function mapConceptData(concept) {
  return {
    concept_id: concept.id,
    unit_id: concept.unit_id,
    title: concept.name || concept.tag,
    definition: concept.definition
  };
}

/**
 * Transforms array of concepts from API format to component format
 *
 * @param {Array<Object>} concepts - Array of concept objects from API
 * @returns {Array<Object>} Array of mapped concept objects
 *
 * @see mapConceptData
 */
export function mapConceptsArray(concepts) {
  return concepts.map(mapConceptData);
}

// ============================================================================
// QUIZ MAPPERS
// ============================================================================

/**
 * Transforms individual quiz answer from API format to component format
 *
 * Maps answer fields to component naming conventions:
 * - answer_text → text
 * - Preserves correctness marker and explanation for quiz logic
 *
 * @param {Object} answer - Answer object from API
 * @param {number} answer.id - Answer identifier
 * @param {string} answer.answer_text - Answer text content
 * @param {boolean} answer.is_correct - Whether this is the correct answer
 * @param {string} answer.explanation - Explanation shown after answer selection
 * @returns {Object} Mapped answer object for components
 * @returns {number} result.id - Answer identifier
 * @returns {string} result.text - Answer text
 * @returns {boolean} result.is_correct - Correctness flag
 * @returns {string} result.explanation - Answer explanation
 */
export function mapAnswerData(answer) {
  return {
    id: answer.id,
    text: answer.answer_text,
    is_correct: answer.is_correct,
    explanation: answer.explanation
  };
}

/**
 * Transforms quiz card from API format to component format
 *
 * Maps quiz card fields and recursively transforms nested answers
 * using mapAnswerData for consistent answer formatting:
 * - question → text
 * - answers → options (with each answer transformed)
 *
 * @param {Object} quizCard - Quiz card object from API
 * @param {number} quizCard.id - Quiz card identifier
 * @param {string} quizCard.question - Question text
 * @param {Array<Object>} quizCard.answers - Array of answer objects
 * @returns {Object} Mapped quiz card object for components
 * @returns {number} result.id - Quiz card identifier
 * @returns {string} result.text - Question text
 * @returns {Array<Object>} result.options - Mapped answer options
 *
 * @see mapAnswerData
 */
export function mapQuizCardData(quizCard) {
  return {
    id: quizCard.id,
    text: quizCard.question,
    options: quizCard.answers.map(mapAnswerData)
  };
}

/**
 * Transforms array of quiz cards from API format to component format
 *
 * @param {Array<Object>} quizCards - Array of quiz card objects from API
 * @returns {Array<Object>} Array of mapped quiz cards
 *
 * @see mapQuizCardData
 */
export function mapQuizCardsArray(quizCards) {
  return quizCards.map(mapQuizCardData);
}

/**
 * Transforms quiz card to concept page format with detailed answer structure
 *
 * Converts API format to component format specific to concept pages, which
 * display quiz metadata with full answer details. Differs from mapQuizCardData
 * by preserving all answer properties for concept-specific display needs:
 * - Stores quiz_card_id separately for concept relationship
 * - Renames answers to quiz_answers with detailed structure
 * - Includes answer_id for individual answer tracking
 *
 * @param {Object} quizCard - Quiz card object from API
 * @param {number} quizCard.id - Quiz card identifier
 * @param {number} quizCard.concept_id - Parent concept identifier
 * @param {string} quizCard.question - Question text
 * @param {Array<Object>} quizCard.answers - Array of answer objects
 * @returns {Object} Mapped quiz card in concept page format
 * @returns {number} result.quiz_card_id - Quiz card identifier
 * @returns {number} result.concept_id - Parent concept identifier
 * @returns {string} result.question - Question text
 * @returns {Array<Object>} result.quiz_answers - Detailed answer objects
 *
 * @example
 * const apiCard = { id: 1, concept_id: 5, question: 'What is X?', answers: [...] };
 * const mappedCard = mapQuizCardForConcept(apiCard);
 * // Returns with quiz_answers array containing all answer properties
 */
export function mapQuizCardForConcept(quizCard) {
  return {
    quiz_card_id: quizCard.id,
    concept_id: quizCard.concept_id,
    question: quizCard.question,
    // Preserve all answer details for concept page display requirements
    quiz_answers: quizCard.answers.map(a => ({
      answer_id: a.id,
      quiz_card_id: quizCard.id,
      answer_text: a.answer_text,
      is_correct: a.is_correct,
      explanation: a.explanation
    }))
  };
}

/**
 * Transforms array of quiz cards to concept page format
 *
 * @param {Array<Object>} quizCards - Array of quiz card objects from API
 * @returns {Array<Object>} Array of quiz cards in concept page format
 *
 * @see mapQuizCardForConcept
 */
export function mapQuizCardsArrayForConcept(quizCards) {
  return quizCards.map(mapQuizCardForConcept);
}
