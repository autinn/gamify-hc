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
                                {'text': '"Large" vs "big"', 'correct': False, 'explanation': 'Both are neutral and similar in connotation.'},
                                {'text': '"Frugal" vs "cheap"', 'correct': True, 'explanation': '"Cheap" implies low quality; "frugal" implies prudence—classic connotative divergence.'},
                                {'text': '"Begin" vs "start"', 'correct': False, 'explanation': 'Both are neutral and similar in connotation.'},
                                {'text': '"Assist" vs "help"', 'correct': False, 'explanation': 'Both are neutral and similar in connotation.'},
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
                                {'text': 'Increase adjective use', 'correct': False, 'explanation': 'More adjectives don\'t necessarily improve professionalism.'},
                                {'text': 'Run a style/grammar pass and standardize visuals', 'correct': True, 'explanation': 'Proofing and formatting ensure reliability and credibility.'},
                                {'text': 'Replace all passive voice', 'correct': False, 'explanation': 'Passive voice isn\'t unprofessional; it depends on usage.'},
                                {'text': 'Add jokes for warmth', 'correct': False, 'explanation': 'Jokes can be unprofessional if not used carefully.'},
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
                                {'text': 'Assume a general public audience', 'correct': False, 'explanation': 'The specific address suggests a targeted audience, not the general public.'},
                                {'text': 'Identify intended audience and communal norms', 'correct': True, 'explanation': 'Intended audience is a core contextual factor shaping interpretation.'},
                                {'text': 'Focus only on sentence length', 'correct': False, 'explanation': 'Sentence length isn\'t the primary factor in analyzing appeals.'},
                                {'text': 'Ignore speaker identity', 'correct': False, 'explanation': 'The speaker\'s identity is crucial in understanding the speech\'s context and appeals.'},
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
                                {'text': 'Ethos only', 'correct': False, 'explanation': 'Ethos is one aspect; the main issue is jargon use.'},
                                {'text': 'Mismatch between rhetorical choices and audience needs', 'correct': True, 'explanation': 'Effective critique aligns medium, message, and audience comprehension.'},
                                {'text': 'MLA vs APA choice', 'correct': False, 'explanation': 'The citation style isn\'t relevant to the jargon issue.'},
                                {'text': 'Margins and line spacing', 'correct': False, 'explanation': 'Formatting details like margins aren\'t the focus of this critique.'},
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
                                {'text': 'Context only', 'correct': False, 'explanation': 'This demonstrates more than just context; it shows perspective-taking.'},
                                {'text': 'Conscious lens shifting and meta-awareness', 'correct': True, 'explanation': 'Explicitly toggling vantage points foregrounds lens effects on meaning.'},
                                {'text': 'Professionalism', 'correct': False, 'explanation': 'This is about interpretive flexibility, not professionalism.'},
                                {'text': 'Denotative cataloging', 'correct': False, 'explanation': 'This goes beyond mere denotation to interpretation.'},
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

