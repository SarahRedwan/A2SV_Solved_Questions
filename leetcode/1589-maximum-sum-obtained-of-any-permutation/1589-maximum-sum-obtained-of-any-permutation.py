class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        freq=[0]*(n+1)

        for s,e in requests:
            freq[s]+=1
            freq[e+1]-=1
        for i in range(1,n):
            freq[i]+=freq[i-1]

        freq=freq[:n]

        nums.sort()
        freq.sort()
        mod=10**9+7
        res=0
        for i in range(n):
            res=(res+nums[i]*freq[i])%mod
        return res

    