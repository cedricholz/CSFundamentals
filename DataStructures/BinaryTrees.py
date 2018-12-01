import queue
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

###############
#     DFS     #
###############

# Root Left Right
def dfs_preorder(root):
    if not root:
        return
    print(root.val)
    if root.left:
        dfs_preorder(root.left)
    if root.right:
        dfs_preorder(root.right)


# Left Root Right
def dfs_inorder(root):
    if not root:
        return
    if root.left:
        dfs_inorder(root.left)
    print(root.val)
    if root.right:
        dfs_inorder(root.right)

# Left Right Root
def dfs_postorder(root):
    if not root:
        return
    if root.left:
        dfs_postorder(root.left)
    if root.right:
        dfs_postorder(root.right)
    print(root.val)

###############
#     BFS     #
###############

def bfs(root):
    if not root:
        return
    q = queue.Queue()

    q.put(root)

    while not q.empty():
        top_item = q.get()
        print(top_item.val)
        if top_item.left:
            q.put(top_item.left)
        if top_item.right:
            q.put(top_item.right)