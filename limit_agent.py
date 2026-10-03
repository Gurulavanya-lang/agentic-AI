def limit_agent(temp, goal=72, max_iter=10):
    for i in range(max_iter):
        if temp == goal:
            return "success"

        if temp > goal:
            temp -= 1
        else:
            temp += 1

    return "failure"


result = limit_agent(90)

print("Result:", result)