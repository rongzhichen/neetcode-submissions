class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        record = [nums[0]]
        for i in range(1, len(nums)):
            record.append(max(nums[i], nums[i]+record[i-1]))
        return(max(record))
        