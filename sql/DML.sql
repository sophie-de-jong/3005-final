INSERT INTO Member (FirstName, LastName, PhoneNumber, Email, Gender, DateOfBirth)
VALUES
('Sophers', 'de Jophers', 6135550101, 'sophers.dejophers@email.com', 'Female', '1998-04-12'),
('Alex', 'de Meo', 6135550103, 'alex.demeo@email.com', 'Male', '2000-01-15'),
('Deliler', 'Jeliler', 6135550102, 'deliler.jeliler@email.com', 'Female', '1995-08-23'),
('Noah', 'Wilson', 6135550104, 'noah.wilson@email.com', 'Male', '1992-11-30'),
('Ava', 'Martin', 6135550105, 'ava.martin@email.com', 'Female', '1999-06-05'),
('Lucas', 'Taylor', 6135550106, 'lucas.taylor@email.com', 'Male', '1997-03-18'),
('Sophia', 'Anderson', 6135550107, 'sophia.anderson@email.com', 'Female', '2001-09-22'),
('Ethan', 'Thomas', 6135550108, 'ethan.thomas@email.com', 'Male', '1994-12-10'),
('Isabella', 'Jackson', 6135550109, 'isabella.jackson@email.com', 'Female', '1996-07-14'),
('James', 'White', 6135550110, 'james.white@email.com', 'Male', '2002-02-28');

INSERT INTO Trainer (FirstName, LastName)
VALUES
('Mstin', 'Oops'),
('Zang', 'Zang'),
('Oliver', 'Walker'),
('Charlotte', 'Harris');

INSERT INTO Administrator (FirstName, LastName)
VALUES
('Moper', 'Copps'),
('Henry', 'Clark'),
('Amelia', 'Hall');

INSERT INTO Room (RoomName)
VALUES
('Main Fitness Studio'),
('Yoga Studio'),
('Cycling Room'),
('Strength Training Room');

INSERT INTO FitnessGoal (MemberID, GoalType, TargetValue)
VALUES
(1, 'Weight Loss (kg)', 5),
(1, 'Running Distance (km)', 10),
(2, 'Bench Press (kg)', 100),
(3, 'Weight Loss (kg)', 8),
(4, 'Body Weight (kg)', 85),
(5, 'Running Distance (km)', 5),
(6, 'Squat (kg)', 120),
(7, 'Daily Steps', 10000),
(8, 'Bench Press (kg)', 90),
(9, 'Body Weight (kg)', 60),
(10, 'Running Distance (km)', 15);

INSERT INTO PersonalSession (MemberID, TrainerID)
VALUES
(1, 1),
(2, 2),
(3, 1),
(4, 3),
(5, 2),
(6, 4),
(7, 3),
(8, 1),
(9, 4),
(10, 2),
(1, 3),
(5, 1);

INSERT INTO TrainerAvailability (TrainerID, AvailabilityDate, StartTime, EndTime)
VALUES
(1, '2026-12-01', '08:00', '12:00'),
(1, '2026-12-01', '13:00', '17:00'),
(2, '2026-12-01', '09:00', '15:00'),
(3, '2026-12-01', '10:00', '18:00'),
(4, '2026-12-01', '07:00', '11:00'),
(1, '2026-12-02', '08:00', '16:00'),
(2, '2026-12-02', '12:00', '18:00'),
(3, '2026-12-02', '08:00', '14:00'),
(4, '2026-12-02', '09:00', '17:00');

INSERT INTO RoomBooking (RoomID, BookingDate, StartTime, EndTime)
VALUES
(1, '2026-12-01', '09:00', '10:00'),
(2, '2026-12-01', '10:00', '11:00'),
(3, '2026-12-01', '12:00', '13:00'),
(4, '2026-12-01', '14:00', '15:30'),
(1, '2026-12-02', '08:00', '09:00'),
(2, '2026-12-02', '11:00', '12:00'),
(3, '2026-12-02', '13:00', '14:00'),
(4, '2026-12-02', '15:00', '16:00'),
(1, '2026-12-03', '10:00', '11:00');

INSERT INTO Manages (AdministratorID, BookingID)
VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(1, 6),
(2, 7),
(3, 8),
(1, 9);

INSERT INTO HealthMetric (MemberID, HeightMetric, WeightMetric, HeartRate, BloodPressure)
VALUES
(1, 165, 62.5, 72, 118),
(2, 180, 82.0, 68, 120),
(3, 170, 70.5, 75, 115),
(4, 185, 90.0, 65, 125),
(5, 160, 58.0, 80, 110),
(6, 178, 76.5, 70, 122),
(7, 168, 64.0, 74, 116),
(8, 182, 85.0, 67, 128),
(9, 163, 59.5, 78, 112),
(10, 175, 73.0, 71, 119);

INSERT INTO GroupClass (TrainerID, AdministratorID, ClassName, ClassDate, StartTime, EndTime, Capacity)
VALUES
(1, 1, 'Morning HIIT', '2026-12-01', '08:00', '09:00', 20),
(2, 1, 'Yoga for Beginners', '2026-12-01', '10:00', '11:00', 15),
(3, 2, 'Indoor Cycling', '2026-12-01', '12:00', '13:00', 25),
(4, 2, 'Strength Training', '2026-12-01', '14:00', '15:00', 20),
(1, 3, 'Advanced HIIT', '2026-12-02', '09:00', '10:00', 15),
(2, 3, 'Evening Yoga', '2026-12-02', '17:00', '18:00', 18),
(3, 1, 'Cardio Blast', '2026-12-02', '11:00', '12:00', 20),
(4, 2, 'Full Body Workout', '2026-12-03', '15:00', '16:00', 20);

INSERT INTO RegistersFor (MemberID, ClassID)
VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 2),
(6, 2),
(7, 3),
(8, 3),
(9, 3),
(10, 4),
(1, 4),
(2, 5),
(3, 5),
(4, 5),
(5, 6),
(6, 6),
(7, 7),
(8, 7),
(9, 8),
(10, 8);
