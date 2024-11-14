# https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):

    def asteroidCollision(self, asteroids):
        stack = [asteroids.pop(0)]
        while asteroids:
            weight = asteroids.pop(0)
            while True:
                if stack and stack[-1] > 0 and weight < 0:
                    if abs(stack[-1]) < abs(weight):
                        stack.pop()
                    elif abs(stack[-1]) == abs(weight):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(weight)
                    break
        return stack


# print(asteroidCollision(asteroids = [-2,-2,1,-1]), [-2, 2])
print(asteroidCollision(asteroids = [5,10,-5]), [5,10])
print(asteroidCollision(asteroids = [8,-8]), [])
print(asteroidCollision(asteroids = [10,2,-5]), [10])
print(asteroidCollision(asteroids = [10,-2,3,4,-5]), [10])