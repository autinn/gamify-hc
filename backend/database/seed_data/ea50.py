"""
EA50 Course Seed Data
Unit 1: Problem Solving
"""

EA50_DATA = {
    'title': 'EA50',
    'description': 'EA50 Course',
    'units': [
        {
            'title': 'Problem Solving',
            'description': 'EA50 Unit 1',
            'order_index': 0,
            'concepts': [
                {
                    'title': '#rightproblem',
                    'definition': 'Characterize a complex problem in detail to really understand it.',
                    'questions': [
                        {
                            'question': 'A city proposes "add more buses" to cut congestion without describing current traffic flows or success metrics. What\'s missing?',
                            'answers': [
                                {'text': 'Goal state', 'correct': False, 'explanation': 'Goal state is not enough; we need to know the initial state and how we\'ll measure success.'},
                                {'text': 'Initial state and measurement plan', 'correct': True, 'explanation': 'Exactly right! We need to understand the current situation and how we\'ll measure improvement.'},
                                {'text': 'Scale only', 'correct': False, 'explanation': 'Focusing on scale ignores the need for a clear initial state and success metrics.'},
                                {'text': 'Nothing—solution first is fine', 'correct': False, 'explanation': 'Jumping to solutions can be premature without understanding the problem fully.'},
                            ],
                        },
                        {
                            'question': 'Which goal state avoids presupposing a solution?',
                            'answers': [
                                {'text': 'Ban cars downtown', 'correct': False, 'explanation': 'This presupposes a solution (banning cars) rather than describing a goal state.'},
                                {'text': 'Achieve average bus wait time ≤ 7 minutes by Q4', 'correct': True, 'explanation': 'This is a clear goal state focused on outcomes, not specific solutions.'},
                                {'text': 'Build a new subway line', 'correct': False, 'explanation': 'This suggests a specific solution (new subway line) instead of a goal state.'},
                                {'text': 'Switch traffic lights to adaptive control', 'correct': False, 'explanation': 'This is another solution presupposition; the goal state should be outcome-based.'},
                            ],
                        },
                        {
                            'question': 'You listed initial state, goal state, obstacles, and scale, but not likely consequences if nothing changes. What should you add?',
                            'answers': [
                                {'text': 'Constraint list', 'correct': False, 'explanation': 'Constraints are already considered; we need to think about future implications.'},
                                {'text': 'Future implications of the problem', 'correct': True, 'explanation': 'Yes, understanding the future impact of the problem is crucial for robust characterization.'},
                                {'text': 'Budget section only', 'correct': False, 'explanation': 'The budget is part of the constraints; we need to focus on future implications of the problem itself.'},
                                {'text': 'SWOT table', 'correct': False, 'explanation': 'A SWOT analysis is not specifically about the future consequences of the problem.'},
                            ],
                        },
                    ]
                },
                {
                    'title': '#analogies',
                    'definition': 'Use analogies in problem solving appropriately.',
                    'questions': [
                        {
                            'question': 'A team adapts airport "hub-and-spoke" logistics to design a school meal distribution network. What step is essential?',
                            'answers': [
                                {'text': 'Copy all procedures verbatim', 'correct': False, 'explanation': 'Verbatim copying ignores the need to adapt to the new context.'},
                                {'text': 'Ignore domain differences', 'correct': False, 'explanation': 'Domain differences are crucial; ignoring them can lead to failure.'},
                                {'text': 'Map deep structural similarities and differences', 'correct': True, 'explanation': 'Exactly! Mapping similarities and differences ensures appropriate adaptations.'},
                                {'text': 'Focus on catchy metaphors', 'correct': False, 'explanation': 'Catchy metaphors are not enough; we need a deep understanding of structural elements.'},
                            ],
                        },
                        {
                            'question': 'When is #analogies preferred over #gapanalysis?',
                            'answers': [
                                {'text': 'Same domain with minor tweaks', 'correct': False, 'explanation': 'In-domain tweaks are gap analysis territory; analogies suit cross-domain situations.'},
                                {'text': 'No same-domain fit; a cross-domain template matches structure', 'correct': True, 'explanation': 'Right! Analogies are great when a cross-domain template fits the structure of the problem.'},
                                {'text': 'When constraints are already fixed', 'correct': False, 'explanation': 'Fixed constraints don\'t determine the use of analogies vs. gap analysis.'},
                                {'text': 'When time allows exhaustive trials', 'correct': False, 'explanation': 'Exhaustive trials are not related to the choice between analogies and gap analysis.'},
                            ],
                        },
                        {
                            'question': 'Which is an idiosyncratic feature to discard when translating a source solution?',
                            'answers': [
                                {'text': 'Core mechanism', 'correct': False, 'explanation': 'The core mechanism is usually central to the solution and not idiosyncratic.'},
                                {'text': 'Domain-specific regulation irrelevant to target', 'correct': True, 'explanation': 'Exactly! Irrelevant domain-specific regulations should be discarded in the translation.'},
                                {'text': 'Structural mapping', 'correct': False, 'explanation': 'Structural mapping is essential to understand how the solution fits the new context.'},
                                {'text': 'Performance criterion', 'correct': False, 'explanation': 'The performance criterion is important to determine if the solution is effective.'},
                            ],
                        },
                    ]
                },
                {
                    'title': '#constraints',
                    'definition': 'Identify and apply constraint satisfaction as a way to solve problems.',
                    'questions': [
                        {
                            'question': 'Budget is fixed this quarter. How should you treat it?',
                            'answers': [
                                {'text': 'Constraint', 'correct': True, 'explanation': 'Correct! A fixed budget is a constraint that limits options.'},
                                {'text': 'Obstacle', 'correct': False, 'explanation': 'An obstacle is something that prevents progress, but a constraint is a limit we work within.'},
                                {'text': 'Neither', 'correct': False, 'explanation': 'It is both a constraint and an obstacle; calling it neither ignores its impact.'},
                                {'text': 'Both—depends on mood', 'correct': False, 'explanation': 'Constraints and obstacles are not subjective; they have objective characteristics.'},
                            ],
                        },
                        {
                            'question': 'Which action demonstrates constraint satisfaction?',
                            'answers': [
                                {'text': 'Brainstorming without limits', 'correct': False, 'explanation': 'This ignores constraints; brainstorming with constraints can spur creativity.'},
                                {'text': 'Selecting a schedule that fits room capacity, instructor availability, and time windows', 'correct': True, 'explanation': 'Yes! This action satisfies multiple constraints simultaneously.'},
                                {'text': 'Expanding scope until a solution appears', 'correct': False, 'explanation': 'This may ignore constraints and lead to unfeasible solutions.'},
                                {'text': 'Copying a competitor\'s plan', 'correct': False, 'explanation': 'Copying ignores the unique constraints and context of your own situation.'},
                            ],
                        },
                        {
                            'question': 'You misclassified a reparable equipment failure as a constraint. What\'s the fix?',
                            'answers': [
                                {'text': 'Keep it a constraint', 'correct': False, 'explanation': 'If it can be repaired, it\'s not a constraint; it\'s an obstacle that can be overcome.'},
                                {'text': 'Reframe as an obstacle and plan remediation', 'correct': True, 'explanation': 'Exactly! Treat it as an obstacle that can be addressed with a solution.'},
                                {'text': 'Remove it entirely', 'correct': False, 'explanation': 'It shouldn\'t be removed; it needs to be addressed as an obstacle.'},
                                {'text': 'Treat it as a success metric', 'correct': False, 'explanation': 'It\'s not a success metric; it\'s an issue that needs to be fixed.'},
                            ],
                        },
                    ]
                },
                {
                    'title': '#heuristics',
                    'definition': 'Identify when to use heuristics and when to avoid them.',
                    'questions': [
                        {
                            'question': 'When are fast-and-frugal heuristics most appropriate?',
                            'answers': [
                                {'text': 'High stakes, abundant data', 'correct': False, 'explanation': 'High stakes with abundant data call for careful analysis, not heuristics.'},
                                {'text': 'Low stakes, limited time/information', 'correct': True, 'explanation': 'Correct! Heuristics are great when stakes are low and time or information is limited.'},
                                {'text': 'Anytime—they\'re always best', 'correct': False, 'explanation': 'Heuristics are not always best; they\'re useful in specific situations, like under uncertainty.'},
                                {'text': 'Never—use full analysis only', 'correct': False, 'explanation': 'This is too rigid; heuristics can be very useful in the right circumstances.'},
                            ],
                            
                        },
                        {
                            'question': 'Which sequence describes means-ends analysis?',
                            'answers': [
                                {'text': 'Guess and check repeatedly', 'correct': False, 'explanation': 'Means-ends analysis is systematic, not based on guessing.'},
                                {'text': 'Start at goal, step backward once', 'correct': False, 'explanation': 'Means-ends analysis involves iterative refinement, not a single backward step.'},
                                {'text': 'Identify initial/goal states, set subgoals to reduce the gap, iterate', 'correct': True, 'explanation': 'Exactly! This sequence captures the iterative nature of means-ends analysis.'},
                                {'text': 'Randomized trial selection', 'correct': False, 'explanation': 'Means-ends analysis is not about random trials; it\'s a focused, iterative process.'},
                            ],
                        
                        },
                        {
                            'question': 'Which risk matches the availability heuristic?',
                            'answers': [
                                {'text': 'Overweight vivid recent events when estimating likelihoods', 'correct': True, 'explanation': 'Correct! The availability heuristic leads us to overemphasize recent or vivid events.'},
                                {'text': 'Confuse similarity with probability', 'correct': False, 'explanation': 'This is more related to the representativeness heuristic, not the availability heuristic.'},
                                {'text': 'Anchor on a starting number only', 'correct': False, 'explanation': 'Anchoring is a separate cognitive bias; this option doesn\'t match the availability heuristic.'},
                                {'text': 'Use affectless calculation', 'correct': False, 'explanation': 'The availability heuristic is not about calculation; it\'s about how easily examples come to mind.'},
                            ],
                            
                        },
                    ]
                },
                {
                    'title': '#scienceoflearning',
                    'definition': 'Evaluate and use effective strategies to learn or teach specific types of material.',
                    'questions': [
                        {
                            'question': 'You design flashcards with images and words and quiz yourself over days. Which principles are you using?',
                            'answers': [
                                {'text': 'Dual codes and spaced practice', 'correct': True, 'explanation': 'Yes! Using both images and words engages dual coding, and quizzing over days is spaced practice.'},
                                {'text': 'Highlighting and massed practice', 'correct': False, 'explanation': 'Highlighting is not as effective, and massed practice is the opposite of spaced practice.'},
                                {'text': 'Emotion and rote repetition', 'correct': False, 'explanation': 'These are not the principles being used; the focus is on dual coding and spacing.'},
                                {'text': 'Interference and cramming', 'correct': False, 'explanation': 'These are detrimental to learning; the principles used are beneficial.'},
                            ],
                            
                        },
                        {
                            'question': 'Which statement best applies rereading effectively?',
                            'answers': [
                                {'text': 'Immediate rereads are always superior', 'correct': False, 'explanation': 'Immediate rereads can reinforce mistakes; delayed rereads with a goal are better.'},
                                {'text': 'Reread after a delay with a specific goal', 'correct': True, 'explanation': 'Exactly! This approach enhances understanding and retention.'},
                                {'text': 'Never reread', 'correct': False, 'explanation': 'Rereading can be beneficial if done correctly, with a focus on understanding.'},
                                {'text': 'Reread only captions', 'correct': False, 'explanation': 'This is too limited; the entire material may need to be reread for better understanding.'},
                            ],
                            
                        },
                        {
                            'question': 'Which pairing matches Kosslyn\'s Maxims?',
                            'answers': [
                                {'text': 'Think it Through → retrieval cues; Make and Use Associations → deep processing', 'correct': False, 'explanation': 'This is incorrect; the maxims emphasize different aspects.'},
                                {'text': 'Think it Through → deep processing; Make and Use Associations → rich retrieval cues', 'correct': True, 'explanation': 'Correct! This pairing reflects the focus of each maxim.'},
                                {'text': 'Think it Through → dual codes only; Make and Use Associations → spacing only', 'correct': False, 'explanation': 'This is too narrow; the maxims encompass broader principles.'},
                                {'text': 'Both maxims → massed practice', 'correct': False, 'explanation': 'Massed practice is not aligned with the principles of these maxims.'},
                            ],
                            
                        },
                    ]
                },
                {
                    'title': '#breakitdown',
                    'definition': 'Organize problems into tractable components and design solutions.',
                    'questions': [
                        {
                            'question': 'Which illustrates an iterative breakdown?',
                            'answers': [
                                {'text': 'List problems once', 'correct': False, 'explanation': 'Listing problems once is a start, but iterative breakdown involves refining and detailing.'},
                                {'text': '\'Pollution\' → \'air pollution\' → \'PM2.5 from diesel buses\' and tackle the last', 'correct': True, 'explanation': 'Exactly! This shows iterative refinement leading to a specific, actionable subproblem.'},
                                {'text': 'Jump straight to a solution', 'correct': False, 'explanation': 'Jumping to a solution skips the important step of understanding and breaking down the problem.'},
                                {'text': 'Define constraints only', 'correct': False, 'explanation': 'Defining constraints is part of the process, but doesn\'t replace the need to break down the problem.'},
                            ],
                            
                        },
                        {
                            'question': 'Which tool best visualizes subproblems and their categories?',
                            'answers': [
                                {'text': 'Fishbone/Ishikawa diagram', 'correct': True, 'explanation': 'Yes! Fishbone diagrams are excellent for visualizing causes and subproblems by category.'},
                                {'text': 'Gantt chart only', 'correct': False, 'explanation': 'Gantt charts are for scheduling, not for visualizing problem breakdowns.'},
                                {'text': 'Confusion matrix', 'correct': False, 'explanation': 'Confusion matrices are used for evaluating classification models, not for problem breakdowns.'},
                                {'text': 'ROC curve', 'correct': False, 'explanation': 'ROC curves are used for diagnostic test evaluation, not for visualizing problem components.'},
                            ],
                            
                        },
                        {
                            'question': 'What\'s a common pitfall when breaking problems down?',
                            'answers': [
                                {'text': 'Selecting tractable subproblems', 'correct': False, 'explanation': 'Selecting tractable subproblems is essential; this is not a pitfall.'},
                                {'text': 'Explaining links between subproblems', 'correct': False, 'explanation': 'Explaining links is important for understanding the problem as a whole.'},
                                {'text': 'Mislabeling a fixed constraint as a subproblem', 'correct': True, 'explanation': 'Exactly! This confuses the problem-solving process and should be avoided.'},
                                {'text': 'Using evidence to prioritize', 'correct': False, 'explanation': 'Using evidence is crucial for effective problem solving and prioritization.'},
                            ],
                            
                        },
                    ]
                },
                {
                    'title': '#gapanalysis',
                    'definition': 'Identify and evaluate whether there are suitable existing solutions to a problem or whether a creative new solution is required.',
                    'questions': [
                        {
                            'question': 'Your team finds an existing tool that meets requirements with minor configuration. What\'s the correct conclusion?',
                            'answers': [
                                {'text': 'Build a novel solution anyway', 'correct': False, 'explanation': 'If an existing tool works with minor changes, it\'s efficient to use it rather than building a new solution.'},
                                {'text': 'Use the existing tool and document justification', 'correct': True, 'explanation': 'Yes! This is a practical approach that saves time and resources.'},
                                {'text': 'Switch to analogies', 'correct': False, 'explanation': 'Switching to analogies is unnecessary and could complicate the solution.'},
                                {'text': 'Ignore constraints', 'correct': False, 'explanation': 'Constraints are important to consider; ignoring them could lead to problems later.'},
                            ],
                            
                        },
                        {
                            'question': 'Which is required for a solid gap analysis?',
                            'answers': [
                                {'text': 'Listing one familiar option', 'correct': False, 'explanation': 'One option is not enough; multiple solutions should be evaluated.'},
                                {'text': 'Deep evaluation of multiple existing solutions against requirements/constraints', 'correct': True, 'explanation': 'Exactly! This thorough evaluation is key to effective gap analysis.'},
                                {'text': 'Brainstorming new ideas only', 'correct': False, 'explanation': 'Gap analysis focuses on evaluating existing solutions, not just brainstorming new ones.'},
                                {'text': 'Assuming gaps exist', 'correct': False, 'explanation': 'Assumptions should be based on evidence; gaps should be identified through analysis.'},
                            ],
                            
                        },
                        {
                            'question': 'Using a proven same-domain solution with slight tweaks typically reflects:',
                            'answers': [
                                {'text': '#analogies', 'correct': False, 'explanation': 'Analogies involve cross-domain solutions; this is an in-domain adaptation.'},
                                {'text': '#heuristics', 'correct': False, 'explanation': 'Heuristics are mental shortcuts; this situation calls for gap analysis, not heuristics.'},
                                {'text': '#gapanalysis', 'correct': True, 'explanation': 'Yes! This is a classic case of gap analysis, adapting an existing solution to fit the current problem.'},
                                {'text': '#rightproblem', 'correct': False, 'explanation': 'Right problem framing is essential, but this question is about applying an existing solution.'},
                            ],
                            
                        },
                    ]
                },
                {
                    'title': 'Unit-Level Challenge',
                    'definition': 'Integrative Scenarios — Harder',
                    'questions': [
                        {
                            'question': 'A nonprofit defines "reduce food insecurity by 20% in 18 months," lists stakeholders, and maps constraints (budget cap, delivery windows). What\'s the best next step?',
                            'answers': [
                                {'text': '#analogies', 'correct': False, 'explanation': 'Analogies are not the next step; the problem needs to be broken down first.'},
                                {'text': '#breakitdown', 'correct': True, 'explanation': 'Correct! Breaking down the problem will help in selecting tractable subproblems.'},
                                {'text': '#gapanalysis', 'correct': False, 'explanation': 'Gap analysis is not the immediate next step; the problem needs to be broken down first.'},
                                {'text': '#rightproblem', 'correct': False, 'explanation': 'The right problem has already been framed; now it needs to be broken down into components.'},
                            ],
                            
                        },
                        {
                            'question': 'A city compares nationwide meal-voucher programs and finds one that meets needs with minor policy edits. Which HC combo fits best?',
                            'answers': [
                                {'text': '#gapanalysis + #constraints', 'correct': True, 'explanation': 'Yes! This combination allows for evaluating an existing solution against fixed requirements.'},
                                {'text': '#analogies + #heuristics', 'correct': False, 'explanation': 'This combination is not suitable; the situation calls for gap analysis and constraint consideration.'},
                                {'text': '#breakitdown + #scienceoflearning', 'correct': False, 'explanation': 'These are not the relevant heuristics/constraints for this scenario.'},
                                {'text': '#rightproblem + #heuristics', 'correct': False, 'explanation': 'Heuristics are not the focus here; the situation requires gap analysis and constraint evaluation.'},
                            ],
                            
                        },
                        {
                            'question': 'A startup must choose quickly between two marketing channels with limited data and small downside. Which approach fits best?',
                            'answers': [
                                {'text': '#systemdynamics', 'correct': False, 'explanation': 'System dynamics is not applicable for a quick choice between two options.'},
                                {'text': '#heuristics', 'correct': True, 'explanation': 'Correct! Heuristics are suitable here due to the low stakes and limited information.'},
                                {'text': '#gapanalysis', 'correct': False, 'explanation': 'Gap analysis is not needed for a quick decision between two clear options.'},
                                {'text': '#analogies', 'correct': False, 'explanation': 'Analogies are not relevant for choosing between two known marketing channels.'},
                            ],
                            
                        },
                        {
                            'question': 'A class wants to master dense readings this term with spaced quizzes, dual-coded notes, and self-explanations. Which HC best captures this plan?',
                            'answers': [
                                {'text': '#scienceoflearning', 'correct': True, 'explanation': 'Yes! This heuristic captures the effective learning strategies being employed.'},
                                {'text': '#heuristics', 'correct': False, 'explanation': 'This is not a heuristic application; it\'s a well-defined learning plan.'},
                                {'text': '#breakitdown', 'correct': False, 'explanation': 'Breaking down is not the focus here; it\'s about applying effective learning strategies.'},
                                {'text': '#rightproblem', 'correct': False, 'explanation': 'The problem is already well-framed; the focus is on applying learning strategies.'},
                            ],
                            
                        },
                        {
                            'question': 'After characterizing a transit problem and mapping constraints, the team considers borrowing hospital triage logic to prioritize bus lanes. What must they apply?',
                            'answers': [
                                {'text': '#analogies', 'correct': False, 'explanation': 'Analogies alone are not enough; the solution must also fit within the constraints.'},
                                {'text': '#constraints', 'correct': False, 'explanation': 'Constraints are important, but this situation also requires an analogical transfer of knowledge.'},
                                {'text': '#analogies + #constraints', 'correct': True, 'explanation': 'Exactly! Both analogies and constraints must be considered in this cross-domain application.'},
                                {'text': '#gapanalysis', 'correct': False, 'explanation': 'Gap analysis is not the focus here; it\'s about applying known logic to a new situation.'},
                            ],
                            
                        },
                    ]
                },
            ]
        }
    ]
}

