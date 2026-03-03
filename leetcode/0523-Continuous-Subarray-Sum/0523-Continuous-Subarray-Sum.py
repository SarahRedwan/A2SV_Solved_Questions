class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curr=0
        count=0
        freq={0:1}
        for num in nums:
            curr+=num
            if len(nums)>=2 and curr%k==0:
                return True
            freq[curr]=freq.get(curr,0)+1
        else:
            return False