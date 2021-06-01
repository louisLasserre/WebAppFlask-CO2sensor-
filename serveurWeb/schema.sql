DROP TABLE IF EXISTS capteurUn;
DROP TABLE IF EXISTS globale;

CREATE TABLE capteurUn (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime')),
    seuil INTEGER NOT NULL,
    salle TEXT NOT NULL
);

CREATE TABLE globale (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seuil INTEGER,
    salle TEXT,
    temps TIMESTAMP
);