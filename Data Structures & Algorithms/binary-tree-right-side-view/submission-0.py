# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def depth(root,dept):
            if not root:
                return None
            if len(res)==dept:
                res.append([])
            res[dept].append(root.val)
            depth(root.left, dept+1)
            depth(root.right, dept+1)
        depth(root,0)
        r=[]
        for i in range(len(res)):
            r.append(res[i][-1])
        return r
