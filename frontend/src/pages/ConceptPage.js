import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Button from '../components/common/UI/Button';
import QuestionAnswerBlocks from '../components/concept/QuestionAnswerBlocks';
import './ConceptPage.css';

/**
 * ConceptPage - Concept details page with quiz cards (questions and answers)
 *
 * Displays concept name, quiz questions and answers.
 * Uses URL parameters :courseId, :unitId, and :conceptId to determine which concept to display.
 * Uses PageLayout for consistent two-column structure.
 */
const ConceptPage = () => {
  const { courseId, unitId, conceptId } = useParams();
  const navigate = useNavigate();
  const courseIdInt = parseInt(courseId, 10);
  const unitIdInt = parseInt(unitId, 10);
  const conceptIdInt = parseInt(conceptId, 10);

  // Dummy data: Concepts with quiz cards and answers (aligned with DB schema)
  // Keyed by concept_id (int)
  // Replace this with actual API call when backend is ready
  const conceptData = {
    6: { // concept_id: 6
      concept_id: 6,
      unit_id: 1,
      title: '#heuristics',
      definition: 'Mental shortcuts for problem-solving',
      quiz_cards: [
        {
          quiz_card_id: 1,
          concept_id: 6,
          question: 'What are heuristics?',
          quiz_answers: [
            {
              answer_id: 1,
              quiz_card_id: 1,
              answer_text: 'Heuristics are mental shortcuts or rules of thumb that help people make decisions and solve problems quickly and efficiently, often when dealing with incomplete information or complex situations.',
              is_correct: true,
              explanation: 'Heuristics help simplify decision-making processes by reducing the cognitive load required to process information.'
            },
            {
              answer_id: 2,
              quiz_card_id: 1,
              answer_text: 'Complex algorithms that require extensive computation',
              is_correct: false,
              explanation: 'Heuristics are actually simple mental shortcuts, not complex algorithms.'
            }
          ]
        },
        {
          quiz_card_id: 2,
          concept_id: 6,
          question: 'When should you use heuristics in problem-solving?',
          quiz_answers: [
            {
              answer_id: 3,
              quiz_card_id: 2,
              answer_text: 'When you need to make quick decisions with limited information, or when the cost of a perfect solution is too high compared to a good-enough solution.',
              is_correct: true,
              explanation: 'Heuristics are most valuable when time or resources are limited, and a satisfactory solution is acceptable.'
            },
            {
              answer_id: 4,
              quiz_card_id: 2,
              answer_text: 'Only when you have complete information about all variables',
              is_correct: false,
              explanation: 'Heuristics are specifically designed for situations with incomplete information.'
            }
          ]
        },
        {
          quiz_card_id: 3,
          concept_id: 6,
          question: 'What is a potential limitation of using heuristics?',
          quiz_answers: [
            {
              answer_id: 5,
              quiz_card_id: 3,
              answer_text: 'Heuristics can lead to cognitive biases and systematic errors, as they prioritize speed and efficiency over accuracy.',
              is_correct: true,
              explanation: 'While heuristics are useful, they can introduce biases like confirmation bias, availability heuristic, or anchoring bias.'
            }
          ]
        }
      ]
    },
    1: { // concept_id: 1
      concept_id: 1,
      unit_id: 1,
      title: '#rightproblem',
      definition: 'Identifying the correct problem to solve',
      quiz_cards: [
        {
          quiz_card_id: 4,
          concept_id: 1,
          question: 'Why is it important to identify the right problem?',
          quiz_answers: [
            {
              answer_id: 6,
              quiz_card_id: 4,
              answer_text: 'Solving the wrong problem wastes time and resources, while solving the right problem addresses the root cause and creates meaningful impact.',
              is_correct: true,
              explanation: 'Problem identification is critical because it determines the direction and effectiveness of all subsequent problem-solving efforts.'
            }
          ]
        }
      ]
    }
    // Add more concepts as needed
  };

  // Dummy data: Courses (aligned with DB schema)
  // Schema: course_id (int, PK), title (varchar), description (varchar)
  const courses = {
    1: { course_id: 1, title: 'EA50', description: 'Problem Solving and Analysis' },
    2: { course_id: 2, title: 'FA50', description: 'Fundamental Analysis' },
    3: { course_id: 3, title: 'MC50', description: 'Metacognition and Critical Thinking' },
    4: { course_id: 4, title: 'CX50', description: 'Complex Systems and Design' },
  };

  // Get unit names for display in greeting (aligned with DB schema)
  const units = {
    1: { unit_id: 1, course_id: 1, title: 'Scientific Method', description: 'Introduction to scientific methodology', order_index: 1 },
    2: { unit_id: 2, course_id: 1, title: 'Problem Solving', description: 'Problem-solving techniques and heuristics', order_index: 2 },
    3: { unit_id: 3, course_id: 2, title: 'Analysis Techniques', description: 'Methods for data analysis', order_index: 1 },
    4: { unit_id: 4, course_id: 2, title: 'Pattern Recognition', description: 'Identifying patterns in data', order_index: 2 },
    5: { unit_id: 5, course_id: 3, title: 'Metacognition Basics', description: 'Understanding thinking about thinking', order_index: 1 },
    6: { unit_id: 6, course_id: 3, title: 'Self-Assessment', description: 'Evaluating your own understanding', order_index: 2 },
    7: { unit_id: 7, course_id: 4, title: 'User Experience', description: 'Designing for user needs', order_index: 1 },
    8: { unit_id: 8, course_id: 4, title: 'Design Thinking', description: 'Creative problem-solving approach', order_index: 2 },
  };

  const concept = conceptData[conceptIdInt] || null;
  const course = courses[courseIdInt] || null;
  const unit = units[unitIdInt] || null;

  // Build greeting with course and unit names
  const greeting = course && unit 
    ? `${course.title} - ${unit.title}`
    : course 
    ? `${course.title} - Unit ${unitId}`
    : unit 
    ? `${courseId} - ${unit.title}`
    : `${courseId} - Unit ${unitId}`;

  // Handle quiz button click
  const handleStartQuiz = () => {
    navigate(`/course/${courseId}/unit/${unitId}/concept/${conceptId}/quiz`);
  };

  if (!concept) {
    return (
      <div className="concept-page">
        <div className="concept-page__header">
          <p className="concept-page__greeting">{greeting}</p>
          <h1 className="concept-page__title">Concept Not Found</h1>
        </div>
      </div>
    );
  }

  return (
    <div className="concept-page">
      {/* Header Section */}
      <div className="concept-page__header">
        <p className="concept-page__greeting">{greeting}</p>
        <div className="concept-page__header-row">
          <h1 className="concept-page__title">{concept.title}</h1>
          <div className="concept-page__button-container">
            <Button label="Start Quiz" variant="primary" onClick={handleStartQuiz} />
          </div>
        </div>
        {concept.definition && (
          <p className="concept-page__definition">{concept.definition}</p>
        )}
      </div>

      {/* Content Section */}
      <div className="concept-page__content">
        <QuestionAnswerBlocks quizCards={concept.quiz_cards} />
      </div>
    </div>
  );
};

export default ConceptPage;

