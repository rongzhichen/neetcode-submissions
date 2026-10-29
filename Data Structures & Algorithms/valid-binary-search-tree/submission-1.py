# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, lower, upper):
            if node is None:
                return True
            if lower< node.val < upper:
                if valid(node.left, lower, min(upper, node.val)) and valid(node.right, max(lower, node.val), upper):
                    return True
                else:
                    return False
            else:
                return False
        
        return(valid(root, -1000000001, 1000000001))
        

        