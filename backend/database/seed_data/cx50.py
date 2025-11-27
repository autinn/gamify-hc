"""
CX50 Course Seed Data
Unit 1: Characteristics of Complex Systems
"""

CX50_DATA = {
    'title': 'CX50',
    'description': 'CX50 Course',
    'units': [
        {
            'title': 'Characteristics of Complex Systems',
            'description': 'CX50 Unit 1',
            'order_index': 0,
            'concepts': [
                {
                    'title': '#complexcausality',
                    'definition': 'Identify how multiple causes interact to produce complex effects.',
                    'questions': [
                        {
                            'question': 'A polar region experiences accelerating ice melt: as sea ice disappears, darker ocean water absorbs more heat, further speeding melting. Which best describes this interaction?',
                            'answers': [
                                {'text': 'Linear causation', 'correct': False},
                                {'text': 'Random correlation', 'correct': False},
                                {'text': 'Reinforcing feedback loop', 'correct': True},
                                {'text': 'Isolated cause–effect chain', 'correct': False},
                            ],
                            'explanation': 'Reinforcing loops amplify change within a system through interconnected causes.'
                        },
                        {
                            'question': 'A city introduces free gym memberships to reduce obesity, but finds little effect because fast-food density and work stress remain high. What does this illustrate?',
                            'answers': [
                                {'text': 'A single sufficient cause', 'correct': False},
                                {'text': 'Interacting causal factors that offset each other', 'correct': True},
                                {'text': 'A non-causal coincidence', 'correct': False},
                                {'text': 'Random variance', 'correct': False},
                            ],
                            'explanation': 'Multiple interacting causes can neutralize one another, showing complex causality.'
                        },
                        {
                            'question': 'After adding a new bus line, traffic worsens because fewer people carpool and more use feeder roads. Which HC concept explains this?',
                            'answers': [
                                {'text': 'Emergent property', 'correct': False},
                                {'text': 'Complex causality', 'correct': True},
                                {'text': 'Network hub effect', 'correct': False},
                                {'text': 'System mapping', 'correct': False},
                            ],
                            'explanation': 'Complex causality captures unintended outcomes from interdependent variables.'
                        },
                        {
                            'question': 'A hospital implements a hand-hygiene program, but infection rates remain high because antibiotic resistance spreads faster through overcrowded wards. What does this reveal about the intervention?',
                            'answers': [
                                {'text': 'It addressed only one pathway in a multi-causal system', 'correct': True},
                                {'text': 'Hygiene is irrelevant to infection control', 'correct': False},
                                {'text': 'The intervention caused resistance', 'correct': False},
                                {'text': 'All causal factors were addressed', 'correct': False},
                            ],
                            'explanation': 'Multiple causal pathways must be considered; addressing one may be insufficient when others dominate.'
                        },
                        {
                            'question': 'A country subsidizes solar panels to cut emissions, but coal use rises as cheap electricity enables energy-intensive manufacturing. What causal dynamic occurred?',
                            'answers': [
                                {'text': 'Direct linear reduction', 'correct': False},
                                {'text': 'Unintended rebound effect via interacting variables', 'correct': True},
                                {'text': 'Solar panels caused pollution', 'correct': False},
                                {'text': 'Pure coincidence', 'correct': False},
                            ],
                            'explanation': 'Rebound effects illustrate complex causality: interventions trigger cascading responses through interconnected factors.'
                        },
                        {
                            'question': 'A school reduces class sizes to boost test scores. Scores initially rise but plateau as teacher quality varies and curriculum updates lag. What principle applies?',
                            'answers': [
                                {'text': 'Class size is the sole cause of outcomes', 'correct': False},
                                {'text': 'Multiple causes interact; one fix may not sustain gains', 'correct': True},
                                {'text': 'Teacher quality is irrelevant', 'correct': False},
                                {'text': 'The intervention failed completely', 'correct': False},
                            ],
                            'explanation': 'Educational outcomes emerge from interacting factors; single-variable interventions hit limits.'
                        },
                        {
                            'question': 'A drought prompts farmers to pump groundwater, lowering water tables, increasing costs, forcing farm closures, reducing food supply, and raising prices that incentivize distant farms to expand production. Which dynamic is most evident?',
                            'answers': [
                                {'text': 'A simple chain reaction', 'correct': False},
                                {'text': 'Reinforcing loops across multiple causal pathways', 'correct': True},
                                {'text': 'Random environmental variation', 'correct': False},
                                {'text': 'A single root cause', 'correct': False},
                            ],
                            'explanation': 'Each effect becomes a cause in subsequent stages, creating cascading feedback through the system.'
                        },
                        {
                            'question': 'A public health campaign reduces smoking by 10%, but lung cancer rates stay flat for 20 years. Policymakers declare failure. What complexity did they overlook?',
                            'answers': [
                                {'text': 'Temporal lag between intervention and measurable outcome', 'correct': True},
                                {'text': 'Spatial distribution of smokers', 'correct': False},
                                {'text': 'The campaign had no effect', 'correct': False},
                                {'text': 'Cancer is unrelated to smoking', 'correct': False},
                            ],
                            'explanation': 'Time delays in causal chains are a hallmark of complex causality; outcomes may lag interventions by decades.'
                        },
                        {
                            'question': 'A financial regulation reduces risky lending at large banks but pushes activity into unregulated shadow banks, triggering a later crisis. What explains this?',
                            'answers': [
                                {'text': 'Regulation was perfectly designed', 'correct': False},
                                {'text': 'Risk migrated through system boundaries', 'correct': True},
                                {'text': 'Banks became more responsible', 'correct': False},
                                {'text': 'Shadow banks caused the original problem', 'correct': False},
                            ],
                            'explanation': 'Complex causality includes displacement effects: interventions shift problems rather than solving them when system boundaries are incomplete.'
                        },
                        {
                            'question': 'After a city bans plastic bags, litter decreases but reusable bag sales spike, increasing water and energy use for washing. Which HC best frames this trade-off?',
                            'answers': [
                                {'text': '#complexcausality', 'correct': True},
                                {'text': '#emergentproperties', 'correct': False},
                                {'text': '#networks', 'correct': False},
                                {'text': '#systemdynamics', 'correct': False},
                            ],
                            'explanation': 'The intervention triggered competing causal pathways with offsetting environmental effects.'
                        },
                    ]
                },
                {
                    'title': '#emergentproperties',
                    'definition': 'Understand nonlinear effects of complex systems.',
                    'questions': [
                        {
                            'question': 'Crop yield increases dramatically once soil biodiversity passes a threshold. What makes this an emergent property?',
                            'answers': [
                                {'text': 'Each microbe adds yield linearly.', 'correct': False},
                                {'text': 'Yield arises from unpredictable microbe interactions', 'correct': True},
                                {'text': "It results solely from fertilizer inputs.", 'correct': False},
                                {'text': "It's a random spike.", 'correct': False},
                            ],
                            'explanation': 'Emergent properties occur when interactions yield system-level outcomes not explainable by parts alone.'
                        },
                        {
                            'question': 'Two study groups have similar individual skill levels, yet one greatly outperforms the other due to collaboration norms. What is emergent here?',
                            'answers': [
                                {'text': 'Individual intelligence', 'correct': False},
                                {'text': 'Group-level cohesion and productivity', 'correct': True},
                                {'text': 'Instructor bias', 'correct': False},
                                {'text': 'Sample error', 'correct': False},
                            ],
                            'explanation': 'Collective behavior producing new properties beyond individuals signifies emergence.'
                        },
                        {
                            'question': 'A slight rise in car numbers suddenly causes gridlock. Which best explains the phenomenon?',
                            'answers': [
                                {'text': 'Simple addition of vehicles', 'correct': False},
                                {'text': 'An emergent property of driver interactions', 'correct': True},
                                {'text': 'A measurement error', 'correct': False},
                                {'text': 'Unrelated trend', 'correct': False},
                            ],
                            'explanation': 'Nonlinear tipping points in aggregated behavior mark emergent dynamics.'
                        },
                        {
                            'question': 'Individual ants follow simple local rules, yet the colony optimizes foraging routes. Why is this emergent?',
                            'answers': [
                                {'text': 'One ant directs all others', 'correct': False},
                                {'text': 'Colony-level efficiency arises from interactions, not individual intelligence', 'correct': True},
                                {'text': 'Ants are genetically programmed for optimization', 'correct': False},
                                {'text': 'The queen coordinates routes', 'correct': False},
                            ],
                            'explanation': 'Simple rules combine to produce intelligent collective behavior—a hallmark of emergence.'
                        },
                        {
                            'question': 'A social media platform adds a "like" button. Over time, viral content, echo chambers, and polarization emerge. Which HC captures this?',
                            'answers': [
                                {'text': '#emergentproperties', 'correct': True},
                                {'text': '#complexcausality', 'correct': False},
                                {'text': '#networks', 'correct': False},
                                {'text': '#systemmapping', 'correct': False},
                            ],
                            'explanation': 'Platform-level dynamics emerged from simple user interactions and feedback loops, not from deliberate design.'
                        },
                        {
                            'question': 'A classroom of equally skilled students forms study groups. One group develops highly effective problem-solving norms. What is emergent?',
                            'answers': [
                                {'text': 'Individual problem-solving skill', 'correct': False},
                                {'text': 'Group-level norms and collaborative patterns', 'correct': True},
                                {'text': 'Teacher intervention', 'correct': False},
                                {'text': 'Textbook quality', 'correct': False},
                            ],
                            'explanation': 'The group\'s collective performance cannot be reduced to individual capabilities—it emerges from interaction patterns.'
                        },
                        {
                            'question': 'Housing prices in a neighborhood spike once a critical number of high-income residents move in, triggering gentrification. What explains this threshold effect?',
                            'answers': [
                                {'text': 'Linear price accumulation', 'correct': False},
                                {'text': 'An emergent state transition at a critical point', 'correct': True},
                                {'text': 'Government price controls', 'correct': False},
                                {'text': 'Random market fluctuation', 'correct': False},
                            ],
                            'explanation': 'Crossing a threshold creates a qualitatively new state—gentrification emerges when interactions reach critical mass.'
                        },
                        {
                            'question': 'A flock of birds forms intricate patterns governed by three simple rules per bird. Why is this emergence, not aggregation?',
                            'answers': [
                                {'text': 'The pattern is just the sum of individual flights', 'correct': False},
                                {'text': 'Collective shapes arise that no single bird encodes', 'correct': True},
                                {'text': 'The lead bird directs formation', 'correct': False},
                                {'text': 'It is random variation', 'correct': False},
                            ],
                            'explanation': 'Global patterns are generated by local interactions without central control—emergence produces forms no individual contains.'
                        },
                        {
                            'question': 'A city planner adds bike lanes. Initially car traffic slows and buses delay, but the system eventually stabilizes at a new equilibrium with more cycling. Which HCs explain this?',
                            'answers': [
                                {'text': '#emergentproperties and #systemdynamics', 'correct': True},
                                {'text': '#networks and #complexcausality', 'correct': False},
                                {'text': '#levelsofanalysis and #systemmapping', 'correct': False},
                                {'text': 'Linear causality alone', 'correct': False},
                            ],
                            'explanation': 'A new stable state emerged through feedback loops as commuters adapted—combining emergence with system dynamics.'
                        },
                        {
                            'question': 'A market economy produces stable prices without central planning. What makes price stability emergent?',
                            'answers': [
                                {'text': 'Government sets all prices', 'correct': False},
                                {'text': 'Prices emerge from distributed interactions among buyers and sellers', 'correct': True},
                                {'text': 'Businesses coordinate explicitly', 'correct': False},
                                {'text': 'Prices are pre-determined', 'correct': False},
                            ],
                            'explanation': 'Market equilibrium is a system-level property emerging from local transactions, not from central design.'
                        },
                    ]
                },
                {
                    'title': '#levelsofanalysis',
                    'definition': 'Integrate explanations across multiple scales.',
                    'questions': [
                        {
                            'question': 'A scientist studies climate change by combining global atmospheric models, regional land-use patterns, and household energy habits. Which approach is used?',
                            'answers': [
                                {'text': 'System mapping', 'correct': False},
                                {'text': 'Levels of analysis', 'correct': True},
                                {'text': 'Network topology', 'correct': False},
                                {'text': 'Complex causality', 'correct': False},
                            ],
                            'explanation': 'Integrating explanations across scales exemplifies multi-level analysis.'
                        },
                        {
                            'question': 'A company links employee burnout to both team culture and national labor laws. What makes this a strong #levelsofanalysis example?',
                            'answers': [
                                {'text': 'Focus on a single variable', 'correct': False},
                                {'text': 'Connection between individual and structural levels', 'correct': True},
                                {'text': 'Random sampling', 'correct': False},
                                {'text': 'Emergent property alone', 'correct': False},
                            ],
                            'explanation': 'Analyzing interactions between micro and macro levels shows multi-level reasoning.'
                        },
                        {
                            'question': 'Researchers examine how neuronal activity influences group decision outcomes. Which additional level would strengthen their analysis?',
                            'answers': [
                                {'text': 'Only adding more participants', 'correct': False},
                                {'text': 'Considering social context and communication patterns', 'correct': True},
                                {'text': 'Ignoring biology', 'correct': False},
                                {'text': 'Focusing solely on statistics', 'correct': False},
                            ],
                            'explanation': 'Adding higher-order social levels complements lower-level neural analysis.'
                        },
                        {
                            'question': 'Urban planners find that neighborhood walkability depends on sidewalk width (micro), zoning laws (meso), and federal infrastructure funding (macro). Why does this require multi-level analysis?',
                            'answers': [
                                {'text': 'Only one level matters', 'correct': False},
                                {'text': 'Each level independently contributes; integration reveals full causality', 'correct': True},
                                {'text': 'Federal funding alone determines walkability', 'correct': False},
                                {'text': 'Micro-level factors are irrelevant', 'correct': False},
                            ],
                            'explanation': 'Complete understanding requires connecting physical design, policy, and structural resources across scales.'
                        },
                        {
                            'question': 'A public health study shows that diabetes rates correlate with individual diet choices, neighborhood food deserts, and national agricultural subsidies. Which level is missing if researchers only examine personal behavior?',
                            'answers': [
                                {'text': 'The micro level', 'correct': False},
                                {'text': 'The meso and macro structural levels', 'correct': True},
                                {'text': 'The temporal dimension', 'correct': False},
                                {'text': 'The network topology', 'correct': False},
                            ],
                            'explanation': 'Individual choices are shaped by community resources and policy structures; ignoring these levels produces incomplete explanations.'
                        },
                        {
                            'question': 'Economists study inflation by analyzing consumer spending (micro), corporate pricing strategies (meso), and central bank policy (macro). What distinguishes this from single-level analysis?',
                            'answers': [
                                {'text': 'It focuses only on central banks', 'correct': False},
                                {'text': 'It integrates mechanisms across scales to explain system behavior', 'correct': True},
                                {'text': 'It ignores individual actions', 'correct': False},
                                {'text': 'It treats all levels identically', 'correct': False},
                            ],
                            'explanation': 'Multi-level analysis reveals how interactions across scales produce macroeconomic outcomes.'
                        },
                        {
                            'question': 'A school intervention targets individual student motivation (micro), teacher training (meso), and district funding allocation (macro). Early results show gains only when all three levels are addressed. What does this demonstrate?',
                            'answers': [
                                {'text': 'Macro-level policy is sufficient alone', 'correct': False},
                                {'text': 'Interdependence across levels; isolated changes are insufficient', 'correct': True},
                                {'text': 'Micro-level motivation is unimportant', 'correct': False},
                                {'text': 'Only one level needs intervention', 'correct': False},
                            ],
                            'explanation': 'Effective change often requires coordinated intervention across multiple scales; single-level approaches may fail.'
                        },
                        {
                            'question': 'Sociologists explain homelessness by examining personal circumstances (job loss), community housing markets (affordability), and national safety-net policies (welfare programs). Why is this multi-level?',
                            'answers': [
                                {'text': 'It attributes homelessness solely to individual failure', 'correct': False},
                                {'text': 'It connects individual experiences to structural and institutional contexts', 'correct': True},
                                {'text': 'It ignores personal responsibility', 'correct': False},
                                {'text': 'It focuses exclusively on federal policy', 'correct': False},
                            ],
                            'explanation': 'Multi-level analysis situates individual outcomes within broader social and economic structures.'
                        },
                        {
                            'question': 'A tech company analyzes productivity by studying individual work habits (micro), team collaboration norms (meso), and organizational incentive structures (macro). Which insight requires all three levels?',
                            'answers': [
                                {'text': 'Individual habits alone determine outcomes', 'correct': False},
                                {'text': 'Productivity emerges from interactions across personal, social, and institutional levels', 'correct': True},
                                {'text': 'Only organizational policy matters', 'correct': False},
                                {'text': 'Team norms are irrelevant', 'correct': False},
                            ],
                            'explanation': 'Understanding productivity requires analyzing how individual behavior, group dynamics, and institutional design interact.'
                        },
                        {
                            'question': 'Environmental scientists study deforestation through satellite imagery (macro-scale land cover), logging company practices (meso-level economics), and farmer decision-making (micro-level livelihoods). What makes this approach comprehensive?',
                            'answers': [
                                {'text': 'It focuses solely on farmer choices', 'correct': False},
                                {'text': 'It integrates ecological, economic, and behavioral explanations across scales', 'correct': True},
                                {'text': 'It ignores economic incentives', 'correct': False},
                                {'text': 'It examines only satellite data', 'correct': False},
                            ],
                            'explanation': 'Deforestation cannot be understood through one lens; multi-level integration reveals how global, regional, and local factors interact.'
                        },
                    ]
                },
                {
                    'title': '#networks',
                    'definition': 'Analyze the structure of connections to explain system-level outcomes.',
                    'questions': [
                        {
                            'question': "An intern's ideas stay local until shared with a colleague who interacts across departments. Which network feature enabled diffusion?",
                            'answers': [
                                {'text': 'Low density', 'correct': False},
                                {'text': 'High betweenness centrality', 'correct': True},
                                {'text': 'Uniform distribution', 'correct': False},
                                {'text': 'Isolated nodes', 'correct': False},
                            ],
                            'explanation': 'A node with high betweenness bridges clusters, spreading information efficiently.'
                        },
                        {
                            'question': 'In a disease network, some individuals have far more contacts than others. Why do these "super-connectors" matter?',
                            'answers': [
                                {'text': 'They slow infection', 'correct': False},
                                {'text': 'They act as hubs in a scale-free network', 'correct': True},
                                {'text': 'They reduce clustering', 'correct': False},
                                {'text': 'They eliminate paths', 'correct': False},
                            ],
                            'explanation': 'Highly connected hubs accelerate propagation through networks.'
                        },
                        {
                            'question': 'A celebrity tweet causes rapid trend adoption compared to thousands of smaller users posting the same thing. Which concept explains this?',
                            'answers': [
                                {'text': 'Clustering coefficient', 'correct': False},
                                {'text': 'Network centralization and hub influence', 'correct': True},
                                {'text': 'Decentralized graph structure', 'correct': False},
                                {'text': 'Emergent property', 'correct': False},
                            ],
                            'explanation': 'Centralized networks concentrate influence in a few nodes with high reach.'
                        },
                        {
                            'question': 'A rumor spreads faster in a company with tightly knit teams than in one with dispersed connections. Which network property drives this difference?',
                            'answers': [
                                {'text': 'Low betweenness', 'correct': False},
                                {'text': 'High clustering coefficient', 'correct': True},
                                {'text': 'Random topology', 'correct': False},
                                {'text': 'Sparse connectivity', 'correct': False},
                            ],
                            'explanation': 'High clustering creates dense local connections, accelerating information flow within groups.'
                        },
                        {
                            'question': 'Removing a single airport disrupts global travel far more than removing ten small regional airports. What network principle explains this?',
                            'answers': [
                                {'text': 'All nodes have equal importance', 'correct': False},
                                {'text': 'Hub dominance in scale-free networks', 'correct': True},
                                {'text': 'Networks are uniformly distributed', 'correct': False},
                                {'text': 'Regional airports have higher centrality', 'correct': False},
                            ],
                            'explanation': 'Scale-free networks depend on hubs; their removal fragments the system more than removing peripheral nodes.'
                        },
                        {
                            'question': 'In a scientific collaboration network, researchers who bridge different subfields produce more innovative work. Which network concept captures their structural position?',
                            'answers': [
                                {'text': 'Degree centrality', 'correct': False},
                                {'text': 'Structural holes or brokerage', 'correct': True},
                                {'text': 'Clustering density', 'correct': False},
                                {'text': 'Path redundancy', 'correct': False},
                            ],
                            'explanation': 'Brokers who span structural holes connect otherwise isolated groups, facilitating novel combinations of ideas.'
                        },
                        {
                            'question': 'A social movement gains momentum when activists connect previously isolated community groups. What network change enabled this?',
                            'answers': [
                                {'text': 'Decreased connectivity', 'correct': False},
                                {'text': 'Formation of bridging ties across clusters', 'correct': True},
                                {'text': 'Increased isolation', 'correct': False},
                                {'text': 'Removal of central nodes', 'correct': False},
                            ],
                            'explanation': 'Bridging ties link separate clusters, enabling coordinated action and information flow across the network.'
                        },
                        {
                            'question': 'A power grid is designed so that no single failure cascades into widespread blackouts. Which network feature provides this resilience?',
                            'answers': [
                                {'text': 'Centralization around one hub', 'correct': False},
                                {'text': 'Redundant pathways and distributed connections', 'correct': True},
                                {'text': 'Sparse, isolated nodes', 'correct': False},
                                {'text': 'Minimal connectivity', 'correct': False},
                            ],
                            'explanation': 'Redundant pathways ensure that failures can be routed around, preventing system-wide collapse.'
                        },
                        {
                            'question': 'An organization finds that innovation spreads slowly despite many employee connections, because teams rarely interact across departments. What network property is lacking?',
                            'answers': [
                                {'text': 'High within-group clustering', 'correct': False},
                                {'text': 'Weak ties or inter-cluster bridges', 'correct': True},
                                {'text': 'Strong internal bonds', 'correct': False},
                                {'text': 'High local density', 'correct': False},
                            ],
                            'explanation': 'Weak ties that bridge departments enable information and innovation to flow across organizational boundaries.'
                        },
                        {
                            'question': 'Epidemiologists target vaccination at the most-connected individuals in a social network. Why is this strategy effective?',
                            'answers': [
                                {'text': 'It vaccinates the least important people', 'correct': False},
                                {'text': 'It disrupts transmission pathways through high-degree nodes', 'correct': True},
                                {'text': 'It ignores network structure', 'correct': False},
                                {'text': 'It focuses on isolated individuals', 'correct': False},
                            ],
                            'explanation': 'Targeting hubs reduces transmission potential by cutting off key pathways in the network.'
                        },
                    ]
                },
                {
                    'title': '#systemdynamics',
                    'definition': 'Use the tools of phase spaces--including attractors, critical points, and basins--to describe and predict the ways a complex system changes over time.',
                    'questions': [
                        {
                            'question': 'A struggling town invests in beautification, triggering local employment and attracting business until prosperity stabilizes. What phase-space element describes the final state?',
                            'answers': [
                                {'text': 'Critical point', 'correct': False},
                                {'text': 'Attractor', 'correct': True},
                                {'text': 'Feedback loop', 'correct': False},
                                {'text': 'Variable shift', 'correct': False},
                            ],
                            'explanation': 'An attractor is a stable equilibrium toward which the system moves.'
                        },
                        {
                            'question': "An individual's sleep and stress stabilize only after reaching a tipping point of lifestyle adjustments. This tipping point represents:",
                            'answers': [
                                {'text': 'Attractor basin', 'correct': False},
                                {'text': 'Critical point', 'correct': True},
                                {'text': 'Random shock', 'correct': False},
                                {'text': 'Feedback error', 'correct': False},
                            ],
                            'explanation': 'Crossing a critical point shifts the system into a new regime.'
                        },
                        {
                            'question': 'Global warming accelerates beyond 1.5 °C, leading to irreversible ice-sheet loss. Which concept captures this transition?',
                            'answers': [
                                {'text': 'Stable basin', 'correct': False},
                                {'text': 'Critical threshold between basins', 'correct': True},
                                {'text': 'Emergent property', 'correct': False},
                                {'text': 'Linear trend', 'correct': False},
                            ],
                            'explanation': 'Crossing a threshold between basins changes the system\'s trajectory.'
                        },
                        {
                            'question': 'A lake ecosystem alternates between clear water with abundant plants and murky water dominated by algae. Small nutrient increases have little effect until a threshold triggers regime shift. What describes these two stable states?',
                            'answers': [
                                {'text': 'Random fluctuations', 'correct': False},
                                {'text': 'Alternative attractors in different basins', 'correct': True},
                                {'text': 'Linear progressions', 'correct': False},
                                {'text': 'Temporary deviations', 'correct': False},
                            ],
                            'explanation': 'Alternative attractors represent distinct stable states; systems can flip between them when pushed past critical thresholds.'
                        },
                        {
                            'question': 'A rehabilitation program shows that patients with moderate initial improvements tend to continue recovering, while those with minimal early progress often relapse. What phase-space concept explains this pattern?',
                            'answers': [
                                {'text': 'Uniform change across all states', 'correct': False},
                                {'text': 'Basins of attraction pulling toward different outcomes', 'correct': True},
                                {'text': 'Random treatment responses', 'correct': False},
                                {'text': 'Linear dose-response relationship', 'correct': False},
                            ],
                            'explanation': 'Initial conditions determine which basin (recovery vs. relapse) a patient falls into, shaping long-term trajectory.'
                        },
                        {
                            'question': 'A financial market oscillates between boom and bust cycles, stabilizing temporarily in each state before external shocks trigger transitions. Which system dynamics framework applies?',
                            'answers': [
                                {'text': 'Simple linear growth', 'correct': False},
                                {'text': 'Multiple attractors with perturbation-driven transitions', 'correct': True},
                                {'text': 'Continuous smooth progression', 'correct': False},
                                {'text': 'Isolated variables', 'correct': False},
                            ],
                            'explanation': 'Markets exhibit multiple stable attractors; shocks can push the system across thresholds into new regimes.'
                        },
                        {
                            'question': 'A forest fire regime shifts dramatically when average temperature rises by just 2°C, moving from infrequent small fires to frequent large fires. What dynamic occurred?',
                            'answers': [
                                {'text': 'Gradual linear increase in fire size', 'correct': False},
                                {'text': 'Crossing a critical point leading to regime change', 'correct': True},
                                {'text': 'Random environmental variation', 'correct': False},
                                {'text': 'Reversible temperature effect', 'correct': False},
                            ],
                            'explanation': 'Small parameter changes can trigger large qualitative shifts when systems cross critical thresholds.'
                        },
                        {
                            'question': 'A social network platform remains stable with moderate user engagement for years. Suddenly, a viral feature causes explosive growth, then stabilizes at a much higher equilibrium. What phase-space elements are involved?',
                            'answers': [
                                {'text': 'Only one stable state exists', 'correct': False},
                                {'text': 'Transition from one attractor to another via critical point', 'correct': True},
                                {'text': 'Purely random growth patterns', 'correct': False},
                                {'text': 'Linear user accumulation', 'correct': False},
                            ],
                            'explanation': 'The system moved from one stable state (low engagement) through a critical transition to a new attractor (high engagement).'
                        },
                        {
                            'question': 'Urban planners observe that neighborhoods with 15% green space tend to decline in quality over time, while those with 25% green space tend to improve. The 20% threshold marks a transition point. What best describes this?',
                            'answers': [
                                {'text': 'Green space has no systematic effect', 'correct': False},
                                {'text': 'A critical point separating two attractor basins', 'correct': True},
                                {'text': 'All neighborhoods eventually converge', 'correct': False},
                                {'text': 'Random neighborhood variation', 'correct': False},
                            ],
                            'explanation': 'The threshold separates basins of attraction; neighborhoods below it spiral down, those above improve toward stable desirable states.'
                        },
                        {
                            'question': 'A species population remains stable at low levels despite conservation efforts. After habitat restoration crosses a threshold, population rapidly grows and stabilizes at carrying capacity. Which concepts apply?',
                            'answers': [
                                {'text': 'Simple linear growth from conservation', 'correct': False},
                                {'text': 'Critical point triggering transition between population attractors', 'correct': True},
                                {'text': 'Random population fluctuation', 'correct': False},
                                {'text': 'Conservation has no effect', 'correct': False},
                            ],
                            'explanation': 'The system was trapped in a low-population attractor; crossing the critical threshold enabled transition to a high-population stable state.'
                        },
                    ]
                },
                {
                    'title': '#systemmapping',
                    'definition': 'Develop and analyze representations of complex systems by deconstructing them and conceptualizing their constituent parts in different ways, guided by an explanatory challenge.',
                    'questions': [
                        {
                            'question': 'Mapping the hospital by department hides inefficiencies; mapping by function reveals redundant education campaigns. Which map was better and why?',
                            'answers': [
                                {'text': "By department, because it's simpler", 'correct': False},
                                {'text': 'By function, because it aligned with the explanatory challenge', 'correct': True},
                                {'text': 'By hierarchy, because it\'s traditional', 'correct': False},
                                {'text': 'By budget size', 'correct': False},
                            ],
                            'explanation': 'The chosen deconstruction must best address the explanatory challenge.'
                        },
                        {
                            'question': 'Researchers group variables into extrinsic (fence features) and intrinsic (animal behavior) factors. What makes this a strong application of #systemmapping?',
                            'answers': [
                                {'text': 'Clear functional decomposition', 'correct': True},
                                {'text': 'Random variable listing', 'correct': False},
                                {'text': 'Focus on causal loops', 'correct': False},
                                {'text': 'Lack of structure', 'correct': False},
                            ],
                            'explanation': 'Grouping components by function clarifies relevant relationships.'
                        },
                        {
                            'question': 'Three students categorize attendees differently—by industry, by friendliness, by city involvement. Who applies #systemmapping most effectively?',
                            'answers': [
                                {'text': 'The student whose grouping best fits their goal', 'correct': True},
                                {'text': 'The one with most categories', 'correct': False},
                                {'text': 'The fastest approach', 'correct': False},
                                {'text': 'The one who uses random grouping', 'correct': False},
                            ],
                            'explanation': 'System mapping is guided by purpose, not uniform structure.'
                        },
                        {
                            'question': 'A city planner maps traffic flow by arterial roads to assess congestion, then remaps by commuter origin-destination pairs to design transit routes. Why use two different maps?',
                            'answers': [
                                {'text': 'One map is always sufficient', 'correct': False},
                                {'text': 'Different decompositions reveal insights for different challenges', 'correct': True},
                                {'text': 'The second map is redundant', 'correct': False},
                                {'text': 'Maps should never change', 'correct': False},
                            ],
                            'explanation': 'System mapping adapts to the explanatory challenge; different questions require different ways of decomposing the system.'
                        },
                        {
                            'question': 'An education researcher maps a school by grade level, then by student skill trajectories across grades. The second map reveals that struggling readers fall behind in multiple subjects. What principle does this illustrate?',
                            'answers': [
                                {'text': 'Static organizational charts are sufficient', 'correct': False},
                                {'text': 'Reconceptualizing system parts can expose hidden patterns', 'correct': True},
                                {'text': 'Grade-level mapping is always wrong', 'correct': False},
                                {'text': 'Only one valid system representation exists', 'correct': False},
                            ],
                            'explanation': 'Effective system mapping involves trying different decompositions to match the problem being investigated.'
                        },
                        {
                            'question': 'A business consultant maps a company by reporting hierarchy, but finds it obscures collaboration patterns. Remapping by project teams reveals bottlenecks. Why did the second map succeed?',
                            'answers': [
                                {'text': 'It reflected the formal structure', 'correct': False},
                                {'text': 'It aligned system components with the workflow challenge', 'correct': True},
                                {'text': 'Hierarchy is never useful', 'correct': False},
                                {'text': 'Project teams are always the best unit', 'correct': False},
                            ],
                            'explanation': 'The functional grouping (projects) better matched the explanatory goal (workflow efficiency) than the formal grouping (hierarchy).'
                        },
                        {
                            'question': 'Ecologists map a forest by tree species distribution, then by nutrient flow pathways. The second map reveals that key decomposer organisms are declining. What does this demonstrate?',
                            'answers': [
                                {'text': 'Species distribution is irrelevant', 'correct': False},
                                {'text': 'Reconceptualizing by function highlights different causal mechanisms', 'correct': True},
                                {'text': 'Only one ecological map is valid', 'correct': False},
                                {'text': 'Nutrient flow is always the best lens', 'correct': False},
                            ],
                            'explanation': 'Decomposing the system by ecological function (nutrient cycling) exposed dynamics hidden in structural maps (species locations).'
                        },
                        {
                            'question': 'A public health team maps disease transmission by neighborhood boundaries, then by social network connections. The network map shows disease jumping across neighborhoods through workplace contacts. What principle applies?',
                            'answers': [
                                {'text': 'Geographic boundaries fully determine transmission', 'correct': False},
                                {'text': 'Different system decompositions reveal different transmission mechanisms', 'correct': True},
                                {'text': 'Network maps are always superior', 'correct': False},
                                {'text': 'Only one map is needed', 'correct': False},
                            ],
                            'explanation': 'The functional map (social ties) revealed transmission pathways invisible in the spatial map (geography).'
                        },
                        {
                            'question': 'Engineers map an electrical grid by voltage levels to design transformers, then by load patterns to predict failures. Why are both maps necessary?',
                            'answers': [
                                {'text': 'They answer different explanatory challenges', 'correct': True},
                                {'text': 'One is redundant', 'correct': False},
                                {'text': 'Only structural maps matter', 'correct': False},
                                {'text': 'Load patterns are irrelevant', 'correct': False},
                            ],
                            'explanation': 'Design challenges require structural decomposition (voltage), while reliability challenges require functional decomposition (load patterns).'
                        },
                        {
                            'question': 'A software team maps their codebase by file structure, but this hides dependencies. Remapping by feature modules reveals tightly coupled components that cause bugs. What does this illustrate about system mapping?',
                            'answers': [
                                {'text': 'File structure is the only valid organization', 'correct': False},
                                {'text': 'The decomposition should match the problem being solved', 'correct': True},
                                {'text': 'Dependencies are unimportant', 'correct': False},
                                {'text': 'One map fits all purposes', 'correct': False},
                            ],
                            'explanation': 'System mapping is guided by explanatory goals; debugging requires decomposing by functional relationships, not just file organization.'
                        },
                    ]
                },
                {
                    'title': 'Unit-Level Challenge',
                    'definition': 'Integrative Scenarios — Harder',
                    'questions': [
                        {
                            'question': 'Five years after Metroville launched a downtown congestion tax, emissions initially fell by 30%. But new data show that suburban air pollution has increased, as delivery companies rerouted trucks through outer residential zones. City officials are debating whether to adjust tolling patterns or redesign distribution networks. Which combination of HCs best explains this outcome?',
                            'answers': [
                                {'text': '#systemmapping and #complexcausality', 'correct': True},
                                {'text': '#networks and #systemdynamics', 'correct': False},
                                {'text': '#levelsofanalysis and #emergentproperties', 'correct': False},
                                {'text': '#systemmapping and #levelsofanalysis', 'correct': False},
                            ],
                            'explanation': 'The system\'s design must be remapped to account for causal spillovers — a hallmark of complex causality revealed through system mapping.'
                        },
                        {
                            'question': 'After a major company transitions to a flat organizational structure, innovation rates spike — but internal conflict also rises. Cross-functional teams now rely on dense Slack channels, creating "communication clusters" that unintentionally isolate departments. Some employees thrive through inter-cluster collaboration, while others disengage. Which HCs together help diagnose this system\'s new dynamics?',
                            'answers': [
                                {'text': '#emergentproperties and #networks', 'correct': True},
                                {'text': '#complexcausality and #systemmapping', 'correct': False},
                                {'text': '#systemdynamics and #levelsofanalysis', 'correct': False},
                                {'text': '#networks and #complexcausality', 'correct': False},
                            ],
                            'explanation': 'The interplay between informal network patterns and emergent team behavior explains the dual effect of creativity and conflict.'
                        },
                        {
                            'question': 'Researchers studying global drought find that smallholder farmers in Sub-Saharan Africa experience water scarcity differently depending on local irrigation practices, national subsidies, and global grain markets. Their final model links individual behavior to policy incentives and planetary climate shifts. Which HC is most crucial for producing this comprehensive model?',
                            'answers': [
                                {'text': '#levelsofanalysis', 'correct': True},
                                {'text': '#systemmapping', 'correct': False},
                                {'text': '#complexcausality', 'correct': False},
                                {'text': '#systemdynamics', 'correct': False},
                            ],
                            'explanation': 'Integrating micro (farm), meso (policy), and macro (climate) explanations typifies reasoning across multiple levels of analysis.'
                        },
                        {
                            'question': 'A country\'s financial system stays stable for years despite rising debt. Then, following a rumor of bank insolvency, credit availability collapses overnight — triggering widespread recession even in unrelated industries. Analysts later show that public confidence was the "control variable" governing systemic stability. Which HC best characterizes this shift?',
                            'answers': [
                                {'text': '#systemdynamics', 'correct': True},
                                {'text': '#emergentproperties', 'correct': False},
                                {'text': '#networks', 'correct': False},
                                {'text': '#complexcausality', 'correct': False},
                            ],
                            'explanation': 'A small perturbation crossed a critical threshold, moving the economy from one attractor state (stability) into another (recession).'
                        },
                        {
                            'question': 'A rainforest restoration project reveals that simply replanting trees fails to restore biodiversity. Only when native pollinators return, soil microorganisms recover, and predator-prey cycles reestablish does the ecosystem stabilize. The project team maps out interdependent species interactions and identifies feedback loops driving resilience. Which combination of HCs best captures this system\'s recovery pattern?',
                            'answers': [
                                {'text': '#complexcausality, #networks, and #emergentproperties', 'correct': True},
                                {'text': '#systemdynamics and #levelsofanalysis', 'correct': False},
                                {'text': '#systemmapping and #complexcausality', 'correct': False},
                                {'text': '#networks and #systemdynamics', 'correct': False},
                            ],
                            'explanation': 'Resilience arises from interacting causes (complex causality) across networked relationships that collectively yield emergent properties.'
                        },
                    ]
                },
            ]
        }
    ]
}

