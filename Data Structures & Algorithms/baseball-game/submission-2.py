class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        
        for i in range(len(operations)):
                
            if operations[i]=="C":
                res.pop()
                
            elif operations[i]=="D":
                p=res.pop()
                pp=p*2
                res.append(p)
                res.append(pp)
                
            elif operations[i]=="+":
                a=res.pop()
                b=res.pop()
                c=a+b
                res.append(b)
                res.append(a)
                res.append(c)
                
            else:
                res.append(int(operations[i]))
                
        r=sum(res)
        return r