class Solution:
    def findMin(self, nums: List[int]) -> int: #
        left = 0
        right = len(nums)-1
        center = math.floor((right-left)/2)

        while left != center and right != center:
            if nums[center] > nums[right]:
                left = center
                center = left + math.floor((right-left) /2)
            else:
                right = center
                center = left + math.floor((right-left) /2)
            
        return min(nums[left], nums[right])