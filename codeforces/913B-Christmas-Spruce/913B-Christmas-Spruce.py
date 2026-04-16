n=int(input())

child=[[] for _ in range(n+1)]
for i in range(2,n+1):
    p=int(input())
    child[p].append(i)
ok=True
for node in range(1,n+1):
    if len(child[node])==0:
        continue

    leaf_count = 0
    
    for cc in child[node]:
        if len(child[cc]) == 0:
            leaf_count += 1
    
    if leaf_count < 3:
        ok=False
        break
if ok:
    print("Yes")
else:
    print("No")