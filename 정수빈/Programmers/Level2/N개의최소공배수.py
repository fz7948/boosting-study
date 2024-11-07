# https://school.programmers.co.kr/learn/courses/30/lessons/12953
# 설명: 유클리드 호제법을 이용하여 최소공배수를 구하는 문제입니다.
# 앞의 두 수를 먼저 최대공약수를 구하고 그 수를 이용하여 다음 수와 최대공약수를 구하면 최소공배수를 구할 수 있습니다.


def gcd(a, b):
    while b > 0:
        a, b = b, a%b 
    return a

def solution(arr):
    b = 1
    for n in arr:
        a = n
        b = (a * b) // gcd(a, b)
    return b