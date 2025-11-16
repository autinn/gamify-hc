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
                                {'text': 'Centralized network', 'correct': True},
                                {'text': 'Decentralized graph', 'correct': False},
                                {'text': 'Emergent property', 'correct': False},
                            ],
                            'explanation': 'Centralized networks concentrate influence in a few nodes.'
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

