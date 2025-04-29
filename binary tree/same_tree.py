# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      #both trees are empty  
        if p is None and q is None: 
            return True
        #Trees are not the same so False
        if p is None or q is None:
            return False
        #Recursively check left and right subtrees, if they match exactly then it will return True
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
#Time Complexity: O(n) - will visit every node once
#Space Complexity: O(n) or O(log n)

  
