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
                                {'text': 'Linear causation', 'correct': False, 'explanation': 'Linear causation assumes a direct, proportional relationship, which does not apply here.'},
                                {'text': 'Random correlation', 'correct': False, 'explanation': 'The interaction is systematic and feedback-driven, emphasizing the role of feedback.'},
                                {'text': 'Reinforcing feedback loop', 'correct': True, 'explanation': 'Correct! The process accelerates itself through positive feedback.'},
                                {'text': 'Isolated cause–effect chain', 'correct': False, 'explanation': 'This is an interconnected, complex the system.'},
                            ],
                        },
                        {
                            'question': 'A city introduces free gym memberships to reduce obesity, but finds little effect because fast-food density and work stress remain high. What does this illustrate?',
                            'answers': [
                                {'text': 'A single sufficient cause', 'correct': False, 'explanation': 'Obesity is not caused by a single factor; it involves multiple interacting causes.'},
                                {'text': 'Interacting causal factors that offset each other', 'correct': True, 'explanation': 'Correct! Multiple causes interact, neutralizing the intended effect of the intervention.'},
                                {'text': 'A non-causal coincidence', 'correct': False, 'explanation': 'The outcome is due to interacting causes, showcasing systematic interactions.'},
                                {'text': 'Random variance', 'correct': False, 'explanation': 'The outcome is not random; it is driven by systematic interactions.'},
                            ],
                        },
                        {
                            'question': 'After adding a new bus line, traffic worsens because fewer people carpool and more use feeder roads. Which HC concept explains the wosened traffic?',
                            'answers': [
                                {'text': 'Emergent property', 'correct': False, 'explanation': 'Emergent properties describe system-level outcomes, but this is about causal interactions.'},
                                {'text': 'Complex causality', 'correct': True, 'explanation': 'Correct! The unintended outcome arises from interdependent variables.'},
                                {'text': 'Network hub effect', 'correct': False, 'explanation': 'The buses might be considered network hubs in some analysis, but that doesn'\t explain the traffic.'},
                                {'text': 'System mapping', 'correct': False, 'explanation': 'System mapping is a tool, not the concept explaining this outcome.'},
                            ],
                        },
                        {
                            'question': 'A hospital implements a hand-hygiene program, but infection rates remain high because antibiotic resistance spreads faster through overcrowded wards. What does this reveal about the intervention?',
                            'answers': [
                                {'text': 'It addressed only one pathway in a multi-causal system', 'correct': True, 'explanation': 'Correct! Addressing one pathway is insufficient when other dominant pathways exist.'},
                                {'text': 'Hygiene is irrelevant to infection control', 'correct': False, 'explanation': 'Hygiene is relevant but not sufficient on its own.'},
                                {'text': 'The intervention caused resistance', 'correct': False, 'explanation': 'The intervention did not cause resistance; overcrowding exacerbated it.'},
                                {'text': 'All causal factors were addressed', 'correct': False, 'explanation': 'Not all causal factors were addressed; overcrowding was overlooked.'},
                            ],
                        },
                        {
                            'question': 'A country subsidizes solar panels to cut emissions, but coal use rises as cheap electricity enables energy-intensive manufacturing. What causal dynamic occurred?',
                            'answers': [
                                {'text': 'Direct linear reduction', 'correct': False, 'explanation': 'The outcome involves unintended interactions, demonstrating the complexity of the system.'},
                                {'text': 'Unintended rebound effect via interacting variables', 'correct': True, 'explanation': 'Correct! The rebound effect arises from interconnected causal pathways.'},
                                {'text': 'Solar panels caused pollution', 'correct': False, 'explanation': 'Solar panels did not directly cause pollution; the rebound effect did.'},
                                {'text': 'Pure coincidence', 'correct': False, 'explanation': 'It might seem coincidental because of the complexity, but it results from interacting variables.'},
                            ],
                        },
                        {
                            'question': 'A school reduces class sizes to boost test scores. Scores initially rise but plateau as teacher quality varies and curriculum updates lag. What principle applies?',
                            'answers': [
                                {'text': 'Class size is the sole cause of outcomes', 'correct': False, 'explanation': 'Class size is not the only factor; teacher quality and curriculum also matter.'},
                                {'text': 'Multiple causes interact; one fix may not sustain gains', 'correct': True, 'explanation': 'Correct! Sustained improvement requires addressing multiple interacting factors.'},
                                {'text': 'Teacher quality is irrelevant', 'correct': False, 'explanation': 'Teacher quality is a key factor in student outcomes.'},
                                {'text': 'The intervention failed completely', 'correct': False, 'explanation': 'The intervention had some effect, but other factors limited its sustainability.'},
                            ],
                        },
                        {
                            'question': 'A drought prompts farmers to pump groundwater, lowering water tables, increasing costs, forcing farm closures, reducing food supply, and raising prices that incentivize distant farms to expand production. Which dynamic is most evident?',
                            'answers': [
                                {'text': 'A simple chain reaction', 'correct': False, 'explanation': 'This might seem like a simple chain reaction, but it involves multiple, interacting feedback loops.'},
                                {'text': 'Reinforcing loops across multiple causal pathways', 'correct': True, 'explanation': 'Correct! Each step in the process creates conditions that reinforce the next.'},
                                {'text': 'Random environmental variation', 'correct': False, 'explanation': 'The changes are not random; they result from specific causal interactions.'},
                                {'text': 'A single root cause', 'correct': False, 'explanation': 'There is no single root cause; multiple factors are interconnected.'},
                            ],
                        },
                        {
                            'question': 'A public health campaign reduces smoking by 10%, but lung cancer rates stay flat for 20 years. Policymakers declare failure. What complexity did they overlook?',
                            'answers': [
                                {'text': 'Temporal lag between intervention and measurable outcome', 'correct': True, 'explanation': 'Correct! There can be a long delay between an intervention and its observable effects on health outcomes.'},
                                {'text': 'Spatial distribution of smokers', 'correct': False, 'explanation': 'While relevant, this is not the main reason for the flat lung cancer rates.'},
                                {'text': 'The campaign had no effect', 'correct': False, 'explanation': 'The campaign likely had an effect, but it was not immediately visible in the cancer rates.'},
                                {'text': 'Cancer is unrelated to smoking', 'correct': False, 'explanation': 'Cancer is related to smoking, but other factors and time lags are also important.'},
                            ],
                        },
                        {
                            'question': 'A financial regulation reduces risky lending at large banks but pushes activity into unregulated shadow banks, triggering a later crisis. What explains this?',
                            'answers': [
                                {'text': 'Regulation was perfectly designed', 'correct': False, 'explanation': 'No regulation is perfect; there are always unintended consequences.'},
                                {'text': 'Risk migrated through system boundaries', 'correct': True, 'explanation': 'Correct! The risk did not disappear; it was transferred to less regulated areas of the financial system.'},
                                {'text': 'Banks became more responsible', 'correct': False, 'explanation': 'There is no evidence that banks became more responsible after the regulation.'},
                                {'text': 'Shadow banks caused the original problem', 'correct': False, 'explanation': 'Shadow banks are part of the system\'s response to regulation, not the source of the original problem.'},
                            ],
                        },
                        {
                            'question': 'After a city bans plastic bags, litter decreases but reusable bag sales spike, increasing water and energy use for washing. Which HC best frames this trade-off?',
                            'answers': [
                                {'text': '#complexcausality', 'correct': True, 'explanation': 'Correct! The ban on plastic bags had complex, interrelated effects on the environment.'},
                                {'text': '#emergentproperties', 'correct': False, 'explanation': 'This is not about emergent properties; it is about complex causality.'},
                                {'text': '#networks', 'correct': False, 'explanation': 'Network effects are not the primary factor here.'},
                                {'text': '#systemdynamics', 'correct': False, 'explanation': 'System dynamics is not the best lens for this specific trade-off.'},
                            ],
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
                                {'text': 'Each microbe adds yield linearly.', 'correct': False, 'explanation': 'The relationship is not linear; it is nonlinear and threshold-based.'},
                                {'text': 'Yield arises from unpredictable microbe interactions', 'correct': True, 'explanation': 'Correct! The increase in yield is due to complex interactions among soil microbes.'},
                                {'text': "It results solely from fertilizer inputs.", 'correct': False, 'explanation': 'Fertilizer inputs are not the only factor; microbial interactions are crucial.'},
                                {'text': "It's a random spike.", 'correct': False, 'explanation': 'The increase in yield is not random; it is caused by crossing a threshold of biodiversity.'},
                            ],
                        },
                        {
                            'question': 'Two study groups have similar individual skill levels, yet one greatly outperforms the other due to collaboration norms. What is emergent here?',
                            'answers': [
                                {'text': 'Individual intelligence', 'correct': False, 'explanation': 'The emergence comes from group dynamics, not individual traits.'},
                                {'text': 'Group-level cohesion and productivity', 'correct': True, 'explanation': 'Correct! The group\'s performance is enhanced by effective collaboration norms.'},
                                {'text': 'Instructor bias', 'correct': False, 'explanation': 'Instructor bias does not explain the difference in group performance.'},
                                {'text': 'Sample error', 'correct': False, 'explanation': 'The difference is not due to sampling error; it is due to group dynamics.'},
                            ],
                        },
                        {
                            'question': 'A slight rise in car numbers suddenly causes gridlock. Which best explains the phenomenon?',
                            'answers': [
                                {'text': 'Simple addition of vehicles', 'correct': False, 'explanation': 'The increase in cars is not the only factor; it\'s how they interact that matters.'},
                                {'text': 'An emergent property of driver interactions', 'correct': True, 'explanation': 'Correct! The gridlock is an emergent property of complex interactions among drivers.'},
                                {'text': 'A measurement error', 'correct': False, 'explanation': 'There is no indication that this is a measurement error.'},
                                {'text': 'Unrelated trend', 'correct': False, 'explanation': 'The trend is related to the increase in cars and the resulting interactions.'},
                            ],
                        },
                        {
                            'question': 'Individual ants follow simple local rules, yet the colony optimizes foraging routes. Why is this emergent?',
                            'answers': [
                                {'text': 'One ant directs all others', 'correct': False, 'explanation': 'No single ant directs the others; it is a collective emergent behavior.'},
                                {'text': 'Colony-level efficiency arises from interactions, not individual intelligence', 'correct': True, 'explanation': 'Correct! The colony\'s efficiency emerges from the interactions of individual ants following simple rules.'},
                                {'text': 'Ants are genetically programmed for optimization', 'correct': False, 'explanation': 'While ants have evolved behaviors, the optimization of foraging routes is an emergent property, not a programmed one.'},
                                {'text': 'The queen coordinates routes', 'correct': False, 'explanation': 'The queen does not coordinate the foraging routes; this is an emergent behavior of the colony.'},
                            ],
                        },
                        {
                            'question': 'A social media platform adds a "like" button. Over time, viral content, echo chambers, and polarization emerge. Which HC captures this?',
                            'answers': [
                                {'text': '#emergentproperties', 'correct': True, 'explanation': 'Correct! The dynamics of the platform led to emergent social phenomena.'},
                                {'text': '#complexcausality', 'correct': False, 'explanation': 'This is not primarily about complex causality; it\'s about emergent properties.'},
                                {'text': '#networks', 'correct': False, 'explanation': 'Network effects are involved, but they are not the main focus here.'},
                                {'text': '#systemmapping', 'correct': False, 'explanation': 'System mapping is a tool, not the concept explaining these social phenomena.'},
                            ],
                        },
                        {
                            'question': 'A classroom of equally skilled students forms study groups. One group develops highly effective problem-solving norms. What is emergent?',
                            'answers': [
                                {'text': 'Individual problem-solving skill', 'correct': False, 'explanation': 'The emergence is at the group level, not the individual level.'},
                                {'text': 'Group-level norms and collaborative patterns', 'correct': True, 'explanation': 'Correct! The group developed norms that enhanced their problem-solving effectiveness.'},
                                {'text': 'Teacher intervention', 'correct': False, 'explanation': 'The teacher did not intervene in the development of these norms.'},
                                {'text': 'Textbook quality', 'correct': False, 'explanation': 'The quality of the textbook is not the factor here; it\'s the group dynamics.'},
                            ],
                        },
                        {
                            'question': 'Housing prices in a neighborhood spike once a critical number of high-income residents move in, triggering gentrification. What explains this threshold effect?',
                            'answers': [
                                {'text': 'Linear price accumulation', 'correct': False, 'explanation': 'The relationship is not linear; it involves a threshold effect.'},
                                {'text': 'An emergent state transition at a critical point', 'correct': True, 'explanation': 'Correct! The gentrification emerges when the number of high-income residents crosses a critical threshold.'},
                                {'text': 'Government price controls', 'correct': False, 'explanation': 'Price controls are not the reason for this threshold effect.'},
                                {'text': 'Random market fluctuation', 'correct': False, 'explanation': 'The spike in housing prices is not due to random fluctuations; it is a systematic effect.'},
                            ],
                        },
                        {
                            'question': 'A flock of birds forms intricate patterns governed by three simple rules per bird. Why is this emergence, not aggregation?',
                            'answers': [
                                {'text': 'The pattern is just the sum of individual flights', 'correct': False, 'explanation': 'The pattern is not simply the sum; it is a result of complex interactions.'},
                                {'text': 'Collective shapes arise that no single bird encodes', 'correct': True, 'explanation': 'Correct! The emergent patterns are not directed or encoded by any single bird.'},
                                {'text': 'The lead bird directs formation', 'correct': False, 'explanation': 'There is no single lead bird directing the formation; it is a collective emergent behavior.'},
                                {'text': 'It is random variation', 'correct': False, 'explanation': 'The patterns are not random; they result from the interaction of simple rules.'},
                            ],
                        },
                        {
                            'question': 'A city planner adds bike lanes. Initially car traffic slows and buses delay, but the system eventually stabilizes at a new equilibrium with more cycling. Which HCs explain this?',
                            'answers': [
                                {'text': '#emergentproperties and #systemdynamics', 'correct': True, 'explanation': 'Correct! The new equilibrium is an emergent property of the system dynamics at play.'},
                                {'text': '#networks and #complexcausality', 'correct': False, 'explanation': 'These are not the primary concepts explaining the stabilization at a new equilibrium.'},
                                {'text': '#levelsofanalysis and #systemmapping', 'correct': False, 'explanation': 'These concepts do not directly explain the emergent stabilization observed.'},
                                {'text': 'Linear causality alone', 'correct': False, 'explanation': 'The situation does not resolve through linear causality; it involves emergent properties and system dynamics.'},
                            ],
                        },
                        {
                            'question': 'A market economy produces stable prices without central planning. What makes price stability emergent?',
                            'answers': [
                                {'text': 'Government sets all prices', 'correct': False, 'explanation': 'If the government set all prices, they would not be emergent properties of the market.'},
                                {'text': 'Prices emerge from distributed interactions among buyers and sellers', 'correct': True, 'explanation': 'Correct! Price stability emerges from the collective interactions in the market, not from central planning.'},
                                {'text': 'Businesses coordinate explicitly', 'correct': False, 'explanation': 'There is no need for explicit coordination among businesses for prices to stabilize.'},
                                {'text': 'Prices are pre-determined', 'correct': False, 'explanation': 'Prices are not pre-determined; they emerge from the dynamics of supply and demand.'},
                            ],
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
                                {'text': 'System mapping', 'correct': False, 'explanation': 'System mapping is a tool, not the approach being described.'},
                                {'text': 'Levels of analysis', 'correct': True, 'explanation': 'Correct! This approach integrates explanations across different scales of analysis.'},
                                {'text': 'Network topology', 'correct': False, 'explanation': 'Network topology is not the focus here; it\'s about levels of analysis.'},
                                {'text': 'Complex causality', 'correct': False, 'explanation': 'Complex causality describes interactions, but this is about integrating levels of analysis.'},
                            ],
                        },
                        {
                            'question': 'A company links employee burnout to both team culture and national labor laws. What makes this a strong #levelsofanalysis example?',
                            'answers': [
                                {'text': 'Focus on a single variable', 'correct': False, 'explanation': 'A strong #levelsofanalysis example considers multiple interacting variables at different levels.'},
                                {'text': 'Connection between individual and structural levels', 'correct': True, 'explanation': 'Correct! It links individual experiences of burnout to broader structural factors.'},
                                {'text': 'Random sampling', 'correct': False, 'explanation': 'Random sampling is not relevant to the levels of analysis framework.'},
                                {'text': 'Emergent property alone', 'correct': False, 'explanation': 'Focusing on emergent properties alone does not capture the multi-level analysis.'},
                            ],
                        },
                        {
                            'question': 'Researchers examine how neuronal activity influences group decision outcomes. Which additional level would strengthen their analysis?',
                            'answers': [
                                {'text': 'Only adding more participants', 'correct': False, 'explanation': 'Simply adding more participants does not address the multi-level analysis.'},
                                {'text': 'Considering social context and communication patterns', 'correct': True, 'explanation': 'Correct! Adding the social context provides a more comprehensive multi-level analysis.'},
                                {'text': 'Ignoring biology', 'correct': False, 'explanation': 'Biological factors at the neuronal level are part of the analysis, not to be ignored.'},
                                {'text': 'Focusing solely on statistics', 'correct': False, 'explanation': 'Statistics alone do not provide a multi-level analysis; the underlying mechanisms matter.'},
                            ],
                        },
                        {
                            'question': 'Urban planners find that neighborhood walkability depends on sidewalk width (micro), zoning laws (meso), and federal infrastructure funding (macro). Why does this require multi-level analysis?',
                            'answers': [
                                {'text': 'Only one level matters', 'correct': False, 'explanation': 'This is a multi-level issue; all mentioned levels interact to affect walkability.'},
                                {'text': 'Each level independently contributes; integration reveals full causality', 'correct': True, 'explanation': 'Correct! Understanding walkability requires integrating factors from all these levels.'},
                                {'text': 'Federal funding alone determines walkability', 'correct': False, 'explanation': 'Federal funding is a factor, but not the only one; local factors also play a significant role.'},
                                {'text': 'Micro-level factors are irrelevant', 'correct': False, 'explanation': 'Micro-level factors, like sidewalk width, are crucial to the overall analysis.'},
                            ],
                        },
                        {
                            'question': 'A public health study shows that diabetes rates correlate with individual diet choices, neighborhood food deserts, and national agricultural subsidies. Which level is missing if researchers only examine personal behavior?',
                            'answers': [
                                {'text': 'The micro level', 'correct': False, 'explanation': 'The micro level is included in personal behavior; the missing levels are meso and macro.'},
                                {'text': 'The meso and macro structural levels', 'correct': True, 'explanation': 'Correct! These levels provide essential context for understanding individual behavior.'},
                                {'text': 'The temporal dimension', 'correct': False, 'explanation': 'The temporal dimension is not the focus here; it\'s about levels of analysis.'},
                                {'text': 'The network topology', 'correct': False, 'explanation': 'Network topology is not directly relevant to the levels of analysis in this context.'},
                            ],
                        },
                        {
                            'question': 'Economists study inflation by analyzing consumer spending (micro), corporate pricing strategies (meso), and central bank policy (macro). What distinguishes this from single-level analysis?',
                            'answers': [
                                {'text': 'It focuses only on central banks', 'correct': False, 'explanation': 'This analysis includes multiple levels, not just central banks.'},
                                {'text': 'It integrates mechanisms across scales to explain system behavior', 'correct': True, 'explanation': 'Correct! It shows how interactions across levels produce macroeconomic outcomes.'},
                                {'text': 'It ignores individual actions', 'correct': False, 'explanation': 'Individual actions are considered at the micro level of analysis.'},
                                {'text': 'It treats all levels identically', 'correct': False, 'explanation': 'Different levels are analyzed for their specific contributions, not treated identically.'},
                            ],
                        },
                        {
                            'question': 'A school intervention targets individual student motivation (micro), teacher training (meso), and district funding allocation (macro). Early results show gains only when all three levels are addressed. What does this demonstrate?',
                            'answers': [
                                {'text': 'Macro-level policy is sufficient alone', 'correct': False, 'explanation': 'Macro-level policy alone is not sufficient; all levels need to be addressed.'},
                                {'text': 'Interdependence across levels; isolated changes are insufficient', 'correct': True, 'explanation': 'Correct! Effective intervention requires coordinated action across multiple levels.'},
                                {'text': 'Micro-level motivation is unimportant', 'correct': False, 'explanation': 'Micro-level motivation is important, but it must be supported by meso and macro-level changes.'},
                                {'text': 'Only one level needs intervention', 'correct': False, 'explanation': 'This is not true; interventions at multiple levels are necessary for sustained improvement.'},
                            ],
                        },
                        {
                            'question': 'Sociologists explain homelessness by examining personal circumstances (job loss), community housing markets (affordability), and national safety-net policies (welfare programs). Why is this multi-level?',
                            'answers': [
                                {'text': 'It attributes homelessness solely to individual failure', 'correct': False, 'explanation': 'This explanation ignores the structural factors that contribute to homelessness.'},
                                {'text': 'It connects individual experiences to structural and institutional contexts', 'correct': True, 'explanation': 'Correct! It shows how individual outcomes are linked to broader social and economic structures.'},
                                {'text': 'It ignores personal responsibility', 'correct': False, 'explanation': 'Personal responsibility is considered, but it is not the only factor; context matters.'},
                                {'text': 'It focuses exclusively on federal policy', 'correct': False, 'explanation': 'Federal policy is one aspect, but local and individual factors are also important.'},
                            ],
                        },
                        {
                            'question': 'A tech company analyzes productivity by studying individual work habits (micro), team collaboration norms (meso), and organizational incentive structures (macro). Which insight requires all three levels?',
                            'answers': [
                                {'text': 'Individual habits alone determine outcomes', 'correct': False, 'explanation': 'This ignores the influence of team and organizational factors on productivity.'},
                                {'text': 'Productivity emerges from interactions across personal, social, and institutional levels', 'correct': True, 'explanation': 'Correct! Productivity is affected by factors at all these levels and their interactions.'},
                                {'text': 'Only organizational policy matters', 'correct': False, 'explanation': 'Organizational policy is important, but individual and team factors also play crucial roles.'},
                                {'text': 'Team norms are irrelevant', 'correct': False, 'explanation': 'Team norms are relevant and can significantly impact productivity outcomes.'},
                            ],
                        },
                        {
                            'question': 'Environmental scientists study deforestation through satellite imagery (macro-scale land cover), logging company practices (meso-level economics), and farmer decision-making (micro-level livelihoods). What makes this approach comprehensive?',
                            'answers': [
                                {'text': 'It focuses solely on farmer choices', 'correct': False, 'explanation': 'Focusing only on farmer choices ignores the broader economic and environmental context.'},
                                {'text': 'It integrates ecological, economic, and behavioral explanations across scales', 'correct': True, 'explanation': 'Correct! This multi-level approach provides a comprehensive understanding of deforestation drivers.'},
                                {'text': 'It ignores economic incentives', 'correct': False, 'explanation': 'Economic incentives are considered at the meso level of analysis.'},
                                {'text': 'It examines only satellite data', 'correct': False, 'explanation': 'Satellite data provides one perspective; ground-level practices and decisions are also crucial.'},
                            ],
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
                                {'text': 'Low density', 'correct': False, 'explanation': 'Low density would slow down diffusion, not enable it.'},
                                {'text': 'High betweenness centrality', 'correct': True, 'explanation': 'Correct! The colleague acts as a bridge, spreading the intern\'s ideas across departmental boundaries.'},
                                {'text': 'Uniform distribution', 'correct': False, 'explanation': 'A uniform distribution of connections does not facilitate the diffusion of ideas.'},
                                {'text': 'Isolated nodes', 'correct': False, 'explanation': 'Isolated nodes would hinder, not help, the diffusion of ideas.'},
                            ],
                        },
                        {
                            'question': 'In a disease network, some individuals have far more contacts than others. Why do these "super-connectors" matter?',
                            'answers': [
                                {'text': 'They slow infection', 'correct': False, 'explanation': 'Super-connectors do not slow infection; they can actually accelerate it.'},
                                {'text': 'They act as hubs in a scale-free network', 'correct': True, 'explanation': 'Correct! These super-connectors are crucial in maintaining the network\'s connectivity and functionality.'},
                                {'text': 'They reduce clustering', 'correct': False, 'explanation': 'Super-connectors typically increase clustering in a network.'},
                                {'text': 'They eliminate paths', 'correct': False, 'explanation': 'Super-connectors do not eliminate paths; they provide important connections within the network.'},
                            ],
                        },
                        {
                            'question': 'A celebrity tweet causes rapid trend adoption compared to thousands of smaller users posting the same thing. Which concept explains this?',
                            'answers': [
                                {'text': 'Clustering coefficient', 'correct': False, 'explanation': 'The clustering coefficient is not the main factor in the rapid adoption of trends.'},
                                {'text': 'Network centralization and hub influence', 'correct': True, 'explanation': 'Correct! The influence of hubs in a centralized network explains the rapid trend adoption.'},
                                {'text': 'Decentralized graph structure', 'correct': False, 'explanation': 'A decentralized structure would not lead to rapid trend adoption from a single tweet.'},
                                {'text': 'Emergent property', 'correct': False, 'explanation': 'This is not an emergent property; it is a result of network centralization.'},
                            ],
                        },
                        {
                            'question': 'A rumor spreads faster in a company with tightly knit teams than in one with dispersed connections. Which network property drives this difference?',
                            'answers': [
                                {'text': 'Low betweenness', 'correct': False, 'explanation': 'Low betweenness would slow down the spread of the rumor, not speed it up.'},
                                {'text': 'High clustering coefficient', 'correct': True, 'explanation': 'Correct! A high clustering coefficient means more direct connections, speeding up rumor transmission.'},
                                {'text': 'Random topology', 'correct': False, 'explanation': 'A random topology would not facilitate the rapid spread of rumors.'},
                                {'text': 'Sparse connectivity', 'correct': False, 'explanation': 'Sparse connectivity would hinder, not help, the spread of information.'},
                            ],
                        },
                        {
                            'question': 'Removing a single airport disrupts global travel far more than removing ten small regional airports. What network principle explains this?',
                            'answers': [
                                {'text': 'All nodes have equal importance', 'correct': False, 'explanation': 'Not all nodes have equal importance; some are critical hubs.'},
                                {'text': 'Hub dominance in scale-free networks', 'correct': True, 'explanation': 'Correct! The removal of a hub has a disproportionately large impact on the network.'},
                                {'text': 'Networks are uniformly distributed', 'correct': False, 'explanation': 'Networks are not uniformly distributed; they have hubs and spoke patterns.'},
                                {'text': 'Regional airports have higher centrality', 'correct': False, 'explanation': 'This is not true; major airports typically have higher centrality.'},
                            ],
                        },
                        {
                            'question': 'In a scientific collaboration network, researchers who bridge different subfields produce more innovative work. Which network concept captures their structural position?',
                            'answers': [
                                {'text': 'Degree centrality', 'correct': False, 'explanation': 'Degree centrality refers to the number of direct connections, not bridging different subfields.'},
                                {'text': 'Structural holes or brokerage', 'correct': True, 'explanation': 'Correct! Bridging structural holes between subfields enhances innovative potential.'},
                                {'text': 'Clustering density', 'correct': False, 'explanation': 'Clustering density refers to how interconnected a node\'s neighbors are, not to bridging subfields.'},
                                {'text': 'Path redundancy', 'correct': False, 'explanation': 'Path redundancy refers to multiple pathways between nodes, not to the bridging of subfields.'},
                            ],
                        },
                        {
                            'question': 'A social movement gains momentum when activists connect previously isolated community groups. What network change enabled this?',
                            'answers': [
                                {'text': 'Decreased connectivity', 'correct': False, 'explanation': 'Decreased connectivity would hinder, not help, the growth of a social movement.'},
                                {'text': 'Formation of bridging ties across clusters', 'correct': True, 'explanation': 'Correct! Bridging ties connect isolated groups, enabling coordinated action.'},
                                {'text': 'Increased isolation', 'correct': False, 'explanation': 'Increased isolation would prevent the coordination needed for a social movement to gain momentum.'},
                                {'text': 'Removal of central nodes', 'correct': False, 'explanation': 'The removal of central nodes would likely disrupt, not enable, the movement.'},
                            ],
                        },
                        {
                            'question': 'A power grid is designed so that no single failure cascades into widespread blackouts. Which network feature provides this resilience?',
                            'answers': [
                                {'text': 'Centralization around one hub', 'correct': False, 'explanation': 'Centralization around one hub would create a single point of failure, reducing resilience.'},
                                {'text': 'Redundant pathways and distributed connections', 'correct': True, 'explanation': 'Correct! Redundant pathways ensure that failures can be bypassed, maintaining system stability.'},
                                {'text': 'Sparse, isolated nodes', 'correct': False, 'explanation': 'Sparse, isolated nodes would reduce the network\'s overall connectivity and resilience.'},
                                {'text': 'Minimal connectivity', 'correct': False, 'explanation': 'Minimal connectivity would make the system more vulnerable, not resilient.'},
                            ],
                        },
                        {
                            'question': 'An organization finds that innovation spreads slowly despite many employee connections, because teams rarely interact across departments. What network property is lacking?',
                            'answers': [
                                {'text': 'High within-group clustering', 'correct': False, 'explanation': 'High within-group clustering means strong connections within teams, but weak between teams.'},
                                {'text': 'Weak ties or inter-cluster bridges', 'correct': True, 'explanation': 'Correct! Weak ties between different teams or clusters are important for spreading innovation.'},
                                {'text': 'Strong internal bonds', 'correct': False, 'explanation': 'Strong internal bonds can exist, but without inter-cluster connections, innovation spread is limited.'},
                                {'text': 'High local density', 'correct': False, 'explanation': 'High local density refers to many connections in a localized area, not between different teams or departments.'},
                            ],
                        },
                        {
                            'question': 'Epidemiologists target vaccination at the most-connected individuals in a social network. Why is this strategy effective?',
                            'answers': [
                                {'text': 'It vaccinates the least important people', 'correct': False, 'explanation': 'The strategy targets the most important people in terms of network connectivity.'},
                                {'text': 'It disrupts transmission pathways through high-degree nodes', 'correct': True, 'explanation': 'Correct! Targeting highly connected individuals helps to quickly disrupt potential transmission pathways.'},
                                {'text': 'It ignores network structure', 'correct': False, 'explanation': 'The strategy specifically takes network structure into account, targeting key individuals.'},
                                {'text': 'It focuses on isolated individuals', 'correct': False, 'explanation': 'The focus is on individuals who are well-connected, not isolated.'},
                            ],
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
                                {'text': 'Critical point', 'correct': False, 'explanation': 'The critical point refers to a specific moment of change, not the stable state.'},
                                {'text': 'Attractor', 'correct': True, 'explanation': 'Correct! The final state of prosperity represents an attractor the system moves toward.'},
                                {'text': 'Feedback loop', 'correct': False, 'explanation': 'A feedback loop is a process, not a state; the question asks for a description of the final state.'},
                                {'text': 'Variable shift', 'correct': False, 'explanation': 'Variable shift does not specifically describe the stable, final state of the system.'},
                            ],
                        },
                        {
                            'question': "An individual's sleep and stress stabilize only after reaching a tipping point of lifestyle adjustments. This tipping point represents:",
                            'answers': [
                                {'text': 'Attractor basin', 'correct': False, 'explanation': 'The attractor basin is the range of conditions leading to stability, not the tipping point itself.'},
                                {'text': 'Critical point', 'correct': True, 'explanation': 'Correct! The critical point is where small changes can lead to significant shifts in the system.'},
                                {'text': 'Random shock', 'correct': False, 'explanation': 'The tipping point is not a random shock; it is a specific threshold of change.'},
                                {'text': 'Feedback error', 'correct': False, 'explanation': 'Feedback error does not describe the tipping point in this context.'},
                            ],
                        },
                        {
                            'question': 'Global warming accelerates beyond 1.5 °C, leading to irreversible ice-sheet loss. Which concept captures this transition?',
                            'answers': [
                                {'text': 'Stable basin', 'correct': False, 'explanation': 'A stable basin refers to a consistent state, not a transition between states.'},
                                {'text': 'Critical threshold between basins', 'correct': True, 'explanation': 'Correct! The transition occurs when crossing a critical threshold between different basins of attraction.'},
                                {'text': 'Emergent property', 'correct': False, 'explanation': 'This transition is not an emergent property; it is a crossing of a critical threshold.'},
                                {'text': 'Linear trend', 'correct': False, 'explanation': 'The change is not linear; it involves crossing thresholds that lead to different stable states.'},
                            ],
                        },
                        {
                            'question': 'A lake ecosystem alternates between clear water with abundant plants and murky water dominated by algae. Small nutrient increases have little effect until a threshold triggers regime shift. What describes these two stable states?',
                            'answers': [
                                {'text': 'Random fluctuations', 'correct': False, 'explanation': 'The shifts between states are not random; they are triggered by crossing thresholds.'},
                                {'text': 'Alternative attractors in different basins', 'correct': True, 'explanation': 'Correct! The clear and murky water states are alternative attractors in separate basins.'},
                                {'text': 'Linear progressions', 'correct': False, 'explanation': 'The changes are not linear progressions; they are shifts between different stable states.'},
                                {'text': 'Temporary deviations', 'correct': False, 'explanation': 'The shifts are not temporary deviations; they represent different stable states the system can occupy.'},
                            ],
                        },
                        {
                            'question': 'A rehabilitation program shows that patients with moderate initial improvements tend to continue recovering, while those with minimal early progress often relapse. What phase-space concept explains this pattern?',
                            'answers': [
                                {'text': 'Uniform change across all states', 'correct': False, 'explanation': 'The change is not uniform; it depends on the initial conditions and the basin of attraction.'},
                                {'text': 'Basins of attraction pulling toward different outcomes', 'correct': True, 'explanation': 'Correct! Patients are pulled toward different outcomes based on their initial progress and the corresponding basin of attraction.'},
                                {'text': 'Random treatment responses', 'correct': False, 'explanation': 'The responses are not random; they are influenced by the initial conditions and the basin dynamics.'},
                                {'text': 'Linear dose-response relationship', 'correct': False, 'explanation': 'The relationship is not linear; it depends on the interaction with the basin of attraction.'},
                            ],
                        },
                        {
                            'question': 'A financial market oscillates between boom and bust cycles, stabilizing temporarily in each state before external shocks trigger transitions. Which system dynamics framework applies?',
                            'answers': [
                                {'text': 'Simple linear growth', 'correct': False, 'explanation': 'The market does not follow a simple linear growth pattern; it oscillates between different states.'},
                                {'text': 'Multiple attractors with perturbation-driven transitions', 'correct': True, 'explanation': 'Correct! The market has multiple stable attractors, and transitions occur when perturbed by external shocks.'},
                                {'text': 'Continuous smooth progression', 'correct': False, 'explanation': 'The market does not progress smoothly; it has distinct boom and bust states.'},
                                {'text': 'Isolated variables', 'correct': False, 'explanation': 'The variables are not isolated; they are interconnected and influence the system dynamics.'},
                            ],
                        },
                        {
                            'question': 'A forest fire regime shifts dramatically when average temperature rises by just 2°C, moving from infrequent small fires to frequent large fires. What dynamic occurred?',
                            'answers': [
                                {'text': 'Gradual linear increase in fire size', 'correct': False, 'explanation': 'The increase in fire size is not gradual or linear; it is a sudden shift to a new regime.'},
                                {'text': 'Crossing a critical point leading to regime change', 'correct': True, 'explanation': 'Correct! The regime shift occurs when crossing a critical temperature threshold.'},
                                {'text': 'Random environmental variation', 'correct': False, 'explanation': 'The shift is not due to random variation; it is a response to systematic changes in temperature.'},
                                {'text': 'Reversible temperature effect', 'correct': False, 'explanation': 'The effect is not reversible; once the regime shifts, it stabilizes at a new level until another shift occurs.'},
                            ],
                        },
                        {
                            'question': 'A social network platform remains stable with moderate user engagement for years. Suddenly, a viral feature causes explosive growth, then stabilizes at a much higher equilibrium. What phase-space elements are involved?',
                            'answers': [
                                {'text': 'Only one stable state exists', 'correct': False, 'explanation': 'There are multiple stable states; the system moved from one to another.'},
                                {'text': 'Transition from one attractor to another via critical point', 'correct': True, 'explanation': 'Correct! The system transitioned from one attractor (moderate engagement) to another (high engagement) through a critical point.'},
                                {'text': 'Purely random growth patterns', 'correct': False, 'explanation': 'The growth patterns are not random; they follow a specific dynamic.'},
                                {'text': 'Linear user accumulation', 'correct': False, 'explanation': 'The user accumulation is not linear; it involves crossing a critical threshold.'},
                            ],
                        },
                        {
                            'question': 'Urban planners observe that neighborhoods with 15% green space tend to decline in quality over time, while those with 25% green space tend to improve. The 20% threshold marks a transition point. What best describes this?',
                            'answers': [
                                {'text': 'Green space has no systematic effect', 'correct': False, 'explanation': 'The amount of green space has a systematic effect, but it is not linear.'},
                                {'text': 'A critical point separating two attractor basins', 'correct': True, 'explanation': 'Correct! The 20% threshold is a critical point that separates two different basins of attraction.'},
                                {'text': 'All neighborhoods eventually converge', 'correct': False, 'explanation': 'Neighborhoods do not necessarily converge; they can stabilize in different attractor basins.'},
                                {'text': 'Random neighborhood variation', 'correct': False, 'explanation': 'The variation is not random; it is systematic and related to the amount of green space.'},
                            ],
                        },
                        {
                            'question': 'A species population remains stable at low levels despite conservation efforts. After habitat restoration crosses a threshold, population rapidly grows and stabilizes at carrying capacity. Which concepts apply?',
                            'answers': [
                                {'text': 'Simple linear growth from conservation', 'correct': False, 'explanation': 'The growth is not linear; it involves crossing a critical threshold.'},
                                {'text': 'Critical point triggering transition between population attractors', 'correct': True, 'explanation': 'Correct! The transition to a high-population stable state occurs when crossing a critical threshold.'},
                                {'text': 'Random population fluctuation', 'correct': False, 'explanation': 'The changes in population are not random; they are driven by crossing a threshold.'},
                                {'text': 'Conservation has no effect', 'correct': False, 'explanation': 'Conservation efforts have an effect, but their impact may not be immediately visible.'},
                            ],
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
                                {'text': "By department, because it's simpler", 'correct': False, 'explanation': 'Simplicity is not the only criterion; the map must also address the explanatory challenge.'},
                                {'text': 'By function, because it aligned with the explanatory challenge', 'correct': True, 'explanation': 'Correct! The functional map better revealed the inefficiencies related to the educational campaigns.'},
                                {'text': 'By hierarchy, because it\'s traditional', 'correct': False, 'explanation': 'Tradition does not guarantee effectiveness; the map must serve the explanatory purpose.'},
                                {'text': 'By budget size', 'correct': False, 'explanation': 'Mapping by budget size does not directly address the inefficiencies in the education campaigns.'},
                            ],
                        },
                        {
                            'question': 'Researchers group variables into extrinsic (fence features) and intrinsic (animal behavior) factors. What makes this a strong application of #systemmapping?',
                            'answers': [
                                {'text': 'Clear functional decomposition', 'correct': True, 'explanation': 'Correct! The grouping clarifies the functional relationships and causal mechanisms at play.'},
                                {'text': 'Random variable listing', 'correct': False, 'explanation': 'The variables are not listed randomly; they are grouped by their functional role in the system.'},
                                {'text': 'Focus on causal loops', 'correct': False, 'explanation': 'The focus here is on functional grouping, not directly on causal loops.'},
                                {'text': 'Lack of structure', 'correct': False, 'explanation': 'There is a clear structure in how the variables are grouped by function.'},
                            ],
                        },
                        {
                            'question': 'Three students categorize attendees differently—by industry, by friendliness, by city involvement. Who applies #systemmapping most effectively?',
                            'answers': [
                                {'text': 'The student whose grouping best fits their goal', 'correct': True, 'explanation': 'Correct! The effectiveness of the mapping depends on how well it serves the specific explanatory goal.'},
                                {'text': 'The one with most categories', 'correct': False, 'explanation': 'Having more categories does not necessarily mean a better system map.'},
                                {'text': 'The fastest approach', 'correct': False, 'explanation': 'Speed is not a criterion for effective system mapping; it must be purposeful and clear.'},
                                {'text': 'The one who uses random grouping', 'correct': False, 'explanation': 'Random grouping does not constitute a valid application of system mapping.'},
                            ],
                        },
                        {
                            'question': 'A city planner maps traffic flow by arterial roads to assess congestion, then remaps by commuter origin-destination pairs to design transit routes. Why use two different maps?',
                            'answers': [
                                {'text': 'One map is always sufficient', 'correct': False, 'explanation': 'One map is not always sufficient; different questions may require different mappings.'},
                                {'text': 'Different decompositions reveal insights for different challenges', 'correct': True, 'explanation': 'Correct! Each map provides unique insights that inform different aspects of transit planning.'},
                                {'text': 'The second map is redundant', 'correct': False, 'explanation': 'The second map is not redundant; it offers a different perspective that is crucial for designing effective transit routes.'},
                                {'text': 'Maps should never change', 'correct': False, 'explanation': 'Maps should change as needed to address different explanatory challenges and improve understanding.'},
                            ],
                        },
                        {
                            'question': 'An education researcher maps a school by grade level, then by student skill trajectories across grades. The second map reveals that struggling readers fall behind in multiple subjects. What principle does this illustrate?',
                            'answers': [
                                {'text': 'Static organizational charts are sufficient', 'correct': False, 'explanation': 'Static charts are not sufficient; they do not capture the dynamics of student skill development.'},
                                {'text': 'Reconceptualizing system parts can expose hidden patterns', 'correct': True, 'explanation': 'Correct! The second map reconceptualizes the system in a way that reveals important patterns and relationships.'},
                                {'text': 'Grade-level mapping is always wrong', 'correct': False, 'explanation': 'Grade-level mapping is not wrong, but it may be incomplete without considering skill trajectories.'},
                                {'text': 'Only one valid system representation exists', 'correct': False, 'explanation': 'There can be multiple valid representations, each serving different explanatory purposes.'},
                            ],
                        },
                        {
                            'question': 'A business consultant maps a company by reporting hierarchy, but finds it obscures collaboration patterns. Remapping by project teams reveals bottlenecks. Why did the second map succeed?',
                            'answers': [
                                {'text': 'It reflected the formal structure', 'correct': False, 'explanation': 'The formal structure does not always represent the actual collaboration patterns within the company.'},
                                {'text': 'It aligned system components with the workflow challenge', 'correct': True, 'explanation': 'Correct! The second map better aligned with the functional relationships and workflow challenges.'},
                                {'text': 'Hierarchy is never useful', 'correct': False, 'explanation': 'Hierarchy can be useful, but it may not always reveal the functional dynamics at play.'},
                                {'text': 'Project teams are always the best unit', 'correct': False, 'explanation': 'Project teams are not inherently the best unit; it depends on the context and the explanatory challenge.'},
                            ],
                        },
                        {
                            'question': 'Ecologists map a forest by tree species distribution, then by nutrient flow pathways. The second map reveals that key decomposer organisms are declining. What does this demonstrate?',
                            'answers': [
                                {'text': 'Species distribution is irrelevant', 'correct': False, 'explanation': 'Species distribution is relevant, but it is not the only factor; functional relationships matter too.'},
                                {'text': 'Reconceptualizing by function highlights different causal mechanisms', 'correct': True, 'explanation': 'Correct! Mapping by function reveals important causal mechanisms that are not apparent in structural maps.'},
                                {'text': 'Only one ecological map is valid', 'correct': False, 'explanation': 'There can be multiple valid ecological maps, each highlighting different aspects of the ecosystem.'},
                                {'text': 'Nutrient flow is always the best lens', 'correct': False, 'explanation': 'Nutrient flow is an important lens, but it is not the only one; other factors are also crucial.'},
                            ],
                        },
                        {
                            'question': 'A public health team maps disease transmission by neighborhood boundaries, then by social network connections. The network map shows disease jumping across neighborhoods through workplace contacts. What principle applies?',
                            'answers': [
                                {'text': 'Geographic boundaries fully determine transmission', 'correct': False, 'explanation': 'Geographic boundaries do not fully determine transmission; social networks also play a crucial role.'},
                                {'text': 'Different system decompositions reveal different transmission mechanisms', 'correct': True, 'explanation': 'Correct! The different mappings reveal how the disease can spread through social networks, not just geographic proximity.'},
                                {'text': 'Network maps are always superior', 'correct': False, 'explanation': 'Network maps are not inherently superior; the best map depends on the explanatory challenge.'},
                                {'text': 'Only one map is needed', 'correct': False, 'explanation': 'Multiple maps can provide complementary insights and a more comprehensive understanding of the system.'},
                            ],
                        },
                        {
                            'question': 'Engineers map an electrical grid by voltage levels to design transformers, then by load patterns to predict failures. Why are both maps necessary?',
                            'answers': [
                                {'text': 'They answer different explanatory challenges', 'correct': True, 'explanation': 'Correct! Each map addresses a different aspect of the system, providing essential information for design and reliability.'},
                                {'text': 'One is redundant', 'correct': False, 'explanation': 'Neither map is redundant; they provide different but equally important perspectives on the system.'},
                                {'text': 'Only structural maps matter', 'correct': False, 'explanation': 'Both structural and functional (load pattern) maps are important for a comprehensive understanding.'},
                                {'text': 'Load patterns are irrelevant', 'correct': False, 'explanation': 'Load patterns are highly relevant for predicting system behavior and potential failure points.'},
                            ],
                        },
                        {
                            'question': 'A software team maps their codebase by file structure, but this hides dependencies. Remapping by feature modules reveals tightly coupled components that cause bugs. What does this illustrate about system mapping?',
                            'answers': [
                                {'text': 'File structure is the only valid organization', 'correct': False, 'explanation': 'File structure is one way to organize code, but it does not always reveal functional dependencies.'},
                                {'text': 'The decomposition should match the problem being solved', 'correct': True, 'explanation': 'Correct! The mapping should be guided by the explanatory challenge and the relationships that need to be understood.'},
                                {'text': 'Dependencies are unimportant', 'correct': False, 'explanation': 'Dependencies are crucial for understanding how different parts of the system interact.'},
                                {'text': 'One map fits all purposes', 'correct': False, 'explanation': 'Different problems may require different mappings; there is no one-size-fits-all map.'},
                            ],
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
                                {'text': '#systemmapping and #complexcausality', 'correct': True, 'explanation': 'Correct! The initial reduction in emissions followed by an increase due to rerouting illustrates complex causality, and system mapping can reveal these dynamics.'},
                                {'text': '#networks and #systemdynamics', 'correct': False, 'explanation': 'These are not the primary concepts needed to understand the described outcome.'},
                                {'text': '#levelsofanalysis and #emergentproperties', 'correct': False, 'explanation': 'These concepts do not directly address the complexities of the congestion tax outcome.'},
                                {'text': '#systemmapping and #levelsofanalysis', 'correct': False, 'explanation': 'While relevant, this combination does not fully capture the complexity of the situation.'},
                            ],
                        },
                        {
                            'question': 'After a major company transitions to a flat organizational structure, innovation rates spike — but internal conflict also rises. Cross-functional teams now rely on dense Slack channels, creating "communication clusters" that unintentionally isolate departments. Some employees thrive through inter-cluster collaboration, while others disengage. Which HCs together help diagnose this system\'s new dynamics?',
                            'answers': [
                                {'text': '#emergentproperties and #networks', 'correct': True, 'explanation': 'Correct! The emergence of new communication patterns and their impact on innovation and conflict can be understood through these HCs.'},
                                {'text': '#complexcausality and #systemmapping', 'correct': False, 'explanation': 'These do not directly address the emergent communication dynamics and their effects.'},
                                {'text': '#systemdynamics and #levelsofanalysis', 'correct': False, 'explanation': 'This combination does not effectively capture the new dynamics at play in the organization.'},
                                {'text': '#networks and #complexcausality', 'correct': False, 'explanation': 'While relevant, this combination does not fully address the emergent properties of the new communication patterns.'},
                            ],
                        },
                        {
                            'question': 'Researchers studying global drought find that smallholder farmers in Sub-Saharan Africa experience water scarcity differently depending on local irrigation practices, national subsidies, and global grain markets. Their final model links individual behavior to policy incentives and planetary climate shifts. Which HC is most crucial for producing this comprehensive model?',
                            'answers': [
                                {'text': '#levelsofanalysis', 'correct': True, 'explanation': 'Correct! This HC is essential for integrating the multiple levels of influence on water scarcity into a comprehensive model.'},
                                {'text': '#systemmapping', 'correct': False, 'explanation': 'System mapping is a tool that may be used within the levels of analysis, but it is not the overarching HC needed here.'},
                                {'text': '#complexcausality', 'correct': False, 'explanation': 'Complex causality describes interactions but does not by itself ensure a comprehensive, multi-level model.'},
                                {'text': '#systemdynamics', 'correct': False, 'explanation': 'System dynamics focuses on changes over time, which is not the primary concern of the comprehensive model described.'},
                            ],
                        },
                        {
                            'question': 'A country\'s financial system stays stable for years despite rising debt. Then, following a rumor of bank insolvency, credit availability collapses overnight — triggering widespread recession even in unrelated industries. Analysts later show that public confidence was the "control variable" governing systemic stability. Which HC best characterizes this shift?',
                            'answers': [
                                {'text': '#systemdynamics', 'correct': True, 'explanation': 'Correct! The sudden shift in stability due to a change in public confidence illustrates a dynamic system response.'},
                                {'text': '#emergentproperties', 'correct': False, 'explanation': 'This is not primarily about emergent properties; it\'s about system dynamics and control variables.'},
                                {'text': '#networks', 'correct': False, 'explanation': 'Network structure is not the main factor in this particular systemic shift.'},
                                {'text': '#complexcausality', 'correct': False, 'explanation': 'Complex causality involves multiple causes and effects, but the key issue here is the control variable and system dynamics.'},
                            ],
                        },
                        {
                            'question': 'A rainforest restoration project reveals that simply replanting trees fails to restore biodiversity. Only when native pollinators return, soil microorganisms recover, and predator-prey cycles reestablish does the ecosystem stabilize. The project team maps out interdependent species interactions and identifies feedback loops driving resilience. Which combination of HCs best captures this system\'s recovery pattern?',
                            'answers': [
                                {'text': '#complexcausality, #networks, and #emergentproperties', 'correct': True, 'explanation': 'Correct! The recovery of the ecosystem involves complex causal interactions, networked relationships, and emergent properties of the restored ecosystem.'},
                                {'text': '#systemdynamics and #levelsofanalysis', 'correct': False, 'explanation': 'These do not fully capture the complexity and interdependencies involved in the ecosystem recovery.'},
                                {'text': '#systemmapping and #complexcausality', 'correct': False, 'explanation': 'While relevant, this combination does not adequately address the emergent and network aspects of the recovery.'},
                                {'text': '#networks and #systemdynamics', 'correct': False, 'explanation': 'This combination overlooks the complex causality and emergent properties critical to the ecosystem\'s recovery.'},
                            ],
                        },
                    ]
                },
            ]
        }
    ]
}