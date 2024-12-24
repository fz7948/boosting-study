n = int(input())
cust = list(map(int, input().split()))
ldr, mbr = list(map(int, input().split()))
import math
cust = list(map(lambda x: math.ceil(max(x - ldr, 0) / mbr), cust))

print(sum(cust)+n)