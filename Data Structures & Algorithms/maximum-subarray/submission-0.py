class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for i, num in enumerate(nums):
            if num > current_sum + num:
                current_sum = num
            else:
                current_sum += num
            max_sum = max(max_sum, current_sum)

        return max_sum