CREATE TABLE OSOBY (
	ID integer PRIMARY KEY AUTOINCREMENT,
	jmeno varchar,
	prijmeni varchar,
	ucebnice_id integer
);

CREATE TABLE UCEBNICE (
	ID integer PRIMARY KEY AUTOINCREMENT,
	nazev varchar,
	jazyk varchar
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
	osoby_id integer,
	lekce_id integer,
	uspesnost integer,
	datum datetime
);

CREATE TABLE TESTOVANA_SLOVICKA (
	osoba_id integer,
	slovicko_id integer,
	testovat boolean
);
