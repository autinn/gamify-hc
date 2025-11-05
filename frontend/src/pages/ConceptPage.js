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

  // Dummy data: Concepts with quiz cards and answers (aligned with DB schema)
  // Keyed by courseId-unitId-conceptId combination
  // Replace this with actual API call when backend is ready
  const conceptData = {
    'EA50-1-6': {
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
    'EA50-1-1': {
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

  // Get unit names for display in greeting
  const unitNames = {
    'EA50-1': 'Problem - Solving',
    'EA50-2': 'Problem Solving',
    'FA50-1': 'Analysis Techniques',
    'FA50-2': 'Pattern Recognition',
    'MC50-1': 'Metacognition Basics',
    'MC50-2': 'Self-Assessment',
    'CX50-1': 'User Experience',
    'CX50-2': 'Design Thinking',
  };

  const concept = conceptData[`${courseId}-${unitId}-${conceptId}`] || null;
  const unitName = unitNames[`${courseId}-${unitId}`] || 'Unit';

  // Handle quiz button click
  const handleStartQuiz = () => {
    navigate(`/course/${courseId}/unit/${unitId}/concept/${conceptId}/quiz`);
  };

  if (!concept) {
    return (
      <div className="concept-page">
        <div className="concept-page__header">
          <p className="concept-page__greeting">{`${courseId} - ${unitName}`}</p>
          <h1 className="concept-page__title">Concept Not Found</h1>
        </div>
      </div>
    );
  }

  return (
    <div className="concept-page">
      {/* Header Section */}
      <div className="concept-page__header">
        <p className="concept-page__greeting">{`${courseId} - ${unitName}`}</p>
        <div className="concept-page__header-row">
          <h1 className="concept-page__title">{concept.title}</h1>
          <div className="concept-page__button-container">
            <Button label="Start Quiz" variant="primary" onClick={handleStartQuiz} />
          </div>
        </div>
      </div>

      {/* Content Section */}
      <div className="concept-page__content">
        <QuestionAnswerBlocks quizCards={concept.quiz_cards} />
      </div>
    </div>
  );
};

export default ConceptPage;

