from connect import connection

# Member class.

class Member:
    def __init__(self, member_id, first_name, last_name, email):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @staticmethod
    def register(first_name, last_name, phone, email, gender, dob):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Member
                    (FirstName, LastName, PhoneNumber, Email, Gender, DateOfBirth)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING MemberID""", 
                    (first_name, last_name, phone, email, gender, dob)
                )
                member_id = cursor.fetchone()[0]

            connection.commit()
            return Member(member_id, first_name, last_name, email)
        except Exception:
            connection.rollback()
            raise

    @staticmethod
    def login(email):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT MemberID, FirstName, LastName, Email
                FROM Member
                WHERE Email = %s""", 
                (email,)
            )
            result = cursor.fetchone()

        if result is None:
            return None
        member_id, first, last, email = result
        return Member(member_id, first, last, email)

    def update_profile(self, first_name, last_name, phone, email, gender, dob):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE Member
                    SET FirstName = %s,
                        LastName = %s,
                        PhoneNumber = %s,
                        Email = %s,
                        Gender = %s,
                        DateOfBirth = %s
                    WHERE MemberID = %s""",
                    (first_name, last_name, phone, email, gender, dob, self.member_id)
                )

            connection.commit()
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
        except Exception:
            connection.rollback()
            raise

    def add_goal(self, goal_type, target_value):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO FitnessGoal
                    (MemberID, GoalType, TargetValue)
                    VALUES (%s, %s, %s)""", 
                    (self.member_id, goal_type, target_value)
                )

            connection.commit()
        except Exception:
            connection.rollback()
            raise

    def add_health_metric(self, height=None, weight=None, heart_rate=None, blood_pressure=None):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO HealthMetric
                    (MemberID, HeightMetric, WeightMetric, HeartRate, BloodPressure)
                    VALUES (%s, %s, %s, %s, %s)""", 
                    (self.member_id, height, weight, heart_rate, blood_pressure)
                )

            connection.commit()

        except Exception:
            connection.rollback()
            raise

    def get_health_history(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT HeightMetric, WeightMetric, HeartRate, BloodPressure, CreatedAt
                FROM HealthMetric
                WHERE MemberID = %s
                ORDER BY CreatedAt DESC, MetricID DESC""", 
                (self.member_id,)
            )
            return cursor.fetchall()

    def get_dashboard(self):
        with connection.cursor() as cursor:
            # Latest health metrics
            cursor.execute("""
                SELECT HeightMetric, WeightMetric, HeartRate, BloodPressure, CreatedAt
                FROM HealthMetric
                WHERE MemberID = %s
                ORDER BY CreatedAt DESC, MetricID DESC
                LIMIT 1""", 
                (self.member_id,)
            )
            latest_metrics = cursor.fetchone()

            # Fitness goals
            cursor.execute("""
                SELECT GoalType, TargetValue
                FROM FitnessGoal
                WHERE MemberID = %s
                ORDER BY GoalID DESC""", 
                (self.member_id,)
            )
            goals = cursor.fetchall()

            # Number of past group classes
            cursor.execute("""
                SELECT COUNT(*)
                FROM RegistersFor RF
                JOIN GroupClass GC ON RF.ClassID = GC.ClassID
                WHERE RF.MemberID = %s AND GC.ClassDate < CURRENT_DATE""", 
                (self.member_id,)
            )
            past_classes = cursor.fetchone()[0]

            # Upcoming registered group classes
            cursor.execute("""
                SELECT GC.ClassName, GC.ClassDate,
                       GC.StartTime, GC.EndTime
                FROM RegistersFor RF
                JOIN GroupClass GC ON RF.ClassID = GC.ClassID
                WHERE RF.MemberID = %s AND GC.ClassDate >= CURRENT_DATE
                ORDER BY GC.ClassDate, GC.StartTime""", 
                (self.member_id,)
            )
            upcoming_sessions = cursor.fetchall()

        return {
            "latest_metrics": latest_metrics,
            "goals": goals,
            "past_classes": past_classes,
            "upcoming_sessions": upcoming_sessions
        }
