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
                                {'text': 'Goal state', 'correct': False},
                                {'text': 'Initial state and measurement plan', 'correct': True},
                                {'text': 'Scale only', 'correct': False},
                                {'text': 'Nothing—solution first is fine', 'correct': False},
                            ],
                            'explanation': '#rightproblem requires a clear baseline and how success will be measured before proposing solutions.'
                        },
                        {
                            'question': 'Which goal state avoids presupposing a solution?',
                            'answers': [
                                {'text': 'Ban cars downtown', 'correct': False},
                                {'text': 'Achieve average bus wait time ≤ 7 minutes by Q4', 'correct': True},
                                {'text': 'Build a new subway line', 'correct': False},
                                {'text': 'Switch traffic lights to adaptive control', 'correct': False},
                            ],
                            'explanation': 'A measurable goal describes outcomes, not specific interventions.'
                        },
                        {
                            'question': 'You listed initial state, goal state, obstacles, and scale, but not likely consequences if nothing changes. What should you add?',
                            'answers': [
                                {'text': 'Constraint list', 'correct': False},
                                {'text': 'Future implications of the problem', 'correct': True},
                                {'text': 'Budget section only', 'correct': False},
                                {'text': 'SWOT table', 'correct': False},
                            ],
                            'explanation': 'Robust characterization includes likely consequences and implications.'
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
                                {'text': 'Copy all procedures verbatim', 'correct': False},
                                {'text': 'Ignore domain differences', 'correct': False},
                                {'text': 'Map deep structural similarities and differences', 'correct': True},
                                {'text': 'Focus on catchy metaphors', 'correct': False},
                            ],
                            'explanation': 'Valid analogies require similarity mapping and adaptations.'
                        },
                        {
                            'question': 'When is #analogies preferred over #gapanalysis?',
                            'answers': [
                                {'text': 'Same domain with minor tweaks', 'correct': False},
                                {'text': 'No same-domain fit; a cross-domain template matches structure', 'correct': True},
                                {'text': 'When constraints are already fixed', 'correct': False},
                                {'text': 'When time allows exhaustive trials', 'correct': False},
                            ],
                            'explanation': 'Analogies generate novel solutions across domains; gap analysis reuses in-domain solutions.'
                        },
                        {
                            'question': 'Which is an idiosyncratic feature to discard when translating a source solution?',
                            'answers': [
                                {'text': 'Core mechanism', 'correct': False},
                                {'text': 'Domain-specific regulation irrelevant to target', 'correct': True},
                                {'text': 'Structural mapping', 'correct': False},
                                {'text': 'Performance criterion', 'correct': False},
                            ],
                            'explanation': 'Drop details that don\'t transfer to the target context.'
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
                                {'text': 'Constraint', 'correct': True},
                                {'text': 'Obstacle', 'correct': False},
                                {'text': 'Neither', 'correct': False},
                                {'text': 'Both—depends on mood', 'correct': False},
                            ],
                            'explanation': 'Non-negotiable boundaries are constraints in the current framing.'
                        },
                        {
                            'question': 'Which action demonstrates constraint satisfaction?',
                            'answers': [
                                {'text': 'Brainstorming without limits', 'correct': False},
                                {'text': 'Selecting a schedule that fits room capacity, instructor availability, and time windows', 'correct': True},
                                {'text': 'Expanding scope until a solution appears', 'correct': False},
                                {'text': 'Copying a competitor\'s plan', 'correct': False},
                            ],
                            'explanation': 'Constraint satisfaction finds solutions that meet all constraints simultaneously.'
                        },
                        {
                            'question': 'You misclassified a reparable equipment failure as a constraint. What\'s the fix?',
                            'answers': [
                                {'text': 'Keep it a constraint', 'correct': False},
                                {'text': 'Reframe as an obstacle and plan remediation', 'correct': True},
                                {'text': 'Remove it entirely', 'correct': False},
                                {'text': 'Treat it as a success metric', 'correct': False},
                            ],
                            'explanation': 'Solvable items are obstacles; treat with actions, not as fixed bounds.'
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
                                {'text': 'High stakes, abundant data', 'correct': False},
                                {'text': 'Low stakes, limited time/information', 'correct': True},
                                {'text': 'Anytime—they\'re always best', 'correct': False},
                                {'text': 'Never—use full analysis only', 'correct': False},
                            ],
                            'explanation': 'Heuristics shine under uncertainty with manageable costs.'
                        },
                        {
                            'question': 'Which sequence describes means-ends analysis?',
                            'answers': [
                                {'text': 'Guess and check repeatedly', 'correct': False},
                                {'text': 'Start at goal, step backward once', 'correct': False},
                                {'text': 'Identify initial/goal states, set subgoals to reduce the gap, iterate', 'correct': True},
                                {'text': 'Randomized trial selection', 'correct': False},
                            ],
                            'explanation': 'Means-ends iteratively creates subgoals to shrink discrepancies.'
                        },
                        {
                            'question': 'Which risk matches the availability heuristic?',
                            'answers': [
                                {'text': 'Overweight vivid recent events when estimating likelihoods', 'correct': True},
                                {'text': 'Confuse similarity with probability', 'correct': False},
                                {'text': 'Anchor on a starting number only', 'correct': False},
                                {'text': 'Use affectless calculation', 'correct': False},
                            ],
                            'explanation': 'Ease of recall substitutes for true frequency.'
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
                                {'text': 'Dual codes and spaced practice', 'correct': True},
                                {'text': 'Highlighting and massed practice', 'correct': False},
                                {'text': 'Emotion and rote repetition', 'correct': False},
                                {'text': 'Interference and cramming', 'correct': False},
                            ],
                            'explanation': 'Multiple modalities + spacing strengthen retrieval.'
                        },
                        {
                            'question': 'Which statement best applies rereading effectively?',
                            'answers': [
                                {'text': 'Immediate rereads are always superior', 'correct': False},
                                {'text': 'Reread after a delay with a specific goal', 'correct': True},
                                {'text': 'Never reread', 'correct': False},
                                {'text': 'Reread only captions', 'correct': False},
                            ],
                            'explanation': 'Delayed, purpose-driven rereads aid organization and distinction.'
                        },
                        {
                            'question': 'Which pairing matches Kosslyn\'s Maxims?',
                            'answers': [
                                {'text': 'Think it Through → retrieval cues; Make and Use Associations → deep processing', 'correct': False},
                                {'text': 'Think it Through → deep processing; Make and Use Associations → rich retrieval cues', 'correct': True},
                                {'text': 'Think it Through → dual codes only; Make and Use Associations → spacing only', 'correct': False},
                                {'text': 'Both maxims → massed practice', 'correct': False},
                            ],
                            'explanation': 'Maxim 1 emphasizes processing; Maxim 2 emphasizes associative retrieval.'
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
                                {'text': 'List problems once', 'correct': False},
                                {'text': '\'Pollution\' → \'air pollution\' → \'PM2.5 from diesel buses\' and tackle the last', 'correct': True},
                                {'text': 'Jump straight to a solution', 'correct': False},
                                {'text': 'Define constraints only', 'correct': False},
                            ],
                            'explanation': 'Iterate until a subproblem is concretely solvable.'
                        },
                        {
                            'question': 'Which tool best visualizes subproblems and their categories?',
                            'answers': [
                                {'text': 'Fishbone/Ishikawa diagram', 'correct': True},
                                {'text': 'Gantt chart only', 'correct': False},
                                {'text': 'Confusion matrix', 'correct': False},
                                {'text': 'ROC curve', 'correct': False},
                            ],
                            'explanation': 'Fishbone diagrams organize causes/subproblems by category.'
                        },
                        {
                            'question': 'What\'s a common pitfall when breaking problems down?',
                            'answers': [
                                {'text': 'Selecting tractable subproblems', 'correct': False},
                                {'text': 'Explaining links between subproblems', 'correct': False},
                                {'text': 'Mislabeling a fixed constraint as a subproblem', 'correct': True},
                                {'text': 'Using evidence to prioritize', 'correct': False},
                            ],
                            'explanation': 'Subproblems are solvable obstacles; constraints are fixed bounds.'
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
                                {'text': 'Build a novel solution anyway', 'correct': False},
                                {'text': 'Use the existing tool and document justification', 'correct': True},
                                {'text': 'Switch to analogies', 'correct': False},
                                {'text': 'Ignore constraints', 'correct': False},
                            ],
                            'explanation': 'Gap analysis can conclude no novel solution is needed.'
                        },
                        {
                            'question': 'Which is required for a solid gap analysis?',
                            'answers': [
                                {'text': 'Listing one familiar option', 'correct': False},
                                {'text': 'Deep evaluation of multiple existing solutions against requirements/constraints', 'correct': True},
                                {'text': 'Brainstorming new ideas only', 'correct': False},
                                {'text': 'Assuming gaps exist', 'correct': False},
                            ],
                            'explanation': 'Survey and evaluate the landscape before proposing novelty.'
                        },
                        {
                            'question': 'Using a proven same-domain solution with slight tweaks typically reflects:',
                            'answers': [
                                {'text': '#analogies', 'correct': False},
                                {'text': '#heuristics', 'correct': False},
                                {'text': '#gapanalysis', 'correct': True},
                                {'text': '#rightproblem', 'correct': False},
                            ],
                            'explanation': 'Minor adaptation of in-domain solutions is classic gap analysis.'
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
                                {'text': '#analogies', 'correct': False},
                                {'text': '#breakitdown', 'correct': True},
                                {'text': '#gapanalysis', 'correct': False},
                                {'text': '#rightproblem', 'correct': False},
                            ],
                            'explanation': 'After #rightproblem and constraints, use #breakitdown to select tractable subproblems.'
                        },
                        {
                            'question': 'A city compares nationwide meal-voucher programs and finds one that meets needs with minor policy edits. Which HC combo fits best?',
                            'answers': [
                                {'text': '#gapanalysis + #constraints', 'correct': True},
                                {'text': '#analogies + #heuristics', 'correct': False},
                                {'text': '#breakitdown + #scienceoflearning', 'correct': False},
                                {'text': '#rightproblem + #heuristics', 'correct': False},
                            ],
                            'explanation': 'Evaluate existing solutions against fixed requirements and adopt with modifications.'
                        },
                        {
                            'question': 'A startup must choose quickly between two marketing channels with limited data and small downside. Which approach fits best?',
                            'answers': [
                                {'text': '#systemdynamics', 'correct': False},
                                {'text': '#heuristics', 'correct': True},
                                {'text': '#gapanalysis', 'correct': False},
                                {'text': '#analogies', 'correct': False},
                            ],
                            'explanation': 'Low stakes + limited info favors fast-and-frugal #heuristics.'
                        },
                        {
                            'question': 'A class wants to master dense readings this term with spaced quizzes, dual-coded notes, and self-explanations. Which HC best captures this plan?',
                            'answers': [
                                {'text': '#scienceoflearning', 'correct': True},
                                {'text': '#heuristics', 'correct': False},
                                {'text': '#breakitdown', 'correct': False},
                                {'text': '#rightproblem', 'correct': False},
                            ],
                            'explanation': '#scienceoflearning ties techniques to principles like dual codes, generation, and spacing.'
                        },
                        {
                            'question': 'After characterizing a transit problem and mapping constraints, the team considers borrowing hospital triage logic to prioritize bus lanes. What must they apply?',
                            'answers': [
                                {'text': '#analogies', 'correct': False},
                                {'text': '#constraints', 'correct': False},
                                {'text': '#analogies + #constraints', 'correct': True},
                                {'text': '#gapanalysis', 'correct': False},
                            ],
                            'explanation': 'Cross-domain adoption requires #analogies mapping and compatibility with #constraints.'
                        },
                    ]
                },
            ]
        }
    ]
}

