# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        current_level = [root]
        while len(current_level):  # sort of bfs
            next_level = []
            for x in current_level:
                if x and x.left:
                    next_level.append(x.left)
                if x and x.right:
                    next_level.append(x.right)
            result.append([x.val for x in current_level if x])
            current_level = next_level
        return result
