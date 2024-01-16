# leetcode 230. Kth Smallest Element in a BST
# BST: binary search tree
# for every node

# find the leftmost node first
# remove that node and reduce k by 1
# then add to the stack that node right child

# we use DFS b/c we want to search from bottom to top 
# unlike BFS which search from top to bottom
def k(self, root):
    # depth first search
    stack = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
            # the above gets us to the leftmost element
            root = stack.pop() # this will pop the element in the stack and then reassign root
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    return root

# time: O(n), where n is the num of nodes in BST
# space: O(n), 