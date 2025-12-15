# Interview Insights

**Last Updated:** December 15, 2025  
**Project:** Gamify HC

This document captures all user interviews chronologically with key findings and implementation impact.

---

## Interview Timeline

| # | Interviewer | Date | Participant | Due Date |
|---|-------------|------|-------------|----------|
| 1 | Rachael | Oct 23, 2025 | Minerva M29 (first-year) | Oct 28 |
| 2 | Autinn | Nov 18, 2025 | Minerva M29 (Michael) | Nov 18 |
| 3 | Aldiyar | Nov 27, 2025 | Ali Zhumatayev (M29) | Nov 28 |
| 4 | Taher | Dec 4, 2025 | Minerva M29 (Sevval) | Dec 4 |
| 5 | Sophie | Dec 10, 2025 | Adeel (CS162 LBA) | Dec 10 |
| 6 | Merrick | Dec 14, 2025 | Chukwudaru Vincent | Dec 16 |

---

## 1. Figma Interview: Rachael

**Due:** Oct 28  
**Completed:** Oct 23, 2025 (frontend meeting)  
**Participant:** Minerva M29 (first-year student)

### Interview Goals and Purpose
- Is the navigation intuitive?
- Is it visually appealing?
- Does the design feel appropriate to the context and purpose of the app?

### Key Findings
- Course flow was clear and intuitive, but navigation back to the main page wasn't clear → add global back button and persistent navbar.
- Quiz layout felt crowded → redesigned into four smaller answer cards.
- "Start Quiz" button blended in → changed to black with white text for contrast.
- Minimalist black-and-white design felt "clean" and "very Minerva."
- Participant rated UX 4/5 and said it would "really help freshmen learn HCs."

### Impact
Validated concept, clarified early design priorities, and set direction for first code sprint beginning Oct 28.

---

## 2. User Question-Focused Interview: Autinn

**Due:** Nov 18  
**Completed:** Nov 18  
**Participant:** Minerva M29 (Michael)

### Interview Goals and Purpose
- Are the questions clear?
- Are they useful?
- Are they an appropriate difficulty level?
- Do they have the right tone?
- What is the overall quiz experience like?

### Key Findings
1. Presenting users with the full database of questions for a course or unit felt overwhelming; the interviewee suggested a smaller, fixed set of questions per quiz to support focused practice.
2. The user was unclear about how the quiz worked, specifically whether there was a timer, how many attempts were allowed, and how progress was measured, indicating the need for clearer onboarding.
3. Although explanations were implemented, the interview highlighted the importance of providing differentiated explanations in the future, as well as improving overall question quality through simpler wording, more straightforward prompts, and more clearly distinguishable answer choices.

### Impact
- Sophie's PR (#22): introducing a five-question quiz logic per quiz
- Sophie's PR (#26): improving question and explanation quality, added explanations for wrong answers.
- Autinn's PR (#34): instruction / onboarding guide updates.

---

## 3. Second Full User Experience Interview and Progress Tracking: Aldiyar

**Due:** Nov 28th (before Friday meeting)  
**Completed:** November 27th  
**Participant:** Ali Zhumatayev, Minerva M29

### Interview Goals and Purpose
- Watch someone use the app without guidance.
- Is the UI intuitive?
- Does anything feel missing?
- What do you like? What do you dislike?
- What metrics reflect progress best?
- What do you interpret from the current progress tracking chart?

### Key Findings
- UI was intuitive; user navigated independently, found classes, and started quizzes without guidance.
- Performance issues were critical: progress charts took 5–10 seconds to load, causing frustration when switching views.
- Progress tracking needed more depth: user wanted percentage-based success rates broken down by course → unit → concept.
- Password validation was inconsistent: frontend showed 6-character minimum, backend required 8.

### Impact
- PR #29: database indexing optimization reduced load times from 5–10s to near-instant.
- PR #31: added hierarchical, percentage-based progress metrics at course/unit/concept levels.
- PR #35: standardized 8-character password validation.
- Reinforced design principles: performance is essential, users need granular actionable data, and consistency builds trust during onboarding.

---

## 4. Full User Experience Interview: Taher

**Due:** Dec 4  
**Completed:** Dec 4  
**Participant:** Future user "M29" (Sevval)

### Interview Goals and Purpose
- Evaluate the holistic user experience.
- Find snag points where the app might be unintuitive.
- Identify users desires for the app.

### Key Findings
- Navigation felt clear and intuitive, but she asked for an instructions/"how it works" page before starting quizzes and for HC/unit options to appear directly on the first screen rather than after an extra click.
- She liked the neutral black-and-white academic look, found question difficulty mixed but preferred more semester-1 focus, and wanted richer explanations, especially about why incorrect options are wrong.

### Impact
- Prioritize an explicit pre-quiz instructions screen and surface HC/unit selection on the home screen to streamline onboarding and quiz discovery, aligning with best practices for onboarding.
- Maintain the neutral academic color palette while refining content: bias item selection toward semester-1 questions and expand feedback to cover both correct and incorrect choices to better scaffold learning.

---

## 5. TA Question Interview: Sophie

**Due:** December 10  
**Completed:** December 10  
**Participant:** CS162 LBA Interview — Adeel

### Interview Goals and Purpose
- Get an alternate, informed perspective on the quiz questions.
- Do the questions address the common confusions of first years?
- Would the concept page be a useful reference for first years while writing assignments, given the common mistakes they make?
- General recommendations and critique.

### Key Findings
- TAs could be alternate users, and this app could be used for PCW.
- Specificity and keywords were the biggest recurring comments.
- Students making extra efforts, coming to TAs, are interested in moving from 3s to 4s.
- The questions should use more keywords.
- Some questions are too broad, and the explanations are sometimes too negative.

### Impact
- Sophie's PR (#40): final question refinement.

---

## 6. Final Product Reflection: Merrick

**Due:** December 16  
**Completed:** December 14  
**Participant:** Chukwudaru (Praise) Vincent

### Interview Goals and Purpose
- Reflection on the product.
- Future Design Process Suggestions.

### Key Findings
- The progress-tracking system's cumulative scoring permanently reflects past errors, making recent perfect performance feel unrewarding.
- Progress bars often start near 100% and decline over time, inaccurately representing user learning progress.
- The app's intended usage frequency is unclear, with the participant anticipating use only 2–3 times per week.
- Account creation caused usability friction, as the participant attempted to log in with institutional credentials without having an account.
- The participant largely ignored answer explanations, even after incorrect responses.
- The quiz feature itself was perceived as effective, indicating a strong core interaction.
- The platform name "gamify-hc" was perceived as too overt, while the visual design was positively received.
- High autonomy in selecting content led to engagement that appeared unfocused and directionless.

### Future Design Process Suggestions
- Redesign the progress-tracking system to make perfect performance intrinsically rewarding and to provide clear, predefined goals.
- Introduce structured endpoints (e.g., mastery states or levels) to make progress visible and interpretable.
- Collect empirical data on long-term engagement rather than relying on self-reported usage.
- Implement longitudinal analytics capturing session frequency, duration, and interaction patterns.
- Add a low-friction, in-product feedback channel to gather qualitative insights during use.
- Conduct a limited pilot deployment to observe real-world study behavior.
- Increase the visual prominence of answer explanations, potentially through staggered feedback cues.
- Migrate authentication to OAuth to reduce account-creation confusion, if resources permit.
- Consider rebranding the application name to improve user-facing appeal.
