class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq=deque()
        maxq=deque()
        left=0
        ans=0
        for right in range(len(nums)):
            while minq and nums[right]<minq[-1]:
                minq.pop()
            minq.append(nums[right])
            while maxq and nums[right]>maxq[-1]:
                maxq.pop()
            maxq.append(nums[right])

            if maxq[0]-minq[0]>limit:
                if nums[left]==minq[0]:
                    minq.popleft()
                if nums[left]==maxq[0]:
                    maxq.popleft()
                left+=1
            ans=max(ans,right-left+1)
        return ans