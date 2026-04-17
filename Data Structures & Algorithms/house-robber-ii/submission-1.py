class Solution:
    def rob(self, nums: List[int]) -> int:
        
        N = len(nums)
        v1 = [None] * N
        v2 = [None] * N
        if N == 1:
            return nums[0]
        def dp(index, v, N):
            if index >= N:
                return 0 
            elif v[index] is not None:
                return v[index]
            else:
                v[index] = max(nums[index] + dp(index+2, v, N), dp(index + 1, v, N))
                return v[index]
        result = max(dp(0, v1, N-1), dp(1, v2, N))
        print(v1 , v2)
        return result