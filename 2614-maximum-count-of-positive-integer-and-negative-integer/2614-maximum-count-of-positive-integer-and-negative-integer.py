class Solution:
    def maximumCount(self, nums):
        positiveCount = len(nums) - self.upper_bound(nums)
        negativeCount = self.lower_bound(nums)
        return max(positiveCount, negativeCount)

    def lower_bound(self, nums): 
        low = 0
        high = len(nums) - 1
        index = len(nums)
        while low <=high:
            mid = (high + low) // 2
            if nums[mid] < 0:
                low = mid + 1
            else:
                high = mid - 1
                index = mid
        return index

    def upper_bound(self, nums): 
        low = 0
        high = len(nums) - 1
        index = len(nums)
        while low <=high:
            mid = (high + low) // 2
            if nums[mid] <= 0:
                low = mid + 1
            else:
                high = mid - 1
                index = mid
        return index