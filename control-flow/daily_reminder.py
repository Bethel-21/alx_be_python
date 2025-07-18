

task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        print("is a high priority")
        if time_bound == "yes":
            print(f"{task} is a {priority} task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} task. Consider completing it when you have free time.")
    case "medium":
        print("is a medium priority")
        if time_bound == "yes":
             print(f"{task} is a {priority} task that requires immediate attention today!")
        else:
             print(f"{task} is a {priority} task. Consider completing it when you have free time.")
    case "low":
        print("is a low priority task")
        if time_bound == "yes":
             print(f"{task} is a {priority} task that requires immediate attention today!")
        else:
             print(f"{task} is a {priority} task. Consider completing it when you have free time.")
    case _:
        print("Incorrect")

