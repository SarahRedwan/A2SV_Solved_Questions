n = int(input())
a = list(map(int, input().split()))
    
a.sort()
    
day = 0
for x in a:
    if x >= day + 1:
        day += 1
    
print(day)