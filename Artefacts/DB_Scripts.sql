CREATE TABLE member(
    pid INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    occupation VARCHAR(30),
    prev_projects BOOLEAN,
    experience INTEGER,
    time_commitment VARCHAR(10)
);

CREATE TABLE interests(
    pid INTEGER,
    aoi VARCHAR(100),
    CONSTRAINT PK PRIMARY KEY interests(pid, aoi),
    CONSTRAINT FK FOREIGN KEY interests(pid) REFERENCES member(pid)
);

CREATE TABLE workedon(
    pid INTEGER,
    worked VARCHAR(100),
    CONSTRAINT workedon_PK PRIMARY KEY workedon(pid, worked),
    CONSTRAINT workedon_FK FOREIGN KEY workedon(pid) REFERENCES member(pid)
);

CREATE TABLE teams(
    tid INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    pid INTEGER NOT NULL,
    CONSTRAINT FOREIGN KEY teams(pid) REFERENCES member(pid)
);
