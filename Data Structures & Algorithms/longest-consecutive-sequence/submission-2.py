class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_numbers = set()
        for num in nums:
            set_of_numbers.add(num)
        
        longest_sequence = 0
        seen_numbers = set()
        for num in set_of_numbers:
            if num in seen_numbers:
                continue
            else:
                seen_numbers.add(num)

            current_sequence = 1
            while num+1 in set_of_numbers:
                seen_numbers.add(num+1)
                current_sequence = current_sequence + 1
                num = num+1

            longest_sequence = max(current_sequence, longest_sequence)

        return longest_sequence