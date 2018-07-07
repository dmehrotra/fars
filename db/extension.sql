CREATE TABLE location
(
"State Name" text,
"State Code" int,
"City Code" int,
"City Name" text,
"County Code" int,
"County Name" text
);

CREATE TABLE body_typ
(
"Code" int,
"Desc" text
);


COPY body_typ("Code","Desc")
	FROM 'body_types.csv' DELIMITER ',' CSV HEADER;

COPY location("State Name","State Code","City Code","City Name","County Code","County Name")
	FROM 'city-state.csv' DELIMITER ',' CSV HEADER;
