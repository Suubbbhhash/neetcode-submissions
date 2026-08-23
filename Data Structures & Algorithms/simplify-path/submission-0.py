class Solution:
    def simplifyPath(self, path: str) -> str:
        res=[]
        for cha in path.split("/"):
            if cha=="" or cha==".":
                continue
            elif cha=="..":
                if res:
                    res.pop()
            else:
                res.append(cha)
        return "/"+"/".join(res)