INSERT INTO Tournament (id, name) VALUES (1, 'РФПЛ');

INSERT INTO Team (name) VALUES 
    ('Динамо'), ('Ростов'), ('Зенит'), ('Динамо Мх'), ('Локомотив'), 
    ('Рубин'), ('ЦСКА'), ('Спартак'), ('Акрон'), ('Крылья Советов'),
    ('Ахмат'), ('Пари НН'), ('Факел'), ('Химки'), ('Краснодар'), ('Оренбург');

INSERT INTO Event (time_start, tournament, home_team, guest_team, home_team_score, guest_team_score) VALUES 
    (FROM_UNIXTIME(1730487600), 1, (SELECT id FROM Team WHERE name='Динамо'), (SELECT id FROM Team WHERE name='Ростов'), 1, 1),
    (FROM_UNIXTIME(1730570400), 1, (SELECT id FROM Team WHERE name='Зенит'), (SELECT id FROM Team WHERE name='Динамо Мх'), 2, 1),
    (FROM_UNIXTIME(1730570400), 1, (SELECT id FROM Team WHERE name='Локомотив'), (SELECT id FROM Team WHERE name='Рубин'), 1, 0),
    (FROM_UNIXTIME(1730580300), 1, (SELECT id FROM Team WHERE name='ЦСКА'), (SELECT id FROM Team WHERE name='Спартак'), 0, 2),
    (FROM_UNIXTIME(1730638800), 1, (SELECT id FROM Team WHERE name='Акрон'), (SELECT id FROM Team WHERE name='Крылья Советов'), 2, 0),
    (FROM_UNIXTIME(1730646900), 1, (SELECT id FROM Team WHERE name='Ахмат'), (SELECT id FROM Team WHERE name='Пари НН'), 0, 2),
    (FROM_UNIXTIME(1730655000), 1, (SELECT id FROM Team WHERE name='Факел'), (SELECT id FROM Team WHERE name='Химки'), 1, 1),
    (FROM_UNIXTIME(1730663100), 1, (SELECT id FROM Team WHERE name='Краснодар'), (SELECT id FROM Team WHERE name='Оренбург'), 4, 0);
