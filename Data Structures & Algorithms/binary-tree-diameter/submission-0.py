# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0
        self.dfs(root)
        return self.dia

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left=self.dfs(root.left)
        right=self.dfs(root.right)
        self.dia=max(self.dia,left+right)
        return 1+max(left,right)