class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False
        
        # Buckets will store numbers within range of valueDiff
        buckets = {}
        # Width of each bucket
        width = valueDiff + 1
        
        for i in range(len(nums)):
            # Determine which bucket the current number belongs to
            bucket_id = nums[i] // width
            
            # 1. Check if the current bucket already has a number
            if bucket_id in buckets:
                return True
            
            # 2. Check the neighboring bucket (left)
            if (bucket_id - 1) in buckets and abs(nums[i] - buckets[bucket_id - 1]) <= valueDiff:
                return True
                
            # 3. Check the neighboring bucket (right)
            if (bucket_id + 1) in buckets and abs(nums[i] - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            # Add current number to its bucket
            buckets[bucket_id] = nums[i]
            
            # Maintain the sliding window size of indexDiff
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // width]
                
        return False
