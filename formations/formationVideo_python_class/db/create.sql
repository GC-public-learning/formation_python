CREATE TABLE players (
    pid     INTEGER PRIMARY KEY AUTOINCREMENT,
    login   TEXT,
    passwd  TEXT,
    score   INTEGER
);


CREATE TABLE heros (
    hid     INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT,
    hp      INTEGER,
    energy  INTEGER,
    attack  INTEGER
);


CREATE TABLE unlockheros (
    pid     INTEGER,
    hid     INTEGER
);

