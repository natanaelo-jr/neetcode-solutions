class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Criar os arrays
        # Chamar recursivamente
        # Se passa do target retorno
        # Se atinge o target coloco o array numa lista
        # Se chega no fim do array retorno
        results = []
        def callRecursive(current_sum, array):
            if current_sum > target:
                return
            if current_sum == target:
                results.append(array)
                return
            for number in nums:
                new_array = array.copy()
                if len(new_array) > 0 and number < new_array[-1]:
                    continue
                new_array.append(number)
                
                callRecursive(current_sum+number, new_array)

        callRecursive(0, [])
        return results


