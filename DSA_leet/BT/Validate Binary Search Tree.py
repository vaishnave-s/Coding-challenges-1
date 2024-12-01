# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateBST(current,low=-math.inf,high=math.inf):
            if not current:
                return True
            if current.val<=low or current.val>=high:
                return False
            return validateBST(current.left,low,current.val) and validateBST(current.right,current.val,high) 
        return(validateBST(root))
