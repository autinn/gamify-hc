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
                        {
                            'question': 'A hospital aims to "reduce patient complaints" but doesn\'t specify which types of complaints or current frequency. Why is this problematic?',
                            'answers': [
                                {'text': 'The goal is too ambitious', 'correct': False},
                                {'text': 'Without baseline data and specificity, success cannot be measured', 'correct': True},
                                {'text': 'Complaints are not important', 'correct': False},
                                {'text': 'Solutions should come before measurement', 'correct': False},
                            ],
                            'explanation': 'Characterizing the right problem requires quantifying the initial state and defining specific success criteria.'
                        },
                        {
                            'question': 'A startup identifies "low user engagement" as their problem but hasn\'t examined which features users actually use or why they leave. What critical step is missing?',
                            'answers': [
                                {'text': 'Defining the goal state', 'correct': False},
                                {'text': 'Characterizing the initial state through data analysis', 'correct': True},
                                {'text': 'Listing constraints', 'correct': False},
                                {'text': 'Brainstorming solutions', 'correct': False},
                            ],
                            'explanation': 'Understanding the current state in detail—including user behavior patterns—is essential before defining solutions.'
                        },
                        {
                            'question': 'Two teams tackle food waste. Team A defines the goal as "implement composting programs." Team B defines it as "reduce cafeteria waste by 40% within 6 months." Which follows #rightproblem better?',
                            'answers': [
                                {'text': 'Team A, because composting is a proven solution', 'correct': False},
                                {'text': 'Team B, because they specify measurable outcomes without presupposing one solution', 'correct': True},
                                {'text': 'Both equally, since goals are subjective', 'correct': False},
                                {'text': 'Neither, since waste reduction is too vague', 'correct': False},
                            ],
                            'explanation': 'Outcome-focused goals leave room for multiple solution paths; solution-focused goals prematurely narrow options.'
                        },
                        {
                            'question': 'A school says "students are failing math" but hasn\'t identified whether the issue is foundational gaps, teaching methods, or motivation. What should they do first?',
                            'answers': [
                                {'text': 'Hire more tutors immediately', 'correct': False},
                                {'text': 'Characterize the problem by analyzing failure patterns and root causes', 'correct': True},
                                {'text': 'Switch to a new curriculum', 'correct': False},
                                {'text': 'Increase homework assignments', 'correct': False},
                            ],
                            'explanation': 'Understanding the nature and scope of failures is essential before selecting interventions.'
                        },
                        {
                            'question': 'A company characterizes a problem with initial state, goal state, and obstacles—but omits constraints like budget and regulatory requirements. What risk does this create?',
                            'answers': [
                                {'text': 'The problem becomes too easy to solve', 'correct': False},
                                {'text': 'Solutions may be infeasible or illegal', 'correct': True},
                                {'text': 'Obstacles will disappear', 'correct': False},
                                {'text': 'The initial state will change', 'correct': False},
                            ],
                            'explanation': 'Constraints define what is permissible and achievable; ignoring them leads to impractical solutions.'
                        },
                        {
                            'question': 'A nonprofit states their problem as "need more funding" rather than "cannot serve 200+ families on waitlist due to capacity limits." Which framing better applies #rightproblem?',
                            'answers': [
                                {'text': 'The first, because funding is always the core issue', 'correct': False},
                                {'text': 'The second, because it describes the real problem and goal state without presupposing one solution', 'correct': True},
                                {'text': 'Both are equally valid', 'correct': False},
                                {'text': 'Neither, since nonprofits should not define problems', 'correct': False},
                            ],
                            'explanation': 'Reframing from "need X resource" to "cannot achieve Y outcome" opens up multiple solution pathways.'
                        },
                        {
                            'question': 'An urban planning team characterizes traffic congestion by documenting peak hours, bottleneck locations, commuter origins, and economic costs. What component would complete their characterization?',
                            'answers': [
                                {'text': 'A list of potential solutions', 'correct': False},
                                {'text': 'Projected consequences if congestion continues unchecked', 'correct': True},
                                {'text': 'A detailed budget breakdown', 'correct': False},
                                {'text': 'Stakeholder voting results', 'correct': False},
                            ],
                            'explanation': 'Full problem characterization includes implications—what happens if the problem persists.'
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
                        {
                            'question': 'A designer uses ant colony optimization (how ants find food) to route delivery trucks efficiently. What makes this a strong analogy?',
                            'answers': [
                                {'text': 'Ants and trucks both move', 'correct': False},
                                {'text': 'Both systems solve path optimization through decentralized feedback', 'correct': True},
                                {'text': 'The metaphor sounds interesting', 'correct': False},
                                {'text': 'Ants are commonly studied', 'correct': False},
                            ],
                            'explanation': 'Strong analogies map underlying mechanisms, not superficial features.'
                        },
                        {
                            'question': 'A city borrows "immune system response" to model epidemic containment: detect threats, isolate infections, mobilize resources. What must they adapt?',
                            'answers': [
                                {'text': 'Nothing—biological systems translate directly', 'correct': False},
                                {'text': 'Scale, timescales, and human behavioral factors absent in cellular immunity', 'correct': True},
                                {'text': 'The entire analogy should be discarded', 'correct': False},
                                {'text': 'Only visual metaphors', 'correct': False},
                            ],
                            'explanation': 'Analogies require adaptation to account for differences between source and target domains.'
                        },
                        {
                            'question': 'A software team applies "assembly line" principles to code review: each reviewer checks one specific aspect sequentially. What structural similarity justifies this analogy?',
                            'answers': [
                                {'text': 'Both involve computers', 'correct': False},
                                {'text': 'Both use sequential specialization to improve quality and efficiency', 'correct': True},
                                {'text': 'Code and manufacturing are unrelated', 'correct': False},
                                {'text': 'Assembly lines are outdated', 'correct': False},
                            ],
                            'explanation': 'The analogy works because both systems decompose complex tasks into specialized sequential stages.'
                        },
                        {
                            'question': 'When applying analogical reasoning, why is it risky to rely on surface similarities (e.g., "schools and prisons both have cafeterias")?',
                            'answers': [
                                {'text': 'Surface features often don\'t reflect structural or functional similarities', 'correct': True},
                                {'text': 'Cafeterias are unimportant', 'correct': False},
                                {'text': 'All similarities are equally valid', 'correct': False},
                                {'text': 'Analogies should never compare institutions', 'correct': False},
                            ],
                            'explanation': 'Effective analogies depend on deep structural parallels, not superficial resemblances.'
                        },
                        {
                            'question': 'A team uses "Netflix recommendation algorithms" as an analogy for suggesting personalized learning paths in education. What challenge must they address?',
                            'answers': [
                                {'text': 'Students and viewers are identical', 'correct': False},
                                {'text': 'Educational goals differ from entertainment engagement; success metrics must be redefined', 'correct': True},
                                {'text': 'The analogy is completely invalid', 'correct': False},
                                {'text': 'Algorithms cannot be applied to education', 'correct': False},
                            ],
                            'explanation': 'The structural mechanism (personalized recommendations) transfers, but goals and metrics must be adapted to educational outcomes.'
                        },
                        {
                            'question': 'A business consultant suggests "a company is like a sports team" to improve collaboration. When does this analogy break down?',
                            'answers': [
                                {'text': 'Companies and teams both have members', 'correct': False},
                                {'text': 'Corporate goals are often more ambiguous and long-term than game outcomes', 'correct': True},
                                {'text': 'Sports teams never collaborate', 'correct': False},
                                {'text': 'All organizational analogies are perfect', 'correct': False},
                            ],
                            'explanation': 'Analogies have limits; recognizing where source and target diverge is critical for effective application.'
                        },
                        {
                            'question': 'Researchers apply "traffic flow models" to analyze data packet routing in computer networks. What validates this cross-domain analogy?',
                            'answers': [
                                {'text': 'Cars and data are both physical objects', 'correct': False},
                                {'text': 'Both systems exhibit congestion, bottlenecks, and throughput optimization challenges', 'correct': True},
                                {'text': 'Traffic and networks are unrelated', 'correct': False},
                                {'text': 'All analogies between transport and computing work', 'correct': False},
                            ],
                            'explanation': 'The analogy succeeds because both domains share structural properties related to flow, capacity, and congestion.'
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
                        {
                            'question': 'A team must schedule a conference with 5 constraints: venue availability, speaker schedules, budget limits, accessibility requirements, and catering lead times. What approach applies #constraints?',
                            'answers': [
                                {'text': 'Pick one constraint and ignore the rest', 'correct': False},
                                {'text': 'Find a solution that simultaneously satisfies all 5 constraints', 'correct': True},
                                {'text': 'Remove constraints until the problem is easy', 'correct': False},
                                {'text': 'Prioritize constraints and violate lower-priority ones', 'correct': False},
                            ],
                            'explanation': 'Constraint satisfaction requires meeting all constraints at once, not sequentially or selectively.'
                        },
                        {
                            'question': 'A city faces "traffic congestion during construction season." Is the construction a constraint or an obstacle?',
                            'answers': [
                                {'text': 'Obstacle, because construction can be rescheduled or phased differently', 'correct': True},
                                {'text': 'Constraint, because construction is happening', 'correct': False},
                                {'text': 'Neither, because it\'s temporary', 'correct': False},
                                {'text': 'Both equally', 'correct': False},
                            ],
                            'explanation': 'Obstacles can be addressed through interventions; constraints are fixed within the problem framing.'
                        },
                        {
                            'question': 'A software project has hard constraints (regulatory compliance, system compatibility) and soft preferences (user interface aesthetics). How should they be treated?',
                            'answers': [
                                {'text': 'Treat preferences as constraints to simplify', 'correct': False},
                                {'text': 'Satisfy hard constraints first; optimize preferences within feasible solutions', 'correct': True},
                                {'text': 'Ignore hard constraints if they conflict with preferences', 'correct': False},
                                {'text': 'All constraints are equally negotiable', 'correct': False},
                            ],
                            'explanation': 'Hard constraints must be satisfied; soft preferences guide optimization among valid solutions.'
                        },
                        {
                            'question': 'A meal planner must satisfy: dietary restrictions (vegan, nut-free), budget ($50), prep time (under 2 hours), and ingredient availability. Two menus meet all constraints. What should guide the final choice?',
                            'answers': [
                                {'text': 'Additional preferences like taste or nutrition balance', 'correct': True},
                                {'text': 'Randomly select one', 'correct': False},
                                {'text': 'Add more constraints until only one remains', 'correct': False},
                                {'text': 'Violate one constraint to simplify', 'correct': False},
                            ],
                            'explanation': 'Once constraints are satisfied, preferences or secondary criteria guide selection among feasible options.'
                        },
                        {
                            'question': 'A warehouse layout must accommodate: fire safety codes (constraint), forklift turning radii (constraint), and "easy access to popular items" (preference). What distinguishes the constraint from the preference?',
                            'answers': [
                                {'text': 'Constraints are legally mandated or physically necessary; preferences are desirable but negotiable', 'correct': True},
                                {'text': 'Preferences are always more important', 'correct': False},
                                {'text': 'Constraints can be violated with enough creativity', 'correct': False},
                                {'text': 'There is no distinction', 'correct': False},
                            ],
                            'explanation': 'Constraints define the feasible solution space; preferences guide optimization within that space.'
                        },
                        {
                            'question': 'A project faces "insufficient expertise in the team" and "a non-negotiable December deadline." Which is the constraint?',
                            'answers': [
                                {'text': 'The expertise gap, because it limits capability', 'correct': False},
                                {'text': 'The December deadline, because it cannot be changed', 'correct': True},
                                {'text': 'Both are constraints', 'correct': False},
                                {'text': 'Neither—both are just challenges', 'correct': False},
                            ],
                            'explanation': 'Constraints are fixed boundaries; expertise gaps are obstacles that can be addressed (training, hiring).'
                        },
                        {
                            'question': 'A school must assign 30 teachers to 30 classrooms, ensuring each teacher\'s subject matches room equipment, schedule fits personal constraints, and no room is double-booked. This is an example of:',
                            'answers': [
                                {'text': 'A heuristic problem', 'correct': False},
                                {'text': 'A constraint satisfaction problem', 'correct': True},
                                {'text': 'An unconstrained optimization', 'correct': False},
                                {'text': 'A purely creative task', 'correct': False},
                            ],
                            'explanation': 'Constraint satisfaction problems require finding assignments that meet multiple interacting constraints simultaneously.'
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
                        {
                            'question': 'A doctor quickly diagnoses a patient based on the most common symptoms matching typical cases. This uses which heuristic?',
                            'answers': [
                                {'text': 'Anchoring', 'correct': False},
                                {'text': 'Representativeness', 'correct': True},
                                {'text': 'Means-ends analysis', 'correct': False},
                                {'text': 'Constraint satisfaction', 'correct': False},
                            ],
                            'explanation': 'Representativeness judges likelihood by similarity to prototypes, useful for quick pattern matching.'
                        },
                        {
                            'question': 'A manager sets project timelines by starting with an initial estimate (30 days) and adjusting slightly upward (35 days). What heuristic bias might occur?',
                            'answers': [
                                {'text': 'Anchoring—the initial 30 days overly influences the final estimate', 'correct': True},
                                {'text': 'Availability', 'correct': False},
                                {'text': 'Means-ends analysis', 'correct': False},
                                {'text': 'Representativeness', 'correct': False},
                            ],
                            'explanation': 'Anchoring occurs when initial values disproportionately shape subsequent judgments, even when adjusted.'
                        },
                        {
                            'question': 'A team uses means-ends analysis to plan a product launch: identify launch date (goal), determine current readiness (initial state), then define subgoals (complete testing, finalize marketing). What makes this effective?',
                            'answers': [
                                {'text': 'It relies on random exploration', 'correct': False},
                                {'text': 'It systematically decomposes the gap into manageable subgoals', 'correct': True},
                                {'text': 'It ignores constraints', 'correct': False},
                                {'text': 'It avoids planning altogether', 'correct': False},
                            ],
                            'explanation': 'Means-ends analysis structures problem-solving by breaking down the distance between current and goal states.'
                        },
                        {
                            'question': 'After a plane crash receives heavy media coverage, people overestimate flight risks despite statistical safety. Which heuristic explains this?',
                            'answers': [
                                {'text': 'Availability—vivid recent events are easily recalled', 'correct': True},
                                {'text': 'Representativeness', 'correct': False},
                                {'text': 'Anchoring', 'correct': False},
                                {'text': 'Means-ends', 'correct': False},
                            ],
                            'explanation': 'Availability heuristic causes people to judge frequency or risk by how easily examples come to mind.'
                        },
                        {
                            'question': 'When should you avoid heuristics and use comprehensive analysis instead?',
                            'answers': [
                                {'text': 'When making low-stakes decisions with time pressure', 'correct': False},
                                {'text': 'When decisions are high-stakes with available data and time for thorough evaluation', 'correct': True},
                                {'text': 'Always—heuristics are never useful', 'correct': False},
                                {'text': 'Only for creative tasks', 'correct': False},
                            ],
                            'explanation': 'High-stakes decisions with adequate resources warrant rigorous analysis to avoid heuristic biases.'
                        },
                        {
                            'question': 'A hiring manager judges a candidate as "highly competent" because they attended a prestigious school, without reviewing actual work samples. Which heuristic is active?',
                            'answers': [
                                {'text': 'Representativeness—prestige signals competence via similarity to successful prototypes', 'correct': True},
                                {'text': 'Availability', 'correct': False},
                                {'text': 'Means-ends', 'correct': False},
                                {'text': 'Constraint satisfaction', 'correct': False},
                            ],
                            'explanation': 'Representativeness judges based on similarity to stereotypes or prototypes, which can overlook individual variation.'
                        },
                        {
                            'question': 'A software team uses "working backward" from the desired user experience to identify necessary features and then current capabilities. What problem-solving approach is this?',
                            'answers': [
                                {'text': 'Random trial and error', 'correct': False},
                                {'text': 'Means-ends analysis', 'correct': True},
                                {'text': 'Anchoring heuristic', 'correct': False},
                                {'text': 'Availability heuristic', 'correct': False},
                            ],
                            'explanation': 'Working backward from the goal to define intermediate steps is a form of means-ends analysis.'
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
                        {
                            'question': 'A student studies biology by creating concept maps linking terms, testing themselves weekly, and teaching concepts to peers. Which science of learning principles are applied?',
                            'answers': [
                                {'text': 'Highlighting and rereading only', 'correct': False},
                                {'text': 'Deep processing, retrieval practice, and elaboration', 'correct': True},
                                {'text': 'Massed practice and passive review', 'correct': False},
                                {'text': 'Cramming and surface-level review', 'correct': False},
                            ],
                            'explanation': 'Concept mapping fosters deep processing, self-testing enables retrieval practice, and teaching requires elaboration.'
                        },
                        {
                            'question': 'Why is spaced practice more effective than massed practice (cramming) for long-term retention?',
                            'answers': [
                                {'text': 'It takes less total time', 'correct': False},
                                {'text': 'Spacing allows consolidation and strengthens retrieval pathways', 'correct': True},
                                {'text': 'Cramming always produces better results', 'correct': False},
                                {'text': 'Spaced practice eliminates the need for review', 'correct': False},
                            ],
                            'explanation': 'Spacing supports memory consolidation and makes retrieval more effortful, which strengthens learning.'
                        },
                        {
                            'question': 'A teacher presents a lesson using diagrams, verbal explanations, and hands-on activities. Which learning principle is being applied?',
                            'answers': [
                                {'text': 'Massed practice', 'correct': False},
                                {'text': 'Dual coding—combining verbal and visual modalities', 'correct': True},
                                {'text': 'Interference', 'correct': False},
                                {'text': 'Rote memorization', 'correct': False},
                            ],
                            'explanation': 'Dual coding leverages multiple representational systems (verbal, visual, kinesthetic) to enhance memory.'
                        },
                        {
                            'question': 'Students who quiz themselves without looking at notes perform better on exams than those who repeatedly reread. What explains this?',
                            'answers': [
                                {'text': 'Rereading is more effortful', 'correct': False},
                                {'text': 'Retrieval practice strengthens memory more than passive review', 'correct': True},
                                {'text': 'Quizzing reduces study time', 'correct': False},
                                {'text': 'Rereading always fails', 'correct': False},
                            ],
                            'explanation': 'Retrieval practice (testing effect) forces active recall, which strengthens memory traces more than passive rereading.'
                        },
                        {
                            'question': 'A student learns vocabulary by creating sentences that link new words to personal experiences. Which principle is this?',
                            'answers': [
                                {'text': 'Shallow processing', 'correct': False},
                                {'text': 'Elaboration—connecting new information to existing knowledge', 'correct': True},
                                {'text': 'Massed practice', 'correct': False},
                                {'text': 'Passive review', 'correct': False},
                            ],
                            'explanation': 'Elaboration creates meaningful associations, making information easier to retrieve later.'
                        },
                        {
                            'question': 'Why is interleaved practice (mixing problem types) often more effective than blocked practice (one type at a time)?',
                            'answers': [
                                {'text': 'Interleaving is easier and less confusing', 'correct': False},
                                {'text': 'Interleaving requires discriminating between problem types, strengthening learning', 'correct': True},
                                {'text': 'Blocked practice always produces better results', 'correct': False},
                                {'text': 'Interleaving eliminates errors', 'correct': False},
                            ],
                            'explanation': 'Interleaving forces learners to identify which strategy applies, building stronger conceptual understanding and transfer.'
                        },
                        {
                            'question': 'A medical student uses mnemonics, visual diagrams, and teaches concepts to study partners. Which combination of strategies is most effective according to science of learning?',
                            'answers': [
                                {'text': 'Only mnemonics', 'correct': False},
                                {'text': 'Elaboration (mnemonics), dual coding (diagrams), and retrieval practice (teaching)', 'correct': True},
                                {'text': 'Passive rereading only', 'correct': False},
                                {'text': 'Cramming the night before', 'correct': False},
                            ],
                            'explanation': 'Combining multiple evidence-based strategies (elaboration, dual coding, retrieval) maximizes learning effectiveness.'
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
                        {
                            'question': 'A team faces "low customer satisfaction." They break it down into: slow response times, product defects, and unclear instructions. What makes this effective?',
                            'answers': [
                                {'text': 'It creates more problems', 'correct': False},
                                {'text': 'It decomposes a vague issue into specific, actionable components', 'correct': True},
                                {'text': 'It ignores root causes', 'correct': False},
                                {'text': 'It avoids prioritization', 'correct': False},
                            ],
                            'explanation': 'Breaking down transforms abstract problems into concrete subproblems that can be individually addressed.'
                        },
                        {
                            'question': 'A project manager decomposes "launch product" into: design MVP, conduct user testing, fix bugs, prepare marketing, and train support staff. What principle is applied?',
                            'answers': [
                                {'text': 'Keeping the problem vague', 'correct': False},
                                {'text': 'Breaking into sequential, manageable tasks', 'correct': True},
                                {'text': 'Avoiding structure', 'correct': False},
                                {'text': 'Treating the problem as indivisible', 'correct': False},
                            ],
                            'explanation': 'Decomposition organizes complex goals into ordered, tractable components.'
                        },
                        {
                            'question': 'A city addresses "traffic congestion" by breaking it into: peak-hour bottlenecks, inadequate public transit, and parking shortages. Why is this better than tackling "congestion" directly?',
                            'answers': [
                                {'text': 'It creates unnecessary complexity', 'correct': False},
                                {'text': 'It identifies specific leverage points for intervention', 'correct': True},
                                {'text': 'It avoids solving anything', 'correct': False},
                                {'text': 'General solutions are always better', 'correct': False},
                            ],
                            'explanation': 'Breaking down reveals specific causes that can be targeted with tailored solutions.'
                        },
                        {
                            'question': 'When decomposing a problem, what should guide how granular the breakdown becomes?',
                            'answers': [
                                {'text': 'Always break down to the smallest possible pieces', 'correct': False},
                                {'text': 'Stop when subproblems are tractable and actionable', 'correct': True},
                                {'text': 'Never break down beyond one level', 'correct': False},
                                {'text': 'Random stopping points', 'correct': False},
                            ],
                            'explanation': 'The goal is to reach a level of specificity where solutions become clear and implementable.'
                        },
                        {
                            'question': 'A researcher studying "student dropout" breaks it down into: financial barriers, academic preparation gaps, and social isolation. They then further decompose "financial barriers" into tuition costs, living expenses, and lost income. What process is this?',
                            'answers': [
                                {'text': 'Avoiding the problem', 'correct': False},
                                {'text': 'Iterative decomposition—refining subproblems into smaller components', 'correct': True},
                                {'text': 'Random categorization', 'correct': False},
                                {'text': 'Constraint identification', 'correct': False},
                            ],
                            'explanation': 'Iterative breakdown refines each subproblem until actionable components emerge.'
                        },
                        {
                            'question': 'A software team decomposes "improve app performance" into: reduce load times, optimize database queries, and minimize memory usage. They use a fishbone diagram to visualize these categories. What's the advantage?',
                            'answers': [
                                {'text': 'Diagrams make problems disappear', 'correct': False},
                                {'text': 'Visual organization clarifies relationships and facilitates systematic analysis', 'correct': True},
                                {'text': 'Fishbone diagrams solve problems automatically', 'correct': False},
                                {'text': 'Visualization is unnecessary', 'correct': False},
                            ],
                            'explanation': 'Fishbone diagrams organize subproblems by category, revealing structure and guiding investigation.'
                        },
                        {
                            'question': 'After breaking "reduce hospital readmissions" into multiple subproblems, a team realizes one component ("state regulations") is a fixed constraint, not solvable. What should they do?',
                            'answers': [
                                {'text': 'Try to solve the constraint anyway', 'correct': False},
                                {'text': 'Reclassify it as a constraint and focus effort on solvable subproblems', 'correct': True},
                                {'text': 'Abandon the entire breakdown', 'correct': False},
                                {'text': 'Ignore regulations completely', 'correct': False},
                            ],
                            'explanation': 'Recognizing constraints vs. solvable subproblems helps allocate effort effectively.'
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
                        {
                            'question': 'A company needs scheduling software. After evaluating 5 existing platforms, they find one that meets 90% of needs with minor customization. What should they do?',
                            'answers': [
                                {'text': 'Build custom software from scratch for 100% fit', 'correct': False},
                                {'text': 'Adopt the existing solution with targeted customization', 'correct': True},
                                {'text': 'Continue searching indefinitely for a perfect match', 'correct': False},
                                {'text': 'Use analogies from unrelated domains', 'correct': False},
                            ],
                            'explanation': 'Gap analysis aims to find "good enough" existing solutions before investing in new development.'
                        },
                        {
                            'question': 'A hospital reviews 10 patient check-in systems used by similar institutions. None fully meet their needs due to unique regulatory requirements. What does gap analysis conclude?',
                            'answers': [
                                {'text': 'Force-fit an inadequate existing solution', 'correct': False},
                                {'text': 'A gap exists; custom development or major adaptation is needed', 'correct': True},
                                {'text': 'Give up on improving check-in', 'correct': False},
                                {'text': 'Ignore regulatory requirements', 'correct': False},
                            ],
                            'explanation': 'When existing solutions cannot satisfy constraints, gap analysis identifies the need for novel approaches.'
                        },
                        {
                            'question': 'What distinguishes #gapanalysis from #analogies?',
                            'answers': [
                                {'text': 'Gap analysis looks within the same domain; analogies transfer across domains', 'correct': True},
                                {'text': 'They are identical approaches', 'correct': False},
                                {'text': 'Gap analysis never uses existing solutions', 'correct': False},
                                {'text': 'Analogies only work within the same field', 'correct': False},
                            ],
                            'explanation': 'Gap analysis evaluates existing same-domain solutions; analogies adapt cross-domain structures.'
                        },
                        {
                            'question': 'A startup evaluates CRM platforms. Platform A meets 80% of needs at low cost; Platform B meets 95% at 5x cost. Gap analysis suggests:',
                            'answers': [
                                {'text': 'Always choose the most complete solution', 'correct': False},
                                {'text': 'Weigh trade-offs between fit, cost, and customization; 80% may suffice', 'correct': True},
                                {'text': 'Build entirely from scratch', 'correct': False},
                                {'text': 'Choose randomly', 'correct': False},
                            ],
                            'explanation': 'Gap analysis balances solution completeness against resource constraints and adaptation costs.'
                        },
                        {
                            'question': 'After thorough gap analysis, a team finds no existing solutions meet their needs. What should they do next?',
                            'answers': [
                                {'text': 'Force an existing solution despite poor fit', 'correct': False},
                                {'text': 'Pursue novel solution development or explore cross-domain analogies', 'correct': True},
                                {'text': 'Abandon the project', 'correct': False},
                                {'text': 'Repeat the same gap analysis', 'correct': False},
                            ],
                            'explanation': 'Confirmed gaps signal the need for creative problem-solving through new development or analogical transfer.'
                        },
                        {
                            'question': 'A university wants to improve advising. They find that 3 peer institutions use similar systems successfully. What does gap analysis recommend?',
                            'answers': [
                                {'text': 'Ignore peer solutions and invent something entirely new', 'correct': False},
                                {'text': 'Evaluate and adapt proven peer solutions to local context', 'correct': True},
                                {'text': 'Adopt without any evaluation', 'correct': False},
                                {'text': 'Use analogies from unrelated industries', 'correct': False},
                            ],
                            'explanation': 'Gap analysis leverages proven same-domain solutions, adapting them to specific constraints.'
                        },
                        {
                            'question': 'Why conduct gap analysis before designing new solutions?',
                            'answers': [
                                {'text': 'To waste time', 'correct': False},
                                {'text': 'To avoid reinventing the wheel and leverage existing work', 'correct': True},
                                {'text': 'To ensure no solutions exist', 'correct': False},
                                {'text': 'Gap analysis is unnecessary', 'correct': False},
                            ],
                            'explanation': 'Gap analysis prevents duplication of effort by identifying reusable existing solutions before committing to new development.'
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

