create table genres (
	id integer primary key, 
	name varchar unique not null
); 

create table cinemas (
	id integer primary key,
	name varchar,
	address varchar,
	district varchar check (district in ('Bemowo', 'Białołęka', 'Bielany', 'Mokotów', 'Ochota', 'Praga-Południe', 'Praga-Północ', 'Rembertów', 'Śródmieście', 'Targówek', 'Ursus', 'Ursynów', 'Wawer', 'Wesoła', 'Wilanów', 'Włochy', 'Wola', 'Żoliborz'))
);

create table movies (
	id integer primary key,
	title varchar not null,
	description varchar,
	production_date int check (production_date > 1900),
	url_filmweb varchar,
	url_imdb varchar
);

create table movie_genres (
	movie_id integer,
	genre_id integer,
	primary key(movie_id, genre_id)
);