class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = 0
        table = {}

        for i, c in enumerate(s):
            if c not in table:
                current += 1
            elif i - table[c] > current:
                current += 1
            else:
                current = i - table[c]
            print(current)
            table[c] = i
            longest = max(current, longest)

        print(table)
        return longest

