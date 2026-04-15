class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Posso começar do n pra trás e tentar chegar no 0
        # consigo colocar iterativamente os índices que me levam pro fim do array
        # exemplo [1 2 0 1 0]
        # n -> trivial (adiciona n num set)
        # n-1 -> true pois nums[n-1] + n-1 tá no set

        n = len(nums) - 1
        indexes = set()
        indexes.add(n)

        for i in range(1, n+1):
            index = n-i
            max_jump = nums[index]
            for jump in range(1, max_jump+1):
                if index + jump in indexes:
                    indexes.add(index)
                    break
        return True if 0 in indexes else False
