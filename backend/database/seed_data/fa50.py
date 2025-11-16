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
                                {'text': 'More condition branches', 'correct': False},
                                {'text': 'Termination and explicit error handling for missing receipt', 'correct': True},
                                {'text': 'A fancier flowchart tool', 'correct': False},
                                {'text': 'Converting to recursion', 'correct': False},
                            ],
                            'explanation': 'Good algorithms are finite and handle failures/edge cases explicitly.'
                        },
                        {
                            'question': 'You must assign 1,200 riders to 1,200 scooters minimizing total walking distance on a grid. Best first strategy?',
                            'answers': [
                                {'text': 'Brute-force all matchings', 'correct': False},
                                {'text': 'Use a polynomial-time assignment algorithm (Hungarian)', 'correct': True},
                                {'text': 'Greedy nearest-neighbor only', 'correct': False},
                                {'text': 'Depth-first search over all permutations', 'correct': False},
                            ],
                            'explanation': 'This is a classic assignment problem; Hungarian beats brute/greedy here.'
                        },
                        {
                            'question': 'A sorting routine works on random arrays but fails on arrays with all equal values. Best test design fix?',
                            'answers': [
                                {'text': 'Larger random arrays', 'correct': False},
                                {'text': 'Systematic unit tests covering edge classes: empty, single, sorted, reverse, all-equal', 'correct': True},
                                {'text': 'Rename variables clearly', 'correct': False},
                                {'text': 'Measure Big-O only', 'correct': False},
                            ],
                            'explanation': 'Robustness comes from targeted edge-case coverage.'
                        },
                    ]
                },
                {
                    'title': '#estimation',
                    'definition': 'Use estimation and approximation techniques appropriately.',
                    'questions': [
                        {
                            'question': 'A venue fits between 400–1,600 people. Midpoint for order-of-magnitude planning?',
                            'answers': [
                                {'text': '1,000 (arithmetic mean)', 'correct': False},
                                {'text': '800 (geometric mean proxy between 4×10² and 16×10²)', 'correct': True},
                                {'text': '500', 'correct': False},
                                {'text': '1,600', 'correct': False},
                            ],
                            'explanation': 'When bounds span factors, geometric mean better centers magnitude.'
                        },
                        {
                            'question': 'Estimate daily coffee cups sold by 50 campus cafés. First step?',
                            'answers': [
                                {'text': 'Ask one barista', 'correct': False},
                                {'text': 'Break into cafés × hours open × customers/hour × cups/customer with unit tracking', 'correct': True},
                                {'text': 'Check last year\'s invoice total', 'correct': False},
                                {'text': 'Assume 1,000 per café', 'correct': False},
                            ],
                            'explanation': '#breakitdown + unit consistency → defensible Fermi.'
                        },
                        {
                            'question': 'Your time-to-finish estimate ignores context-switching overhead. Which bias likely?',
                            'answers': [
                                {'text': 'Base-rate fallacy', 'correct': False},
                                {'text': 'Planning fallacy / optimism bias', 'correct': True},
                                {'text': 'Gambler\'s fallacy', 'correct': False},
                                {'text': 'Survivorship bias', 'correct': False},
                            ],
                            'explanation': 'Systematic underestimation = classic planning fallacy.'
                        },
                    ]
                },
                {
                    'title': '#deduction',
                    'definition': 'Analyze and apply deductive reasoning.',
                    'questions': [
                        {
                            'question': 'All A are B. All B are C. Therefore all A are C. This is:',
                            'answers': [
                                {'text': 'Valid; soundness depends on truth of premises', 'correct': True},
                                {'text': 'Sound regardless', 'correct': False},
                                {'text': 'Inductive', 'correct': False},
                                {'text': 'Invalid', 'correct': False},
                            ],
                            'explanation': 'Form guarantees validity; soundness needs true premises.'
                        },
                        {
                            'question': '¬Q; P → Q; therefore ¬P. This is:',
                            'answers': [
                                {'text': 'Modus ponens', 'correct': False},
                                {'text': 'Modus tollens', 'correct': True},
                                {'text': 'Disjunctive syllogism', 'correct': False},
                                {'text': 'Non sequitur', 'correct': False},
                            ],
                            'explanation': 'Deny consequent → deny antecedent.'
                        },
                        {
                            'question': 'Which equivalence is correct?',
                            'answers': [
                                {'text': '¬(P ∨ Q) ≡ ¬P ∨ ¬Q', 'correct': False},
                                {'text': '¬(P ∧ Q) ≡ ¬P ∨ ¬Q', 'correct': True},
                                {'text': '¬(P ∧ Q) ≡ ¬P ∧ ¬Q', 'correct': False},
                                {'text': 'P → Q ≡ P ∧ ¬Q', 'correct': False},
                            ],
                            'explanation': 'First De Morgan law shown in (B).'
                        },
                    ]
                },
                {
                    'title': '#fallacies',
                    'definition': 'Identify and correct logical fallacies.',
                    'questions': [
                        {
                            'question': '"If remote work increases, cities die. Cities aren\'t dying, so remote work isn\'t increasing."',
                            'answers': [
                                {'text': 'Modus tollens', 'correct': False},
                                {'text': 'Denying the consequent? (No—actually affirming the negation incorrectly) → Affirming the negation / Invalid converse-style reasoning', 'correct': True},
                                {'text': 'Sound argument', 'correct': False},
                                {'text': 'Straw man', 'correct': False},
                            ],
                            'explanation': 'From ¬Q infer ¬P given only P→Q is invalid unless Q→P also holds.'
                        },
                        {
                            'question': '"No study proves aliens don\'t exist; therefore aliens exist."',
                            'answers': [
                                {'text': 'Red herring', 'correct': False},
                                {'text': 'Appeal to ignorance', 'correct': True},
                                {'text': 'Bandwagon', 'correct': False},
                                {'text': 'Slippery slope', 'correct': False},
                            ],
                            'explanation': 'Absence of disconfirming evidence ≠ evidence of truth.'
                        },
                        {
                            'question': '"Don\'t trust her inflation analysis—she once misreported her taxes."',
                            'answers': [
                                {'text': 'Weak analogy', 'correct': False},
                                {'text': 'Ad hominem (abusive/circumstantial)', 'correct': True},
                                {'text': 'False dichotomy', 'correct': False},
                                {'text': 'Questionable cause', 'correct': False},
                            ],
                            'explanation': 'Attacks person, not the argument.'
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
                                {'text': 'Authority', 'correct': False},
                                {'text': 'Prediction from past data', 'correct': True},
                                {'text': 'Analogy', 'correct': False},
                                {'text': 'Deduction', 'correct': False},
                            ],
                            'explanation': 'Temporal generalization.'
                        },
                        {
                            'question': 'Anecdotes → strong generalization requires:',
                            'answers': [
                                {'text': 'Louder claims', 'correct': False},
                                {'text': 'Larger, representative samples; multiple evidence types; narrower claims', 'correct': True},
                                {'text': 'Only expert quotes', 'correct': False},
                                {'text': 'One perfect case study', 'correct': False},
                            ],
                            'explanation': 'Quantity + quality + scope fit.'
                        },
                        {
                            'question': 'A strong meta-analysis relies on:',
                            'answers': [
                                {'text': 'P-values only', 'correct': False},
                                {'text': 'True/accurate premises: good data, low bias, correct methods (#sourcequality)', 'correct': True},
                                {'text': 'Persuasive writing', 'correct': False},
                                {'text': 'Single-lab replication', 'correct': False},
                            ],
                            'explanation': 'Reliability = strong + true premises.'
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
                                {'text': '#induction', 'correct': False},
                                {'text': '#algorithms', 'correct': True},
                                {'text': '#estimation', 'correct': False},
                                {'text': '#fallacies', 'correct': False},
                            ],
                            'explanation': ''
                        },
                        {
                            'question': 'A proposal claims a museum expansion will "double visitors." You do a back-of-napkin capacity + dwell-time + opening-hours check.',
                            'answers': [
                                {'text': '#estimation', 'correct': True},
                                {'text': '#deduction', 'correct': False},
                                {'text': '#fallacies', 'correct': False},
                                {'text': '#algorithms', 'correct': False},
                            ],
                            'explanation': ''
                        },
                        {
                            'question': 'An op-ed argues "crime rose because policy Y passed" using two cherry-picked months. You diagnose the flaw and suggest proper evidence.',
                            'answers': [
                                {'text': '#algorithms', 'correct': False},
                                {'text': '#estimation', 'correct': False},
                                {'text': '#fallacies + #induction', 'correct': True},
                                {'text': '#deduction', 'correct': False},
                            ],
                            'explanation': ''
                        },
                        {
                            'question': 'Given: If a transaction exceeds $10k it must be flagged; this transfer exceeds $10k; therefore it must be flagged.',
                            'answers': [
                                {'text': '#deduction', 'correct': True},
                                {'text': '#induction', 'correct': False},
                                {'text': '#fallacies', 'correct': False},
                                {'text': '#estimation', 'correct': False},
                            ],
                            'explanation': ''
                        },
                        {
                            'question': 'You must pair 5,000 mentors/mentees under hard constraints and minimize total mismatch score.',
                            'answers': [
                                {'text': '#algorithms + #optimization (related)', 'correct': True},
                                {'text': '#estimation', 'correct': False},
                                {'text': '#fallacies', 'correct': False},
                                {'text': '#induction', 'correct': False},
                            ],
                            'explanation': ''
                        },
                        {
                            'question': 'Before committing to a pilot, you approximate expected sign-ups using city population × target share × conversion rate, then compare to venue limits.',
                            'answers': [
                                {'text': '#estimation', 'correct': True},
                                {'text': '#deduction', 'correct': False},
                                {'text': '#fallacies', 'correct': False},
                                {'text': '#algorithms', 'correct': False},
                            ],
                            'explanation': ''
                        },
                    ]
                },
            ]
        }
    ]
}

