import React from 'react';
import { useParams } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import QuizAnswers from '../components/quiz/QuizAnswers';
import QuizQuestion from '../components/quiz/QuizQuestion';
import '../components/quiz/QuizAnswers.css';

/**
 * QuizPage - page wrapper for quizzes.
 * Supports contextual routes:
 *  - /quiz
 *  - /course/:courseId/quiz
 *  - /course/:courseId/unit/:unitId/quiz
 */
const QuizPage = () => {
	const { courseId, unitId } = useParams();

	const greeting = courseId ? `Quiz for ${courseId}` : 'Quiz';
	const title = unitId ? `Unit ${unitId}` : courseId ? courseId : 'Practice';


	return (
		<PageLayout
			greeting={greeting}
			title={title}
				showButton={false}
				leftContent={<QuizQuestion />}
				rightContent={<QuizAnswers />}
		/>
	);
};

export default QuizPage;
