class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def callAndGen(text, lCount, rCount):
            if lCount > n:
                return
            if lCount == n and rCount == n:
                results.append(text)
                return
            
            if rCount < lCount:
                callAndGen(text+")", lCount, rCount+1)
            
            callAndGen(text+"(", lCount+1, rCount)
        
        callAndGen("", 0, 0)
        return results