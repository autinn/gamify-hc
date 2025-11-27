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
                        {
                            'question': 'An algorithm must process a list of transactions and flag duplicates. What are the essential components?',
                            'answers': [
                                {'text': 'Only input and output', 'correct': False},
                                {'text': 'Clear input, step-by-step procedure, termination condition, and defined output', 'correct': True},
                                {'text': 'Just a flowchart', 'correct': False},
                                {'text': 'Any working code', 'correct': False},
                            ],
                            'explanation': 'Algorithms require: well-defined inputs, unambiguous steps, guaranteed termination, and clear outputs.'
                        },
                        {
                            'question': 'A search algorithm must find a student record in a database of 100,000 entries. Comparing binary search (O(log n)) vs. linear search (O(n)), which is more efficient?',
                            'answers': [
                                {'text': 'Linear search, because it\'s simpler', 'correct': False},
                                {'text': 'Binary search, because it examines far fewer entries', 'correct': True},
                                {'text': 'Both are equally efficient', 'correct': False},
                                {'text': 'Efficiency doesn\'t matter with modern computers', 'correct': False},
                            ],
                            'explanation': 'Binary search requires ~17 comparisons vs. up to 100,000 for linear search, demonstrating algorithmic efficiency.'
                        },
                        {
                            'question': 'You write an algorithm to calculate factorial recursively but it crashes on large inputs. What\'s likely missing?',
                            'answers': [
                                {'text': 'Base case to ensure termination', 'correct': True},
                                {'text': 'More recursion', 'correct': False},
                                {'text': 'Faster hardware', 'correct': False},
                                {'text': 'Better variable names', 'correct': False},
                            ],
                            'explanation': 'Recursive algorithms need explicit base cases to terminate; without them, they recurse infinitely.'
                        },
                        {
                            'question': 'An algorithm sorts data correctly but takes hours on 10,000 items. What should you analyze?',
                            'answers': [
                                {'text': 'Only correctness matters', 'correct': False},
                                {'text': 'Time complexity—the algorithm may be inefficient (e.g., O(n²) instead of O(n log n))', 'correct': True},
                                {'text': 'Variable naming only', 'correct': False},
                                {'text': 'Code formatting', 'correct': False},
                            ],
                            'explanation': 'Time complexity determines scalability; inefficient algorithms become impractical with larger inputs.'
                        },
                        {
                            'question': 'Which demonstrates decomposition in algorithmic thinking?',
                            'answers': [
                                {'text': 'Writing one large function to do everything', 'correct': False},
                                {'text': 'Breaking "process order" into: validate payment, update inventory, send confirmation', 'correct': True},
                                {'text': 'Avoiding modularity', 'correct': False},
                                {'text': 'Using only loops, no functions', 'correct': False},
                            ],
                            'explanation': 'Decomposition breaks complex problems into manageable subproblems, each solvable by simpler algorithms.'
                        },
                        {
                            'question': 'An algorithm must handle edge cases: empty input, single item, and maximum capacity. Why is this important?',
                            'answers': [
                                {'text': 'Edge cases are rare and can be ignored', 'correct': False},
                                {'text': 'Robust algorithms handle boundary conditions explicitly to prevent failures', 'correct': True},
                                {'text': 'Edge cases only matter for testing', 'correct': False},
                                {'text': 'Algorithms should crash on edge cases', 'correct': False},
                            ],
                            'explanation': 'Edge cases expose algorithmic weaknesses; explicit handling ensures reliability in real-world conditions.'
                        },
                        {
                            'question': 'You design a route-planning algorithm. It produces correct paths but sometimes runs indefinitely on circular routes. What\'s the fix?',
                            'answers': [
                                {'text': 'Add more conditions randomly', 'correct': False},
                                {'text': 'Implement cycle detection and termination conditions', 'correct': True},
                                {'text': 'Ignore the problem', 'correct': False},
                                {'text': 'Use faster hardware', 'correct': False},
                            ],
                            'explanation': 'Algorithms must guarantee termination; cycle detection prevents infinite loops in graph traversal.'
                        },
                        {
                            'question': 'What distinguishes a greedy algorithm from other approaches?',
                            'answers': [
                                {'text': 'It always finds the optimal solution', 'correct': False},
                                {'text': 'It makes locally optimal choices at each step, which may not yield global optimum', 'correct': True},
                                {'text': 'It examines all possible solutions', 'correct': False},
                                {'text': 'It never works in practice', 'correct': False},
                            ],
                            'explanation': 'Greedy algorithms choose what looks best immediately; this works for some problems but not all.'
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
                        {
                            'question': 'Estimate how many piano tuners work in Chicago. Which approach applies Fermi estimation?',
                            'answers': [
                                {'text': 'Look up the exact number', 'correct': False},
                                {'text': 'Estimate: population → households → pianos → tunings/year → tuner capacity', 'correct': True},
                                {'text': 'Guess randomly', 'correct': False},
                                {'text': 'Assume it\'s unknowable', 'correct': False},
                            ],
                            'explanation': 'Fermi estimation decomposes unknowns into estimable factors, multiplying reasonable approximations.'
                        },
                        {
                            'question': 'You need to estimate project completion time. Historical similar projects took 8, 10, and 15 weeks. What\'s a reasonable estimate?',
                            'answers': [
                                {'text': 'Exactly 8 weeks (minimum)', 'correct': False},
                                {'text': '10-12 weeks, accounting for typical overruns', 'correct': True},
                                {'text': 'Exactly 15 weeks (maximum)', 'correct': False},
                                {'text': '1 week with aggressive timeline', 'correct': False},
                            ],
                            'explanation': 'Reference class forecasting uses historical data; median with buffer accounts for planning fallacy.'
                        },
                        {
                            'question': 'Estimate the weight of a blue whale without scales. Which method is most appropriate?',
                            'answers': [
                                {'text': 'Pure guessing', 'correct': False},
                                {'text': 'Use volume estimation (length × width × depth) × water density, then adjust', 'correct': True},
                                {'text': 'Ask for opinions and average them', 'correct': False},
                                {'text': 'It cannot be estimated', 'correct': False},
                            ],
                            'explanation': 'Physical estimation uses dimensional analysis and known constants to approximate unknowns.'
                        },
                        {
                            'question': 'When is a rough estimate (order of magnitude) sufficient vs. precise calculation?',
                            'answers': [
                                {'text': 'Precise calculation is always necessary', 'correct': False},
                                {'text': 'Rough estimates suffice for feasibility checks; precision needed for final decisions', 'correct': True},
                                {'text': 'Estimates are never useful', 'correct': False},
                                {'text': 'Precision doesn\'t matter', 'correct': False},
                            ],
                            'explanation': 'Estimation helps evaluate options quickly; precision matters when committing resources.'
                        },
                        {
                            'question': 'You estimate server capacity needs by multiplying: users × requests/user × data/request. One factor is off by 10x. What happens?',
                            'answers': [
                                {'text': 'The error cancels out', 'correct': False},
                                {'text': 'The final estimate is off by ~10x, potentially causing over/under-provisioning', 'correct': True},
                                {'text': 'It doesn\'t matter', 'correct': False},
                                {'text': 'The estimate becomes more accurate', 'correct': False},
                            ],
                            'explanation': 'Errors in component estimates compound multiplicatively; large errors in any factor dominate.'
                        },
                        {
                            'question': 'A city plans to estimate water usage. They have: population, average household size, and per-capita consumption data. What estimation technique applies?',
                            'answers': [
                                {'text': 'Bottom-up decomposition using available parameters', 'correct': True},
                                {'text': 'Pure intuition', 'correct': False},
                                {'text': 'Wait for perfect data', 'correct': False},
                                {'text': 'Random sampling only', 'correct': False},
                            ],
                            'explanation': 'Bottom-up estimation combines known quantities to approximate the target value.'
                        },
                        {
                            'question': 'Why round intermediate estimates to 1-2 significant figures in Fermi calculations?',
                            'answers': [
                                {'text': 'To introduce errors deliberately', 'correct': False},
                                {'text': 'False precision is misleading; rounding acknowledges uncertainty', 'correct': True},
                                {'text': 'Exact numbers are always better', 'correct': False},
                                {'text': 'Rounding makes math harder', 'correct': False},
                            ],
                            'explanation': 'Fermi estimation uses rough approximations; spurious precision implies accuracy that doesn\'t exist.'
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
                        {
                            'question': 'If it rains, the game is cancelled. It is raining. Therefore:',
                            'answers': [
                                {'text': 'The game might be cancelled', 'correct': False},
                                {'text': 'The game is cancelled', 'correct': True},
                                {'text': 'The game continues', 'correct': False},
                                {'text': 'Nothing follows', 'correct': False},
                            ],
                            'explanation': 'Modus ponens: P → Q; P; therefore Q.'
                        },
                        {
                            'question': 'All programmers know logic. Alice knows logic. Therefore Alice is a programmer. This reasoning is:',
                            'answers': [
                                {'text': 'Valid', 'correct': False},
                                {'text': 'Invalid—affirming the consequent', 'correct': True},
                                {'text': 'Sound', 'correct': False},
                                {'text': 'Modus ponens', 'correct': False},
                            ],
                            'explanation': 'From P → Q and Q, you cannot conclude P. Others who aren\'t programmers may also know logic.'
                        },
                        {
                            'question': 'Either the server is down or the network is slow. The server is not down. Therefore:',
                            'answers': [
                                {'text': 'Both are down', 'correct': False},
                                {'text': 'The network is slow', 'correct': True},
                                {'text': 'Nothing follows', 'correct': False},
                                {'text': 'The server is fast', 'correct': False},
                            ],
                            'explanation': 'Disjunctive syllogism: P ∨ Q; ¬P; therefore Q.'
                        },
                        {
                            'question': 'What makes deductive reasoning different from inductive reasoning?',
                            'answers': [
                                {'text': 'Deduction is always wrong', 'correct': False},
                                {'text': 'Deduction guarantees the conclusion if premises are true; induction provides probable conclusions', 'correct': True},
                                {'text': 'Induction is always better', 'correct': False},
                                {'text': 'They are identical', 'correct': False},
                            ],
                            'explanation': 'Deduction is truth-preserving; valid deductive arguments cannot have true premises and false conclusions.'
                        },
                        {
                            'question': 'If a number is divisible by 6, it is divisible by 3. The number 18 is divisible by 6. What follows deductively?',
                            'answers': [
                                {'text': 'Nothing certain', 'correct': False},
                                {'text': '18 is divisible by 3', 'correct': True},
                                {'text': '18 might not be divisible by 3', 'correct': False},
                                {'text': '18 is not divisible by 3', 'correct': False},
                            ],
                            'explanation': 'Modus ponens applied to mathematical facts yields certain conclusions.'
                        },
                        {
                            'question': 'All arguments with true premises and valid form are:',
                            'answers': [
                                {'text': 'Invalid', 'correct': False},
                                {'text': 'Sound', 'correct': True},
                                {'text': 'Inductive', 'correct': False},
                                {'text': 'Fallacious', 'correct': False},
                            ],
                            'explanation': 'Soundness = validity + true premises.'
                        },
                        {
                            'question': 'Given: All mammals are warm-blooded. Whales are mammals. What can be deduced?',
                            'answers': [
                                {'text': 'Whales might be warm-blooded', 'correct': False},
                                {'text': 'Whales are warm-blooded', 'correct': True},
                                {'text': 'Whales are cold-blooded', 'correct': False},
                                {'text': 'Nothing certain', 'correct': False},
                            ],
                            'explanation': 'Categorical syllogism: All A are B; C is A; therefore C is B.'
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
                        {
                            'question': '"If we allow students to redo exams, soon they\'ll demand unlimited retakes and academic standards will collapse."',
                            'answers': [
                                {'text': 'Slippery slope', 'correct': True},
                                {'text': 'Straw man', 'correct': False},
                                {'text': 'False dichotomy', 'correct': False},
                                {'text': 'Appeal to authority', 'correct': False},
                            ],
                            'explanation': 'Assumes one step inevitably leads to extreme consequences without justification.'
                        },
                        {
                            'question': '"Everyone is switching to electric cars, so you should too."',
                            'answers': [
                                {'text': 'Ad hominem', 'correct': False},
                                {'text': 'Bandwagon (appeal to popularity)', 'correct': True},
                                {'text': 'Red herring', 'correct': False},
                                {'text': 'Circular reasoning', 'correct': False},
                            ],
                            'explanation': 'Appeals to popularity as evidence rather than merit.'
                        },
                        {
                            'question': '"We must choose between complete freedom or total government control."',
                            'answers': [
                                {'text': 'False dichotomy (false dilemma)', 'correct': True},
                                {'text': 'Slippery slope', 'correct': False},
                                {'text': 'Appeal to ignorance', 'correct': False},
                                {'text': 'Circular reasoning', 'correct': False},
                            ],
                            'explanation': 'Presents only two options when more exist; ignores middle ground.'
                        },
                        {
                            'question': '"This medicine works because it has healing properties." What fallacy?',
                            'answers': [
                                {'text': 'Circular reasoning (begging the question)', 'correct': True},
                                {'text': 'Straw man', 'correct': False},
                                {'text': 'Ad hominem', 'correct': False},
                                {'text': 'Appeal to authority', 'correct': False},
                            ],
                            'explanation': 'The conclusion ("works") is restated in the premise ("healing properties") without independent evidence.'
                        },
                        {
                            'question': '"A famous actor endorses this investment strategy, so it must be sound."',
                            'answers': [
                                {'text': 'Hasty generalization', 'correct': False},
                                {'text': 'Appeal to false authority', 'correct': True},
                                {'text': 'Slippery slope', 'correct': False},
                                {'text': 'Post hoc', 'correct': False},
                            ],
                            'explanation': 'Appeals to authority outside their area of expertise; actors aren\'t financial experts.'
                        },
                        {
                            'question': '"After the mayor took office, crime increased. Therefore, the mayor caused the crime increase."',
                            'answers': [
                                {'text': 'Post hoc ergo propter hoc (false cause)', 'correct': True},
                                {'text': 'Circular reasoning', 'correct': False},
                                {'text': 'Straw man', 'correct': False},
                                {'text': 'Appeal to ignorance', 'correct': False},
                            ],
                            'explanation': 'Assumes temporal sequence implies causation without ruling out other factors.'
                        },
                        {
                            'question': '"You say we should reduce carbon emissions, but you drove here in a car!"',
                            'answers': [
                                {'text': 'Tu quoque (appeal to hypocrisy)', 'correct': True},
                                {'text': 'Bandwagon', 'correct': False},
                                {'text': 'False dichotomy', 'correct': False},
                                {'text': 'Slippery slope', 'correct': False},
                            ],
                            'explanation': 'Dismisses an argument by pointing out the arguer\'s inconsistency rather than addressing the argument\'s merit.'
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
                        {
                            'question': 'Every swan observed in Europe for 1,000 years was white. Conclusion: "All swans are white." What happened when explorers found Australia?',
                            'answers': [
                                {'text': 'The inductive conclusion was proven certain', 'correct': False},
                                {'text': 'Black swans disproved the generalization, showing induction\'s limits', 'correct': True},
                                {'text': 'The observations were irrelevant', 'correct': False},
                                {'text': 'Deduction would have failed too', 'correct': False},
                            ],
                            'explanation': 'Induction provides probability, not certainty; new evidence can overturn generalizations.'
                        },
                        {
                            'question': 'A doctor observes that 95% of patients with symptom X have disease Y. A new patient presents with symptom X. What can be inferred?',
                            'answers': [
                                {'text': 'The patient definitely has disease Y', 'correct': False},
                                {'text': 'The patient probably has disease Y', 'correct': True},
                                {'text': 'The patient definitely does not have disease Y', 'correct': False},
                                {'text': 'No inference is possible', 'correct': False},
                            ],
                            'explanation': 'Inductive reasoning from statistical patterns yields probable, not certain, conclusions.'
                        },
                        {
                            'question': 'What strengthens an inductive argument?',
                            'answers': [
                                {'text': 'Smaller sample size', 'correct': False},
                                {'text': 'Larger, more representative sample and consistent patterns', 'correct': True},
                                {'text': 'Ignoring counterexamples', 'correct': False},
                                {'text': 'Emotional appeals', 'correct': False},
                            ],
                            'explanation': 'Inductive strength increases with sample size, representativeness, and pattern consistency.'
                        },
                        {
                            'question': 'A company finds that their top 5 salespeople all started in customer service. They conclude: "Customer service experience makes great salespeople." What could weaken this induction?',
                            'answers': [
                                {'text': 'The sample is too small and may not be representative', 'correct': True},
                                {'text': 'This is deductive, not inductive reasoning', 'correct': False},
                                {'text': 'The conclusion is definitely false', 'correct': False},
                                {'text': 'Induction cannot be weakened', 'correct': False},
                            ],
                            'explanation': 'Small samples and selection bias weaken inductive generalizations.'
                        },
                        {
                            'question': '"The sun has risen every day for billions of years, so it will rise tomorrow." This is:',
                            'answers': [
                                {'text': 'Deductively certain', 'correct': False},
                                {'text': 'A strong inductive inference based on consistent patterns', 'correct': True},
                                {'text': 'A fallacy', 'correct': False},
                                {'text': 'Impossible to evaluate', 'correct': False},
                            ],
                            'explanation': 'Induction from overwhelming consistent evidence yields high confidence, though not logical certainty.'
                        },
                        {
                            'question': 'Scientific theories are supported by:',
                            'answers': [
                                {'text': 'Pure deduction from axioms', 'correct': False},
                                {'text': 'Inductive reasoning from repeated observations and experiments', 'correct': True},
                                {'text': 'Personal beliefs only', 'correct': False},
                                {'text': 'Authority alone', 'correct': False},
                            ],
                            'explanation': 'Science uses induction: generalizing from observed instances to form theories, which remain probabilistic.'
                        },
                        {
                            'question': 'A survey of 10,000 voters shows 52% support a candidate. Conclusion: "The candidate will likely win." What makes this induction strong?',
                            'answers': [
                                {'text': 'It guarantees victory', 'correct': False},
                                {'text': 'Large, representative sample size and clear majority pattern', 'correct': True},
                                {'text': 'The candidate is popular', 'correct': False},
                                {'text': 'Surveys are always accurate', 'correct': False},
                            ],
                            'explanation': 'Strong induction requires adequate sample size and representativeness; it still yields probability, not certainty.'
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


