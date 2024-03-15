# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        root = self.recursion(root)
        return self.result if root else []  
    
    def recursion(self, root):
        if root:
            self.recursion(root.left)
            self.result.append(root.val)
            self.recursion(root.right)
        return root
    