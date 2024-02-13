# 트리순회
'''https://www.acmicpc.net/problem/1991'''

import sys

def preorder_traversal(node):
    if node == ".":
        return ""
    return node + preorder_traversal(tree[node][0]) + preorder_traversal(tree[node][1])
def inorder_traversal(node):
    if node == ".":
        return ""
    return inorder_traversal(tree[node][0]) + node + inorder_traversal(tree[node][1])
def postorder_traversal(node):
    if node == ".":
        return ""
    return postorder_traversal(tree[node][0]) + postorder_traversal(tree[node][1]) +node


try:
    N = int(sys.stdin.readline())

    tree = dict()
    
    for idx in range(N):
        input_data = sys.stdin.readline().rstrip().split(" ")
        tree[input_data[0]] = input_data[1:]
        
    print(preorder_traversal("A"))    
    print(inorder_traversal("A"))
    print(postorder_traversal("A"))
    
except ValueError or IndexError as e:
    print(e)