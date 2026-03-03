n,k=map(int,input().split())
a=list(map(int,input().split()))
freq={}
unique=0
max_len=0
left=0
best_l=0
best_r=0
for r in range(n):
    if a[r] not in freq:
        freq[a[r]]=0
    if freq[a[r]]==0:
        unique+=1
    freq[a[r]]+=1

    while unique>k:
        freq[a[left]]-=1
        if freq[a[left]]==0:
            unique-=1
        left+=1

    if r-left+1>max_len:
        max_len=r-left+1
        best_l=left
        best_r=r
print(best_l+1,best_r+1)