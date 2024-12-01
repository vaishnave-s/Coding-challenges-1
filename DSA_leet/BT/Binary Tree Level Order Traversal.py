# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        main_l=[]
        def traversal():
            stack=[root]
            
            while stack:
                stack_len = len(stack)
                left_right=[]
                for i in range(stack_len):
                    current_node = stack.pop(0)
                    left_right.append(current_node.val)
                    if current_node.left:
                        stack.append(current_node.left)
                        

                    if current_node.right:
                        stack.append(current_node.right)
                    
                if left_right:
                    print(left_right)
                    main_l.append(left_right)

        if root:
            traversal()
            return(main_l)
        return []
