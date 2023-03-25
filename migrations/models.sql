BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

INFO  [alembic.runtime.migration] Running upgrade  -> 90eed17af1b5, empty message
-- Running upgrade  -> 90eed17af1b5

CREATE TABLE universe (
    id UUID NOT NULL, 
    name VARCHAR(50) NOT NULL, 
    size FLOAT NOT NULL, 
    composition TEXT, 
    PRIMARY KEY (id)
);

CREATE TABLE galaxy (
    id UUID NOT NULL, 
    name VARCHAR(50) NOT NULL, 
    universe_id UUID, 
    size FLOAT NOT NULL, 
    shape VARCHAR(50), 
    composition TEXT, 
    distance_from_earth FLOAT, 
    PRIMARY KEY (id), 
    FOREIGN KEY(universe_id) REFERENCES universe (id)
);

CREATE TABLE constellation (
    id UUID NOT NULL, 
    galaxy_id UUID, 
    name VARCHAR(50) NOT NULL, 
    shape VARCHAR(50), 
    abbreviation VARCHAR(50), 
    history TEXT, 
    PRIMARY KEY (id), 
    FOREIGN KEY(galaxy_id) REFERENCES galaxy (id)
);

CREATE TABLE star (
    id UUID NOT NULL, 
    name VARCHAR(50) NOT NULL, 
    galaxy_id UUID, 
    spectral_type VARCHAR(50) NOT NULL, 
    luminosity FLOAT NOT NULL, 
    distance_from_earth FLOAT NOT NULL, 
    temperature FLOAT NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(galaxy_id) REFERENCES galaxy (id)
);

CREATE TABLE planet (
    id UUID NOT NULL, 
    name VARCHAR(50) NOT NULL, 
    mass FLOAT NOT NULL, 
    diameter FLOAT NOT NULL, 
    distance_from_star FLOAT NOT NULL, 
    orbital_period TIME WITHOUT TIME ZONE, 
    surface_temperature FLOAT, 
    star_id UUID, 
    PRIMARY KEY (id), 
    FOREIGN KEY(star_id) REFERENCES star (id)
);

CREATE TABLE star_constellation (
    star_id UUID NOT NULL, 
    constellation_id UUID NOT NULL, 
    PRIMARY KEY (star_id, constellation_id), 
    FOREIGN KEY(constellation_id) REFERENCES constellation (id), 
    FOREIGN KEY(star_id) REFERENCES star (id)
);

INSERT INTO alembic_version (version_num) VALUES ('90eed17af1b5') RETURNING alembic_version.version_num;

COMMIT;
