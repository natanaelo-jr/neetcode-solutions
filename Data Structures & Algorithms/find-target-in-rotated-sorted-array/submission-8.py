class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums) - 1
        left = 0
        right = N
        mid = (left + right) // 2

        while left < right:
            if nums[mid] < nums[right]:
                right = mid
                mid = (left + right) // 2
            else:
                left = mid+1
                mid = (left + right) // 2
        # No fim o mid vai ser o primeiro elemento após o breakpoint
        # mid = 0 left = 0 right = 0
        if mid == 0:
            left = 0
            right = N
        elif target >= nums[0] and target <= nums[mid-1]:
            left = 0
            right = mid-1
        else:
            left = mid
            right = N

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        while left < right:
            if nums[mid] < target:
                left = mid+1
                mid = (left + right) // 2
            elif nums[mid] > target: 
                right = mid
                mid = (left + right) // 2
            if nums[mid] == target:
                return mid
        
        return -1
