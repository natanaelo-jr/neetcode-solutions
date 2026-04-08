class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        indexes = {}
        for index, c in enumerate(s):
            if c not in indexes:
                indexes[c] = 0
        
        for i, c in enumerate(s):
            for unique_char in indexes:
                actual_k = k
                actual_i = i
                current_length = 0
                while actual_i < len(s):
                    if s[actual_i] != unique_char:
                        actual_k -= 1
                    actual_i += 1
                    current_length += 1
                    if actual_k < 0:
                        break
                    indexes[c] = max(current_length, indexes[c])
                    
        result = 0
        for c in indexes:
            result = max(indexes[c], result)
        return result


