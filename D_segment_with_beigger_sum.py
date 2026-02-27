n,s=map(int,input().split())
a=list(map(int,input().split()))
left=0
total=0
count=0


for right in range(n):
    total+=a[right]

    while total>=s:
        count+=n-right
        total-=a[left]
        left+=1
        

print(count)


        
    
