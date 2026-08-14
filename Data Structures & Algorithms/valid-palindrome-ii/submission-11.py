class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pal(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        count = 0

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                count += 1

                if count > 1:
                    return False

                if pal(s[i+1:j+1]):
                    i += 1
                elif pal(s[i:j]):
                    j -= 1
                else:
                    return False

        return True