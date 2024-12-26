# https://www.codetree.ai/training-field/frequent-problems/problems/max-of-outsourcing-profit/submissions?page=4&pageSize=20

n = int(input())
projects = []
for _ in range(n):
    projects.append(list(map(int, input().split())))

max_total = 0

def bk(time, idx, total):
    global max_total
    if idx > n-1:
        return

    if idx + projects[idx][0] > n:
        return 
    
    total += projects[idx][1]
    time += projects[idx][0]
    max_total = max(total, max_total)
    t = projects[idx][0]

    for i in range(1, n-idx):        
        if i >= t:
            bk(time, idx+i, total)

for i in range(n):
    bk(0, i, 0)


print(max_total)