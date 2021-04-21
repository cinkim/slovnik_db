CREATE TABLE OSOBY (
	ID integer PRIMARY KEY AUTOINCREMENT,
	jmeno text,
	akt_jazyk_id integer
);

CREATE TABLE UCEBNICE (
	ID integer PRIMARY KEY AUTOINCREMENT,
	nazev varchar,
	jazyk_id integer
);

CREATE TABLE LEKCE (
	ID integer PRIMARY KEY AUTOINCREMENT,
	ucebnice_id integer,
	cislo integer,
	nazev varchar
);

CREATE TABLE SLOVICKA (
	ID integer PRIMARY KEY AUTOINCREMENT,
	cz varchar,
	preklad varchar,
	lekce_id integer
);

CREATE TABLE VYSLEDKY (
	ID integer PRIMARY KEY AUTOINCREMENT,
	osoba_id integer,
	lekce_id integer,
	uspesnost integer,
	datum datetime
);

CREATE TABLE TESTOVANA_SLOVICKA (
	osoba_id integer,
	slovicko_id integer,
	testovat boolean
);

CREATE TABLE JAZYKY (
	ID integer PRIMARY KEY AUTOINCREMENT,
	nazev varchar,
	to_speak string
);

CREATE TABLE OSOBY_JAZYKY (
	osoba_id integer,
	jazyk_id integer,
	akt_ucebnice_id integer
);
