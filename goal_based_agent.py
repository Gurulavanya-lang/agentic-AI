def goal_based_agent(current_temperature, goal_temperature=72):
    if current_temperature > goal_temperature:
        return "cool"
    elif current_temperature < goal_temperature:
        return "heat"
    else:
        return "idle"


temperatures = [110, 90, 72, 60, 40]

for temp in temperatures:
    action = goal_based_agent(temp)
    print(
        f"Temperature: {temp}F | "
        f"Goal: 72F | "
        f"Action: {action}"
    )