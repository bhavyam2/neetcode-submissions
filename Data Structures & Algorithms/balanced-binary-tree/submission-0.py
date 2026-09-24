# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node, depth):
            if not node:
                return depth

            left_depth = height(node.left, depth + 1)
            right_depth = height(node.right, depth + 1)

            return max(left_depth, right_depth)

        def check(node):
            if not node:
                return True

            left_height = height(node.left, 0)
            right_height = height(node.right, 0)

            if abs(left_height - right_height) > 1:
                return False

            return check(node.left) and check(node.right)

        return check(root)