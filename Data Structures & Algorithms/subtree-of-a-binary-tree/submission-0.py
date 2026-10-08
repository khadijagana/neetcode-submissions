# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree (self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None and subRoot==None:
            return True
        elif root==None and subRoot!=None or root!=None and subRoot==None:
            return False
        elif root.val==subRoot.val:
            bool_left=self.sameTree(root.left, subRoot.left)
            bool_right=self.sameTree(root.right, subRoot.right)
        else:
            return False
        
        return bool_left and bool_right


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        bool1=False
        bool2=False
        bool3=False
        if root is None or subRoot is None: return False
        if root.val == subRoot.val:
            bool1= self.sameTree(root, subRoot)    
        if root!=None and subRoot!=None:
            bool2= self.isSubtree(root.left, subRoot)
            bool3= self.isSubtree(root.right, subRoot)
            return bool1 or bool2 or bool3
        return False    
    
