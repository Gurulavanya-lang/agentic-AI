def temperature_agent(temp, goal=72):
    # Decide
    if temp > goal:
        return "Cool"
    elif temp < goal:
        return "Heat"
    else:
        return "Idle"


temperatures = [90, 65, 72]

for i, temp in enumerate(temperatures, start=1):
    # Observe
    print(f"\nIteration {i}")
    print(f"Observe: Temperature = {temp}°F")

    # Decide
    action = temperature_agent(temp)
    print(f"Decide: {action}")

    # Act
    print(f"Act: {action}")