INSERT INTO universe (id, name, size, composition)
VALUES
('a287b06f-9397-47d3-9ce8-92f2676d522c'::uuid, 'Andromeda', 1.5, 'Stellar, dust, and gas'),
('9cbbf051-2c1a-428f-8c23-98e714f2cf1c'::uuid, 'Whirlpool', 0.5, 'Stellar, dust, and gas'),
('eae94eb1-6f60-4f84-a9c9-ccf59b3d05c3'::uuid, 'Pinwheel', 0.75, 'Stellar, dust, and gas');

INSERT INTO galaxy (id, name, universe_id, size, shape, composition, distance_from_earth)
VALUES
('8d4a54a4-4c11-4db5-a8a5-86e55a124f61'::uuid, 'Triangulum', 'a287b06f-9397-47d3-9ce8-92f2676d522c'::uuid, 0.3, 'Spiral', 'Stellar, dust, and gas', 3.0),
('2d3a05a3-9296-4397-8d89-ae7388cb92ed'::uuid, 'Bode', '9cbbf051-2c1a-428f-8c23-98e714f2cf1c'::uuid, 0.2, 'Spiral', 'Stellar, dust, and gas', 4.0),
('48bea8d2-98c1-4f68-a94b-bf8d2fbff111'::uuid, 'Sunflower', 'eae94eb1-6f60-4f84-a9c9-ccf59b3d05c3'::uuid, 0.6, 'Spiral', 'Stellar, dust, and gas', 2.5);

INSERT INTO constellation (id, galaxy_id, name, shape, abbreviation, history)
VALUES
('c32b81a9-83a2-40cf-97fc-bcbecc223ee7'::uuid, '8d4a54a4-4c11-4db5-a8a5-86e55a124f61'::uuid, 'Triangulum', 'Triangular', 'Tri', 'Named after the Latin word for triangle'),
('d4a81c3b-d481-4e0d-a8d5-7c987b2e9f02'::uuid, '2d3a05a3-9296-4397-8d89-ae7388cb92ed'::uuid, 'Bode', 'W-shaped', 'Boo', 'Named after the German astronomer Johann Elert Bode'),
('84b94c48-f9af-43db-b2a2-b7d50be72de5'::uuid, '48bea8d2-98c1-4f68-a94b-bf8d2fbff111'::uuid, 'Hercules', 'Irregular', 'Her', 'Named after the mythological Greek hero Hercules');

INSERT INTO star (id, name, galaxy_id, spectral_type, luminosity, distance_from_earth, temperature)
VALUES 
    ('cc98dce8-afec-4d5c-b027-3a3a3a3a3a3a'::uuid, 'Sol', '8d4a54a4-4c11-4db5-a8a5-86e55a124f61'::uuid, 'G2V', 1.0, 8.31, 5778),
    ('f6a51829-9e2f-4c5f-a1c7-7115d8bda7fc'::uuid, 'Proxima Centauri', '8d4a54a4-4c11-4db5-a8a5-86e55a124f61'::uuid, 'M5Ve', 0.0015, 4.24, 3042),
    ('c54ba042-0c11-4b0e-9d9b-c5f5c5b5d86c'::uuid, 'Alpha Centauri A', '8d4a54a4-4c11-4db5-a8a5-86e55a124f61'::uuid, 'G2V', 1.1, 4.37, 5790),
    ('76a2a29a-af8c-4617-bb57-0d79b1319d04'::uuid, 'Alpha Centauri B', '8d4a54a4-4c11-4db5-a8a5-86e55a124f61'::uuid, 'K1V', 0.907, 4.37, 5260),
    ('af14baab-2e2b-4a12-a9f9-007aa0a0e64e'::uuid, 'Barnards Star', '8d4a54a4-4c11-4db5-a8a5-86e55a124f61'::uuid, 'M4Ve', 0.0004, 5.96, 3134);
