-- This is the DDL file for the Final Project of TEAM 10 (Alex De Meo, Sophie De Jong, Justin Koops)
CREATE TABLE Member(
    MemberID SERIAL UNIQUE PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    PhoneNumber TEXT UNIQUE,
    email TEXT UNIQUE,
    Gender TEXT,
    DateOfBirth DATE 
);

CREATE TABLE Trainer(
    TrainerID SERIAL UNIQUE PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT
);

CREATE TABLE Administrator(
    AdministratorID SERIAL UNIQUE PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT
);

CREATE TABLE Room(
    RoomID SERIAL UNIQUE PRIMARY KEY,
    RoomName TEXT 
);

CREATE TABLE FitnessGoal(
    GoalID SERIAL UNIQUE PRIMARY KEY,
    MemberID INT,
    GoalType TEXT,
    TargetValue NUMERIC,
    FOREIGN KEY (MemberID) REFERENCES Member (MemberID)
);

CREATE TABLE PersonalSession(
    SessionID SERIAL UNIQUE PRIMARY KEY,
    MemberID INT,
    TrainerID INT,
    FOREIGN KEY (MemberID) REFERENCES Member (MemberID),
    FOREIGN KEY (TrainerID) REFERENCES Trainer (TrainerID) 
);

CREATE TABLE TrainerAvailability(
    AvailabilityID SERIAL UNIQUE PRIMARY KEY,
    TrainerID INT,
    AvailabilityDate DATE,
    StartTime TIME,
    EndTime TIME,
    FOREIGN KEY (TrainerID) REFERENCES Trainer (TrainerID)
);

CREATE TABLE RoomBooking(
    BookingID SERIAL UNIQUE PRIMARY KEY,
    RoomID INT,
    BookingDate DATE,
    StartTime TIME,
    EndTime TIME,
    FOREIGN KEY (RoomID) REFERENCES Room (RoomID)
);

CREATE TABLE Manages(
    AdministratorID INT,
    BookingID INT,
    FOREIGN KEY (AdministratorID) REFERENCES Administrator (AdministratorID),
    FOREIGN KEY (BookingID) REFERENCES RoomBooking (BookingID)
);

CREATE TABLE HealthMetric(
    MetricID SERIAL UNIQUE PRIMARY KEY,
    MemberID INT,
    HeightMetric NUMERIC,
    WeightMetric NUMERIC,
    HeartRate NUMERIC,
    BloodPressure NUMERIC,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (MemberID) REFERENCES Member (MemberID)
);

CREATE TABLE GroupClass(
    ClassID SERIAL UNIQUE PRIMARY KEY,
    TrainerID INT,
    AdministratorID INT,
    ClassName TEXT,
    ClassDate DATE,
    StartTime TIME,
    EndTime TIME,
    Capacity INT,
    FOREIGN KEY (TrainerID) REFERENCES Trainer (TrainerID),
    FOREIGN KEY (AdministratorID) REFERENCES Administrator (AdministratorID)
);

CREATE TABLE RegistersFor(
    MemberID INT,
    ClassID INT,
    FOREIGN KEY (MemberID) REFERENCES Member (MemberID),
    FOREIGN KEY (ClassID) REFERENCES GroupClass (ClassID)
);

