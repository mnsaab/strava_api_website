drop table IF EXISTS userEntry;

CREATE TABLE userEntry(
	entryID int not null primary key AUTO_INCREMENT,
	username varchar(50) not null,
	cycPerWeek double precision,
	aveDistPerRide double precision,
	aveSpeedPerRide double precision,
	cycLongDist double precision,
	cycLongDurat double precision,
	runsPerWeek double precision,
	aveDistPerRun double precision,
	avePacePerRun double precision,
	fastestAvePace double precision,
	runLongDist double precision,
	runLongDurat double precision,
	dateMade timestamp default current_timestamp

);