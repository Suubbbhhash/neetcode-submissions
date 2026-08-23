class Solution:
    def decodeString(self, s: str) -> str:
       string_stack=[]
       count_stack=[]
       st=""
       c=0
       for ch in s:
            if ch.isdigit():
                c=c*10+int(ch)
            elif ch=="[":
                string_stack.append(st)
                count_stack.append(c)
                st=""
                c=0
            elif ch=="]":
                temp=st
                count=count_stack.pop()
                st=string_stack.pop()
                st += temp * count
            else:
                st+=ch
       return st 