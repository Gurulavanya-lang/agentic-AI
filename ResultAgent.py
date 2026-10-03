def result_agent(temp, goal=72, max_iter=10):
    state = {
        "done": False,
        "steps": 0
    }

    for i in range(max_iter):
        if temp == goal:
            state["done"] = True
            return "success", state

        if temp > goal:
            temp -= 1
        else:
            temp += 1

        state["steps"] += 1

    if temp == goal:
        state["done"] = True
        return "success", state
    else:
        return "failure", state


result = result_agent(90)

print("Result:", result)