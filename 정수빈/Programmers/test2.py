import math

def distance(x ,y):
    return math.sqrt(x**2 + y**2)

def solution(x, y, r, d, target=[]):
    
    in_target = []
    count = 0

    for t in target:
        if distance(t[0] ,t[1]) <= r:
            in_target.append(t)

    d = math.radians(d)
    for it in in_target:
        cos = (x * it[0] + y * it[1]) / (distance(x ,y) * distance(it[0],it[1]))
        if math.acos(cos) <= d:
            count += 1
    return count


                    

print(solution(-1, 2, 2, 60, [[0, 1], [-1, 1], [1, 0], [-2, 2]]),2)