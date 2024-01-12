# leetcode 98

def isValidBST(self, root):
    def check(root, l_boundary, r_boundary):
        if not root:
            return True
        elif l_boundary <  root.val < r_boundary:
            return check(root.left, l_boundary, root.val) and check(root.right, root.val, r_boundary)
        else:
            return False
        
    check(root, -float('inf'), float('int'))