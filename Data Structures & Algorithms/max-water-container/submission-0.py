class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = (right - left) * min(heights[left], heights[right])
        current_area = max_area

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            current_area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, current_area)
        return max_area 


        