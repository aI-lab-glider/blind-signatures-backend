BEGIN;

CREATE TABLE IF NOT EXISTS models_user (
    id serial PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    public_key VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS models_polls (
    id serial PRIMARY KEY,
    title VARCHAR (255) NOT NULL,
    category VARCHAR (255),
    description VARCHAR (255),
    expiration_date TIMESTAMP
);

CREATE TABLE IF NOT EXISTS models_questions (
    id serial PRIMARY KEY,
    poll_id INTEGER NOT NULL,
    question_text VARCHAR (255) NOT NULL,
    answer_set VARCHAR (255) NOT NULL,
    answer_count VARCHAR (255) NOT NULL
);

CREATE TABLE IF NOT EXISTS models_internal_ids (
    id serial PRIMARY KEY,
    poll_id INTEGER NOT NULL
);

ALTER TABLE ONLY models_questions
    ADD CONSTRAINT poll_id_fk
    FOREIGN KEY (poll_id)
    REFERENCES models_polls(id);

ALTER TABLE ONLY models_internal_ids
    ADD CONSTRAINT poll_id_fk
    FOREIGN KEY (poll_id)
    REFERENCES models_polls(id);

COMMIT;