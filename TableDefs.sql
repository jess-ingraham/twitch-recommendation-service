#steam tables

CREATE TABLE users(
	steamID int,
	vanityURL varchar(250),
	personaName varchar(50),
	profileStatus tinyint,
	PRIMARY KEY(steamID) 
);

CREATE TABLE friends(
	steamID int references users(steamID) on delete restrict,
	friendID int references users(steamID) on delete restrict,
	PRIMARY KEY(steamID, friendID) 
);

CREATE TABLE games(
	appID int,
	name varchar(50),
	pictureID varchar(255),
	PRIMARY KEY (appID)
);

CREATE TABLE ownedGames(
	userID int references users(steamID),
	appID int references games(appID),
	playTimeTwoWeeks bigint, 
	playTimeForever bigint,
	PRIMARY KEY(userID, appID)
);




