# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        self.recursion(root)

        return root

    def recursion(self, root):
        if root:
            root.left, root.right  = root.right, root.left

            self.recursion(root.left)
            self.recursion(root.right)