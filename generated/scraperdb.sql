CREATE TABLE Users (
	id VARCHAR(255),	-- added default type
	name VARCHAR(255),	-- added default type
	email VARCHAR(255),	-- added default type
	urllist VARCHAR(255),	-- added default type
	interval VARCHAR(255),	-- added default type
	PRIMARY KEY (id)
);
CREATE TABLE Intervals (
	id VARCHAR(255),	-- added default type
	daily VARCHAR(255),	-- added default type
	weekly VARCHAR(255),	-- added default type
	monthly VARCHAR(255),	-- added default type
	attr1 VARCHAR(255),	-- added default type
	PRIMARY KEY (id)
);
