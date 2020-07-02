# inorder, pre order and post order traversal of a tree.
from tree import root

iorder = []


def inorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        iorder.append(root.val)


post = []


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        post.append(root.val)


preord = []


def preorder(root):
    if root:
        preord.append(root.val)
        preorder(root.left)
        preorder(root.right)


inorder(root)
preorder(root)
postorder(root)

print(f'in {iorder} , preorder  {preord} and post {post}')
