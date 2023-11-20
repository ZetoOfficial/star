BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

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

CREATE OR REPLACE FUNCTION count_constellations() RETURNS INTEGER AS $$
DECLARE
    count INTEGER;
BEGIN
    SELECT COUNT(*) INTO count FROM constellation;
    RETURN count;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_planets_by_star(star_id UUID) RETURNS SETOF planet AS $$
BEGIN
    RETURN QUERY SELECT * FROM planet WHERE planet.star_id = get_planets_by_star.star_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_star_by_name(name VARCHAR, OUT id UUID, OUT spectral_type VARCHAR, OUT luminosity FLOAT) AS $$
BEGIN
    SELECT star.id, star.spectral_type, star.luminosity INTO id, spectral_type, luminosity FROM star WHERE star.name = get_star_by_name.name;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER add_star_trigger
AFTER INSERT ON star
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM star_constellation WHERE star_id = NEW.id) THEN
        INSERT INTO star_constellation (star_id, constellation_id) VALUES (NEW.id, NEW.constellation_id);
    END IF;
END;

CREATE TRIGGER add_universe_trigger
AFTER INSERT ON universe
FOR EACH ROW
BEGIN
  RAISE NOTICE 'universe';
  RETURN NEW;
END;