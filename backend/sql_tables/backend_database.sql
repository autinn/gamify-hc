-- ===============================
-- 1. CONTENT TABLES (Courses, Units, Habits of Mind)
-- ===============================

-- A course is a collection of units.
CREATE TABLE courses (
    course_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    title            TEXT NOT NULL CHECK(length(title)),
    description      TEXT CHECK(length(description) > 0),
    );

-- A unit is a collection of concepts.
CREATE TABLE units (
    unit_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id        INTEGER NOT NULL,
    title            TEXT NOT NULL CHECK(length(title) > 0),
    description      TEXT CHECK(length(description) > 0),
    order_index      INTEGER CHECK(order_index >= 0),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- A concept is an HC. Terminology was borrowed from frontend team.
CREATE TABLE concepts (
    concept_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_id          INTEGER NOT NULL,
    title            TEXT NOT NULL CHECK(length(title) > 0),
    definition       TEXT CHECK(length(definition) > 0),
    FOREIGN KEY (unit_id) REFERENCES units(unit_id) ON DELETE CASCADE
);

-- ===============================
-- 2. LEARNING TABLES (Quizzes)
-- ===============================

-- each concept has a set of quiz cards associated with it.
CREATE TABLE quiz_cards (
    quiz_card_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    concept_id       INTEGER NOT NULL,
    question         TEXT NOT NULL CHECK(length(question) > 0),
    FOREIGN KEY (concept_id) REFERENCES concepts(concept_id) ON DELETE CASCADE
);

-- A quiz card has a question, a topic concept, an arbitrary number of answers, arbitrary number of explanations, and correct answer(s). 
CREATE TABLE quiz_answers (
    answer_id        INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique across all answers
    quiz_card_id     INTEGER NOT NULL,                    -- Links to quiz card
    answer_text      TEXT NOT NULL CHECK(length(answer_text) > 0),
    is_correct       BOOLEAN NOT NULL,
    explanation      TEXT NOT NULL CHECK(length(explanation) > 0),
    FOREIGN KEY (quiz_card_id) REFERENCES quiz_cards(quiz_card_id) ON DELETE CASCADE
);

-- ===============================
-- 3. USER TABLES
-- ===============================

--Uuser implementation, has major security flaws, but is a good starting point for the MVP.
CREATE TABLE users (
    user_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    username         TEXT UNIQUE NOT NULL CHECK(length(username) >= 3 AND length(username) <= 50),
    email            TEXT UNIQUE NOT NULL CHECK(email LIKE '%_@_%._%'),
    password_hash    TEXT NOT NULL CHECK(length(password_hash) >= 60),
    created_at       DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Keeps track of user's aptitude for any given quiz card.
-- Uses user_id and quiz_card_id as composite primary key.
CREATE TABLE user_card (
    user_id          INTEGER NOT NULL,
    quiz_card_id     INTEGER NOT NULL,
    ease_factor      REAL DEFAULT 2.5 CHECK(ease_factor >= 1.3 AND ease_factor <= 3.0),
    interval_days    INTEGER DEFAULT 0 CHECK(interval_days >= 0),
    due_date         DATETIME,
    last_reviewed    DATETIME,
    repetitions      INTEGER DEFAULT 0 CHECK(repetitions >= 0),
    success_rate     REAL DEFAULT 0.0 CHECK(success_rate >= 0.0 AND success_rate <= 1.0),
    PRIMARY KEY (user_id, quiz_card_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (quiz_card_id) REFERENCES quiz_cards(quiz_card_id) ON DELETE CASCADE
);

-- ===============================
-- 4. INDEXES FOR PERFORMANCE
-- ===============================

-- Foreign key indexes (improve JOIN performance)
CREATE INDEX idx_units_course_id ON units(course_id);                    -- Fast lookup of units by course
CREATE INDEX idx_concepts_unit_id ON concepts(unit_id);                    -- Fast lookup of concepts by unit
CREATE INDEX idx_quiz_cards_concept_id ON quiz_cards(concept_id);         -- Fast lookup of quiz cards by concept
CREATE INDEX idx_quiz_answers_quiz_card_id ON quiz_answers(quiz_card_id); -- Fast lookup of answers by quiz card
CREATE INDEX idx_user_card_user_id ON user_card(user_id);                 -- Fast lookup of user's cards
CREATE INDEX idx_user_card_quiz_card_id ON user_card(quiz_card_id);       -- Fast lookup of card's users

-- Query optimization indexes (improve specific query patterns)
CREATE INDEX idx_user_card_due_date ON user_card(due_date);               -- Spaced repetition: find cards due for review
CREATE INDEX idx_user_card_last_reviewed ON user_card(last_reviewed);     -- Analytics: find recently reviewed cards
CREATE INDEX idx_quiz_answers_is_correct ON quiz_answers(is_correct);     -- Fast filtering of correct/incorrect answers