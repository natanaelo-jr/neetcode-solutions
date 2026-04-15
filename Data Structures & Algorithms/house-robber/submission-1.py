class Solution:
    def rob(self, nums: List[int]) -> int:
        # posso armazenar o meu valor escolhendo a casa i num vetor de tamanho n e ir crescendo este vetor.
        # alternativamente posso ir armazenando o ótimo atual nesse vetor, onde v[i] = maximo até i (independente das escolhas)
        # prefixos
        # como trato o caso onde pego [...1 0 0 1...] ?
        # como eu quebro o problema em casos base:
            # |v| = 1 -> v[0]
            # |v| = 2 -> max(v[0], v[1])
            # |v| = 3 -> max(v[0] + v[2], v[1])
            # |v| = 4 -> max do caso onde eu escolho max(v[0],).
        # generalizando:
            # v(i) = max(v[i] + v(i+2), v(i+1)) 
        v = [-1] * len(nums);
        N = len(nums) - 1
        def search_solution(v, index):
            if index > N:
                return 0
            if v[index] != -1:
                return v[index]
            solution = max(nums[index] + search_solution(v,index+2), search_solution(v,index+1))
            v[index] = solution
            return solution
        return search_solution(v, 0)