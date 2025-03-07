-- Select cities from table
SELECT cities.id, cities.name, (SELECT states.name FROM states WHERE states.id = cities.states_id)
FROM cities
ORDER BY cities.id ASC;