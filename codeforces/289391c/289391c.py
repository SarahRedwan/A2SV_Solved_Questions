import sys
sys.setrecursionlimit(1 << 25)
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n+1)

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def Union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)

        if rootx==rooty:
            return 
        if self.size[rootx]>self.size[rooty]:
            self.parent[rooty]=rootx
            self.size[rootx]+=self.size[rooty]
        else:
            self.parent[rootx]=rooty
            self.size[rooty]+=self.size[rootx]

n,q=map(int,input().split())
dsu=DSU(n)
nxt=list(range(n+2))

def get_nxt(x):
    if nxt[x]!=x:
        nxt[x]=get_nxt(nxt[x])
    return nxt[x]
    
for _ in range(q):
    t,x,y=map(int,input().split())

    if t==1:
        dsu.Union(x,y)
    elif t==2:
        curr=get_nxt(x)

        while curr<y:
            dsu.Union(curr,curr+1)
            nxt[curr]=get_nxt(curr+1)
            curr=get_nxt(curr)
    else:
        if dsu.find(x)==dsu.find(y):
            print("YES")
        else:
            print("NO")