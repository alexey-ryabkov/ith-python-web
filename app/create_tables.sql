CREATE TABLE IF NOT EXISTS User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(64) NOT NULL,
    email VARCHAR(64) NOT NULL,
    password VARCHAR(128) NOT NULL,
    time_create TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    time_change TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Team (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS Tournament (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS Event (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time_start TIMESTAMP NOT NULL,
    tournament INT,
    home_team INT,
    guest_team INT,
    home_team_score INT DEFAULT 0,
    guest_team_score INT DEFAULT 0,
    FOREIGN KEY (tournament) REFERENCES Tournament(id),
    FOREIGN KEY (home_team) REFERENCES Team(id),
    FOREIGN KEY (guest_team) REFERENCES Team(id)
);

CREATE TABLE IF NOT EXISTS FavoriteEvent (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user INT,
    event INT,
    FOREIGN KEY (user) REFERENCES User(id),
    FOREIGN KEY (event) REFERENCES Event(id)
);
