class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha="".join(char for char in s if char.isalnum())
        alp=alpha.lower()
        i=0
        j=len(alp)-1
        status=True
        while(i<(len(alp)/2)):
            if alp[i]!=alp[j]:
                status=False
            i+=1
            j-=1
        return status
        