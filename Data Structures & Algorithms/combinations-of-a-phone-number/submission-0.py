class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='':
            return []
        res,sol=[],[]
        digits_rack={'2':'abc','3':'edf','4':'ghi','5':'jkl','6':
        'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        n=len(digits)
        def backtrack(i):
            if i==n:
                res.append(''.join(sol))
                return
            for digit in digits_rack[digits[i]]:
                sol.append(digit)
                backtrack(i+1)
                sol.pop()
        backtrack(0)
        return res