class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:  # Check if the root is None
            return 0

        sum = 0
        # If current node's value is within the range, add it to the sum.
        if low <= root.val <= high:
            sum += root.val

        # If the current node's value is greater than the lower bound,
        # there may be nodes within range in the left subtree.
        if root.val > low:
            sum += self.rangeSumBST(root.left, low, high)
        
        # If the current node's value is less than the upper bound,
        # there may be nodes within range in the right subtree.
        if root.val < high:
            sum += self.rangeSumBST(root.right, low, high)
        
        return sum
