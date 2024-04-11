import time
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_BST(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_BST(root.left, val)
        else:
            root.right = insert_into_BST(root.right, val)
        return root

def dfs(root):
        if root:
            dfs(root.left)
            dfs(root.right)

def bfs(root):
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

with open('File.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

target_number = 94067

root = None
for number in numbers:
    root = insert_into_BST(root, number)

start_time = time.time()
dfs(root)
dfs_time = (time.time() - start_time) * 1_000_000  # convert to microseconds
print(f'DFS Time Complexity: {dfs_time:.2f} microseconds')

start_time = time.time()
bfs(root)
bfs_time = (time.time() - start_time) * 1_000_000  # convert to microseconds
print(f'BFS Time Complexity: {bfs_time:.2f} microseconds')

