# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recur(node,ans):
    if node!=None:
        if node.left!=None:
            recur(node.left,ans)
        ans.append(node.val)
        if node.right!=None:
            recur(node.right,ans)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        recur(root,ans)
        return ans
        