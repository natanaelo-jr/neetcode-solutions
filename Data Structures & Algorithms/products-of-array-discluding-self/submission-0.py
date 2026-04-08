class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = list()
        sufixes = list()
        prefixes.append(1)
        sufixes.append(1)
        # 1 1 2 8
        # 1 6 24 48
        for i in range (len(nums) - 1):
            end = len(nums) - 1
            prefixes.append(prefixes[i] * nums[i])
            sufixes.append(sufixes[i] * nums[end-i])
        
        print(prefixes)
        print(sufixes)

        response = list()
        for i in range(len(nums)):
            end = len(nums)-1
            response.append(prefixes[i] * sufixes[end-i])

        return response