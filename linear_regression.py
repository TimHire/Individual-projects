import numpy as np
import pandas as pd
import random

x_data = [3, 5, 6, 8, 10, 12, 13, 15, 16, 18]
y_data = [36, 50, 53, 61, 69, 79, 82, 90, 88, 96]
data = pd.DataFrame({"x_data": x_data, "y_data": y_data})
print(data)


def cost(data, a, b):         #Assuming the line of regression in form a + bx
    new_gradient = -1 / b
    total, direction, std_dir = 0, 0, []
    matrixA = np.array([[new_gradient, -1], [b, -1]])
    for i in range(len(data)):
        matrixB = np.array([new_gradient * data.x_data[i] - data.y_data[i], -a])
        x_meet, y_meet = np.linalg.solve(matrixA, matrixB)
        distance = ((x_meet - data.x_data[i])**2 + (y_meet - data.y_data[i])**2) ** 0.5
        dir = lambda x: 1 if (x_meet - data.x_data[i]) > 0 else -1
        std_dir.append(dir(i) * distance)
        direction += (x_meet - data.x_data[i])
        total += distance
    return total / len(data), direction / len(data), np.mean(np.array(std_dir[-4:])) - np.mean(np.array(std_dir[:5]))           #np.std(np.array(std_dir))

print(cost(data, 28, -3))
print(cost(data, 28, 3))
print(cost(data, 29.0210157, 3.90367775))
print(cost(data, 4, 9))
print(cost(data, -10, 23))

def neighbour(old_a, old_b, direction, std_grad):
    if direction < 0:
        a = old_a + (random.randint(-10, 100) / 100) * (random.randint(-10, 100) / 100) * (random.randint(-10, 100) / 100) * (random.randint(-10, 100) / 100) * (random.randint(-10, 100) / 100)
    else:
        a = old_a - (random.randint(-100, 100) / 100) * (random.randint(-100, 100) / 100) * (random.randint(-100, 100) / 100) * (random.randint(-100, 100) / 100) * (random.randint(-100, 100) / 100)
    if std_grad > 0:
        b = old_b + (random.randint(-10, 100) / 100) * (random.randint(-10, 100) / 100) * (random.randint(-10, 100) / 100) * (random.randint(-10, 100) / 100) * (random.randint(-10, 100) / 100)
    else:
        b = old_b - (random.randint(-100, 10) / 100) * (random.randint(-100, 10) / 100) * (random.randint(-100, 10) / 100) * (random.randint(-100, 10) / 100) * (random.randint(-100, 10) / 100)
    return a, b


#Need to split of the process one at a time to get the gradient correct first --> lowest difference in length between the first and last points of data


def SA_mine(data, **kwargs):       #where f is the input function and a and b are the bounds between which a solution is looked for
    a_low, a_high, b_low, b_high = kwargs.get("bounds", [None, None, None, None])
    focus = 0.909
    t = 100
    t_min = 1
    best_a, best_b = 0, 0
    while True:
        initial_a, initial_b = random.randint(-10, 10), random.randint(-10, 10)
        if initial_b != 0:
            break
    while t > t_min:
        i = 1
        while i <= 10000:
            c_score, c_dir, c_grad = cost(data, initial_a, initial_b)
            next_a, next_b = neighbour(initial_a, initial_b, c_dir, c_grad)
            n_score, n_dir, n_grad = cost(data, next_a, next_b)
            if n_score <= c_score:
                best_a, best_b = next_a, next_b
            if ((n_score - c_score) / t) > 999:
                if np.exp(999) >= random.randint(0, 10):
                    initial_a, initial_b = next_a, next_b
                else:
                    if np.exp((n_score - c_score) / t) >= random.randint(0,10):
                        initial_a, initial_b = next_a, next_b
            i += 1
            t = t * focus
    return best_a, best_b, cost(data, best_a, best_b)

for i in range(5):
    print(SA_mine(data))