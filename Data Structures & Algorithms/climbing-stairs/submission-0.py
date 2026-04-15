class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 -> 1
        # 2 -> 1 + 1, 2
        # 3-> |(1+1)+1, (2)+1|, |1 +2|
        # n -> (n-1) + (n-2)
        prefixes = [1, 2]
        for i in range(2, n):
            prefixes.append(prefixes[i-1] + prefixes[i-2])

        return prefixes[n-1]