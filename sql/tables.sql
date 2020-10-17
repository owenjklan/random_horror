CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    user_name   TEXT NOT NULL,
    pword_hash  TEXT NOT NULL,
);


CREATE TABLE story (
    id           INTEGER PRIMARY KEY,
    user_id      INTEGER NOT NULL,
    who          TEXT NOT NULL,
    place        TEXT NOT NULL,
    plot_device  TEXT NOT NULL,
    items        TEXT NOT NULL,

    FOREIGN KEY (user_id) REFERENCES user(user_id)
);


CREATE TABLE rating (
    id       INTEGER PRIMARY KEY,
    by_user  INTEGER NOT NULL,
    story_id INTEGER NOT NULL,
    rating   INTEGER NOT NULL,

    FOREIGN KEY (by_user) REFERENCES user(id),
    FOREIGN KEY (story_id) REFERENCES story(id)
);
