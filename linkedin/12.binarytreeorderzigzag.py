# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # ! corner
        if root == None:
            return []
        # initialize extendable lists (or use len of nodes)
        # discovered = [1]
        dist = [0]
        queue = [root]
        result = list()
        cd, cl = 0, list()
        while queue != []:
            d = dist.pop(0)
            if d % 2 == 1:
                u = queue.pop()
                if u.right is not None:
                    queue.insert(0, u.right)
                    dist.append(d + 1)
                if u.left is not None:
                    queue.insert(0, u.left)
                    dist.append(d + 1)
            else:  # right, left
                u = queue.pop(0)
                if u.left is not None:
                    queue.append(u.left)
                    dist.append(d + 1)
                if u.right is not None:
                    queue.append(u.right)
                    dist.append(d + 1)
            # print
            if d > cd:
                result.append(cl)
                cd = d
                cl = list()
            cl.append(u.val)  # ! always do
        # ! final list
        result.append(cl)
        # result
        return result