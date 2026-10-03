def temperature_agent(temp):
    goal = 72

    while temp != goal:
        if temp > goal:
            temp -= 1
            print("Cooling... Temperature:", temp)
        else:
            temp += 1
            print("Heating... Temperature:", temp)

    print("Goal reached! Temperature is", temp)


temperature_agent(75)