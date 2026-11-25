
from connect import connection
from member import Member


def main():
    try:
        while True:
            print("\n========== FITNESS SYSTEM ==========")
            print("1. Login")
            print("2. Register")
            print("3. Exit")

            choice = input("\nChoose an option: ")
            if choice == "1":
                member = login_ui()
                if member:
                    member_menu(member)
            elif choice == "2":
                member = register_ui()
                if member:
                    member_menu(member)
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
    finally:
        connection.close()


def member_menu(member):
    while True:
        print("\n========== MEMBER MENU ==========")
        print("1. View Dashboard")
        print("2. Update Profile")
        print("3. Add Fitness Goal")
        print("4. Add Health Metrics")
        print("5. View Health History")
        print("6. Logout")

        choice = input("\nChoose an option: ")
        if choice == "1":
            dashboard_ui(member)
        elif choice == "2":
            profile_ui(member)
        elif choice == "3":
            goal_ui(member)
        elif choice == "4":
            health_ui(member)
        elif choice == "5":
            health_history_ui(member)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")


def register_ui():
    print("\n--- MEMBER REGISTRATION ---")
    first = input("First name: ")
    last = input("Last name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    gender = input("Gender: ")
    dob = input("Date of birth (YYYY-MM-DD): ")

    try:
        member = Member.register(first, last, phone, email, gender, dob)
        print("\nRegistration successful!")
        print(f"Welcome, {member.first_name}!")
        return member
    except Exception as e:
        print(f"\nRegistration failed: {e}")
        return None


def login_ui():
    print("\n--- MEMBER LOGIN ---")
    email = input("Email: ")
    member = Member.login(email)

    if member:
        print(f"\nWelcome back, {member.first_name}!")
        return member

    print("\nInvalid email or password.")
    return None


def profile_ui(member):
    print("\n--- UPDATE PROFILE ---")
    first = input("First name: ")
    last = input("Last name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    gender = input("Gender: ")
    dob = input("Date of birth (YYYY-MM-DD): ")

    try:
        member.update_profile(first, last, phone, email, gender, dob)
        print("Profile updated successfully!")
    except Exception as e:
        print(f"Profile update failed: {e}")


def goal_ui(member):
    print("\n--- ADD FITNESS GOAL ---")
    goal_type = input("Goal type (e.g. Target Weight): ")
    target = float(input("Target value: "))

    try:
        member.add_goal(goal_type, target)
        print("Fitness goal added successfully!")
    except Exception as e:
        print(f"Could not add goal: {e}")


def health_ui(member):
    print("\n--- ADD HEALTH METRICS ---")
    height = input("Height (leave blank to skip): ")
    weight = input("Weight (leave blank to skip): ")
    heart_rate = input("Heart rate (leave blank to skip): ")
    blood_pressure = input("Blood pressure (leave blank to skip): ")

    try:
        member.add_health_metric(
            height=float(height) if height else None,
            weight=float(weight) if weight else None,
            heart_rate=float(heart_rate) if heart_rate else None,
            blood_pressure=float(blood_pressure) if blood_pressure else None
        )
        print("Health metrics saved successfully!")
    except Exception as e:
        print(f"Could not save health metrics: {e}")


def health_history_ui(member):
    print("\n--- HEALTH HISTORY ---")

    history = member.get_health_history()

    if not history:
        print("No health records found.")
        return

    for record in history:
        height, weight, heart_rate, bp, created_at = record
        print(f"\nDate: {created_at}")
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Heart Rate: {heart_rate}")
        print(f"Blood Pressure: {bp}")


def dashboard_ui(member):
    print("\n========== MEMBER DASHBOARD ==========")
    print(f"Welcome, {member.first_name} {member.last_name}!")

    dashboard = member.get_dashboard()

    # Latest health metrics
    print("\n--- LATEST HEALTH STATISTICS ---")
    metrics = dashboard["latest_metrics"]
    if metrics:
        height, weight, heart_rate, bp, created_at = metrics
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Heart Rate: {heart_rate}")
        print(f"Blood Pressure: {bp}")
        print(f"Last updated: {created_at}")
    else:
        print("No health metrics recorded.")

    # Fitness goals
    print("\n--- FITNESS GOALS ---")
    goals = dashboard["goals"]
    if goals:
        for goal_type, target in goals:
            print(f"{goal_type}: {target}")
    else:
        print("No fitness goals set.")

    # Past classes
    print("\n--- CLASS HISTORY ---")
    print(f"Past classes attended: {dashboard['past_classes']}")

    # Upcoming sessions
    print("\n--- UPCOMING SESSIONS ---")
    sessions = dashboard["upcoming_sessions"]
    if sessions:
        for name, date, start, end in sessions:
            print(f"{name} | {date} | {start} - {end}")
    else:
        print("No upcoming sessions.")

    print("\n======================================")


if __name__ == "__main__":
    main()
