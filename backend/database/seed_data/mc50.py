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
                        {
                            'question': 'A job posting describes candidates as "resilient" vs. "stubborn." Both denote persistence. What differs?',
                            'answers': [
                                {'text': 'Nothing—they are synonyms', 'correct': False},
                                {'text': 'Connotation: "resilient" is positive; "stubborn" is negative', 'correct': True},
                                {'text': 'Denotation completely changes', 'correct': False},
                                {'text': 'Grammar rules', 'correct': False},
                            ],
                            'explanation': 'Connotation shapes emotional valence independent of literal meaning.'
                        },
                        {
                            'question': 'An article replaces "elderly" with "senior citizens." What rhetorical effect occurs?',
                            'answers': [
                                {'text': 'Completely changes meaning', 'correct': False},
                                {'text': 'Shifts to a more respectful, neutral connotation', 'correct': True},
                                {'text': 'Makes the text less formal', 'correct': False},
                                {'text': 'No effect whatsoever', 'correct': False},
                            ],
                            'explanation': '"Elderly" can carry condescending overtones; "senior citizens" sounds more dignified.'
                        },
                        {
                            'question': 'A restaurant menu lists "artisanal" bread vs. "handmade" bread. Same denotation. Why choose "artisanal"?',
                            'answers': [
                                {'text': 'It\'s shorter', 'correct': False},
                                {'text': 'It connotes premium quality and craftsmanship', 'correct': True},
                                {'text': 'It\'s more technical', 'correct': False},
                                {'text': 'It removes all connotation', 'correct': False},
                            ],
                            'explanation': 'Connotative associations with "artisanal" suggest higher value and traditional methods.'
                        },
                        {
                            'question': 'A politician calls opponents\' proposal "radical" instead of "progressive." What does this reveal about connotation use?',
                            'answers': [
                                {'text': 'Both terms are equally neutral', 'correct': False},
                                {'text': 'Word choice strategically frames the proposal negatively vs. positively', 'correct': True},
                                {'text': 'The denotation changes completely', 'correct': False},
                                {'text': 'Connotation doesn\'t matter in politics', 'correct': False},
                            ],
                            'explanation': 'Strategic connotation shapes audience perception; "radical" implies danger, "progressive" implies improvement.'
                        },
                        {
                            'question': 'A product review calls a device "simple" vs. "simplistic." Why does tone shift?',
                            'answers': [
                                {'text': 'They mean exactly the same thing', 'correct': False},
                                {'text': '"Simple" is neutral/positive; "simplistic" implies oversimplification', 'correct': True},
                                {'text': '"Simplistic" is more formal', 'correct': False},
                                {'text': 'No tonal difference exists', 'correct': False},
                            ],
                            'explanation': 'Connotative weight: "simple" = user-friendly; "simplistic" = inadequately thought-out.'
                        },
                        {
                            'question': 'A news headline uses "migrant" vs. "immigrant" vs. "refugee." Each carries different connotations. What should a writer consider?',
                            'answers': [
                                {'text': 'All three are interchangeable', 'correct': False},
                                {'text': 'Each term\'s connotations affect audience empathy and perceived legitimacy', 'correct': True},
                                {'text': 'Only denotation matters', 'correct': False},
                                {'text': 'Connotation is irrelevant in journalism', 'correct': False},
                            ],
                            'explanation': 'Precise word choice acknowledges legal status and human circumstances; connotations shape public discourse.'
                        },
                        {
                            'question': 'An email describes a plan as "ambitious" vs. "unrealistic." Both note scale, but what differs?',
                            'answers': [
                                {'text': 'Denotation—they describe different scales', 'correct': False},
                                {'text': 'Connotation—"ambitious" inspires, "unrealistic" dismisses', 'correct': True},
                                {'text': 'Grammar and syntax', 'correct': False},
                                {'text': 'Nothing at all', 'correct': False},
                            ],
                            'explanation': 'Connotation reveals the speaker\'s stance: support vs. skepticism.'
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
                        {
                            'question': 'A resume uses three different fonts, inconsistent bullet styles, and varied margins. What professional standard is violated?',
                            'answers': [
                                {'text': 'Content quality', 'correct': False},
                                {'text': 'Visual consistency and formatting standards', 'correct': True},
                                {'text': 'Grammar rules', 'correct': False},
                                {'text': 'Length requirements', 'correct': False},
                            ],
                            'explanation': 'Professional documents require uniform visual design to convey attention to detail.'
                        },
                        {
                            'question': 'An academic paper due in MLA format uses APA style throughout. What should be corrected?',
                            'answers': [
                                {'text': 'The argument structure', 'correct': False},
                                {'text': 'Convert all citations and formatting to MLA guidelines', 'correct': True},
                                {'text': 'Add more sources', 'correct': False},
                                {'text': 'Change the topic', 'correct': False},
                            ],
                            'explanation': 'Following specified guidelines demonstrates professionalism and respect for conventions.'
                        },
                        {
                            'question': 'A business email addressing executives uses "Hey!" and closes with "Later!" What professional issue exists?',
                            'answers': [
                                {'text': 'Email is too short', 'correct': False},
                                {'text': 'Inappropriate level of formality for the audience and context', 'correct': True},
                                {'text': 'Missing attachments', 'correct': False},
                                {'text': 'Too many paragraphs', 'correct': False},
                            ],
                            'explanation': 'Register and tone must match professional hierarchies and contexts.'
                        },
                        {
                            'question': 'A grant proposal has typos, inconsistent section numbering, and missing page numbers. What does this signal?',
                            'answers': [
                                {'text': 'Creative freedom', 'correct': False},
                                {'text': 'Lack of attention to detail, reducing credibility', 'correct': True},
                                {'text': 'Strong content', 'correct': False},
                                {'text': 'Appropriate informality', 'correct': False},
                            ],
                            'explanation': 'Professional polish reflects competence; errors undermine trust in your work.'
                        },
                        {
                            'question': 'Which action best demonstrates professional self-presentation in a portfolio?',
                            'answers': [
                                {'text': 'Including unfinished drafts', 'correct': False},
                                {'text': 'Curating polished, relevant work with clear descriptions', 'correct': True},
                                {'text': 'Adding personal photos unrelated to work', 'correct': False},
                                {'text': 'Using casual language throughout', 'correct': False},
                            ],
                            'explanation': 'Professionalism means presenting your best, most relevant work with appropriate context.'
                        },
                        {
                            'question': 'A lab report uses first-person "I" throughout, contradicting field conventions for objective reporting. What should change?',
                            'answers': [
                                {'text': 'Nothing—personal voice is always best', 'correct': False},
                                {'text': 'Shift to third-person or passive constructions per scientific writing norms', 'correct': True},
                                {'text': 'Add more personal anecdotes', 'correct': False},
                                {'text': 'Remove all verbs', 'correct': False},
                            ],
                            'explanation': 'Disciplinary conventions guide professional writing; scientific reports typically avoid first-person.'
                        },
                        {
                            'question': 'You submit a presentation with garish color schemes, unreadable fonts, and cluttered slides. What professional principle is violated?',
                            'answers': [
                                {'text': 'Creativity is discouraged', 'correct': False},
                                {'text': 'Visual clarity and audience accessibility', 'correct': True},
                                {'text': 'Content must be controversial', 'correct': False},
                                {'text': 'Presentations should be text-only', 'correct': False},
                            ],
                            'explanation': 'Professional design prioritizes audience comprehension over decorative excess.'
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
                        {
                            'question': 'A 1920s essay uses "race" terminology now considered outdated. What helps explain this?',
                            'answers': [
                                {'text': 'Author was careless', 'correct': False},
                                {'text': 'Historical linguistic norms differed; vocabulary evolved', 'correct': True},
                                {'text': 'Typo in the text', 'correct': False},
                                {'text': 'Modern readers misunderstand', 'correct': False},
                            ],
                            'explanation': 'Historical context clarifies why past texts used language their era accepted.'
                        },
                        {
                            'question': 'An economist writes "perfectly competitive market" assuming rational actors. What disciplinary context matters?',
                            'answers': [
                                {'text': 'Economics sometimes uses idealized models to test theory', 'correct': True},
                                {'text': 'Author is unaware of reality', 'correct': False},
                                {'text': 'All markets are perfectly competitive', 'correct': False},
                                {'text': 'No context needed', 'correct': False},
                            ],
                            'explanation': 'Disciplinary frameworks shape how fields construct arguments and models.'
                        },
                        {
                            'question': 'A physics paper uses jargon like "Hamiltonian" without definition. What contextual assumption is made?',
                            'answers': [
                                {'text': 'The author is being deliberately obscure', 'correct': False},
                                {'text': 'The target audience has disciplinary training in physics', 'correct': True},
                                {'text': 'Jargon should never be used', 'correct': False},
                                {'text': 'The term is self-explanatory', 'correct': False},
                            ],
                            'explanation': 'Disciplinary context shapes vocabulary; experts write for expert peers.'
                        },
                        {
                            'question': 'A novel set during WWII includes rationing and blackout curtains. What context enriches interpretation?',
                            'answers': [
                                {'text': 'Author\'s personal color preferences', 'correct': False},
                                {'text': 'Historical wartime conditions that shaped daily life', 'correct': True},
                                {'text': 'Modern energy-saving tips', 'correct': False},
                                {'text': 'Random plot devices', 'correct': False},
                            ],
                            'explanation': 'Historical context reveals how real conditions inform setting and characterization.'
                        },
                        {
                            'question': 'A manifesto written by a marginalized activist uses confrontational tone. What biographical/cultural context matters?',
                            'answers': [
                                {'text': 'Author is inherently aggressive', 'correct': False},
                                {'text': 'Lived experience of oppression shapes rhetorical urgency', 'correct': True},
                                {'text': 'Tone is irrelevant', 'correct': False},
                                {'text': 'All manifestos are calm', 'correct': False},
                            ],
                            'explanation': 'Biographical and cultural contexts explain why authors choose certain rhetorical strategies.'
                        },
                        {
                            'question': 'A scientific paper from 1850 lacks modern statistical methods. What context explains this?',
                            'answers': [
                                {'text': 'Author was incompetent', 'correct': False},
                                {'text': 'Statistical tools developed later; historical context of methodology', 'correct': True},
                                {'text': 'Statistics are never needed', 'correct': False},
                                {'text': 'Modern methods are always wrong', 'correct': False},
                            ],
                            'explanation': 'Historical disciplinary context shows how methods evolve over time.'
                        },
                        {
                            'question': 'A religious text uses metaphors unfamiliar to modern readers. What context helps?',
                            'answers': [
                                {'text': 'Author wrote poorly', 'correct': False},
                                {'text': 'Historical, cultural, and religious traditions shape symbolic language', 'correct': True},
                                {'text': 'Metaphors are universal', 'correct': False},
                                {'text': 'Modern readers are always correct', 'correct': False},
                            ],
                            'explanation': 'Cultural and historical context unlocks symbolic meanings rooted in tradition.'
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
                        {
                            'question': 'A study claims causation but only shows correlation. What critical question arises?',
                            'answers': [
                                {'text': 'Is the font size appropriate?', 'correct': False},
                                {'text': 'Does the evidence support the causal claim, or are confounds present?', 'correct': True},
                                {'text': 'Is the author famous?', 'correct': False},
                                {'text': 'Was the study published recently?', 'correct': False},
                            ],
                            'explanation': 'Critical readers distinguish correlation from causation and identify logical gaps.'
                        },
                        {
                            'question': 'A politician\'s speech uses emotional appeals but provides no data. What critique is warranted?',
                            'answers': [
                                {'text': 'Emotional appeals are always effective', 'correct': False},
                                {'text': 'Heavy reliance on pathos without logos weakens substantive argument', 'correct': True},
                                {'text': 'All rhetoric is equally valid', 'correct': False},
                                {'text': 'Data is irrelevant in speeches', 'correct': False},
                            ],
                            'explanation': 'Balanced critique assesses whether rhetorical strategies are backed by evidence.'
                        },
                        {
                            'question': 'An advertisement claims "9 out of 10 doctors recommend" without source. What should critics question?',
                            'answers': [
                                {'text': 'The claim is automatically credible', 'correct': False},
                                {'text': 'Source transparency, sample size, and potential bias', 'correct': True},
                                {'text': 'Nothing—statistics are always accurate', 'correct': False},
                                {'text': 'The product color', 'correct': False},
                            ],
                            'explanation': 'Critical engagement demands verification of statistical claims and sources.'
                        },
                        {
                            'question': 'A research paper cherry-picks data supporting its hypothesis while ignoring contradictory findings. What\'s the critique?',
                            'answers': [
                                {'text': 'The paper has strong confirmation bias', 'correct': True},
                                {'text': 'This is standard scientific practice', 'correct': False},
                                {'text': 'The writing style is excellent', 'correct': False},
                                {'text': 'References are well-formatted', 'correct': False},
                            ],
                            'explanation': 'Critical reading identifies selective use of evidence and methodological flaws.'
                        },
                        {
                            'question': 'A blog post makes sweeping generalizations without evidence. Which critical approach applies?',
                            'answers': [
                                {'text': 'Accept claims at face value', 'correct': False},
                                {'text': 'Question the basis for generalizations and demand supporting evidence', 'correct': True},
                                {'text': 'Praise the author\'s confidence', 'correct': False},
                                {'text': 'Ignore the lack of evidence', 'correct': False},
                            ],
                            'explanation': 'Critical engagement requires assessing whether claims are substantiated.'
                        },
                        {
                            'question': 'A news article quotes only sources supporting one political perspective. What critique is appropriate?',
                            'answers': [
                                {'text': 'The article shows perfect balance', 'correct': False},
                                {'text': 'Lack of diverse perspectives suggests potential bias', 'correct': True},
                                {'text': 'All journalism is inherently neutral', 'correct': False},
                                {'text': 'Headlines don\'t matter', 'correct': False},
                            ],
                            'explanation': 'Critical readers evaluate whether multiple perspectives are represented fairly.'
                        },
                        {
                            'question': 'An academic argument relies on outdated theories discredited by recent research. What should critics note?',
                            'answers': [
                                {'text': 'Age of sources is irrelevant', 'correct': False},
                                {'text': 'The argument fails to engage current scholarship and evidence', 'correct': True},
                                {'text': 'Older theories are always superior', 'correct': False},
                                {'text': 'Recent research doesn\'t matter', 'correct': False},
                            ],
                            'explanation': 'Critical analysis assesses whether arguments account for updated knowledge.'
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
                        {
                            'question': 'You notice you interpret economic data differently when presented by sources you trust vs distrust. What does this reveal?',
                            'answers': [
                                {'text': 'All data is inherently biased', 'correct': False},
                                {'text': 'Your prior beliefs and source credibility shape interpretation', 'correct': True},
                                {'text': 'Numbers never lie', 'correct': False},
                                {'text': 'Statistics are always objective', 'correct': False},
                            ],
                            'explanation': 'Recognizing how trust and expectations filter evidence demonstrates interpretive self-awareness.'
                        },
                        {
                            'question': 'Reading a novel set in a culture unfamiliar to you, you initially misinterpret social norms. How should you respond?',
                            'answers': [
                                {'text': 'Assume your first interpretation is correct', 'correct': False},
                                {'text': 'Seek cultural context and revise understanding accordingly', 'correct': True},
                                {'text': 'Blame the author for poor writing', 'correct': False},
                                {'text': 'Ignore unfamiliar elements', 'correct': False},
                            ],
                            'explanation': 'Lens awareness means recognizing your interpretive limits and seeking context.'
                        },
                        {
                            'question': 'Two readers from different political backgrounds reach opposite conclusions about the same policy brief. What explains this?',
                            'answers': [
                                {'text': 'One reader is wrong, the other right', 'correct': False},
                                {'text': 'Interpretive lenses shaped by prior beliefs influence meaning-making', 'correct': True},
                                {'text': 'The brief was poorly written', 'correct': False},
                                {'text': 'Political backgrounds are irrelevant', 'correct': False},
                            ],
                            'explanation': 'Different lenses can yield different but valid interpretations based on perspective.'
                        },
                        {
                            'question': 'You realize you\'re reading a scientific study more skeptically because it contradicts your existing views. What should you do?',
                            'answers': [
                                {'text': 'Dismiss the study immediately', 'correct': False},
                                {'text': 'Acknowledge confirmation bias and evaluate evidence more objectively', 'correct': True},
                                {'text': 'Trust your instincts without question', 'correct': False},
                                {'text': 'Only read studies supporting your views', 'correct': False},
                            ],
                            'explanation': 'Interpretive lens awareness involves recognizing and correcting for cognitive biases.'
                        },
                        {
                            'question': 'A student from an urban background interprets a rural poem differently than a rural student. This illustrates:',
                            'answers': [
                                {'text': 'One interpretation is objectively correct', 'correct': False},
                                {'text': 'Lived experience shapes interpretive frameworks and meanings', 'correct': True},
                                {'text': 'The poem failed to communicate', 'correct': False},
                                {'text': 'Location has no impact on reading', 'correct': False},
                            ],
                            'explanation': 'Personal experience forms an interpretive lens that colors understanding.'
                        },
                        {
                            'question': 'You find yourself assuming a business memo is aggressive because similar past memos preceded layoffs. What\'s happening?',
                            'answers': [
                                {'text': 'The memo is objectively aggressive', 'correct': False},
                                {'text': 'Past experience creates an interpretive lens that colors current reading', 'correct': True},
                                {'text': 'All business memos are aggressive', 'correct': False},
                                {'text': 'Your reading skills are inadequate', 'correct': False},
                            ],
                            'explanation': 'Prior experiences shape expectations and interpretations of new texts.'
                        },
                        {
                            'question': 'To reduce interpretive bias when analyzing a controversial speech, you should:',
                            'answers': [
                                {'text': 'Only read sources you agree with', 'correct': False},
                                {'text': 'Consider multiple perspectives and question your own assumptions', 'correct': True},
                                {'text': 'Trust your first impression completely', 'correct': False},
                                {'text': 'Ignore context and background', 'correct': False},
                            ],
                            'explanation': 'Lens awareness involves actively seeking diverse viewpoints and self-reflection.'
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


