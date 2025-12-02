"""
MC50 Course Seed Data
Unit 1: Close Reading: How does language shape and represent reality?
"""

MC50_DATA = {
    'title': 'MC50',
    'description': 'MC50 Course',
    'units': [
        {
            'title': 'Close Reading: How does language shape and represent reality?',
            'description': 'MC50 Unit 1',
            'order_index': 0,
            'concepts': [
                {
                    'title': '#connotation',
                    'definition': 'Understand and use connotations, tone, and style.',
                    'questions': [
                        {
                            'question': 'A report calls a policy "regime change" instead of "administration transition." What analysis best explains the effect?',
                            'answers': [
                                {'text': 'Semantic equivalence', 'correct': False, 'explanation': 'Both phrases have similar literal meanings.'},
                                {'text': 'Neutral framing', 'correct': False, 'explanation': 'The terms are framed similarly in neutrality.'},
                                {'text': 'Negative connotative shift', 'correct': True, 'explanation': '"Regime" carries hostile/authoritarian connotations, shifting audience perception.'},
                                {'text': 'Genre confusion', 'correct': False, 'explanation': 'Both terms fit within a political genre.'},
                            ],
                        },
                        {
                            'question': 'A scientific abstract uses "breakthrough" and "revolutionary." What\'s the likely issue?',
                            'answers': [
                                {'text': 'Understatement', 'correct': False, 'explanation': 'The terms actually overstate the findings.'},
                                {'text': 'Incongruent tone for genre', 'correct': True, 'explanation': 'Hype-y tone clashes with scientific genre expectations; connotation misaligns with audience.'},
                                {'text': 'Ambiguous denotation only', 'correct': False, 'explanation': 'The words have clear, strong denotations.'},
                                {'text': 'Missing citations', 'correct': False, 'explanation': 'Citations are not relevant to the connotative issue.'},
                            ],
                        },
                        {
                            'question': 'Which pair most changes reader attitude despite similar denotation?',
                            'answers': [
                                {'text': '"Large" vs "big"', 'correct': False, 'explanation': 'These terms have minimal connotative difference.'},
                                {'text': '"Frugal" vs "cheap"', 'correct': True, 'explanation': '"Cheap" implies low quality; "frugal" implies prudence—classic connotative divergence.'},
                                {'text': '"Begin" vs "start"', 'correct': False, 'explanation': 'These terms are nearly interchangeable in tone.'},
                                {'text': '"Assist" vs "help"', 'correct': False, 'explanation': 'These terms have similar connotations.'},
                            ],
                        },
                        {
                            'question': 'A job posting describes candidates as "resilient" vs. "stubborn." Both denote persistence. What differs?',
                            'answers': [
                                {'text': 'Nothing—they are synonyms', 'correct': False, 'explanation': 'The terms differ in connotation, not denotation.'},
                                {'text': 'Connotation: "resilient" is positive; "stubborn" is negative', 'correct': True, 'explanation': 'Connotation shapes emotional valence independent of literal meaning.'},
                                {'text': 'Denotation completely changes', 'correct': False, 'explanation': 'The denotation remains the same; only the connotation changes.'},
                                {'text': 'Grammar rules', 'correct': False, 'explanation': 'Grammar is not relevant to this distinction.'},
                            ],
                        },
                        {
                            'question': 'An article replaces "elderly" with "senior citizens." What rhetorical effect occurs?',
                            'answers': [
                                {'text': 'Completely changes meaning', 'correct': False, 'explanation': 'The meaning remains similar; the tone changes.'},
                                {'text': 'Shifts to a more respectful, neutral connotation', 'correct': True, 'explanation': '"Elderly" can carry condescending overtones; "senior citizens" sounds more dignified.'},
                                {'text': 'Makes the text less formal', 'correct': False, 'explanation': 'The change does not affect formality significantly.'},
                                {'text': 'No effect whatsoever', 'correct': False, 'explanation': 'The change affects tone and connotation.'},
                            ],
                        },
                        {
                            'question': 'A restaurant menu lists "artisanal" bread vs. "handmade" bread. Same denotation. Why choose "artisanal"?',
                            'answers': [
                                {'text': 'It\'s shorter', 'correct': False, 'explanation': 'Length is not a factor in connotation.'},
                                {'text': 'It connotes premium quality and craftsmanship', 'correct': True, 'explanation': 'Connotative associations with "artisanal" suggest higher value and traditional methods.'},
                                {'text': 'It\'s more technical', 'correct': False, 'explanation': 'Technicality is not relevant to the connotative issue.'},
                                {'text': 'It removes all connotation', 'correct': False, 'explanation': 'The term "artisanal" has its own connotations.'},
                            ],
                        },
                        {
                            'question': 'A politician calls opponents\' proposal "radical" instead of "progressive." What does this reveal about connotation use?',
                            'answers': [
                                {'text': 'Both terms are equally neutral', 'correct': False, 'explanation': 'The terms have different connotative meanings.'},
                                {'text': 'Word choice strategically frames the proposal negatively vs. positively', 'correct': True, 'explanation': 'Strategic connotation shapes audience perception; "radical" implies danger, "progressive" implies improvement.'},
                                {'text': 'The denotation changes completely', 'correct': False, 'explanation': 'The denotation remains similar; the connotation changes.'},
                                {'text': 'Connotation doesn\'t matter in politics', 'correct': False, 'explanation': 'Connotation is crucial in political language.'},
                            ],
                        },
                        {
                            'question': 'A product review calls a device "simple" vs. "simplistic." Why does tone shift?',
                            'answers': [
                                {'text': 'They mean exactly the same thing', 'correct': False, 'explanation': 'The terms have different connotations.'},
                                {'text': '"Simple" is neutral/positive; "simplistic" implies oversimplification', 'correct': True, 'explanation': 'Connotative weight: "simple" = user-friendly; "simplistic" = inadequately thought-out.'},
                                {'text': '"Simplistic" is more formal', 'correct': False, 'explanation': 'Formality is not the issue; it\'s the connotation.'},
                                {'text': 'No tonal difference exists', 'correct': False, 'explanation': 'There is a significant tonal difference between the two.'},
                            ],
                        },
                        {
                            'question': 'A news headline uses "migrant" vs. "immigrant" vs. "refugee." Each carries different connotations. What should a writer consider?',
                            'answers': [
                                {'text': 'All three are interchangeable', 'correct': False, 'explanation': 'The terms have distinct legal and connotative meanings.'},
                                {'text': 'Each term\'s connotations affect audience empathy and perceived legitimacy', 'correct': True, 'explanation': 'Precise word choice acknowledges legal status and human circumstances; connotations shape public discourse.'},
                                {'text': 'Only denotation matters', 'correct': False, 'explanation': 'Denotation is not the only consideration; connotation is equally important.'},
                                {'text': 'Connotation is irrelevant in journalism', 'correct': False, 'explanation': 'Connotation is crucial in shaping the impact of journalistic language.'},
                            ],
                        },
                        {
                            'question': 'An email describes a plan as "ambitious" vs. "unrealistic." Both note scale, but what differs?',
                            'answers': [
                                {'text': 'Denotation—they describe different scales', 'correct': False, 'explanation': 'The denotation is similar; the connotation differs.'},
                                {'text': 'Connotation—"ambitious" inspires, "unrealistic" dismisses', 'correct': True, 'explanation': 'Connotation reveals the speaker\'s stance: support vs. skepticism.'},
                                {'text': 'Grammar and syntax', 'correct': False, 'explanation': 'Grammar and syntax are not the issues here.'},
                                {'text': 'Nothing at all', 'correct': False, 'explanation': 'There is a significant difference in connotation.'},
                            ],
                        },
                    ]
                },
                {
                    'title': '#professionalism',
                    'definition': 'Follow established guidelines to present yourself and your work products professionally.',
                    'questions': [
                        {
                            'question': 'A paper mixes APA in-text citations with Chicago footnotes. What\'s the fix prioritized by this HC?',
                            'answers': [
                                {'text': 'Rewrite argument', 'correct': False, 'explanation': 'The argument may be fine; it\'s the citation style that\'s mixed.'},
                                {'text': 'Choose and apply one citation style consistently', 'correct': True, 'explanation': 'Professional presentation demands consistent, field-appropriate conventions.'},
                                {'text': 'Add more quotations', 'correct': False, 'explanation': 'More quotations don\'t fix the citation style issue.'},
                                {'text': 'Remove references', 'correct': False, 'explanation': 'References are necessary; they just need proper formatting.'},
                            ],
                        },
                        {
                            'question': 'A cover letter includes emojis and slang. What violates professionalism?',
                            'answers': [
                                {'text': 'Word count', 'correct': False, 'explanation': 'Word count isn\'t directly related to professionalism here.'},
                                {'text': 'Informal register misaligned with audience', 'correct': True, 'explanation': 'Professional tone should match expectations of the hiring context.'},
                                {'text': 'Lack of headings', 'correct': False, 'explanation': 'Headings aren\'t always necessary; it depends on the context.'},
                                {'text': 'Present-tense verbs', 'correct': False, 'explanation': 'Present-tense verbs are acceptable in professional writing.'},
                            ],
                        },
                        {
                            'question': 'Before submitting a client report, the best professional action is to:',
                            'answers': [
                                {'text': 'Increase adjective use', 'correct': False, 'explanation': 'More adjectives won\'t necessarily improve the report.'},
                                {'text': 'Run a style/grammar pass and standardize visuals', 'correct': True, 'explanation': 'Proofing and formatting ensure reliability and credibility.'},
                                {'text': 'Replace all passive voice', 'correct': False, 'explanation': 'Passive voice is not the issue; clarity and engagement are.'},
                                {'text': 'Add jokes for warmth', 'correct': False, 'explanation': 'Humor is not appropriate in all professional contexts.'},
                            ],
                        },
                        {
                            'question': 'A resume uses three different fonts, inconsistent bullet styles, and varied margins. What professional standard is violated?',
                            'answers': [
                                {'text': 'Content quality', 'correct': False, 'explanation': 'The content may be fine; it\'s the presentation that\'s problematic.'},
                                {'text': 'Visual consistency and formatting standards', 'correct': True, 'explanation': 'Professional documents require uniform visual design to convey attention to detail.'},
                                {'text': 'Grammar rules', 'correct': False, 'explanation': 'Grammar is not the primary issue here.'},
                                {'text': 'Length requirements', 'correct': False, 'explanation': 'Length is not the concern; it\'s the formatting.'},
                            ],
                        },
                        {
                            'question': 'An academic paper due in MLA format uses APA style throughout. What should be corrected?',
                            'answers': [
                                {'text': 'The argument structure', 'correct': False, 'explanation': 'The argument structure is likely fine; it\'s the citation style that\'s mixed.'},
                                {'text': 'Convert all citations and formatting to MLA guidelines', 'correct': True, 'explanation': 'Following specified guidelines demonstrates professionalism and respect for conventions.'},
                                {'text': 'Add more sources', 'correct': False, 'explanation': 'More sources aren\'t needed; proper citation is.'},
                                {'text': 'Change the topic', 'correct': False, 'explanation': 'The topic is not the issue; it\'s the formatting and citations.'},
                            ],
                        },
                        {
                            'question': 'A business email addressing executives uses "Hey!" and closes with "Later!" What professional issue exists?',
                            'answers': [
                                {'text': 'Email is too short', 'correct': False, 'explanation': 'Length isn\'t the issue; it\'s the tone and formality.'},
                                {'text': 'Inappropriate level of formality for the audience and context', 'correct': True, 'explanation': 'Register and tone must match professional hierarchies and contexts.'},
                                {'text': 'Missing attachments', 'correct': False, 'explanation': 'Attachments aren\'t the problem here.'},
                                {'text': 'Too many paragraphs', 'correct': False, 'explanation': 'Paragraph count isn\'t the issue; it\'s the content and tone.'},
                            ],
                        },
                        {
                            'question': 'A grant proposal has typos, inconsistent section numbering, and missing page numbers. What does this signal?',
                            'answers': [
                                {'text': 'Creative freedom', 'correct': False, 'explanation': 'This suggests a lack of attention to detail.'},
                                {'text': 'Lack of attention to detail, reducing credibility', 'correct': True, 'explanation': 'Professional polish reflects competence; errors undermine trust in your work.'},
                                {'text': 'Strong content', 'correct': False, 'explanation': 'Content quality isn\'t the issue; it\'s the presentation.'},
                                {'text': 'Appropriate informality', 'correct': False, 'explanation': 'Informality isn\'t the problem; it\'s the lack of professionalism.'},
                            ],
                        },
                        {
                            'question': 'Which action best demonstrates professional self-presentation in a portfolio?',
                            'answers': [
                                {'text': 'Including unfinished drafts', 'correct': False, 'explanation': 'Unfinished drafts don\'t represent your best work.'},
                                {'text': 'Curating polished, relevant work with clear descriptions', 'correct': True, 'explanation': 'Professionalism means presenting your best, most relevant work with appropriate context.'},
                                {'text': 'Adding personal photos unrelated to work', 'correct': False, 'explanation': 'Personal photos are generally not appropriate in a professional portfolio.'},
                                {'text': 'Using casual language throughout', 'correct': False, 'explanation': 'Language should be professional and appropriate to the context.'},
                            ],
                        },
                        {
                            'question': 'A lab report uses first-person "I" throughout, contradicting field conventions for objective reporting. What should change?',
                            'answers': [
                                {'text': 'Nothing—personal voice is always best', 'correct': False, 'explanation': 'Personal voice is not appropriate in all contexts.'},
                                {'text': 'Shift to third-person or passive constructions per scientific writing norms', 'correct': True, 'explanation': 'Disciplinary conventions guide professional writing; scientific reports typically avoid first-person.'},
                                {'text': 'Add more personal anecdotes', 'correct': False, 'explanation': 'Anecdotes are not suitable in objective reporting.'},
                                {'text': 'Remove all verbs', 'correct': False, 'explanation': 'Verbs are necessary for clear, active writing.'},
                            ],
                        },
                        {
                            'question': 'You submit a presentation with garish color schemes, unreadable fonts, and cluttered slides. What professional principle is violated?',
                            'answers': [
                                {'text': 'Creativity is discouraged', 'correct': False, 'explanation': 'Creativity is not the issue; clarity and professionalism are.'},
                                {'text': 'Visual clarity and audience accessibility', 'correct': True, 'explanation': 'Professional design prioritizes audience comprehension over decorative excess.'},
                                {'text': 'Content must be controversial', 'correct': False, 'explanation': 'Content controversy is not a requirement for professionalism.'},
                                {'text': 'Presentations should be text-only', 'correct': False, 'explanation': 'Visuals can enhance a presentation if used effectively.'},
                            ],
                        },
                    ]
                },
                {
                    'title': '#context',
                    'definition': 'Situate a work in its relevant context (e.g., historical, disciplinary, cultural).',
                    'questions': [
                        {
                            'question': 'A 1930s pamphlet references "breadlines." Understanding the persuasive force requires:',
                            'answers': [
                                {'text': 'Author\'s favorite foods', 'correct': False, 'explanation': 'The author\'s preferences aren\'t relevant to the context of "breadlines."'},
                                {'text': 'Great Depression socio-economic context', 'correct': True, 'explanation': 'Historical conditions frame the text\'s stakes and meanings.'},
                                {'text': 'Printer\'s typeface choice', 'correct': False, 'explanation': 'Typeface doesn\'t significantly affect the contextual understanding of the content.'},
                                {'text': 'The author\'s Instagram', 'correct': False, 'explanation': 'Instagram didn\'t exist in the 1930s; this is irrelevant.'},
                            ],
                        },
                        {
                            'question': 'A piece labeled "satire" uses exaggerated claims. Proper interpretation depends on:',
                            'answers': [
                                {'text': 'Ignoring intent', 'correct': False, 'explanation': 'Ignoring the author\'s intent would lead to misinterpretation.'},
                                {'text': 'Recognizing satirical genre conventions', 'correct': True, 'explanation': 'Genre context guides how we parse exaggeration and irony.'},
                                {'text': 'Translating to another language', 'correct': False, 'explanation': 'Translation isn\'t the key issue; it\'s understanding the genre.'},
                                {'text': 'Counting adjectives', 'correct': False, 'explanation': 'The number of adjectives isn\'t relevant to identifying satire.'},
                            ],
                        },
                        {
                            'question': 'A speech opens, "Fellow veterans…" To analyze appeals, you should first:',
                            'answers': [
                                {'text': 'Assume a general public audience', 'correct': False, 'explanation': 'The audience is likely more specific than "general public."'},
                                {'text': 'Identify intended audience and communal norms', 'correct': True, 'explanation': 'Intended audience is a core contextual factor shaping interpretation.'},
                                {'text': 'Focus only on sentence length', 'correct': False, 'explanation': 'Sentence length is not the primary concern in analyzing appeals.'},
                                {'text': 'Ignore speaker identity', 'correct': False, 'explanation': 'Speaker identity can significantly impact the speech\'s reception.'},
                            ],
                        },
                        {
                            'question': 'A 1920s essay uses "race" terminology now considered outdated. What helps explain this?',
                            'answers': [
                                {'text': 'Author was careless', 'correct': False, 'explanation': 'Carelessness doesn\'t account for historical context.'},
                                {'text': 'Historical linguistic norms differed; vocabulary evolved', 'correct': True, 'explanation': 'Historical context clarifies why past texts used language their era accepted.'},
                                {'text': 'Typo in the text', 'correct': False, 'explanation': 'A typo doesn\'t explain the use of outdated terminology.'},
                                {'text': 'Modern readers misunderstand', 'correct': False, 'explanation': 'The terminology was appropriate for the time it was written.'},
                            ],
                        },
                        {
                            'question': 'An economist writes "perfectly competitive market" assuming rational actors. What disciplinary context matters?',
                            'answers': [
                                {'text': 'Economics sometimes uses idealized models to test theory', 'correct': True, 'explanation': 'Disciplinary frameworks shape how fields construct arguments and models.'},
                                {'text': 'Author is unaware of reality', 'correct': False, 'explanation': 'Unawareness doesn\'t explain the use of idealized models.'},
                                {'text': 'All markets are perfectly competitive', 'correct': False, 'explanation': 'This is a theoretical assumption, not a statement of fact.'},
                                {'text': 'No context needed', 'correct': False, 'explanation': 'Context is always necessary to understand the application of theory.'},
                            ],
                        },
                        {
                            'question': 'A physics paper uses jargon like "Hamiltonian" without definition. What contextual assumption is made?',
                            'answers': [
                                {'text': 'The author is being deliberately obscure', 'correct': False, 'explanation': 'Obscurity is not the intent; precision and brevity for the audience are.'},
                                {'text': 'The target audience has disciplinary training in physics', 'correct': True, 'explanation': 'Disciplinary context shapes vocabulary; experts write for expert peers.'},
                                {'text': 'Jargon should never be used', 'correct': False, 'explanation': 'Jargon is appropriate when used with an audience that understands it.'},
                                {'text': 'The term is self-explanatory', 'correct': False, 'explanation': 'Self-explanatory terms are rare in specialized fields.'},
                            ],
                        },
                        {
                            'question': 'A novel set during WWII includes rationing and blackout curtains. What context enriches interpretation?',
                            'answers': [
                                {'text': 'Author\'s personal color preferences', 'correct': False, 'explanation': 'The author\'s preferences are not relevant to the historical context.'},
                                {'text': 'Historical wartime conditions that shaped daily life', 'correct': True, 'explanation': 'Historical context reveals how real conditions inform setting and characterization.'},
                                {'text': 'Modern energy-saving tips', 'correct': False, 'explanation': 'Modern tips are irrelevant to the historical context of the novel.'},
                                {'text': 'Random plot devices', 'correct': False, 'explanation': 'Plot devices are rarely random; they usually serve a narrative purpose.'},
                            ],
                        },
                        {
                            'question': 'A manifesto written by a marginalized activist uses confrontational tone. What biographical/cultural context matters?',
                            'answers': [
                                {'text': 'Author is inherently aggressive', 'correct': False, 'explanation': 'Aggressiveness is not an inherent trait; it\'s a response to context.'},
                                {'text': 'Lived experience of oppression shapes rhetorical urgency', 'correct': True, 'explanation': 'Biographical and cultural contexts explain why authors choose certain rhetorical strategies.'},
                                {'text': 'Tone is irrelevant', 'correct': False, 'explanation': 'Tone is a crucial part of how messages are received and interpreted.'},
                                {'text': 'All manifestos are calm', 'correct': False, 'explanation': 'Manifestos often have a confrontational or urgent tone by nature.'},
                            ],
                        },
                        {
                            'question': 'A scientific paper from 1850 lacks modern statistical methods. What context explains this?',
                            'answers': [
                                {'text': 'Author was incompetent', 'correct': False, 'explanation': 'Incompetence doesn\'t explain the absence of modern methods.'},
                                {'text': 'Statistical tools developed later; historical context of methodology', 'correct': True, 'explanation': 'Historical disciplinary context shows how methods evolve over time.'},
                                {'text': 'Statistics are never needed', 'correct': False, 'explanation': 'Statistics are essential, but the methods and availability have evolved.'},
                                {'text': 'Modern methods are always wrong', 'correct': False, 'explanation': 'Modern methods are not inherently wrong; they are just different.'},
                            ],
                        },
                        {
                            'question': 'A religious text uses metaphors unfamiliar to modern readers. What context helps?',
                            'answers': [
                                {'text': 'Author wrote poorly', 'correct': False, 'explanation': 'Poor writing doesn\'t account for the use of metaphor.'},
                                {'text': 'Historical, cultural, and religious traditions shape symbolic language', 'correct': True, 'explanation': 'Cultural and historical context unlocks symbolic meanings rooted in tradition.'},
                                {'text': 'Metaphors are universal', 'correct': False, 'explanation': 'Metaphors are often culture-specific and require contextual understanding.'},
                                {'text': 'Modern readers are always correct', 'correct': False, 'explanation': 'Modern interpretations are not always accurate to the original context.'},
                            ],
                        },
                    ]
                },
                {
                    'title': '#critique',
                    'definition': 'Actively and critically engage with texts and other forms of communication.',
                    'questions': [
                        {
                            'question': 'An op-ed cites a single anecdote to generalize a national trend. The critique should first note:',
                            'answers': [
                                {'text': 'Strong external validity', 'correct': False, 'explanation': 'External validity is weak with only one anecdote.'},
                                {'text': 'Sampling/representativeness weakness', 'correct': True, 'explanation': 'One case is insufficient evidence for broad claims.'},
                                {'text': 'Perfect causal identification', 'correct': False, 'explanation': 'Causality can\'t be determined from a single anecdote.'},
                                {'text': 'Tone neutrality', 'correct': False, 'explanation': 'Tone is not neutral in this case; it\'s likely biased.'},
                            ],
                        },
                        {
                            'question': 'A paper\'s discussion repeats the introduction but adds no analysis. Which critique applies?',
                            'answers': [
                                {'text': 'Coherence improved', 'correct': False, 'explanation': 'Repetition without analysis doesn\'t improve coherence.'},
                                {'text': 'Redundancy; weak progression of claims', 'correct': True, 'explanation': 'Good structure advances claims; repetition signals weak argumentative development.'},
                                {'text': 'Excessive operationalization', 'correct': False, 'explanation': 'Operationalization isn\'t the issue; it\'s the lack of analysis.'},
                                {'text': 'Over-citation', 'correct': False, 'explanation': 'Citation amount isn\'t the problem in this context.'},
                            ],
                        },
                        {
                            'question': 'A public health brief uses dense jargon for lay readers. What should critique emphasize?',
                            'answers': [
                                {'text': 'Ethos only', 'correct': False, 'explanation': 'Ethos is not the only concern; clarity is crucial.'},
                                {'text': 'Mismatch between rhetorical choices and audience needs', 'correct': True, 'explanation': 'Effective critique aligns medium, message, and audience comprehension.'},
                                {'text': 'MLA vs APA choice', 'correct': False, 'explanation': 'The citation style is not the primary issue.'},
                                {'text': 'Margins and line spacing', 'correct': False, 'explanation': 'Formatting details are less important than content clarity.'},
                            ],
                        },
                        {
                            'question': 'A study claims causation but only shows correlation. What critical question arises?',
                            'answers': [
                                {'text': 'Is the font size appropriate?', 'correct': False, 'explanation': 'Font size is irrelevant to the study\'s validity.'},
                                {'text': 'Does the evidence support the causal claim, or are confounds present?', 'correct': True, 'explanation': 'Critical readers distinguish correlation from causation and identify logical gaps.'},
                                {'text': 'Is the author famous?', 'correct': False, 'explanation': 'Author fame does not determine the quality of evidence.'},
                                {'text': 'Was the study published recently?', 'correct': False, 'explanation': 'Recency does not guarantee validity; the methodology does.'},
                            ],
                        },
                        {
                            'question': 'A politician\'s speech uses emotional appeals but provides no data. What critique is warranted?',
                            'answers': [
                                {'text': 'Emotional appeals are always effective', 'correct': False, 'explanation': 'Emotional appeals need to be supported by data to be credible.'},
                                {'text': 'Heavy reliance on pathos without logos weakens substantive argument', 'correct': True, 'explanation': 'Balanced critique assesses whether rhetorical strategies are backed by evidence.'},
                                {'text': 'All rhetoric is equally valid', 'correct': False, 'explanation': 'Not all rhetoric is equally valid; it depends on the evidence and logic.'},
                                {'text': 'Data is irrelevant in speeches', 'correct': False, 'explanation': 'Data can be crucial in supporting the claims made in speeches.'},
                            ],
                        },
                        {
                            'question': 'An advertisement claims "9 out of 10 doctors recommend" without source. What should critics question?',
                            'answers': [
                                {'text': 'The claim is automatically credible', 'correct': False, 'explanation': 'No claim is credible without evidence.'},
                                {'text': 'Source transparency, sample size, and potential bias', 'correct': True, 'explanation': 'Critical engagement demands verification of statistical claims and sources.'},
                                {'text': 'Nothing—statistics are always accurate', 'correct': False, 'explanation': 'Statistics can be misleading; sources and methods matter.'},
                                {'text': 'The product color', 'correct': False, 'explanation': 'The color of the product is irrelevant to the claim\'s validity.'},
                            ],
                        },
                        {
                            'question': 'A research paper cherry-picks data supporting its hypothesis while ignoring contradictory findings. What\'s the critique?',
                            'answers': [
                                {'text': 'The paper has strong confirmation bias', 'correct': True, 'explanation': 'Critical reading identifies selective use of evidence and methodological flaws.'},
                                {'text': 'This is standard scientific practice', 'correct': False, 'explanation': 'Standard practice involves comprehensive and unbiased reporting of methods and findings.'},
                                {'text': 'The writing style is excellent', 'correct': False, 'explanation': 'Writing style is not the issue; the integrity of the research is.'},
                                {'text': 'References are well-formatted', 'correct': False, 'explanation': 'Reference formatting does not compensate for biased reporting.'},
                            ],
                        },
                        {
                            'question': 'A blog post makes sweeping generalizations without evidence. Which critical approach applies?',
                            'answers': [
                                {'text': 'Accept claims at face value', 'correct': False, 'explanation': 'Claims should never be accepted without evidence.'},
                                {'text': 'Question the basis for generalizations and demand supporting evidence', 'correct': True, 'explanation': 'Critical engagement requires assessing whether claims are substantiated.'},
                                {'text': 'Praise the author\'s confidence', 'correct': False, 'explanation': 'Confidence is irrelevant; evidence is what matters.'},
                                {'text': 'Ignore the lack of evidence', 'correct': False, 'explanation': 'Ignoring evidence undermines critical engagement.'},
                            ],
                        },
                        {
                            'question': 'A news article quotes only sources supporting one political perspective. What critique is appropriate?',
                            'answers': [
                                {'text': 'The article shows perfect balance', 'correct': False, 'explanation': 'Balance is not achieved by representing only one perspective.'},
                                {'text': 'Lack of diverse perspectives suggests potential bias', 'correct': True, 'explanation': 'Critical readers evaluate whether multiple perspectives are represented fairly.'},
                                {'text': 'All journalism is inherently neutral', 'correct': False, 'explanation': 'Journalism can be biased depending on how information is presented.'},
                                {'text': 'Headlines don\'t matter', 'correct': False, 'explanation': 'Headlines are crucial in shaping reader perception and should be scrutinized.'},
                            ],
                        },
                        {
                            'question': 'An academic argument relies on outdated theories discredited by recent research. What should critics note?',
                            'answers': [
                                {'text': 'Age of sources is irrelevant', 'correct': False, 'explanation': 'The age of sources can be very relevant, especially in fast-evolving fields.'},
                                {'text': 'The argument fails to engage current scholarship and evidence', 'correct': True, 'explanation': 'Critical analysis assesses whether arguments account for updated knowledge.'},
                                {'text': 'Older theories are always superior', 'correct': False, 'explanation': 'The superiority of a theory is not determined by its age but by its empirical support.'},
                                {'text': 'Recent research doesn\'t matter', 'correct': False, 'explanation': 'Recent research is crucial in evaluating the current validity of a theory.'},
                            ],
                        },
                    ]
                },
                {
                    'title': '#interpretivelens',
                    'definition': 'Be mindful of how prior experiences, expectations, and judgments affect inferences drawn from different forms of communication and react accordingly.',
                    'questions': [
                        {
                            'question': 'After a stressful exam, you read a neutral text as hostile. Best reflection?',
                            'answers': [
                                {'text': 'Text is objectively hostile', 'correct': False, 'explanation': 'The text\'s hostility isn\'t objective; it\'s perceived.'},
                                {'text': 'Your current affect skewed interpretation', 'correct': True, 'explanation': 'Prior state shapes perceived tone—recognize and adjust for lens effects.'},
                                {'text': 'The author intended irony', 'correct': False, 'explanation': 'Irony isn\'t the only explanation for a hostile reading.'},
                                {'text': 'The font caused misreading', 'correct': False, 'explanation': 'The font is unlikely to cause a misreading of this nature.'},
                            ],
                        },
                        {
                            'question': 'Before reviewing a memoir on migration, you interview migrants with varied backgrounds. This practice:',
                            'answers': [
                                {'text': 'Eliminates bias entirely', 'correct': False, 'explanation': 'Bias can\'t be entirely eliminated, only acknowledged and mitigated.'},
                                {'text': 'Broadens your interpretive lens via direct perspectives', 'correct': True, 'explanation': 'Perspective-getting widens interpretive bandwidth while acknowledging subjectivity.'},
                                {'text': 'Replaces close reading', 'correct': False, 'explanation': 'This practice complements rather than replaces close reading.'},
                                {'text': 'Determines the "one true" meaning', 'correct': False, 'explanation': 'Meaning isn\'t singular or fixed; it\'s interpreted.'},
                            ],
                        },
                        {
                            'question': 'You produce two analyses of a protest photo: one as a local, one as an outsider. This demonstrates:',
                            'answers': [
                                {'text': 'Context only', 'correct': False, 'explanation': 'Both context and perspective are at play.'},
                                {'text': 'Conscious lens shifting and meta-awareness', 'correct': True, 'explanation': 'Explicitly toggling vantage points foregrounds lens effects on meaning.'},
                                {'text': 'Professionalism', 'correct': False, 'explanation': 'This is more about interpretive flexibility than professionalism.'},
                                {'text': 'Denotative cataloging', 'correct': False, 'explanation': 'This goes beyond mere denotation; it involves interpretation.'},
                            ],
                        },
                        {
                            'question': 'You notice you interpret economic data differently when presented by sources you trust vs distrust. What does this reveal?',
                            'answers': [
                                {'text': 'All data is inherently biased', 'correct': False, 'explanation': 'Data itself is not biased; interpretations of data can be.'},
                                {'text': 'Your prior beliefs and source credibility shape interpretation', 'correct': True, 'explanation': 'Recognizing how trust and expectations filter evidence demonstrates interpretive self-awareness.'},
                                {'text': 'Numbers never lie', 'correct': False, 'explanation': 'Numbers can be misinterpreted or misrepresented.'},
                                {'text': 'Statistics are always objective', 'correct': False, 'explanation': 'Statistics can be presented subjectively, depending on the context.'},
                            ],
                        },
                        {
                            'question': 'Reading a novel set in a culture unfamiliar to you, you initially misinterpret social norms. How should you respond?',
                            'answers': [
                                {'text': 'Assume your first interpretation is correct', 'correct': False, 'explanation': 'First interpretations are often influenced by personal bias.'},
                                {'text': 'Seek cultural context and revise understanding accordingly', 'correct': True, 'explanation': 'Lens awareness means recognizing your interpretive limits and seeking context.'},
                                {'text': 'Blame the author for poor writing', 'correct': False, 'explanation': 'Blaming the author doesn\'t account for the reader\'s interpretive role.'},
                                {'text': 'Ignore unfamiliar elements', 'correct': False, 'explanation': 'Ignoring elements can lead to a superficial understanding of the text.'},
                            ],
                        },
                        {
                            'question': 'Two readers from different political backgrounds reach opposite conclusions about the same policy brief. What explains this?',
                            'answers': [
                                {'text': 'One reader is wrong, the other right', 'correct': False, 'explanation': 'Both can be valid; it depends on the interpretive lens.'},
                                {'text': 'Interpretive lenses shaped by prior beliefs influence meaning-making', 'correct': True, 'explanation': 'Different lenses can yield different but valid interpretations based on perspective.'},
                                {'text': 'The brief was poorly written', 'correct': False, 'explanation': 'The writing quality doesn\'t solely determine interpretive outcomes.'},
                                {'text': 'Political backgrounds are irrelevant', 'correct': False, 'explanation': 'Political backgrounds can significantly influence interpretation.'},
                            ],
                        },
                        {
                            'question': 'You realize you\'re reading a scientific study more skeptically because it contradicts your existing views. What should you do?',
                            'answers': [
                                {'text': 'Dismiss the study immediately', 'correct': False, 'explanation': 'Dismissal doesn\'t engage with the study\'s actual content or methodology.'},
                                {'text': 'Acknowledge confirmation bias and evaluate evidence more objectively', 'correct': True, 'explanation': 'Interpretive lens awareness involves recognizing and correcting for cognitive biases.'},
                                {'text': 'Trust your instincts without question', 'correct': False, 'explanation': 'Instincts can be biased; evidence should guide conclusions.'},
                                {'text': 'Only read studies supporting your views', 'correct': False, 'explanation': 'Exposing oneself only to supportive evidence reinforces bias.'},
                            ],
                        },
                        {
                            'question': 'A student from an urban background interprets a rural poem differently than a rural student. This illustrates:',
                            'answers': [
                                {'text': 'One interpretation is objectively correct', 'correct': False, 'explanation': 'Interpretations are subjective and context-dependent.'},
                                {'text': 'Lived experience shapes interpretive frameworks and meanings', 'correct': True, 'explanation': 'Personal experience forms an interpretive lens that colors understanding.'},
                                {'text': 'The poem failed to communicate', 'correct': False, 'explanation': 'The poem communicates differently depending on the reader\'s lens.'},
                                {'text': 'Location has no impact on reading', 'correct': False, 'explanation': 'Location can significantly impact one\'s interpretive lens.'},
                            ],
                        },
                        {
                            'question': 'You find yourself assuming a business memo is aggressive because similar past memos preceded layoffs. What\'s happening?',
                            'answers': [
                                {'text': 'The memo is objectively aggressive', 'correct': False, 'explanation': 'Objectivity isn\'t applicable here; it\'s about perception.'},
                                {'text': 'Past experience creates an interpretive lens that colors current reading', 'correct': True, 'explanation': 'Prior experiences shape expectations and interpretations of new texts.'},
                                {'text': 'All business memos are aggressive', 'correct': False, 'explanation': 'Memos vary in tone; it\'s not a universal trait.'},
                                {'text': 'Your reading skills are inadequate', 'correct': False, 'explanation': 'Reading skills aren\'t the issue; it\'s the interpretive lens.'},
                            ],
                        },
                        {
                            'question': 'To reduce interpretive bias when analyzing a controversial speech, you should:',
                            'answers': [
                                {'text': 'Only read sources you agree with', 'correct': False, 'explanation': 'This would reinforce bias rather than reduce it.'},
                                {'text': 'Consider multiple perspectives and question your own assumptions', 'correct': True, 'explanation': 'Lens awareness involves actively seeking diverse viewpoints and self-reflection.'},
                                {'text': 'Trust your first impression completely', 'correct': False, 'explanation': 'First impressions can be misleading and biased.'},
                                {'text': 'Ignore context and background', 'correct': False, 'explanation': 'Context and background are crucial for accurate interpretation.'},
                            ],
                        },
                    ]
                },
                {
                    'title': 'Unit-Level Challenge',
                    'definition': 'Integrative Scenarios — Harder',
                    'questions': [
                        {
                            'question': 'A headline switches "protesters clash with police" to "rioters attack police," changing reactions despite identical facts.',
                            'answers': [
                                {'text': '#connotation + #critique', 'correct': True, 'explanation': 'Word choice alters affect while critique evaluates how that change shifts the claim\'s force.'},
                                {'text': '#context', 'correct': False, 'explanation': 'Context isn\'t the primary issue; it\'s the connotation and critique.'},
                                {'text': '#professionalism', 'correct': False, 'explanation': 'Professionalism isn\'t directly relevant to this analysis.'},
                                {'text': '#interpretivelens', 'correct': False, 'explanation': 'Interpretive lens isn\'t the main focus; it\'s the connotation and critique.'},
                            ],
                        },
                        {
                            'question': 'You standardize citations, figure captions, and section headers to match the journal\'s guide.',
                            'answers': [
                                {'text': '#professionalism', 'correct': True, 'explanation': 'Aligning with explicit venue norms is the core of professional presentation.'},
                                {'text': '#critique', 'correct': False, 'explanation': 'Critique isn\'t the primary concern here; it\'s professionalism.'},
                                {'text': '#connotation', 'correct': False, 'explanation': 'Connotation isn\'t directly relevant to citation formatting.'},
                                {'text': '#context', 'correct': False, 'explanation': 'Context isn\'t the main issue; it\'s about following guidelines.'},
                            ],
                        },
                        {
                            'question': 'Two curators disagree on a sculpture\'s satire; one cites the artist\'s letters, the other their own cultural references.',
                            'answers': [
                                {'text': '#context + #interpretivelens', 'correct': True, 'explanation': 'Historical evidence reframes meaning while personal standpoint explains divergent readings.'},
                                {'text': '#connotation', 'correct': False, 'explanation': 'Connotation isn\'t the main issue; it\'s about context and interpretation.'},
                                {'text': '#critique', 'correct': False, 'explanation': 'Critique isn\'t directly relevant to this interpretive disagreement.'},
                                {'text': '#professionalism', 'correct': False, 'explanation': 'Professionalism isn\'t the focus; it\'s about understanding context and perspective.'},
                            ],
                        },
                        {
                            'question': 'You remove charged phrasing and add a representative study to back the claim.',
                            'answers': [
                                {'text': '#connotation + #critique', 'correct': True, 'explanation': 'Calibrating tone and evaluating evidence jointly improve argumentative quality.'},
                                {'text': '#context', 'correct': False, 'explanation': 'Context isn\'t the primary issue; it\'s about connotation and critique.'},
                                {'text': '#professionalism', 'correct': False, 'explanation': 'Professionalism isn\'t the main concern here.'},
                                {'text': '#interpretivelens', 'correct': False, 'explanation': 'Interpretive lens isn\'t the focus; it\'s about improving the argument.'},
                            ],
                        },
                        {
                            'question': 'A course policy sounds punitive; you rephrase to keep expectations firm but supportive.',
                            'answers': [
                                {'text': '#connotation', 'correct': True, 'explanation': 'Tone adjustments change how the same rule is received without altering content.'},
                                {'text': '#context', 'correct': False, 'explanation': 'Context isn\'t the main issue; it\'s about the connotation of the language used.'},
                                {'text': '#professionalism', 'correct': False, 'explanation': 'Professionalism isn\'t directly relevant to this language adjustment.'},
                                {'text': '#critique', 'correct': False, 'explanation': 'Critique isn\'t the primary focus; it\'s about adjusting tone.'},
                            ],
                        },
                    ]
                },
            ]
        }
    ]
}
                            'answers': [
                                {'text': '#professionalism', 'correct': True, 'explanation': 'Aligning with explicit venue norms is the core of professional presentation.'},
                                {'text': '#critique', 'correct': False, 'explanation': 'Critique isn\'t the primary concern here; it\'s professionalism.'},
                                {'text': '#connotation', 'correct': False, 'explanation': 'Connotation isn\'t directly relevant to citation formatting.'},
                                {'text': '#context', 'correct': False, 'explanation': 'Context isn\'t the main issue; it\'s about following guidelines.'},
                            ],
                        },
                        {
                            'question': 'Two curators disagree on a sculpture\'s satire; one cites the artist\'s letters, the other their own cultural references.',
                            'answers': [
                                {'text': '#context + #interpretivelens', 'correct': True, 'explanation': 'Historical evidence reframes meaning while personal standpoint explains divergent readings.'},
                                {'text': '#connotation', 'correct': False, 'explanation': 'Connotation isn\'t the main issue; it\'s about context and interpretation.'},
                                {'text': '#critique', 'correct': False, 'explanation': 'Critique isn\'t directly relevant to this interpretive disagreement.'},
                                {'text': '#professionalism', 'correct': False, 'explanation': 'Professionalism isn\'t the focus; it\'s about understanding context and perspective.'},
                            ],
                        },
                        {
                            'question': 'You remove charged phrasing and add a representative study to back the claim.',
                            'answers': [
                                {'text': '#connotation + #critique', 'correct': True, 'explanation': 'Calibrating tone and evaluating evidence jointly improve argumentative quality.'},
                                {'text': '#context', 'correct': False, 'explanation': 'Context isn\'t the primary issue; it\'s about connotation and critique.'},
                                {'text': '#professionalism', 'correct': False, 'explanation': 'Professionalism isn\'t the main concern here.'},
                                {'text': '#interpretivelens', 'correct': False, 'explanation': 'Interpretive lens isn\'t the focus; it\'s about improving the argument.'},
                            ],
                        },
                        {
                            'question': 'A course policy sounds punitive; you rephrase to keep expectations firm but supportive.',
                            'answers': [
                                {'text': '#connotation', 'correct': True, 'explanation': 'Tone adjustments change how the same rule is received without altering content.'},
                                {'text': '#context', 'correct': False, 'explanation': 'Context isn\'t the main issue; it\'s about the connotation of the language used.'},
                                {'text': '#professionalism', 'correct': False, 'explanation': 'Professionalism isn\'t directly relevant to this language adjustment.'},
                                {'text': '#critique', 'correct': False, 'explanation': 'Critique isn\'t the primary focus; it\'s about adjusting tone.'},
                            ],
                        },
                    ]
                },
            ]
        }
    ]
}

