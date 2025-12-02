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
                                {'text': 'Linear causation', 'correct': False, 'explanation': 'This option suggests a straight-line cause-effect which doesn’t apply as multiple factors are interacting.'},
                                {'text': 'Random correlation', 'correct': False, 'explanation': 'This is not a mere coincidence; the changes are interconnected and influence each other.'},
                                {'text': 'Reinforcing feedback loop', 'correct': True, 'explanation': 'Correct! The melting ice and warmer water create a loop that accelerates the melting process.'},
                                {'text': 'Isolated cause–effect chain', 'correct': False, 'explanation': 'The situation describes a network of interactions, not a single chain of cause and effect.'},
                            ]
                        },
                        {
                            'question': 'A city introduces free gym memberships to reduce obesity, but finds little effect because fast-food density and work stress remain high. What does this illustrate?',
                            'answers': [
                                {'text': 'A single sufficient cause', 'correct': False, 'explanation': 'The outcome shows that one cause is not enough; multiple factors are at play.'},
                                {'text': 'Interacting causal factors that offset each other', 'correct': True, 'explanation': 'Exactly! The positive effect of gym memberships is canceled out by other negative factors.'},
                                {'text': 'A non-causal coincidence', 'correct': False, 'explanation': 'There is a clear causal relationship, it’s just not effective due to other overriding factors.'},
                                {'text': 'Random variance', 'correct': False, 'explanation': 'The lack of effect is not due to chance; it’s because of other interacting causes.'},
                            ]
                        },
                        {
                            'question': 'After adding a new bus line, traffic worsens because fewer people carpool and more use feeder roads. Which HC concept explains this?',
                            'answers': [
                                {'text': 'Emergent property', 'correct': False, 'explanation': 'This is not an emergent property as the bus line was supposed to reduce traffic, not increase it.'},
                                {'text': 'Complex causality', 'correct': True, 'explanation': 'Correct! The new bus line had unexpected consequences that worsened traffic due to complex interactions.'},
                                {'text': 'Network hub effect', 'correct': False, 'explanation': 'The network hub effect doesn’t apply here as the issue is not about network centrality.'},
                                {'text': 'System mapping', 'correct': False, 'explanation': 'System mapping is about understanding the system, but doesn’t specifically explain the worsened traffic.'},
                            ]
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
                                {'text': 'Each microbe adds yield linearly.', 'correct': False, 'explanation': 'The relationship is not linear; it’s the interaction that matters.'},
                                {'text': 'Yield arises from unpredictable microbe interactions', 'correct': True, 'explanation': 'Exactly! The emergent property is the result of complex interactions among microbes.'},
                                {'text': 'It results solely from fertilizer inputs.', 'correct': False, 'explanation': 'Fertilizer alone doesn’t cause this; it’s the soil biodiversity that plays a crucial role.'},
                                {'text': "It's a random spike.", 'correct': False, 'explanation': 'This is not a random spike; it’s a significant change due to crossing a threshold.'},
                            ]
                        },
                        {
                            'question': 'Two study groups have similar individual skill levels, yet one greatly outperforms the other due to collaboration norms. What is emergent here?',
                            'answers': [
                                {'text': 'Individual intelligence', 'correct': False, 'explanation': 'It’s not about individual intelligence but how groups interact and collaborate.'},
                                {'text': 'Group-level cohesion and productivity', 'correct': True, 'explanation': 'Correct! The emergence is at the group level, not the individual level.'},
                                {'text': 'Instructor bias', 'correct': False, 'explanation': 'Instructor bias doesn’t explain the difference in group performance.'},
                                {'text': 'Sample error', 'correct': False, 'explanation': 'The sample is not the issue; it’s the group dynamics that create emergent properties.'},
                            ]
                        },
                        {
                            'question': 'A slight rise in car numbers suddenly causes gridlock. Which best explains the phenomenon?',
                            'answers': [
                                {'text': 'Simple addition of vehicles', 'correct': False, 'explanation': 'It’s not just about adding more cars; the interactions lead to a sudden change.'},
                                {'text': 'An emergent property of driver interactions', 'correct': True, 'explanation': 'Exactly! The gridlock is an emergent property of how drivers interact under certain conditions.'},
                                {'text': 'A measurement error', 'correct': False, 'explanation': 'This is not a measurement error; the phenomenon is real and due to emergent properties.'},
                                {'text': 'Unrelated trend', 'correct': False, 'explanation': 'The trend is related to the increase in cars and the resulting interactions.'},
                            ]
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
                                {'text': 'System mapping', 'correct': False, 'explanation': 'This is more about integrating different levels of analysis, not just mapping the system.'},
                                {'text': 'Levels of analysis', 'correct': True, 'explanation': 'Correct! This approach looks at climate change from multiple analytical levels.'},
                                {'text': 'Network topology', 'correct': False, 'explanation': 'Network topology doesn’t specifically relate to the multi-scale analysis being described.'},
                                {'text': 'Complex causality', 'correct': False, 'explanation': 'Complex causality is about cause-effect relationships, not directly about levels of analysis.'},
                            ]
                        },
                        {
                            'question': 'A company links employee burnout to both team culture and national labor laws. What makes this a strong #levelsofanalysis example?',
                            'answers': [
                                {'text': 'Focus on a single variable', 'correct': False, 'explanation': 'This example clearly looks at multiple variables across different levels, not a single variable.'},
                                {'text': 'Connection between individual and structural levels', 'correct': True, 'explanation': 'Exactly! It connects individual experiences of burnout to larger structural factors.'},
                                {'text': 'Random sampling', 'correct': False, 'explanation': 'Random sampling is not the focus here; it’s about the levels of analysis.'},
                                {'text': 'Emergent property alone', 'correct': False, 'explanation': 'It’s not just about emergent properties; it’s the analysis across levels that matters.'},
                            ]
                        },
                        {
                            'question': 'Researchers examine how neuronal activity influences group decision outcomes. Which additional level would strengthen their analysis?',
                            'answers': [
                                {'text': 'Only adding more participants', 'correct': False, 'explanation': 'Simply adding participants doesn’t address the multi-level analysis needed.'},
                                {'text': 'Considering social context and communication patterns', 'correct': True, 'explanation': 'Correct! This adds a crucial social context level to the analysis.'},
                                {'text': 'Ignoring biology', 'correct': False, 'explanation': 'Biology is a key part of the analysis; it shouldn’t be ignored.'},
                                {'text': 'Focusing solely on statistics', 'correct': False, 'explanation': 'Statistics are important, but they don’t replace the need for a multi-level analysis.'},
                            ]
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
                                {'text': 'Low density', 'correct': False, 'explanation': 'Low density would actually hinder the diffusion of ideas, not help it.'},
                                {'text': 'High betweenness centrality', 'correct': True, 'explanation': 'Correct! The colleague acts as a bridge, connecting different parts of the organization.'},
                                {'text': 'Uniform distribution', 'correct': False, 'explanation': 'A uniform distribution doesn’t facilitate the kind of diffusion described here.'},
                                {'text': 'Isolated nodes', 'correct': False, 'explanation': 'Isolated nodes would prevent, not enable, the diffusion of ideas.'},
                            ]
                        },
                        {
                            'question': 'In a disease network, some individuals have far more contacts than others. Why do these "super-connectors" matter?',
                            'answers': [
                                {'text': 'They slow infection', 'correct': False, 'explanation': 'Super-connectors actually speed up the spread of infection due to their many connections.'},
                                {'text': 'They act as hubs in a scale-free network', 'correct': True, 'explanation': 'Exactly! These super-connectors are crucial in maintaining the network’s connectivity.'},
                                {'text': 'They reduce clustering', 'correct': False, 'explanation': 'They actually increase the network’s clustering due to their multiple connections.'},
                                {'text': 'They eliminate paths', 'correct': False, 'explanation': 'They don’t eliminate paths; they create more paths for the infection to spread.'},
                            ]
                        },
                        {
                            'question': 'A celebrity tweet causes rapid trend adoption compared to thousands of smaller users posting the same thing. Which concept explains this?',
                            'answers': [
                                {'text': 'Clustering coefficient', 'correct': False, 'explanation': 'The clustering coefficient doesn’t specifically explain the rapid trend adoption seen here.'},
                                {'text': 'Centralized network', 'correct': True, 'explanation': 'Correct! The network is centralized around influential nodes like the celebrity.'},
                                {'text': 'Decentralized graph', 'correct': False, 'explanation': 'A decentralized graph would not have the rapid trend adoption seen with a centralized network.'},
                                {'text': 'Emergent property', 'correct': False, 'explanation': 'This is not an emergent property; it’s a result of the network’s centralized structure.'},
                            ]
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
                                {'text': 'Critical point', 'correct': False, 'explanation': 'The critical point refers to a specific moment of change, not the stable state after changes occur.'},
                                {'text': 'Attractor', 'correct': True, 'explanation': 'Exactly! The attractor is the stable state the system tends towards after the changes.'},
                                {'text': 'Feedback loop', 'correct': False, 'explanation': 'A feedback loop is a process, not a state; it doesn’t describe the final stabilized condition.'},  
                                {'text': 'Variable shift', 'correct': False, 'explanation': 'Variable shift doesn’t specifically relate to the stable final state of the system.'},
                            ]
                        },
                        {
                            'question': "An individual's sleep and stress stabilize only after reaching a tipping point of lifestyle adjustments. This tipping point represents:",
                            'answers': [
                                {'text': 'Attractor basin', 'correct': False, 'explanation': 'The attractor basin is the range of conditions for stability, not the tipping point itself.'},
                                {'text': 'Critical point', 'correct': True, 'explanation': 'Correct! The critical point is where a small change can lead to a significant shift in state.'},
                                {'text': 'Random shock', 'correct': False, 'explanation': 'This is not a random shock; it’s a predictable tipping point based on lifestyle changes.'},
                                {'text': 'Feedback error', 'correct': False, 'explanation': 'Feedback error doesn’t relate to the concept of a tipping point in this context.'},
                            ]
                        },
                        {
                            'question': 'Global warming accelerates beyond 1.5 °C, leading to irreversible ice-sheet loss. Which concept captures this transition?',
                            'answers': [
                                {'text': 'Stable basin', 'correct': False, 'explanation': 'A stable basin refers to a consistent state, not a transition between states.'},
                                {'text': 'Critical threshold between basins', 'correct': True, 'explanation': 'Exactly! This transition represents crossing a critical threshold with significant consequences.'},
                                {'text': 'Emergent property', 'correct': False, 'explanation': 'This is not an emergent property; it’s a clear threshold effect between two states.'},
                                {'text': 'Linear trend', 'correct': False, 'explanation': 'The transition is not linear; it involves crossing a critical threshold with nonlinear effects.'},
                            ]
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
                                {'text': "By department, because it's simpler", 'correct': False, 'explanation': 'Simplicity doesn’t address the explanatory challenge; effectiveness does.'},
                                {'text': 'By function, because it aligned with the explanatory challenge', 'correct': True, 'explanation': 'Exactly! The functional map better revealed the inefficiencies related to the challenge.'},
                                {'text': 'By hierarchy, because it\'s traditional', 'correct': False, 'explanation': 'Tradition doesn’t guarantee effectiveness in addressing the explanatory challenge.'},
                                {'text': 'By budget size', 'correct': False, 'explanation': 'Budget size is not relevant to the explanatory challenge regarding education campaigns.'},
                            ]
                        },
                        {
                            'question': 'Researchers group variables into extrinsic (fence features) and intrinsic (animal behavior) factors. What makes this a strong application of #systemmapping?',
                            'answers': [
                                {'text': 'Clear functional decomposition', 'correct': True, 'explanation': 'Correct! This approach clarifies how different factors may influence the system.'},
                                {'text': 'Random variable listing', 'correct': False, 'explanation': 'Random listing doesn’t provide the clarity or structure needed for effective system mapping.'},
                                {'text': 'Focus on causal loops', 'correct': False, 'explanation': 'Focusing on causal loops alone doesn’t capture the full complexity of the system.'},
                                {'text': 'Lack of structure', 'correct': False, 'explanation': 'A lack of structure would make system mapping ineffective, not strong.'},
                            ]
                        },
                        {
                            'question': 'Three students categorize attendees differently—by industry, by friendliness, by city involvement. Who applies #systemmapping most effectively?',
                            'answers': [
                                {'text': 'The student whose grouping best fits their goal', 'correct': True, 'explanation': 'Exactly! The effectiveness of system mapping depends on how well it addresses the specific goal.'},
                                {'text': 'The one with most categories', 'correct': False, 'explanation': 'Having more categories doesn’t necessarily mean a better or more effective system map.'},
                                {'text': 'The fastest approach', 'correct': False, 'explanation': 'Speed doesn’t equate to effectiveness in system mapping; thoroughness and relevance do.'},
                                {'text': 'The one who uses random grouping', 'correct': False, 'explanation': 'Random grouping is not a systematic or effective approach to mapping.'},
                            ]
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
                                {'text': '#systemmapping and #complexcausality', 'correct': True, 'explanation': 'The initial success and subsequent failure highlight the need to remap the system and understand the complex causality at play.'},
                                {'text': '#networks and #systemdynamics', 'correct': False, 'explanation': 'While networks and system dynamics are relevant, they don’t fully capture the need for remapping and understanding complex causality.'},
                                {'text': '#levelsofanalysis and #emergentproperties', 'correct': False, 'explanation': 'These concepts don’t directly address the need to remap the system and understand the specific causal relationships involved.'},
                                {'text': '#systemmapping and #levelsofanalysis', 'correct': False, 'explanation': 'This combination doesn’t fully encompass the need to understand the complex interactions and causal relationships.'},
                            ]
                        },
                        {
                            'question': 'After a major company transitions to a flat organizational structure, innovation rates spike — but internal conflict also rises. Cross-functional teams now rely on dense Slack channels, creating "communication clusters" that unintentionally isolate departments. Some employees thrive through inter-cluster collaboration, while others disengage. Which HCs together help diagnose this system\'s new dynamics?',
                            'answers': [
                                {'text': '#emergentproperties and #networks', 'correct': True, 'explanation': 'The emergence of communication clusters and their impact on innovation and conflict can be understood through the lens of emergent properties and network dynamics.'},
                                {'text': '#complexcausality and #systemmapping', 'correct': False, 'explanation': 'These concepts don’t specifically address the emergent communication patterns and their effects on the organization.'},
                                {'text': '#systemdynamics and #levelsofanalysis', 'correct': False, 'explanation': 'This combination doesn’t effectively capture the emergent and networked nature of the changes occurring in the organization.'},
                                {'text': '#networks and #complexcausality', 'correct': False, 'explanation': 'While relevant, these concepts don’t fully explain the new dynamics arising from the organizational changes.'},
                            ]
                        },
                        {
                            'question': 'Researchers studying global drought find that smallholder farmers in Sub-Saharan Africa experience water scarcity differently depending on local irrigation practices, national subsidies, and global grain markets. Their final model links individual behavior to policy incentives and planetary climate shifts. Which HC is most crucial for producing this comprehensive model?',
                            'answers': [
                                {'text': '#levelsofanalysis', 'correct': True, 'explanation': 'This comprehensive model effectively integrates multiple levels of analysis, from individual to global factors.'},
                                {'text': '#systemmapping', 'correct': False, 'explanation': 'System mapping is part of the process, but the key is the integration across levels of analysis.'},
                                {'text': '#complexcausality', 'correct': False, 'explanation': 'Understanding the complex causality is important, but this question is about the levels of analysis used in the model.'},
                                {'text': '#systemdynamics', 'correct': False, 'explanation': 'System dynamics concepts are not the primary focus in describing the comprehensive model developed by the researchers.'},
                            ]
                        },
                        {
                            'question': 'A country\'s financial system stays stable for years despite rising debt. Then, following a rumor of bank insolvency, credit availability collapses overnight — triggering widespread recession even in unrelated industries. Analysts later show that public confidence was the "control variable" governing systemic stability. Which HC best characterizes this shift?',
                            'answers': [
                                {'text': '#systemdynamics', 'correct': True, 'explanation': 'The sudden shift in the financial system’s stability illustrates a dynamic change, likely crossing a critical threshold.'},
                                {'text': '#emergentproperties', 'correct': False, 'explanation': 'Emergent properties don’t specifically explain the abrupt shift in the financial system’s stability.'},
                                {'text': '#networks', 'correct': False, 'explanation': 'Network dynamics are not the primary factor in the described shift in the financial system.'},
                                {'text': '#complexcausality', 'correct': False, 'explanation': 'While complex causality is relevant, the question specifically pertains to the dynamics of the system and the role of public confidence.'},
                            ]
                        },
                        {
                            'question': 'A rainforest restoration project reveals that simply replanting trees fails to restore biodiversity. Only when native pollinators return, soil microorganisms recover, and predator-prey cycles reestablish does the ecosystem stabilize. The project team maps out interdependent species interactions and identifies feedback loops driving resilience. Which combination of HCs best captures this system\'s recovery pattern?',
                            'answers': [
                                {'text': '#complexcausality, #networks, and #emergentproperties', 'correct': True, 'explanation': 'The recovery of the ecosystem illustrates complex causality, involves networked interactions, and results in emergent properties.'},
                                {'text': '#systemdynamics and #levelsofanalysis', 'correct': False, 'explanation': 'These concepts don’t fully capture the intricate interactions and emergent properties observed in the ecosystem recovery.'},
                                {'text': '#systemmapping and #complexcausality', 'correct': False, 'explanation': 'This combination doesn’t adequately address the networked and emergent aspects of the ecosystem recovery.'},
                                {'text': '#networks and #systemdynamics', 'correct': False, 'explanation': 'While networks and system dynamics are relevant, they don’t fully explain the recovery pattern observed in the rainforest restoration project.'},
                            ]
                        },
                    ]
                },
            ]
        }
    ]
}