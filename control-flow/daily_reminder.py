def main():
    task = input("Enter your task: ")
    priority = input("Enter the task priority (high/medium/low): ").lower()
    time_bound = input("Is it task time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            priority_message = "This is a high-priority task."
        case "medium":
            priority_message = "This is a medium-priority task."
        case "low":
            priority_message = "This is a low-priority task."
        case _:
            print("Invalid priority entered. Defaulting to low priority.")
            priority_message = "This is a low-priority task."

    if time_bound == "yes":
        urgency_message = "that requires immediate attention today!"
    else:
        urgency_message = "You can plan to complete it at your convenience."

    print("\Reminder:")
    print(f"Task: {task}")
    print(priority_message)
    print(urgency_message)

if __name__ == "__main__":
    main()

    