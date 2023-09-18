import random

def estimate_pi(n):
    point_in_circle = 0
    point_in_total = 0

    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)

        distane = x**2 + y**2
        if distane <= 1:
            point_in_circle += 1
        point_in_total += 1

    return float(4*(point_in_circle/point_in_total))

n = input("number of points: ")
result = estimate_pi(int(n))
print(result)