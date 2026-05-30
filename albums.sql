PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS ALBUM;
DROP TABLE IF EXISTS ARTIST;
DROP TABLE IF EXISTS GENRE;
DROP TABLE IF EXISTS PARENT_GENRE;
DROP TABLE IF EXISTS ROOT_GENRE;

--Album storing database

CREATE TABLE ROOT_GENRE(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50)

);

CREATE TABLE PARENT_GENRE(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    root_genre_id INT,
    FOREIGN KEY (root_genre_id) REFERENCES ROOT_GENRE(id) ON DELETE RESTRICT

);

CREATE TABLE GENRE(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    parent_genre_id INT,
    FOREIGN KEY (parent_genre_id) REFERENCES PARENT_GENRE(id) ON DELETE RESTRICT

);

CREATE TABLE ARTIST(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    genre_id INT,
    active BOOLEAN,
    details BLOB,
    FOREIGN KEY (genre_id) REFERENCES Genre(id) ON DELETE RESTRICT

);

CREATE TABLE ALBUM(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    artist_id INT,
    genre_id INT,
    release_date DATE,
    format VARCHAR(50),
    vocals VARCHAR(50),
    length INT,
    personal_rating FLOAT,
    rym_data BLOB,
    FOREIGN KEY (artist_id) REFERENCES Artist(id) ON DELETE RESTRICT,
    FOREIGN KEY (genre_id) REFERENCES Genre(id) ON DELETE RESTRICT,
    CONSTRAINT chk_format CHECK(vocals IN ('male', 'female', 'non-binary', 'none', 'male and female', 'sampling')),
    CONSTRAINT chk_format CHECK(format IN ('Album', 'EP', 'Mixtape', 'Compilation', 'DJ Mix', 'Soundtrack', 'Live', 'Archival'))

);

--DML

-- Initial root genres
INSERT INTO ROOT_GENRE (name) VALUES

    ('Ambient'),
    ('Blues'),
    ('Electronic'),
    ('Pop'),
    ('Rock'),
    ('Dance'),
    ('Hip-Hop'),
    ('Folk'),
    ('Jazz'),
    ('Metal'),
    ('Noise'),
    ('Experimental'),
    ('R&B'),
    ('Classical');

-- Insert 'plain genres' for both parent_genre and genre
INSERT INTO PARENT_GENRE (name, root_genre_id) VALUES

    ('Ambient', 1),
    ('Blues', 2),
    ('Electronic', 3),
    ('Pop', 4),
    ('Rock', 5),
    ('Dance', 6),
    ('Hip-Hop', 7),
    ('Folk', 8),
    ('Jazz', 9),
    ('Metal', 10),
    ('Noise', 11),
    ('Experimental', 12),
    ('R&B', 13),
    ('Classical', 14);

INSERT INTO GENRE (name, parent_genre_id) VALUES

    ('Ambient', 1),
    ('Blues', 2),
    ('Electronic', 3),
    ('Pop', 4),
    ('Rock', 5),
    ('Dance', 6),
    ('Hip-Hop', 7),
    ('Folk', 8),
    ('Jazz', 9),
    ('Metal', 10),
    ('Noise', 11),
    ('Experimental', 12),
    ('R&B', 13),
    ('Classical', 14);
