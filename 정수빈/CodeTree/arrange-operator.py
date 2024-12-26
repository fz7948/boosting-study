n = int(input())
nums = list(map(int, input().split()))
plus, minus, mulitple = list(map(int, input().split()))


min_value = float("inf")
max_value = -float("inf")

def bk(idx, plus, minus, mulitple, total):
    global min_value, max_value
    if idx == n-1:
        min_value = min(min_value, total)
        max_value = max(max_value, total)
        return total

    if plus > 0:
        bk(idx+1, plus-1, minus, mulitple, total + nums[idx+1])
    if minus > 0:
        bk(idx+1, plus, minus-1, mulitple, total - nums[idx+1])
    if mulitple > 0:
        bk(idx+1, plus, minus, mulitple-1, total * nums[idx+1])


bk(0, plus, minus, mulitple, nums[0])
print(min_value, max_value)