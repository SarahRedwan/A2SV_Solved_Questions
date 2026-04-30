from collections import deque


def solve():
    n=int(input())
    names=[input().strip() for _ in range(n)]

    graph=[[] for _ in range(26)]
    indegree=[0]*26
    

    for i in range(n-1):
        a=names[i]
        b=names[i+1]
        minlen=min(len(a),len(b))
        found=False

        for j in range(minlen):
            if a[j]!=b[j]:
                u,v=ord(a[j])-ord('a'),ord(b[j])-ord('a')
                graph[u].append(v)
                indegree[v]+=1
                found=True
                break
        if not found and len(a)>len(b):
            print("Impossible")
            return
    queue=deque([i for i in range(26) if indegree[i]==0])
    order=[]
    
    while queue:
        u=queue.popleft()
        order.append(u)

        for v in graph[u]:
            indegree[v]-=1

            if indegree[v]==0:
                queue.append(v)
        
    if len(order)!=26:
            print("Impossible")
    else:
        alphabat=''.join(chr(i+ord('a')) for i in order)
        print(alphabat)
solve()