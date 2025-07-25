-- 14-my_genres.sql

SELECT tv_genres.name

FROM tv_genres, tv_show_genres, tv_shows

WHERE tv_shows.id = tv_show_genres.show_id

AND tv_show_genres.genre_id = tv_genres.id

AND tv_shows.title = 'Dexter'

ORDER BY tv_genres.name ASC;
