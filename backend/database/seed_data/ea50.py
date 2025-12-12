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
                                {'text': 'Constraint list', 'correct': False, 'explanation': 'Constraints are important, but consequences of inaction are critical for robust problem characterization.'},
                                {'text': 'Future implications of the problem', 'correct': True, 'explanation': 'Correct! Including future implications ensures a complete understanding of the problem.'},
                                {'text': 'Budget section only', 'correct': False, 'explanation': 'Budget is important, but it does not address the consequences of inaction.'},
                                {'text': 'SWOT table', 'correct': False, 'explanation': 'A SWOT table is useful, but it does not replace the need to consider future implications.'},
                            ],
                        },
                        {
                            'question': 'A hospital aims to "reduce patient complaints" but doesn\'t specify which types of complaints or current frequency. Why is this problematic?',
                            'answers': [
                                {'text': 'The goal is too ambitious', 'correct': False, 'explanation': 'Ambition is not the issue; the lack of specificity and baseline data is.'},
                                {'text': 'Without baseline data and specificity, success cannot be measured', 'correct': True, 'explanation': 'Correct! Specificity and baseline data are essential for measuring success.'},
                                {'text': 'Complaints are not important', 'correct': False, 'explanation': 'Complaints are important, but they need to be clearly defined to address them effectively.'},
                                {'text': 'Solutions should come before measurement', 'correct': False, 'explanation': 'Jumping to solutions without measurement is premature.'},
                            ],
                        },
                        {
                            'question': 'A startup identifies "low user engagement" as their problem but hasn\'t examined which features users actually use or why they leave. What critical step is missing?',
                            'answers': [
                                {'text': 'Defining the goal state', 'correct': False, 'explanation': 'Defining the goal state is important, but understanding the initial state comes first.'},
                                {'text': 'Characterizing the initial state through data analysis', 'correct': True, 'explanation': 'Correct! Data analysis of the initial state is critical to understanding user behavior.'},
                                {'text': 'Listing constraints', 'correct': False, 'explanation': 'Constraints are important but do not replace the need for initial state analysis.'},
                                {'text': 'Brainstorming solutions', 'correct': False, 'explanation': 'Brainstorming solutions without understanding the problem is ineffective.'},
                            ],
                        },
                        {
                            'question': 'Two teams tackle food waste. Team A defines the goal as "implement composting programs." Team B defines it as "reduce cafeteria waste by 40% within 6 months." Which follows #rightproblem better?',
                            'answers': [
                                {'text': 'Team A, because composting is a proven solution', 'correct': False, 'explanation': 'Team A presupposes a solution, which limits flexibility.'},
                                {'text': 'Team B, because they specify measurable outcomes without presupposing one solution', 'correct': True, 'explanation': 'Correct! Team B focuses on measurable outcomes, leaving room for multiple solutions.'},
                                {'text': 'Both equally, since goals are subjective', 'correct': False, 'explanation': 'Goals are not purely subjective; measurable outcomes are preferable.'},
                                {'text': 'Neither, since waste reduction is too vague', 'correct': False, 'explanation': 'Waste reduction is not vague when paired with specific metrics like Team B\'s goal.'},
                            ],
                        },
                        {
                            'question': 'A school says "students are failing math" but hasn\'t identified whether the issue is foundational gaps, teaching methods, or motivation. What should they do first?',
                            'answers': [
                                {'text': 'Hire more tutors immediately', 'correct': False, 'explanation': 'Hiring tutors may help, but it\'s not the first step without understanding the problem.'},
                                {'text': 'Characterize the problem by analyzing failure patterns and root causes', 'correct': True, 'explanation': 'Correct! Analyzing failure patterns will identify the real issues needing addressal.'},
                                {'text': 'Switch to a new curriculum', 'correct': False, 'explanation': 'Changing the curriculum might not address the underlying issues causing the failures.'},
                                {'text': 'Increase homework assignments', 'correct': False, 'explanation': 'More homework won\'t help if the fundamental problems are not addressed.'},
                            ],
                        },
                        {
                            'question': 'A company characterizes a problem with initial state, goal state, and obstacles—but omits constraints like budget and regulatory requirements. What risk does this create?',
                            'answers': [
                                {'text': 'The problem becomes too easy to solve', 'correct': False, 'explanation': 'Ignoring constraints does not make the problem easier; it makes solutions impractical.'},
                                {'text': 'Solutions may be infeasible or illegal', 'correct': True, 'explanation': 'Correct! Ignoring constraints can lead to solutions that are not feasible or legal.'},
                                {'text': 'Obstacles will disappear', 'correct': False, 'explanation': 'Obstacles do not disappear just because constraints are ignored.'},
                                {'text': 'The initial state will change', 'correct': False, 'explanation': 'The initial state remains the same regardless of whether constraints are considered.'},
                            ],
                        },
                        {
                            'question': 'A nonprofit states their problem as "need more funding" rather than "cannot serve 200+ families on waitlist due to capacity limits." Which framing better applies #rightproblem?',
                            'answers': [
                                {'text': 'The first, because funding is always the core issue', 'correct': False, 'explanation': 'Framing the problem as a resource need limits solution options.'},
                                {'text': 'The second, because it describes the real problem and goal state without presupposing one solution', 'correct': True, 'explanation': 'Correct! This framing focuses on the outcome and opens up multiple solution pathways.'},
                                {'text': 'Both are equally valid', 'correct': False, 'explanation': 'The second framing is more effective because it avoids presupposing a solution.'},
                                {'text': 'Neither, since nonprofits should not define problems', 'correct': False, 'explanation': 'Nonprofits must define problems to address them effectively.'},
                            ],
                        },
                        {
                            'question': 'An urban planning team characterizes traffic congestion by documenting peak hours, bottleneck locations, commuter origins, and economic costs. What component would complete their characterization?',
                            'answers': [
                                {'text': 'A list of potential solutions', 'correct': False, 'explanation': 'Listing solutions is premature without fully characterizing the problem.'},
                                {'text': 'Projected consequences if congestion continues unchecked', 'correct': True, 'explanation': 'Correct! Considering future implications completes the problem characterization.'},
                                {'text': 'A detailed budget breakdown', 'correct': False, 'explanation': 'A budget breakdown is useful but does not complete the characterization.'},
                                {'text': 'Stakeholder voting results', 'correct': False, 'explanation': 'Stakeholder input is important but not the missing component here.'},
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
                                {'text': 'Core mechanism', 'correct': False, 'explanation': 'The core mechanism is often the key to why the analogy works.'},
                                {'text': 'Domain-specific regulation irrelevant to target', 'correct': True, 'explanation': 'Correct! Irrelevant regulations should be discarded as they don\'t apply to the new context.'},
                                {'text': 'Structural mapping', 'correct': False, 'explanation': 'Structural mapping is essential to maintain the integrity of the analogy.'},
                                {'text': 'Performance criterion', 'correct': False, 'explanation': 'The performance criterion is usually central to the analogy\'s effectiveness.'},
                            ],
                        },
                        {
                            'question': 'A designer uses ant colony optimization (how ants find food) to route delivery trucks efficiently. What makes this a strong analogy?',
                            'answers': [
                                {'text': 'Ants and trucks both move', 'correct': False, 'explanation': 'Movement alone does not constitute a strong analogy; the underlying principles matter.'},
                                {'text': 'Both systems solve path optimization through decentralized feedback', 'correct': True, 'explanation': 'Exactly! Both systems use decentralized feedback for optimization, making this a strong analogy.'},
                                {'text': 'The metaphor sounds interesting', 'correct': False, 'explanation': 'Interest value of a metaphor does not determine the strength of an analogy.'},
                                {'text': 'Ants are commonly studied', 'correct': False, 'explanation': 'Common study of ants does not directly relate to the validity of the analogy for this problem.'},
                            ],
                        },
                        {
                            'question': 'A city borrows "immune system response" to model epidemic containment: detect threats, isolate infections, mobilize resources. What must they adapt?',
                            'answers': [
                                {'text': 'Nothing—biological systems translate directly', 'correct': False, 'explanation': 'This is incorrect; direct translation ignores critical differences between biological and social systems.'},
                                {'text': 'Scale, timescales, and human behavioral factors absent in cellular immunity', 'correct': True, 'explanation': 'Correct! These factors are crucial to consider when adapting the analogy to a new domain.'},
                                {'text': 'The entire analogy should be discarded', 'correct': False, 'explanation': 'Discarding the entire analogy is not necessary; only certain aspects need adaptation.'},
                                {'text': 'Only visual metaphors', 'correct': False, 'explanation': 'Adapting only visual metaphors is insufficient; the underlying concepts also need adaptation.'},
                            ],
                        },
                        {
                            'question': 'A software team applies "assembly line" principles to code review: each reviewer checks one specific aspect sequentially. What structural similarity justifies this analogy?',
                            'answers': [
                                {'text': 'Both involve computers', 'correct': False, 'explanation': 'Involvement of computers is not a structural similarity; it\'s a superficial characteristic.'},
                                {'text': 'Both use sequential specialization to improve quality and efficiency', 'correct': True, 'explanation': 'Exactly! This structural similarity justifies the analogy between assembly lines and the code review process.'},
                                {'text': 'Code and manufacturing are unrelated', 'correct': False, 'explanation': 'This is too broad; while different, there are relevant similarities in processes.'},
                                {'text': 'Assembly lines are outdated', 'correct': False, 'explanation': 'The potential outdatedness of assembly lines does not affect the validity of the analogy if the structure still applies.'},
                            ],
                        },
                        {
                            'question': 'When applying analogical reasoning, why is it risky to rely on surface similarities (e.g., "schools and prisons both have cafeterias")?',
                            'answers': [
                                {'text': 'Surface features often don\'t reflect structural or functional similarities', 'correct': True, 'explanation': 'Exactly! Relying on surface similarities can be misleading if the underlying structures are different.'},
                                {'text': 'Cafeterias are unimportant', 'correct': False, 'explanation': 'The importance of cafeterias is not the issue; it\'s the relevance of the similarity being considered.'},
                                {'text': 'All similarities are equally valid', 'correct': False, 'explanation': 'This is incorrect; some similarities are more relevant and telling than others.'},
                                {'text': 'Analogies should never compare institutions', 'correct': False, 'explanation': 'Comparing institutions can be valid; the key is in the relevance and depth of the comparison.'},
                            ],
                        },
                        {
                            'question': 'A team uses "Netflix recommendation algorithms" as an analogy for suggesting personalized learning paths in education. What challenge must they address?',
                            'answers': [
                                {'text': 'Students and viewers are identical', 'correct': False, 'explanation': 'This is not true; students and viewers have different contexts, needs, and goals.'},
                                {'text': 'Educational goals differ from entertainment engagement; success metrics must be redefined', 'correct': True, 'explanation': 'Correct! The analogy requires adaptation of success metrics to fit the educational context.'},
                                {'text': 'The analogy is completely invalid', 'correct': False, 'explanation': 'The analogy is not completely invalid; it just needs careful adaptation to the new context.'},
                                {'text': 'Algorithms cannot be applied to education', 'correct': False, 'explanation': 'This is too broad; while direct application may be flawed, adapted algorithms can be useful.'},
                            ],
                        },
                        {
                            'question': 'A business consultant suggests "a company is like a sports team" to improve collaboration. When does this analogy break down?',
                            'answers': [
                                {'text': 'Companies and teams both have members', 'correct': False, 'explanation': 'Having members is too vague a similarity; the structures and goals of the entities matter more.'},
                                {'text': 'Corporate goals are often more ambiguous and long-term than game outcomes', 'correct': True, 'explanation': 'Exactly! This difference in goal clarity and timeframe can limit the analogy\'s applicability.'},
                                {'text': 'Sports teams never collaborate', 'correct': False, 'explanation': 'This is false; sports teams often collaborate with other teams, coaches, and staff.'},
                                {'text': 'All organizational analogies are perfect', 'correct': False, 'explanation': 'This is not true; analogies can be helpful but are never perfect due to the uniqueness of each organization.'},
                            ],
                        },
                        {
                            'question': 'Researchers apply "traffic flow models" to analyze data packet routing in computer networks. What validates this cross-domain analogy?',
                            'answers': [
                                {'text': 'Cars and data are both physical objects', 'correct': False, 'explanation': 'This is too superficial; the validity of an analogy depends on deeper structural similarities.'},
                                {'text': 'Both systems exhibit congestion, bottlenecks, and throughput optimization challenges', 'correct': True, 'explanation': 'Exactly! These shared characteristics validate the use of traffic flow models as an analogy for data packet routing.'},
                                {'text': 'Traffic and networks are unrelated', 'correct': False, 'explanation': 'This is not true; there are relevant similarities that make the analogy valid.'},
                                {'text': 'All analogies between transport and computing work', 'correct': False, 'explanation': 'This is too broad; each analogy must be evaluated on its own merits and relevance.'},
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
                                {'text': 'Keep it a constraint', 'correct': False, 'explanation': 'If it can be repaired, it should not be classified as a constraint which is typically fixed.'},
                                {'text': 'Reframe as an obstacle and plan remediation', 'correct': True, 'explanation': 'Correct! This allows for addressing the issue directly rather than treating it as an unchangeable constraint.'},
                                {'text': 'Remove it entirely', 'correct': False, 'explanation': 'This is not feasible if the equipment is essential and the failure is reparable.'},
                                {'text': 'Treat it as a success metric', 'correct': False, 'explanation': 'This is incorrect; it does not measure success but rather indicates a problem that needs fixing.'},
                            ],
                        },
                        {
                            'question': 'A team must schedule a conference with 5 constraints: venue availability, speaker schedules, budget limits, accessibility requirements, and catering lead times. What approach applies #constraints?',
                            'answers': [
                                {'text': 'Pick one constraint and ignore the rest', 'correct': False, 'explanation': 'This is not feasible as multiple constraints must be satisfied simultaneously.'},
                                {'text': 'Find a solution that simultaneously satisfies all 5 constraints', 'correct': True, 'explanation': 'Yes, this is the correct approach to satisfy all constraints.'},
                                {'text': 'Remove constraints until the problem is easy', 'correct': False, 'explanation': 'This is not a valid approach as it may lead to overlooking important factors.'},
                                {'text': 'Prioritize constraints and violate lower-priority ones', 'correct': False, 'explanation': 'This could lead to significant issues if lower-priority constraints are violated.'},
                            ],
                        },
                        {
                            'question': 'A city faces "traffic congestion during construction season." Is the construction a constraint or an obstacle?',
                            'answers': [
                                {'text': 'Obstacle, because construction can be rescheduled or phased differently', 'correct': True, 'explanation': 'Correct! Construction is an obstacle that can be managed, not a fixed constraint.'},
                                {'text': 'Constraint, because construction is happening', 'correct': False, 'explanation': 'This is incorrect; construction is an obstacle that affects traffic flow.'},
                                {'text': 'Neither, because it\'s temporary', 'correct': False, 'explanation': 'The temporary nature does not change the fact that it is an obstacle.'},
                                {'text': 'Both equally', 'correct': False, 'explanation': 'This is not accurate; it is primarily an obstacle.'},
                            ],
                        },
                        {
                            'question': 'A software project has hard constraints (regulatory compliance, system compatibility) and soft preferences (user interface aesthetics). How should they be treated?',
                            'answers': [
                                {'text': 'Treat preferences as constraints to simplify', 'correct': False, 'explanation': 'This is incorrect; preferences are not constraints and should not be treated as such.'},
                                {'text': 'Satisfy hard constraints first; optimize preferences within feasible solutions', 'correct': True, 'explanation': 'Correct! This ensures that essential requirements are met while still considering preferences.'},
                                {'text': 'Ignore hard constraints if they conflict with preferences', 'correct': False, 'explanation': 'This is not feasible as hard constraints are non-negotiable requirements.'},
                                {'text': 'All constraints are equally negotiable', 'correct': False, 'explanation': 'This is not true; some constraints are fixed while others are flexible.'},
                            ],
                        },
                        {
                            'question': 'A meal planner must satisfy: dietary restrictions (vegan, nut-free), budget ($50), prep time (under 2 hours), and ingredient availability. Two menus meet all constraints. What should guide the final choice?',
                            'answers': [
                                {'text': 'Additional preferences like taste or nutrition balance', 'correct': True, 'explanation': 'Yes! Additional preferences should guide the final choice between equally viable options.'},
                                {'text': 'Randomly select one', 'correct': False, 'explanation': 'This is not a good idea as it does not consider the best option available.'},
                                {'text': 'Add more constraints until only one remains', 'correct': False, 'explanation': 'This is not practical or necessary; the goal is to find a satisfactory solution, not to eliminate options.'},
                                {'text': 'Violate one constraint to simplify', 'correct': False, 'explanation': 'This is not advisable as it could lead to an unsatisfactory or unviable solution.'},
                            ],
                        },
                        {
                            'question': 'A warehouse layout must accommodate: fire safety codes (constraint), forklift turning radii (constraint), and "easy access to popular items" (preference). What distinguishes the constraint from the preference?',
                            'answers': [
                                {'text': 'Constraints are legally mandated or physically necessary; preferences are desirable but negotiable', 'correct': True, 'explanation': 'Exactly! Constraints are mandatory requirements, while preferences are additional desirable factors.'},
                                {'text': 'Preferences are always more important', 'correct': False, 'explanation': 'This is not true; preferences are not more important than constraints.'},
                                {'text': 'Constraints can be violated with enough creativity', 'correct': False, 'explanation': 'This is incorrect; constraints are fixed and cannot be violated.'},
                                {'text': 'There is no distinction', 'correct': False, 'explanation': 'This is not accurate; there is a clear distinction between constraints and preferences.'},
                            ],
                        },
                        {
                            'question': 'A project faces "insufficient expertise in the team" and "a non-negotiable December deadline." Which is the constraint?',
                            'answers': [
                                {'text': 'The expertise gap, because it limits capability', 'correct': False, 'explanation': 'This is not a constraint; it is a gap that needs to be addressed.'},
                                {'text': 'The December deadline, because it cannot be changed', 'correct': True, 'explanation': 'Correct! The December deadline is a fixed constraint that must be met.'},
                                {'text': 'Both are constraints', 'correct': False, 'explanation': 'This is not accurate; only the December deadline is a constraint.'},
                                {'text': 'Neither—both are just challenges', 'correct': False, 'explanation': 'This is incorrect; the December deadline is a clear constraint.'},
                            ],
                        },
                        {
                            'question': 'A school must assign 30 teachers to 30 classrooms, ensuring each teacher\'s subject matches room equipment, schedule fits personal constraints, and no room is double-booked. This is an example of:',
                            'answers': [
                                {'text': 'A heuristic problem', 'correct': False, 'explanation': 'This is not a heuristic problem; it is a complex problem with multiple constraints.'},
                                {'text': 'A constraint satisfaction problem', 'correct': True, 'explanation': 'Exactly! This problem requires satisfying multiple constraints simultaneously.'},
                                {'text': 'An unconstrained optimization', 'correct': False, 'explanation': 'This is not an unconstrained optimization problem; there are clear constraints that must be met.'},
                                {'text': 'A purely creative task', 'correct': False, 'explanation': 'This task is not purely creative; it requires careful consideration of constraints.'},
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
                                {'text': 'Overweight vivid recent events when estimating likelihoods', 'correct': True, 'explanation': 'Exactly! This heuristic leads people to give undue weight to recent, memorable events.'},
                                {'text': 'Confuse similarity with probability', 'correct': False, 'explanation': 'This is more related to the representativeness heuristic.'},
                                {'text': 'Anchor on a starting number only', 'correct': False, 'explanation': 'This describes the anchoring heuristic, not the availability heuristic.'},
                                {'text': 'Use affectless calculation', 'correct': False, 'explanation': 'The availability heuristic is not about calculation; it\'s about biased recall.'},
                            ],
                        },
                        {
                            'question': 'A doctor quickly diagnoses a patient based on the most common symptoms matching typical cases. This uses which heuristic?',
                            'answers': [
                                {'text': 'Anchoring', 'correct': False, 'explanation': 'This is not anchoring; it\'s using representative symptoms to make a quick diagnosis.'},
                                {'text': 'Representativeness', 'correct': True, 'explanation': 'Correct! This is an example of the representativeness heuristic in action.'},
                                {'text': 'Means-ends analysis', 'correct': False, 'explanation': 'This is not means-ends analysis; it\'s a quick, heuristic-based diagnosis.'},
                                {'text': 'Constraint satisfaction', 'correct': False, 'explanation': 'This is not about satisfying constraints; it\'s about matching symptoms to diagnoses.'},
                            ],
                        },
                        {
                            'question': 'A manager sets project timelines by starting with an initial estimate (30 days) and adjusting slightly upward (35 days). What heuristic bias might occur?',
                            'answers': [
                                {'text': 'Anchoring—the initial 30 days overly influences the final estimate', 'correct': True, 'explanation': 'Exactly! This is a classic case of anchoring bias in decision making.'},
                                {'text': 'Availability', 'correct': False, 'explanation': 'This is not related to the availability heuristic; it\'s about anchoring to an initial value.'},
                                {'text': 'Means-ends analysis', 'correct': False, 'explanation': 'This is not means-ends analysis; it\'s a biased adjustment of an initial estimate.'},
                                {'text': 'Representativeness', 'correct': False, 'explanation': 'This is not representativeness; it\'s a cognitive bias affecting the estimate.'},
                            ],
                        },
                        {
                            'question': 'A team uses means-ends analysis to plan a product launch: identify launch date (goal), determine current readiness (initial state), then define subgoals (complete testing, finalize marketing). What makes this effective?',
                            'answers': [
                                {'text': 'It relies on random exploration', 'correct': False, 'explanation': 'This is not random; it\'s a systematic approach to problem-solving.'},
                                {'text': 'It systematically decomposes the gap into manageable subgoals', 'correct': True, 'explanation': 'Exactly! This systematic decomposition is key to effective means-ends analysis.'},
                                {'text': 'It ignores constraints', 'correct': False, 'explanation': 'This is not true; effective means-ends analysis considers relevant constraints.'},
                                {'text': 'It avoids planning altogether', 'correct': False, 'explanation': 'This is incorrect; means-ends analysis is a form of planning.'},
                            ],
                        },
                        {
                            'question': 'After a plane crash receives heavy media coverage, people overestimate flight risks despite statistical safety. Which heuristic explains this?',
                            'answers': [
                                {'text': 'Availability—vivid recent events are easily recalled', 'correct': True, 'explanation': 'Exactly! This is a clear example of the availability heuristic affecting risk perception.'},
                                {'text': 'Representativeness', 'correct': False, 'explanation': 'This is not related to representativeness; it\'s about the availability of recent, vivid memories.'},
                                {'text': 'Anchoring', 'correct': False, 'explanation': 'This is not anchoring; it\'s a biased recall of recent events that skews perception of risk.'},
                                {'text': 'Means-ends', 'correct': False, 'explanation': 'This is not means-ends analysis; it\'s a cognitive bias affecting judgment.'},
                            ],
                        },
                        {
                            'question': 'When should you avoid heuristics and use comprehensive analysis instead?',
                            'answers': [
                                {'text': 'When making low-stakes decisions with time pressure', 'correct': False, 'explanation': 'This is a good situation for heuristics; comprehensive analysis is not always feasible.'},
                                {'text': 'When decisions are high-stakes with available data and time for thorough evaluation', 'correct': True, 'explanation': 'Exactly! High-stakes decisions with available data require careful, comprehensive analysis.'},
                                {'text': 'Always—heuristics are never useful', 'correct': False, 'explanation': 'This is too rigid; heuristics can be very useful in the right circumstances.'},
                                {'text': 'Only for creative tasks', 'correct': False, 'explanation': 'This is not accurate; heuristics can be used in various types of tasks, not just creative ones.'},
                            ],
                        },
                        {
                            'question': 'A hiring manager judges a candidate as "highly competent" because they attended a prestigious school, without reviewing actual work samples. Which heuristic is active?',
                            'answers': [
                                {'text': 'Representativeness—prestige signals competence via similarity to successful prototypes', 'correct': True, 'explanation': 'Exactly! This is an example of the representativeness heuristic based on social stereotypes.'},
                                {'text': 'Availability', 'correct': False, 'explanation': 'This is not related to the availability heuristic; it\'s about making judgments based on perceived similarities.'},
                                {'text': 'Means-ends', 'correct': False, 'explanation': 'This is not means-ends analysis; it\'s a heuristic based on representativeness.'},
                                {'text': 'Constraint satisfaction', 'correct': False, 'explanation': 'This is not about satisfying constraints; it\'s about judging competence based on school prestige.'},
                            ],
                        },
                        {
                            'question': 'A software team uses "working backward" from the desired user experience to identify necessary features and then current capabilities. What problem-solving approach is this?',
                            'answers': [
                                {'text': 'Random trial and error', 'correct': False, 'explanation': 'This is not random; it\'s a systematic approach to identifying necessary features.'},
                                {'text': 'Means-ends analysis', 'correct': True, 'explanation': 'Exactly! This approach involves working backward to identify and close the gap between current capabilities and desired features.'},
                                {'text': 'Anchoring heuristic', 'correct': False, 'explanation': 'This is not anchoring; it\'s a focused analysis of means and ends.'},
                                {'text': 'Availability heuristic', 'correct': False, 'explanation': 'This is not about availability; it\'s a systematic means-ends analysis.'},
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
                                {'text': 'Think it Through → retrieval cues; Make and Use Associations → deep processing', 'correct': False, 'explanation': 'This is not the correct pairing according to Kosslyn\'s Maxims.'},
                                {'text': 'Think it Through → deep processing; Make and Use Associations → rich retrieval cues', 'correct': True, 'explanation': 'Correct! This pairing aligns with Kosslyn\'s Maxims for effective learning.'},
                                {'text': 'Think it Through → dual codes only; Make and Use Associations → spacing only', 'correct': False, 'explanation': 'This is not accurate; the maxims involve broader principles than just dual codes and spacing.'},
                                {'text': 'Both maxims → massed practice', 'correct': False, 'explanation': 'This is incorrect; massed practice is not aligned with the principles of spaced practice and retrieval practice.'},
                            ],
                        },
                        {
                            'question': 'A student studies biology by creating concept maps linking terms, testing themselves weekly, and teaching concepts to peers. Which science of learning principles are applied?',
                            'answers': [
                                {'text': 'Highlighting and rereading only', 'correct': False, 'explanation': 'This is not correct; the student is using more active and effective strategies.'},
                                {'text': 'Deep processing, retrieval practice, and elaboration', 'correct': True, 'explanation': 'Exactly! These principles are all about actively engaging with the material for better learning.'},
                                {'text': 'Massed practice and passive review', 'correct': False, 'explanation': 'This is not accurate; the student is using spaced practice, not massed practice.'},
                                {'text': 'Cramming and surface-level review', 'correct': False, 'explanation': 'This is incorrect; the student is using effective, active learning strategies, not cramming.'},
                            ],
                        },
                        {
                            'question': 'Why is spaced practice more effective than massed practice (cramming) for long-term retention?',
                            'answers': [
                                {'text': 'It takes less total time', 'correct': False, 'explanation': 'This is not true; spaced practice may take more time but is more effective for retention.'},
                                {'text': 'Spacing allows consolidation and strengthens retrieval pathways', 'correct': True, 'explanation': 'Exactly! Spacing out practice sessions helps to consolidate learning and strengthen memory retrieval pathways.'},
                                {'text': 'Cramming always produces better results', 'correct': False, 'explanation': 'This is not true; cramming is less effective for long-term retention compared to spaced practice.'},
                                {'text': 'Spaced practice eliminates the need for review', 'correct': False, 'explanation': 'This is incorrect; spaced practice actually emphasizes the importance of review for reinforcement.'},
                            ],
                        },
                        {
                            'question': 'A teacher presents a lesson using diagrams, verbal explanations, and hands-on activities. Which learning principle is being applied?',
                            'answers': [
                                {'text': 'Massed practice', 'correct': False, 'explanation': 'This is not massed practice; it\'s an integrated approach using multiple modalities.'},
                                {'text': 'Dual coding—combining verbal and visual modalities', 'correct': True, 'explanation': 'Exactly! This approach uses dual coding to enhance learning through multiple channels.'},
                                {'text': 'Interference', 'correct': False, 'explanation': 'This is not interference; it\'s a well-structured, multimodal teaching approach.'},
                                {'text': 'Rote memorization', 'correct': False, 'explanation': 'This is not rote memorization; it\'s an active learning approach engaging multiple senses.'},
                            ],
                        },
                        {
                            'question': 'Students who quiz themselves without looking at notes perform better on exams than those who repeatedly reread. What explains this?',
                            'answers': [
                                {'text': 'Rereading is more effortful', 'correct': False, 'explanation': 'This is not the reason; the key is in the effectiveness of retrieval practice.'},
                                {'text': 'Retrieval practice strengthens memory more than passive review', 'correct': True, 'explanation': 'Exactly! Actively retrieving information strengthens memory retention much more than passive review like rereading.'},
                                {'text': 'Quizzing reduces study time', 'correct': False, 'explanation': 'This is not the main factor; it\'s about the effectiveness of the retrieval practice itself.'},
                                {'text': 'Rereading always fails', 'correct': False, 'explanation': 'This is not true; rereading can be effective, but it\'s not as effective as retrieval practice.'},
                            ],
                        },
                        {
                            'question': 'A student learns vocabulary by creating sentences that link new words to personal experiences. Which principle is this?',
                            'answers': [
                                {'text': 'Shallow processing', 'correct': False, 'explanation': 'This is not shallow processing; it\'s a deep, meaningful way to learn and remember new words.'},
                                {'text': 'Elaboration—connecting new information to existing knowledge', 'correct': True, 'explanation': 'Exactly! This principle of elaboration helps to create strong mental connections for better recall.'},
                                {'text': 'Massed practice', 'correct': False, 'explanation': 'This is not massed practice; it\'s an active engagement strategy for learning.'},
                                {'text': 'Passive review', 'correct': False, 'explanation': 'This is not passive review; it\'s an active and meaningful way to learn vocabulary.'},
                            ],
                        },
                        {
                            'question': 'Why is interleaved practice (mixing problem types) often more effective than blocked practice (one type at a time)?',
                            'answers': [
                                {'text': 'Interleaving is easier and less confusing', 'correct': False, 'explanation': 'This is not true; interleaving is often harder and requires more cognitive effort.'},
                                {'text': 'Interleaving requires discriminating between problem types, strengthening learning', 'correct': True, 'explanation': 'Exactly! This discrimination process strengthens learning and improves problem-solving skills.'},
                                {'text': 'Blocked practice always produces better results', 'correct': False, 'explanation': 'This is not true; blocked practice can lead to faster forgetting and is less effective for long-term retention.'},
                                {'text': 'Interleaving eliminates errors', 'correct': False, 'explanation': 'This is not accurate; interleaving helps to reduce errors over time but does not eliminate them.'},
                            ],
                        },
                        {
                            'question': 'A medical student uses mnemonics, visual diagrams, and teaches concepts to study partners. Which combination of strategies is most effective according to science of learning?',
                            'answers': [
                                {'text': 'Only mnemonics', 'correct': False, 'explanation': 'This is not enough; mnemonics are helpful but should be combined with other strategies.'},
                                {'text': 'Elaboration (mnemonics), dual coding (diagrams), and retrieval practice (teaching)', 'correct': True, 'explanation': 'Exactly! This combination engages multiple effective learning principles for deeper understanding and retention.'},
                                {'text': 'Passive rereading only', 'correct': False, 'explanation': 'This is not effective; passive rereading is one of the least effective study strategies.'},
                                {'text': 'Cramming the night before', 'correct': False, 'explanation': 'This is not effective for long-term retention and understanding; it\'s a poor study strategy.'},
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
                                {'text': 'Selecting tractable subproblems', 'correct': False, 'explanation': 'This is important; selecting intractable subproblems is the real pitfall.'},
                                {'text': 'Explaining links between subproblems', 'correct': False, 'explanation': 'This is crucial for understanding the problem; failing to explain links is a pitfall.'},
                                {'text': 'Mislabeling a fixed constraint as a subproblem', 'correct': True, 'explanation': 'Exactly! This is a common pitfall that can confuse the problem-solving process.'},
                                {'text': 'Using evidence to prioritize', 'correct': False, 'explanation': 'This is important; not using evidence to prioritize is a pitfall.'},
                            ],
                        },
                        {
                            'question': 'A team faces "low customer satisfaction." They break it down into: slow response times, product defects, and unclear instructions. What makes this effective?',
                            'answers': [
                                {'text': 'It creates more problems', 'correct': False, 'explanation': 'This is not true; breaking down a problem into components does not create more problems.'},
                                {'text': 'It decomposes a vague issue into specific, actionable components', 'correct': True, 'explanation': 'Exactly! This decomposition makes the problem more manageable and solutions more actionable.'},
                                {'text': 'It ignores root causes', 'correct': False, 'explanation': 'This is not necessarily true; breaking down a problem can help to identify root causes.'},
                                {'text': 'It avoids prioritization', 'correct': False, 'explanation': 'This is not accurate; breaking down a problem can actually help with prioritization of issues.'},
                            ],
                        },
                        {
                            'question': 'A project manager decomposes "launch product" into: design MVP, conduct user testing, fix bugs, prepare marketing, and train support staff. What principle is applied?',
                            'answers': [
                                {'text': 'Keeping the problem vague', 'correct': False, 'explanation': 'This is not vague; it\'s a clear breakdown of the product launch process.'},
                                {'text': 'Breaking into sequential, manageable tasks', 'correct': True, 'explanation': 'Exactly! This principle of breaking down tasks makes the project more manageable.'},
                                {'text': 'Avoiding structure', 'correct': False, 'explanation': 'This is not avoiding structure; it\'s creating a structured plan for the project.'},
                                {'text': 'Treating the problem as indivisible', 'correct': False, 'explanation': 'This is not accurate; the problem is being broken down into manageable parts.'},
                            ],
                        },
                        {
                            'question': 'A city addresses "traffic congestion" by breaking it into: peak-hour bottlenecks, inadequate public transit, and parking shortages. Why is this better than tackling "congestion" directly?',
                            'answers': [
                                {'text': 'It creates unnecessary complexity', 'correct': False, 'explanation': 'This is not true; breaking down a problem usually clarifies complexity rather than creating it.'},
                                {'text': 'It identifies specific leverage points for intervention', 'correct': True, 'explanation': 'Exactly! This approach helps to identify specific areas where interventions can be most effective.'},
                                {'text': 'It avoids solving anything', 'correct': False, 'explanation': 'This is not accurate; breaking down a problem is a step towards finding effective solutions.'},
                                {'text': 'General solutions are always better', 'correct': False, 'explanation': 'This is not true; specific solutions are often more effective than general ones.'},
                            ],
                        },
                        {
                            'question': 'When decomposing a problem, what should guide how granular the breakdown becomes?',
                            'answers': [
                                {'text': 'Always break down to the smallest possible pieces', 'correct': False, 'explanation': 'This is not practical; the breakdown should be as granular as necessary to make the problem manageable.'},
                                {'text': 'Stop when subproblems are tractable and actionable', 'correct': True, 'explanation': 'Exactly! The breakdown should result in subproblems that are manageable and actionable.'},
                                {'text': 'Never break down beyond one level', 'correct': False, 'explanation': 'This is too rigid; some problems may require multiple levels of breakdown to be manageable.'},
                                {'text': 'Random stopping points', 'correct': False, 'explanation': 'This is not effective; the stopping point should be determined by the nature of the problem, not randomly.'},
                            ],
                        },
                        {
                            'question': 'A researcher studying "student dropout" breaks it down into: financial barriers, academic preparation gaps, and social isolation. They then further decompose "financial barriers" into tuition costs, living expenses, and lost income. What process is this?',
                            'answers': [
                                {'text': 'Avoiding the problem', 'correct': False, 'explanation': 'This is not avoiding the problem; it\'s a detailed breakdown to understand the problem better.'},
                                {'text': 'Iterative decomposition—refining subproblems into smaller components', 'correct': True, 'explanation': 'Exactly! This process helps to refine the understanding of the problem and identify specific areas for intervention.'},
                                {'text': 'Random categorization', 'correct': False, 'explanation': 'This is not random; it\'s a systematic process of breaking down the problem.'},
                                {'text': 'Constraint identification', 'correct': False, 'explanation': 'This is not about identifying constraints; it\'s about breaking down the problem into manageable parts.'},
                            ],
                        },
                        {
                            'question': 'A software team decomposes "improve app performance" into: reduce load times, optimize database queries, and minimize memory usage. They use a fishbone diagram to visualize these categories. What\'s the advantage?',
                            'answers': [
                                {'text': 'Diagrams make problems disappear', 'correct': False, 'explanation': 'This is not true; diagrams do not solve problems, but they help to visualize and organize thoughts.'},
                                {'text': 'Visual organization clarifies relationships and facilitates systematic analysis', 'correct': True, 'explanation': 'Exactly! Visual organization helps to see the relationships between different parts of the problem and facilitates a systematic approach to analysis.'},
                                {'text': 'Fishbone diagrams solve problems automatically', 'correct': False, 'explanation': 'This is not true; fishbone diagrams are a tool to help organize thoughts, not a solution to problems.'},
                                {'text': 'Visualization is unnecessary', 'correct': False, 'explanation': 'This is not accurate; visualization can be a very helpful part of the problem-solving process.'},
                            ],
                        },
                        {
                            'question': 'After breaking "reduce hospital readmissions" into multiple subproblems, a team realizes one component ("state regulations") is a fixed constraint, not solvable. What should they do?',
                            'answers': [
                                {'text': 'Try to solve the constraint anyway', 'correct': False, 'explanation': 'This is not feasible; fixed constraints cannot be solved or changed.'},
                                {'text': 'Reclassify it as a constraint and focus effort on solvable subproblems', 'correct': True, 'explanation': 'Exactly! This allows the team to focus on subproblems that can actually be solved.'},
                                {'text': 'Abandon the entire breakdown', 'correct': False, 'explanation': 'This is not necessary; only the approach to the unsolvable subproblem needs to be adjusted.'},
                                {'text': 'Ignore regulations completely', 'correct': False, 'explanation': 'This is not advisable; regulations are important and must be considered in the problem-solving process.'},
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
                                {'text': 'Build a novel solution anyway', 'correct': False, 'explanation': 'This is not efficient; if an existing tool works with minor changes, it\'s better to use it.'},
                                {'text': 'Use the existing tool and document justification', 'correct': True, 'explanation': 'Exactly! This is a practical approach that saves time and resources.'},
                                {'text': 'Switch to analogies', 'correct': False, 'explanation': 'This is unnecessary; the problem can be solved with the existing tool.'},
                                {'text': 'Ignore constraints', 'correct': False, 'explanation': 'This is not advisable; constraints are important to consider in problem-solving.'},
                            ],
                            
                        },
                        {
                            'question': 'Which is required for a solid gap analysis?',
                            'answers': [
                                {'text': 'Listing one familiar option', 'correct': False, 'explanation': 'This is not enough; multiple solutions should be evaluated for a solid gap analysis.'},
                                {'text': 'Deep evaluation of multiple existing solutions against requirements/constraints', 'correct': True, 'explanation': 'Exactly! This thorough evaluation is key to effective gap analysis.'},
                                {'text': 'Brainstorming new ideas only', 'correct': False, 'explanation': 'Gap analysis focuses on evaluating existing solutions, not just brainstorming new ones.'},
                                {'text': 'Assuming gaps exist', 'correct': False, 'explanation': 'This is not correct; gaps should be identified through analysis, not assumed.'},
                            ],
                            
                        },
                        {
                            'question': 'Using a proven same-domain solution with slight tweaks typically reflects:',
                            'answers': [
                                {'text': '#analogies', 'correct': False, 'explanation': 'This is not an analogy; it\'s an adaptation of an existing solution.'},
                                {'text': '#heuristics', 'correct': False, 'explanation': 'This is not a heuristic; it\'s a practical approach to using existing solutions.'},
                                {'text': '#gapanalysis', 'correct': True, 'explanation': 'Exactly! This reflects a gap analysis approach where an existing solution is used with minor tweaks.'},
                                {'text': '#rightproblem', 'correct': False, 'explanation': 'This is not directly related to framing the problem; it\'s about using an existing solution.'},
                            ],
                        },
                        {
                            'question': 'A company needs scheduling software. After evaluating 5 existing platforms, they find one that meets 90% of needs with minor customization. What should they do?',
                            'answers': [
                                {'text': 'Build custom software from scratch for 100% fit', 'correct': False, 'explanation': 'This is not efficient; building custom software is time-consuming and costly.'},
                                {'text': 'Adopt the existing solution with targeted customization', 'correct': True, 'explanation': 'Exactly! This is a practical and efficient approach to meet the company\'s needs.'},
                                {'text': 'Continue searching indefinitely for a perfect match', 'correct': False, 'explanation': 'This is not practical; it\'s better to use a good existing solution than to keep searching indefinitely.'},
                                {'text': 'Use analogies from unrelated domains', 'correct': False, 'explanation': 'This is unnecessary; the problem can be solved with an existing solution in the same domain.'},
                            ],
                        },
                        {
                            'question': 'A hospital reviews 10 patient check-in systems used by similar institutions. None fully meet their needs due to unique regulatory requirements. What does gap analysis conclude?',
                            'answers': [
                                {'text': 'Force-fit an inadequate existing solution', 'correct': False, 'explanation': 'This is not advisable; forcing a solution that doesn\'t fit can cause more problems.'},
                                {'text': 'A gap exists; custom development or major adaptation is needed', 'correct': True, 'explanation': 'Exactly! The gap analysis shows that the existing solutions do not fully meet the hospital\'s needs.'},
                                {'text': 'Give up on improving check-in', 'correct': False, 'explanation': 'This is not a solution; the hospital should find a way to meet its check-in needs.'},
                                {'text': 'Ignore regulatory requirements', 'correct': False, 'explanation': 'This is not advisable; regulatory requirements are important and must be followed.'},
                            ],
                        },
                        {
                            'question': 'What distinguishes #gapanalysis from #analogies?',
                            'answers': [
                                {'text': 'Gap analysis looks within the same domain; analogies transfer across domains', 'correct': True, 'explanation': 'Exactly! Gap analysis evaluates solutions within the same domain, while analogies apply solutions from one domain to another.'},
                                {'text': 'They are identical approaches', 'correct': False, 'explanation': 'This is not true; they are different approaches used in different situations.'},
                                {'text': 'Gap analysis never uses existing solutions', 'correct': False, 'explanation': 'This is not correct; gap analysis often involves evaluating existing solutions.'},
                                {'text': 'Analogies only work within the same field', 'correct': False, 'explanation': 'This is not true; analogies are used to transfer knowledge across different domains.'},
                            ],
                        },
                        {
                            'question': 'A startup evaluates CRM platforms. Platform A meets 80% of needs at low cost; Platform B meets 95% at 5x cost. Gap analysis suggests:',
                            'answers': [
                                {'text': 'Always choose the most complete solution', 'correct': False, 'explanation': 'This is not always the best approach; the most complete solution may not be the most cost-effective.'},
                                {'text': 'Weigh trade-offs between fit, cost, and customization; 80% may suffice', 'correct': True, 'explanation': 'Exactly! This is a practical approach that considers multiple factors in the decision.'},
                                {'text': 'Build entirely from scratch', 'correct': False, 'explanation': 'This is not efficient; building from scratch is time-consuming and costly.'},
                                {'text': 'Choose randomly', 'correct': False, 'explanation': 'This is not a sensible approach; the decision should be based on careful analysis, not random choice.'},
                            ],
                        },
                        {
                            'question': 'After thorough gap analysis, a team finds no existing solutions meet their needs. What should they do next?',
                            'answers': [
                                {'text': 'Force an existing solution despite poor fit', 'correct': False, 'explanation': 'This is not advisable; forcing a solution that doesn\'t fit can cause more problems.'},
                                {'text': 'Pursue novel solution development or explore cross-domain analogies', 'correct': True, 'explanation': 'Exactly! This is a good approach when no existing solutions fit the needs.'},
                                {'text': 'Abandon the project', 'correct': False, 'explanation': 'This is not a solution; the project should be adjusted to find a viable path forward.'},
                                {'text': 'Repeat the same gap analysis', 'correct': False, 'explanation': 'This is not useful; the gap analysis has already been done, and the next steps should be solution-oriented.'},
                            ],
                        },
                        {
                            'question': 'A university wants to improve advising. They find that 3 peer institutions use similar systems successfully. What does gap analysis recommend?',
                            'answers': [
                                {'text': 'Ignore peer solutions and invent something entirely new', 'correct': False, 'explanation': 'This is not advisable; ignoring potential solutions wastes time and resources.'},
                                {'text': 'Evaluate and adapt proven peer solutions to local context', 'correct': True, 'explanation': 'Exactly! This is a practical approach that builds on proven solutions.'},
                                {'text': 'Adopt without any evaluation', 'correct': False, 'explanation': 'This is not advisable; adopting without evaluation may lead to unsuitable solutions being implemented.'},
                                {'text': 'Use analogies from unrelated industries', 'correct': False, 'explanation': 'This is not necessary; there are already proven solutions in similar institutions.'},
                            ],
                        },
                        {
                            'question': 'Why conduct gap analysis before designing new solutions?',
                            'answers': [
                                {'text': 'To waste time', 'correct': False, 'explanation': 'This is not true; gap analysis saves time by identifying existing solutions.'},
                                {'text': 'To avoid reinventing the wheel and leverage existing work', 'correct': True, 'explanation': 'Exactly! Gap analysis helps to build on existing solutions and avoid unnecessary duplication of effort.'},
                                {'text': 'To ensure no solutions exist', 'correct': False, 'explanation': 'This is not the goal; the goal is to find the best solution, whether existing or new.'},
                                {'text': 'Gap analysis is unnecessary', 'correct': False, 'explanation': 'This is not true; gap analysis is a valuable part of the problem-solving process.'},
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

