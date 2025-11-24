/**
 * Data Mappers - Shared field mapping utilities
 * 
 * Transforms API responses to component-expected formats.
 * Centralized mapping functions reduce duplication across services.
 */

/**
 * Map course data from API to component format
 * API: {id, name/code, description}
 * Component: {course_id, title, description}
 */
export function mapCourseData(course) {
  return {
    course_id: course.id,
    title: course.name || course.code,
    description: course.description
  };
}

/**
 * Map array of courses
 */
export function mapCoursesArray(courses) {
  return courses.map(mapCourseData);
}

/**
 * Map unit data from API to component format
 * API: {id, name, course_id, description, order_index}
 * Component: {unit_id, course_id, title, description, order_index}
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
 * Map array of units
 */
export function mapUnitsArray(units) {
  return units.map(mapUnitData);
}

/**
 * Map concept data from API to component format
 * API: {id, name/tag, unit_id, definition}
 * Component: {concept_id, unit_id, title, definition}
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
 * Map array of concepts
 */
export function mapConceptsArray(concepts) {
  return concepts.map(mapConceptData);
}

/**
 * Map quiz card answer from API to component format
 * API: {id, answer_text, is_correct, explanation}
 * Component: {id, text, is_correct, explanation}
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
 * Map quiz card from API to component format
 * API: {id, question, answers: [{...}]}
 * Component: {id, text, options: [{...}]}
 */
export function mapQuizCardData(quizCard) {
  return {
    id: quizCard.id,
    text: quizCard.question,
    options: quizCard.answers.map(mapAnswerData)
  };
}

/**
 * Map array of quiz cards
 */
export function mapQuizCardsArray(quizCards) {
  return quizCards.map(mapQuizCardData);
}

/**
 * Format quiz card for storage/display in concept page format
 * API: {id, concept_id, question, answers}
 * Component: {quiz_card_id, concept_id, question, quiz_answers}
 */
export function mapQuizCardForConcept(quizCard) {
  return {
    quiz_card_id: quizCard.id,
    concept_id: quizCard.concept_id,
    question: quizCard.question,
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
 * Map array of quiz cards for concept format
 */
export function mapQuizCardsArrayForConcept(quizCards) {
  return quizCards.map(mapQuizCardForConcept);
}
