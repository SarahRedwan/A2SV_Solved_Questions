import sys
input = sys.stdin.readline

n,m=map(int, input().split())

parent=list(range(n + 1))
size=[1]*(n + 1)

exp=[0]*(n+1)
diff=[0]*(n+1)

def find(x):
    if parent[x]==x:
        return x

    p =parent[x]
    root = find(p)

    diff[x]+=diff[p]
    parent[x]=root
    return root


def get_exp(x):
    find(x)
    return diff[x]+exp[parent[x]]


def union(x, y):
    rx = find(x)
    ry = find(y)

    if rx==ry:
        return

    if size[rx] < size[ry]:
        rx, ry=ry, rx

    parent[ry] = rx
    diff[ry]=exp[ry]-exp[rx]

    size[rx]+=size[ry]


for _ in range(m):
    query=input().split()

    if query[0] == "join":
        x=int(query[1])
        y=int(query[2])

        union(x, y)

    elif query[0]=="add":
        x=int(query[1])
        v=int(query[2])

        root=find(x)
        exp[root] += v

    else:
        x=int(query[1])
        print(get_exp(x))