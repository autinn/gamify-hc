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
                                {'text': 'Semantic equivalence', 'correct': False},
                                {'text': 'Neutral framing', 'correct': False},
                                {'text': 'Negative connotative shift', 'correct': True},
                                {'text': 'Genre confusion', 'correct': False},
                            ],
                            'explanation': '"Regime" carries hostile/authoritarian connotations, shifting audience perception.'
                        },
                        {
                            'question': 'A scientific abstract uses "breakthrough" and "revolutionary." What\'s the likely issue?',
                            'answers': [
                                {'text': 'Understatement', 'correct': False},
                                {'text': 'Incongruent tone for genre', 'correct': True},
                                {'text': 'Ambiguous denotation only', 'correct': False},
                                {'text': 'Missing citations', 'correct': False},
                            ],
                            'explanation': 'Hype-y tone clashes with scientific genre expectations; connotation misaligns with audience.'
                        },
                        {
                            'question': 'Which pair most changes reader attitude despite similar denotation?',
                            'answers': [
                                {'text': '"Large" vs "big"', 'correct': False},
                                {'text': '"Frugal" vs "cheap"', 'correct': True},
                                {'text': '"Begin" vs "start"', 'correct': False},
                                {'text': '"Assist" vs "help"', 'correct': False},
                            ],
                            'explanation': '"Cheap" implies low quality; "frugal" implies prudence—classic connotative divergence.'
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
                                {'text': 'Rewrite argument', 'correct': False},
                                {'text': 'Choose and apply one citation style consistently', 'correct': True},
                                {'text': 'Add more quotations', 'correct': False},
                                {'text': 'Remove references', 'correct': False},
                            ],
                            'explanation': 'Professional presentation demands consistent, field-appropriate conventions.'
                        },
                        {
                            'question': 'A cover letter includes emojis and slang. What violates professionalism?',
                            'answers': [
                                {'text': 'Word count', 'correct': False},
                                {'text': 'Informal register misaligned with audience', 'correct': True},
                                {'text': 'Lack of headings', 'correct': False},
                                {'text': 'Present-tense verbs', 'correct': False},
                            ],
                            'explanation': 'Professional tone should match expectations of the hiring context.'
                        },
                        {
                            'question': 'Before submitting a client report, the best professional action is to:',
                            'answers': [
                                {'text': 'Increase adjective use', 'correct': False},
                                {'text': 'Run a style/grammar pass and standardize visuals', 'correct': True},
                                {'text': 'Replace all passive voice', 'correct': False},
                                {'text': 'Add jokes for warmth', 'correct': False},
                            ],
                            'explanation': 'Proofing and formatting ensure reliability and credibility.'
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
                                {'text': 'Author\'s favorite foods', 'correct': False},
                                {'text': 'Great Depression socio-economic context', 'correct': True},
                                {'text': 'Printer\'s typeface choice', 'correct': False},
                                {'text': 'The author\'s Instagram', 'correct': False},
                            ],
                            'explanation': 'Historical conditions frame the text\'s stakes and meanings.'
                        },
                        {
                            'question': 'A piece labeled "satire" uses exaggerated claims. Proper interpretation depends on:',
                            'answers': [
                                {'text': 'Ignoring intent', 'correct': False},
                                {'text': 'Recognizing satirical genre conventions', 'correct': True},
                                {'text': 'Translating to another language', 'correct': False},
                                {'text': 'Counting adjectives', 'correct': False},
                            ],
                            'explanation': 'Genre context guides how we parse exaggeration and irony.'
                        },
                        {
                            'question': 'A speech opens, "Fellow veterans…" To analyze appeals, you should first:',
                            'answers': [
                                {'text': 'Assume a general public audience', 'correct': False},
                                {'text': 'Identify intended audience and communal norms', 'correct': True},
                                {'text': 'Focus only on sentence length', 'correct': False},
                                {'text': 'Ignore speaker identity', 'correct': False},
                            ],
                            'explanation': 'Intended audience is a core contextual factor shaping interpretation.'
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
                                {'text': 'Strong external validity', 'correct': False},
                                {'text': 'Sampling/representativeness weakness', 'correct': True},
                                {'text': 'Perfect causal identification', 'correct': False},
                                {'text': 'Tone neutrality', 'correct': False},
                            ],
                            'explanation': 'One case is insufficient evidence for broad claims.'
                        },
                        {
                            'question': 'A paper\'s discussion repeats the introduction but adds no analysis. Which critique applies?',
                            'answers': [
                                {'text': 'Coherence improved', 'correct': False},
                                {'text': 'Redundancy; weak progression of claims', 'correct': True},
                                {'text': 'Excessive operationalization', 'correct': False},
                                {'text': 'Over-citation', 'correct': False},
                            ],
                            'explanation': 'Good structure advances claims; repetition signals weak argumentative development.'
                        },
                        {
                            'question': 'A public health brief uses dense jargon for lay readers. What should critique emphasize?',
                            'answers': [
                                {'text': 'Ethos only', 'correct': False},
                                {'text': 'Mismatch between rhetorical choices and audience needs', 'correct': True},
                                {'text': 'MLA vs APA choice', 'correct': False},
                                {'text': 'Margins and line spacing', 'correct': False},
                            ],
                            'explanation': 'Effective critique aligns medium, message, and audience comprehension.'
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
                                {'text': 'Text is objectively hostile', 'correct': False},
                                {'text': 'Your current affect skewed interpretation', 'correct': True},
                                {'text': 'The author intended irony', 'correct': False},
                                {'text': 'The font caused misreading', 'correct': False},
                            ],
                            'explanation': 'Prior state shapes perceived tone—recognize and adjust for lens effects.'
                        },
                        {
                            'question': 'Before reviewing a memoir on migration, you interview migrants with varied backgrounds. This practice:',
                            'answers': [
                                {'text': 'Eliminates bias entirely', 'correct': False},
                                {'text': 'Broadens your interpretive lens via direct perspectives', 'correct': True},
                                {'text': 'Replaces close reading', 'correct': False},
                                {'text': 'Determines the "one true" meaning', 'correct': False},
                            ],
                            'explanation': 'Perspective-getting widens interpretive bandwidth while acknowledging subjectivity.'
                        },
                        {
                            'question': 'You produce two analyses of a protest photo: one as a local, one as an outsider. This demonstrates:',
                            'answers': [
                                {'text': 'Context only', 'correct': False},
                                {'text': 'Conscious lens shifting and meta-awareness', 'correct': True},
                                {'text': 'Professionalism', 'correct': False},
                                {'text': 'Denotative cataloging', 'correct': False},
                            ],
                            'explanation': 'Explicitly toggling vantage points foregrounds lens effects on meaning.'
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
                                {'text': '#connotation + #critique', 'correct': True},
                                {'text': '#context', 'correct': False},
                                {'text': '#professionalism', 'correct': False},
                                {'text': '#interpretivelens', 'correct': False},
                            ],
                            'explanation': 'Word choice alters affect while critique evaluates how that change shifts the claim\'s force.'
                        },
                        {
                            'question': 'You standardize citations, figure captions, and section headers to match the journal\'s guide.',
                            'answers': [
                                {'text': '#professionalism', 'correct': True},
                                {'text': '#critique', 'correct': False},
                                {'text': '#connotation', 'correct': False},
                                {'text': '#context', 'correct': False},
                            ],
                            'explanation': 'Aligning with explicit venue norms is the core of professional presentation.'
                        },
                        {
                            'question': 'Two curators disagree on a sculpture\'s satire; one cites the artist\'s letters, the other their own cultural references.',
                            'answers': [
                                {'text': '#context + #interpretivelens', 'correct': True},
                                {'text': '#connotation', 'correct': False},
                                {'text': '#critique', 'correct': False},
                                {'text': '#professionalism', 'correct': False},
                            ],
                            'explanation': 'Historical evidence reframes meaning while personal standpoint explains divergent readings.'
                        },
                        {
                            'question': 'You remove charged phrasing and add a representative study to back the claim.',
                            'answers': [
                                {'text': '#connotation + #critique', 'correct': True},
                                {'text': '#context', 'correct': False},
                                {'text': '#professionalism', 'correct': False},
                                {'text': '#interpretivelens', 'correct': False},
                            ],
                            'explanation': 'Calibrating tone and evaluating evidence jointly improve argumentative quality.'
                        },
                        {
                            'question': 'A course policy sounds punitive; you rephrase to keep expectations firm but supportive.',
                            'answers': [
                                {'text': '#connotation', 'correct': True},
                                {'text': '#context', 'correct': False},
                                {'text': '#professionalism', 'correct': False},
                                {'text': '#critique', 'correct': False},
                            ],
                            'explanation': 'Tone adjustments change how the same rule is received without altering content.'
                        },
                    ]
                },
            ]
        }
    ]
}

