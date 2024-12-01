# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def levelorder(root,main_l=None):
            if not main_l:
                main_l = []
            stack=[root]
            main_l.append(root.val)
            while stack:
                current = stack.pop(0)
                if current.left:
                    stack.append(current.left)
                    main_l.append(current.left.val)

                else:
                    main_l.append(None)

                if current.right:
                    stack.append(current.right)
                    main_l.append(current.right.val)
                else:
                    main_l.append(None)
            
          
            print(main_l)
            return main_l
        if p==q:
            return True
        if p and q:
            return levelorder(p) == levelorder(q) 
        if p or q:
            return False
        

