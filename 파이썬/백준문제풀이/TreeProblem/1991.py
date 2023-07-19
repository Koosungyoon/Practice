#트리 순회 문제

import sys
LEFT = 0
RIGHT = 1

N = int(sys.stdin.readline().strip())
tree = {}
for _ in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

#root - left - right
def preorder(root): 
    if root != '.':
        print(root,end = '')
        preorder(tree[root][LEFT])
        preorder(tree[root][RIGHT])

#left - root - right
def innerorder(root):
    if root != '.':
        innerorder(tree[root][LEFT])
        print(root,end = '')
        innerorder(tree[root][RIGHT])

#letf - right - root
def postorder(root):
    if root != '.':
        postorder(tree[root][LEFT])
        postorder(tree[root][RIGHT])
        print(root,end = '')

preorder("A")
print()
innerorder("A")
print()
postorder("A")