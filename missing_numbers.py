class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)+1
        for num in range(n):
            if num not in nums:
                return num
