import random


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(random.randint(5, 150))
# level 1
root.right = TreeNode(random.randint(10, 30))
root.left = TreeNode(random.randint(4, 149))
# level 2
root.right.right = TreeNode(random.randint(5, 150))
root.right.left = TreeNode(random.randint(5, 150))
root.left.right = TreeNode(random.randint(5, 150))
root.left.left = TreeNode(random.randint(5, 150))
# lever 3
root.right.right.right = TreeNode(random.randint(5, 150))
root.right.right.left = TreeNode(random.randint(5, 150))
root.right.left.right = TreeNode(random.randint(5, 150))
root.right.left.left = TreeNode(random.randint(5, 150))
root.left.right.right = TreeNode(random.randint(5, 150))
root.left.right.left = TreeNode(random.randint(5, 150))
root.left.left.right = TreeNode(random.randint(5, 150))
root.left.left.left = TreeNode(random.randint(5, 150))
