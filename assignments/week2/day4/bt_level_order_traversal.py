# level order traversal
# BFS
# queue: [ 3 ]
# level:
# level_order: 

from collections import deque


def levelOrder(self,root):
    # time: O(n), n is num of nodes
    # space: O(n), n is the num of nodes
    q = deque()

    if root:
        q.append(root)
    
    level_order = [ ]
    
    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        level_order.append(level)

    return level_order

