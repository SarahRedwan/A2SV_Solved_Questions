class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        max_len=0
        count=0
        for right in range(len(nums)):
            while nums[right]==0:
                right+=1
                left+=1

                if nums[right]==1:
                    right+=1
                    count+=1
            max_len=max(max_len,count)
        return max_len
            
            
       
        
