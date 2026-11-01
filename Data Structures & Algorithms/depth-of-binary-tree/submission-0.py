# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #caso base, se caso nao tenha raiz/não tenha arvore
        if not root:
            return 0


        #verificar filho a esquerda
        depth_left = self.maxDepth(root.left)

        #verificar filho a direita
        depth_right = self.maxDepth(root.right)
        
        
        return 1 + max(depth_left, depth_right)
