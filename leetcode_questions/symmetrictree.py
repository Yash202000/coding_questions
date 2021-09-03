# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sym_helper(ltree,rtree):
    if ltree and rtree:
        return (ltree.val == rtree.val) and sym_helper(ltree.left, rtree.right) and sym_helper(ltree.right, rtree.left)
    return ltree is rtree


            
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return sym_helper(root.left, root.right)