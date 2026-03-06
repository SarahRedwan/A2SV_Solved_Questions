t=int(input())
for _ in range(t):
    s=input().strip()
    left=0
    res=set()
    while left<len(s):
        right=left+1
        if  right>=len(s):
            res.add(s[left])
            left+=1 
        elif s[left]==s[right] :
            left+=2
        else:
            res.add(s[left])
            left+=1

    print("".join(sorted(res)))