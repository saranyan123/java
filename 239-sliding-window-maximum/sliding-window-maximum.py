from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        
        res = []
        dq = deque()  # Stores indices
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window's range
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # 2. Remove indices of elements smaller than the current element
            # because they will never be the maximum in this or future windows
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # 3. Add current element's index
            dq.append(i)
            
            # 4. Once the first window is full, the max is always at the front
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res
