"""
FA50 Course Seed Data
Unit 1: Logical Thinking
"""

FA50_DATA = {
    'title': 'FA50',
    'description': 'FA50 Course',
    'units': [
        {
            'title': 'Logical Thinking',
            'description': 'FA50 Unit 1',
            'order_index': 0,
            'concepts': [
                {
                    'title': '#algorithms',
                    'definition': 'Apply algorithmic thinking strategies to solve problems and effectively implement working code.',
                    'questions': [
                        {
                            'question': 'You design a returns-intake process: input = item + receipt; steps = validate → route by condition → restock/dispose; output = disposition label. What\'s missing for a robust algorithm?',
                            'answers': [
                                {'text': 'More condition branches', 'correct': False, 'explanation': 'Adding more condition branches may seem like it would make the algorithm more robust, but it could also complicate the algorithm unnecessarily. The key issue is handling the case when the receipt is missing.'},
                                {'text': 'Termination and explicit error handling for missing receipt', 'correct': True, 'explanation': 'Good algorithms need to handle all possible cases, including errors. Explicitly handling the case where the receipt is missing is crucial for robustness.'},
                                {'text': 'A fancier flowchart tool', 'correct': False, 'explanation': 'The complexity of the algorithm isn\'t necessarily related to the tool used to design it. A fancier tool won\'t solve the problem of missing receipt handling.'},
                                {'text': 'Converting to recursion', 'correct': False, 'explanation': 'Converting to recursion doesn\'t address the fundamental issues with the algorithm. It may even complicate things further.'},
                            ],
                        },
                        {
                            'question': 'You must assign 1,200 riders to 1,200 scooters minimizing total walking distance on a grid. Best first strategy?',
                            'answers': [
                                {'text': 'Brute-force all matchings', 'correct': False, 'explanation': 'Brute-forcing all matchings would be computationally expensive and inefficient, especially as the number of riders and scooters increases.'},
                                {'text': 'Use a polynomial-time assignment algorithm (Hungarian)', 'correct': True, 'explanation': 'The Hungarian algorithm is specifically designed for assignment problems and works in polynomial time, making it much more efficient for this scenario.'},
                                {'text': 'Greedy nearest-neighbor only', 'correct': False, 'explanation': 'A greedy nearest-neighbor approach doesn\'t guarantee an optimal solution for the overall assignment problem.'},
                                {'text': 'Depth-first search over all permutations', 'correct': False, 'explanation': 'This approach would also be computationally expensive and inefficient, as it involves exploring all possible permutations.'},
                            ],
                        },
                        {
                            'question': 'A sorting routine works on random arrays but fails on arrays with all equal values. Best test design fix?',
                            'answers': [
                                {'text': 'Larger random arrays', 'correct': False, 'explanation': 'Simply using larger random arrays doesn\'t address the specific issue with arrays that have all equal values.'},
                                {'text': 'Systematic unit tests covering edge classes: empty, single, sorted, reverse, all-equal', 'correct': True, 'explanation': 'Testing edge cases, including all-equal arrays, ensures that the sorting routine is robust and works under all conditions.'},
                                {'text': 'Rename variables clearly', 'correct': False, 'explanation': 'While clear variable names are important, they don\'t directly impact the functionality of the sorting routine.'},
                                {'text': 'Measure Big-O only', 'correct': False, 'explanation': 'Knowing the Big-O complexity doesn\'t help in identifying why the sorting routine fails for certain inputs.'},
                            ],
                        },
                        {
                            'question': 'A student explains their triage algorithm by listing inputs/outputs, laying out the main steps, and showing a branching flowchart. So far in this explanation of #algorithms, they have identified components, sequenced the steps, and represented decision points. What could this student do to enhance this 3 into a 4?',
                            'answers': [
                                {'text': 'Add explicit handling for edge cases.', 'correct': True, 'explanation': "A 4 requires explaining why the algorithm works under all conditions, including failures and unusual inputs."},
                                {'text': 'Add all detail to the flowchart.', 'correct': False, 'explanation': "They may believe more detail signals a stronger algorithm, but too much detail could be unclear."},
                                {'text': 'Rewrite the steps using more technical vocabulary.','correct': False,'explanation': "Fancy terminology can feel like an upgrade, but it doesn\'t improve the algorithm\'s completeness or correctness."},
                                {'text': 'Add more branches even if the logic doesn\'t require them.','correct': False,'explanation': "Students may assume ‘more branches = better algorithm,\' but unnecessary branching harms clarity rather than strengthening correctness."}
                            ]
                        }
                    ]
                },
                {
                    'title': '#estimation',
                    'definition': 'Use estimation and approximation techniques appropriately.',
                    'questions': [
                        {
                            'question': 'A venue fits between 400–1,600 people. Midpoint for order-of-magnitude planning?',
                            'answers': [
                                {'text': '1,000 (arithmetic mean)', 'correct': False, 'explanation': 'The arithmetic mean doesn\'t always provide a good estimate for order-of-magnitude planning, especially when the range is large.'},
                                {'text': '800 (geometric mean proxy between 4×10² and 16×10²)', 'correct': True, 'explanation': 'The geometric mean is more appropriate for order-of-magnitude estimates as it better represents the central tendency of multiplicative ranges.'},
                                {'text': '500', 'correct': False, 'explanation': 'This value doesn\'t fall at the midpoint of the given range and isn\'t a good estimate for order-of-magnitude planning.'},
                                {'text': '1,600', 'correct': False, 'explanation': 'This is the upper bound of the range and doesn\'t represent a midpoint estimate.'},
                            ],
                        },
                        {
                            'question': 'Estimate daily coffee cups sold by 50 campus cafés. First step?',
                            'answers': [
                                {'text': 'Ask one barista', 'correct': False, 'explanation': 'Asking one barista won\'t provide a reliable estimate as it doesn\'t account for variations between different cafés.'},
                                {'text': 'Break into cafés × hours open × customers/hour × cups/customer with unit tracking', 'correct': True, 'explanation': 'This methodical breakdown allows for a more accurate and reliable estimation by considering all relevant factors.'},
                                {'text': 'Check last year\'s invoice total', 'correct': False, 'explanation': 'Last year\'s invoice total won\'t provide an accurate estimate for daily coffee cup sales as it doesn\'t account for changes over time.'},
                                {'text': 'Assume 1,000 per café', 'correct': False, 'explanation': 'Making an assumption without any basis or calculation isn\'t a reliable estimation method.'},
                            ],
                        },
                        {
                            'question': 'Your time-to-finish estimate ignores context-switching overhead. Which bias likely?',
                            'answers': [
                                {'text': 'Base-rate fallacy', 'correct': False, 'explanation': 'The base-rate fallacy involves ignoring statistical information in favor of specific information. It doesn\'t directly relate to context-switching overhead.'},
                                {'text': 'Planning fallacy / optimism bias', 'correct': True, 'explanation': 'The planning fallacy is the tendency to underestimate the time needed to complete future tasks, leading to overly optimistic time-to-finish estimates.'},
                                {'text': 'Gambler\'s fallacy', 'correct': False, 'explanation': 'The gambler\'s fallacy is the belief that past events affect the probabilities in random events. It doesn\'t relate to context-switching overhead.'},
                                {'text': 'Survivorship bias', 'correct': False, 'explanation': 'Survivorship bias involves focusing on successful cases while ignoring failures. It doesn\'t directly relate to time estimation.'},
                            ],
                        },
                        {
                            'question': 'A student estimates daily bike-share usage by multiplying stations times bikes per station times turnover rate. So far in this explanation of #estimation, they have decomposed the problem, used reasonable units, and produced an order-of-magnitude answer. What could this student do to enhance this 3 into a 4?',
                            'answers': [
                                {'text': 'Justify each assumption and show how sensitive the estimate is to those assumptions.', 'correct': True,'explanation': "Students often think a single clean estimate is enough, but a 4 needs transparent assumptions and acknowledgement of uncertainty."},
                                { 'text': 'Add more multiplication factors.', 'correct': False, 'explanation': "They may think adding complexity improves rigor, but irrelevant factors weaken the estimate." },
                                {'text': 'Provide the exact real-world number instead of estimating.','correct': False, 'explanation': "Students may believe “precision = quality,” but estimation is about reasoning under uncertainty, not finding the actual value."  },
                                {'text': 'Round everything to whole numbers to avoid decimals.', 'correct': False,'explanation': "Avoiding decimals feels tidy, but it doesn't add value to the application." }
                            ]
                        }
                    ]
                },
                {
                    'title': '#deduction',
                    'definition': 'Analyze and apply deductive reasoning.',
                    'questions': [
                        {
                            'question': 'All A are B. All B are C. Therefore all A are C. This is:',
                            'answers': [
                                {'text': 'Valid; soundness depends on truth of premises', 'correct': True, 'explanation': 'This is a valid deductive argument; if the premises are true, the conclusion must be true.'},
                                {'text': 'Sound regardless', 'correct': False, 'explanation': 'The argument isn\'t necessarily sound, as soundness also requires the premises to be true.'},
                                {'text': 'Inductive', 'correct': False, 'explanation': 'This is a deductive argument, not an inductive one. Inductive arguments involve generalizing from specific cases.'},
                                {'text': 'Invalid', 'correct': False, 'explanation': 'The argument is valid; the conclusion logically follows from the premises.'},
                            ],
                        },
                        {
                            'question': '¬Q; P → Q; therefore ¬P. This is:',
                            'answers': [
                                {'text': 'Modus ponens', 'correct': False, 'explanation': 'Modus ponens would be affirming the antecedent, which isn\'t what this argument is doing.'},
                                {'text': 'Modus tollens', 'correct': True, 'explanation': 'This is an example of modus tollens: denying the consequent to deny the antecedent.'},
                                {'text': 'Disjunctive syllogism', 'correct': False, 'explanation': 'Disjunctive syllogism involves a disjunction and isn\'t applicable here.'},
                                {'text': 'Non sequitur', 'correct': False, 'explanation': 'The conclusion follows logically from the premises, so it isn\'t a non sequitur.'},
                            ],
                        },
                        {
                            'question': 'Which equivalence is correct?',
                            'answers': [
                                {'text': '¬(P ∨ Q) ≡ ¬P ∨ ¬Q', 'correct': False, 'explanation': 'This is a misapplication of De Morgan\'s laws.'},
                                {'text': '¬(P ∧ Q) ≡ ¬P ∨ ¬Q', 'correct': True, 'explanation': 'This is an application of De Morgan\'s laws: the negation of a conjunction is equivalent to the disjunction of the negations.'},
                                {'text': '¬(P ∧ Q) ≡ ¬P ∧ ¬Q', 'correct': False, 'explanation': 'This is incorrect; it reverses the operation instead of applying De Morgan\'s laws.'},
                                {'text': 'P → Q ≡ P ∧ ¬Q', 'correct': False, 'explanation': 'This is a misrepresentation of the implication; it doesn\'t hold logically.'},
                            ],
                        },
                        {
                            'question': 'A student analyzes a deductive argument by restating the premises, identifying the conclusion, and naming the relevant logical structure. So far in this explanation of #deduction, they have correctly recognized form, validity, and structure. What could this student do to enhance this 3 into a 4?',
                            'answers': [
                                {'text': 'Explain why the argument\'s structure guarantees the conclusion and address potential misinterpretations of the premises.','correct': True,'explanation': "Students often stop at naming the form, but a 4 requires justification—showing how the form ensures validity and clarifying the premises’ meaning." },
                                {'text': 'Memorize more named syllogisms to list in the answer.','correct': False,'explanation': "They may think more labels look sophisticated, but deduction requires reasoning, not name-dropping."},
                                {'text': 'Rewrite the argument using symbolic notation.','correct': False,'explanation': "Symbolic notation can help, but using it alone doesn\'t demonstrate deep understanding or justification."},
                                {'text': 'Add rhetorical commentary on why the argument is persuasive.','correct': False,'explanation': "Persuasiveness isn\'t the same as deductive validity; this misses the core of deductive reasoning."}
                            ]
                        }
                    ]
                },
                {
                    'title': '#fallacies',
                    'definition': 'Identify and correct logical fallacies.',
                    'questions': [
                        {
                            'question': '"If remote work increases, cities die. Cities aren\'t dying, so remote work isn\'t increasing."',
                            'answers': [
                                {'text': 'Modus tollens', 'correct': False, 'explanation': 'This isn\'t an example of modus tollens, which would require a different logical structure.'},
                                {'text': 'Denying the consequent? (No—actually affirming the negation incorrectly) → Affirming the negation / Invalid converse-style reasoning', 'correct': True, 'explanation': 'This is an example of invalid reasoning; just because the cities aren\'t dying doesn\'t mean remote work isn\'t increasing.'},
                                {'text': 'Sound argument', 'correct': False, 'explanation': 'The argument isn\'t sound, as it relies on invalid reasoning.'},
                                {'text': 'Straw man', 'correct': False, 'explanation': 'This isn\'t a straw man fallacy, which involves misrepresenting an argument to make it easier to attack.'},
                            ],
                        },
                        {
                            'question': '"No study proves aliens don\'t exist; therefore aliens exist."',
                            'answers': [
                                {'text': 'Red herring', 'correct': False, 'explanation': 'This isn\'t a red herring fallacy, which would involve diverting the argument to unrelated issues.'},
                                {'text': 'Appeal to ignorance', 'correct': True, 'explanation': 'This is an appeal to ignorance; just because we don\'t have evidence against something doesn\'t mean it\'s true.'},
                                {'text': 'Bandwagon', 'correct': False, 'explanation': 'This isn\'t a bandwagon fallacy, which would involve arguing that something is true because many people believe it.'},
                                {'text': 'Slippery slope', 'correct': False, 'explanation': 'This isn\'t a slippery slope fallacy, which would involve arguing that a small first step will lead to a chain of related events.'},
                            ],
                        },
                        {
                            'question': '"Don\'t trust her inflation analysis—she once misreported her taxes."',
                            'answers': [
                                {'text': 'Weak analogy', 'correct': False, 'explanation': 'This isn\'t an analogy, weak or strong. It\'s an attack on the person\'s character or past actions.'},
                                {'text': 'Ad hominem (abusive/circumstantial)', 'correct': True, 'explanation': 'This is an ad hominem fallacy; it attacks the person instead of addressing the argument or analysis.'},
                                {'text': 'False dichotomy', 'correct': False, 'explanation': 'This isn\'t a false dichotomy, which would involve presenting two options as the only possibilities.'},
                                {'text': 'Questionable cause', 'correct': False, 'explanation': 'This isn\'t a questionable cause fallacy, which would involve assuming a cause-and-effect relationship without evidence.'},
                            ],
                        },
                    ]
                },
                {
                    'title': '#induction',
                    'definition': 'A method of reasoning where probable conclusions are drawn based on specific evidence and observations.',
                    'questions': [
                        {
                            'question': '"Past 10 quarters: coupon users have 15–20% higher basket size; next quarter coupons will likely raise basket size."',
                            'answers': [
                                {'text': 'Authority', 'correct': False, 'explanation': 'This isn\'t an appeal to authority, which would involve citing an expert or authority figure to support the argument.'},
                                {'text': 'Prediction from past data', 'correct': True, 'explanation': 'This is an inductive reasoning based on past data; it observes a trend and predicts it will continue.'},
                                {'text': 'Analogy', 'correct': False, 'explanation': 'This isn\'t an analogy, which would involve comparing two different things to highlight some form of similarity.'},
                                {'text': 'Deduction', 'correct': False, 'explanation': 'This isn\'t deduction, which would involve drawing a specific conclusion from general premises or facts.'},
                            ],
                        },
                        {
                            'question': 'Anecdotes → strong generalization requires:',
                            'answers': [
                                {'text': 'Louder claims', 'correct': False, 'explanation': 'Making louder claims doesn\'t strengthen an argument or make it more valid.'},
                                {'text': 'Larger, representative samples; multiple evidence types; narrower claims', 'correct': True, 'explanation': 'A strong generalization from anecdotes requires a larger and more representative sample, as well as consideration of other types of evidence.'},
                                {'text': 'Only expert quotes', 'correct': False, 'explanation': 'Relying solely on expert quotes doesn\'t guarantee a strong or valid generalization.'},
                                {'text': 'One perfect case study', 'correct': False, 'explanation': 'One case study, even if it seems perfect, isn\'t enough to make a strong generalization.'},
                            ],
                        },
                        {
                            'question': 'A strong meta-analysis relies on:',
                            'answers': [
                                {'text': 'P-values only', 'correct': False, 'explanation': 'Relying on p-values alone isn\'t sufficient for a strong meta-analysis; it requires a comprehensive approach to data and methodology.'},
                                {'text': 'True/accurate premises: good data, low bias, correct methods (#sourcequality)', 'correct': True, 'explanation': 'A strong meta-analysis depends on the quality and accuracy of the underlying data and methods used in the analysis.'},
                                {'text': 'Persuasive writing', 'correct': False, 'explanation': 'While persuasive writing is important for presenting arguments, it doesn\'t directly impact the strength of a meta-analysis.'},
                                {'text': 'Single-lab replication', 'correct': False, 'explanation': 'Replication is important, but relying on a single lab\'s replication isn\'t sufficient for a strong meta-analysis.'},
                            ],
                        },
                    ]
                },
                {
                    'title': 'Unit-Level Challenge',
                    'definition': 'Integrative Scenarios — Harder',
                    'questions': [
                        {
                            'question': 'A team formalizes a customer-service protocol as a flowchart with branching conditions, then ships a script to auto-triage tickets.',
                            'answers': [
                                {'text': '#induction', 'correct': False, 'explanation': 'This isn\'t an example of induction, which would involve drawing general conclusions from specific instances.'},
                                {'text': '#algorithms', 'correct': True, 'explanation': 'This is an example of applying algorithmic thinking to create a systematic and automated solution.'},
                                {'text': '#estimation', 'correct': False, 'explanation': 'Estimation isn\'t the primary focus here; it\'s about creating an algorithmic solution.'},
                                {'text': '#fallacies', 'correct': False, 'explanation': 'This doesn\'t involve identifying or correcting logical fallacies.'},
                            ],
                        },
                        {
                            'question': 'A proposal claims a museum expansion will "double visitors." You do a back-of-napkin capacity + dwell-time + opening-hours check.',
                            'answers': [
                                {'text': '#estimation', 'correct': True, 'explanation': 'This involves estimation to quickly evaluate the feasibility of the proposal based on available data.'},
                                {'text': '#deduction', 'correct': False, 'explanation': 'Deduction isn\'t the primary method used here; it\'s more about estimation and quick analysis.'},
                                {'text': '#fallacies', 'correct': False, 'explanation': 'This doesn\'t directly involve identifying or correcting logical fallacies.'},
                                {'text': '#algorithms', 'correct': False, 'explanation': 'While algorithms are important, this specific task is more about estimation and capacity planning.'},
                            ],
                        },
                        {
                            'question': 'An op-ed argues "crime rose because policy Y passed" using two cherry-picked months. You diagnose the flaw and suggest proper evidence.',
                            'answers': [
                                {'text': '#algorithms', 'correct': False, 'explanation': 'This isn\'t directly related to algorithms, which are more about systematic problem-solving.'},
                                {'text': '#estimation', 'correct': False, 'explanation': 'Estimation isn\'t the primary focus here; it\'s about identifying fallacies in the argument.'},
                                {'text': '#fallacies + #induction', 'correct': True, 'explanation': 'This involves identifying the fallacy in the argument (cherry-picking data) and using inductive reasoning to suggest proper evidence.'},
                                {'text': '#deduction', 'correct': False, 'explanation': 'Deduction isn\'t the primary method used here; it\'s more about identifying fallacies and suggesting evidence.'},
                            ],
                        },
                        {
                            'question': 'Given: If a transaction exceeds $10k it must be flagged; this transfer exceeds $10k; therefore it must be flagged.',
                            'answers': [
                                {'text': '#deduction', 'correct': True, 'explanation': 'This is a deductive reasoning example: it follows logically that the transfer must be flagged if it exceeds $10k.'},
                                {'text': '#induction', 'correct': False, 'explanation': 'Induction isn\'t applicable here; this is a clear deductive reasoning case.'},
                                {'text': '#fallacies', 'correct': False, 'explanation': 'There doesn\'t appear to be a fallacy in this reasoning; it follows the given rule.'},
                                {'text': '#estimation', 'correct': False, 'explanation': 'Estimation isn\'t relevant to this deductive reasoning task.'},
                            ],
                        },
                        {
                            'question': 'You must pair 5,000 mentors/mentees under hard constraints and minimize total mismatch score.',
                            'answers': [
                                {'text': '#algorithms + #optimization (related)', 'correct': True, 'explanation': 'This requires algorithmic thinking and possibly optimization techniques to solve the matching problem effectively.'},
                                {'text': '#estimation', 'correct': False, 'explanation': 'Estimation isn\'t the primary focus here; it\'s about solving a complex matching problem.'},
                                {'text': '#fallacies', 'correct': False, 'explanation': 'This doesn\'t directly involve identifying or correcting logical fallacies.'},
                                {'text': '#induction', 'correct': False, 'explanation': 'Induction isn\'t the primary method used here; it\'s more about solving a specific problem.'},
                            ],
                        },
                        {
                            'question': 'Before committing to a pilot, you approximate expected sign-ups using city population × target share × conversion rate, then compare to venue limits.',
                            'answers': [
                                {'text': '#estimation', 'correct': True, 'explanation': 'This involves estimation to approximate expected sign-ups based on available data and then comparing it to venue capacity.'},
                                {'text': '#deduction', 'correct': False, 'explanation': 'Deduction isn\'t the primary method used here; it\'s more about estimation and capacity planning.'},
                                {'text': '#fallacies', 'correct': False, 'explanation': 'This doesn\'t directly involve identifying or correcting logical fallacies.'},
                                {'text': '#algorithms', 'correct': False, 'explanation': 'While algorithms are important, this specific task is more about estimation and capacity planning.'},
                            ],
                        },
                    ]
                },
            ]
        }
    ]
}

