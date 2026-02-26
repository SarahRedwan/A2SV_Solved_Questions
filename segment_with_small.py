n,s=map(int,input().split())
arr=list(map(int,input().split()))
curr_sum=0
max_len=0
left=0
for right in range(n):
    curr_sum+=arr[right]

    if curr_sum>s:
        curr_sum-=arr[left]
        left+=1
max_len=max(max_len,right-left+1)
print(max_len) 
