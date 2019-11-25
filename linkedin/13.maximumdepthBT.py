class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)

        return max(ldepth, rdepth) + 1