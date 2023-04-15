"""
Name: Saloni Sanger
Class: CPSC3400
Professor: Eric Larson
Purpose: Use Python lists to implement BST.
"""

#use python list to store binary search tree of integers
#a tree consists of a single list with either 3 elements [value of root, node, left subtree, right subtree]
#or zero elements [] representing an empty tree
#[value of root, node, left subtree, right subtree] uses NESTED LISTS: left and right subtree are lists

import collections
import sys

def insert(tree, value):
    if not tree: #if root is NULL
        return [value, [], []]
    else:
        if tree[0] != value: #did not find dupe
            if tree[0] < value: #if value greater then root search right, if not search left
                tree[2] = insert(tree[2], value)
            else:
                tree[1] = insert(tree[1], value)
        else:
            print("Duplicate value detected: " + str(value))
    return tree
    #insert value into the tree
    #resulting tree does not need to be balanced
    #if value is already in the tree, do not add entry and throw DuplicateEntry exception
    #must create DuplicateEntry exception
    #return tree with value inserted

def search(tree, value):
    #base case if root is null, didn't find value
    if not tree:
        return False
    #base case value found
    if tree[0] == value:
        return True
    #if value bigger than this root search right, otherwise search left
    if tree[0] < value:
        return search(tree[2], value)
    return search(tree[1], value)
    
    #returns true if the value is in the tree and false otherwise

def inorder(tree):
    if tree:
        yield from inorder(tree[1])
        yield tree[0]
        yield from inorder(tree[2])
    #does inorder traversal of the nodes
    #MUST implement using generator function, it yields the next node in the traversal
    #if you use recursive function (recommended) you need to use "yield from" when 
    #calling inorder recursively. 
    #non-recursive function is allowed

def heights(tree): #uses breadth-first search
    heightDict = {}
    height = 0
    queue = collections.deque() #deque is a doubler ended queue (can add/take from either end)
    if not tree: #if tree has no nodes
        return heightDict
    
    queue.append(tree)

    while queue:
        currSize = len(queue)
        #while queue is not empty
        while currSize > 0:
            #pop elements 1 by 1
            currNode = queue.popleft()
            currSize -= 1

            #check if node is not NULL
            if currNode:
                #for each element popped, add its value, height pair to the dict
                heightDict[currNode[0]] = height

                #check if left/right children exist
                if currNode[1] is not []:
                    queue.append(currNode[1])
                if currNode[2] is not []:
                    queue.append(currNode[2])
        #increment height when currSize = 0
        height += 1

    return heightDict
    #creates a dictionary where there is an entry for each node in the tree
    #the key is the node value, value is height of that node. 
    #height is 0 for the root and the number of edges the node is away from the root
    #for all other nodes

def createTree(tree, fileName):
    file = open(fileName)
    for line in file:
        if (line[-1] == "\n"):
            line = line[:-1] #exclude the newline at the end
        # print(line.isdigit()) #test
        if line.isdigit():
            tree = insert(tree, (int)(line))
        else:
            print("Invalid line: " + line)
    return tree

# DRIVER
tree = []
tree = createTree(tree, sys.argv[1])
print("Step 3:")
print(tree)
print("Step 4:")
for num in range(1, 10):
    present = search(tree, num)
    if present:
        print(str(num) + " YES")
    else:
        print(str(num) + " NO")

print("Step 5:")
for x in inorder(tree):
    print(x)
print("Step 6:")
inorderList = [x for x in inorder(tree)]
print(inorderList)
print("Step 7:")
heightDict = heights(tree)
print(heightDict)
print("Step 8:")
print(max(heightDict.values()))







