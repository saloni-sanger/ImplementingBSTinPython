"""
Name: Saloni Sanger
Class: CPSC3400
Professor: Eric Larson
Purpose: Use Python lists to implement BST.
"""

"""
Note:
A tree consists of a single list with either 3 elements 
[value of root, node, left subtree, right subtree]
or zero elements [] representing an empty tree.
Nested lists are used: left and right subtree are lists.
"""

import collections
import sys

"""
insert() notes for technical understanding:
- base case if root is null add node with empry children
- if duplicate entry found raise exception
- otherwise continue search for where to place value
"""

def insert(tree, value):
    if not tree:
        return [value, [], []]
    else:
        class DuplicateEntry(Exception) : pass
        if (tree[0] == value):
            raise DuplicateEntry
        else:
            if tree[0] < value:
                tree[2] = insert(tree[2], value)
            else:
                tree[1] = insert(tree[1], value)
    return tree

"""
search() notes for technical understanding:
- base case root is null, did not find value
- base case value found
- otherwise continue search
"""

def search(tree, value):
    if not tree:
        return False
    if tree[0] == value:
        return True
    if tree[0] < value:
        return search(tree[2], value)
    return search(tree[1], value)

"""
inorder() notes for technical understanding:
- generator function yields traversal values one by one
"""

def inorder(tree):
    if tree:
        yield from inorder(tree[1])
        yield tree[0]
        yield from inorder(tree[2])

"""
heights() notes for technical understanding:
- uses breadth-first search
- deque is a double-ended queue
- if tree has no nodes return empty dictionary
- append root (everything at height 0) to the queue
- while queue is not empty pop elements from the
current height 1 by 1
if popped node is not null:
add its value and height to the dictionary
append left/right children to queue if they exist
- once current level is finished increase height value and 
process next level's queue.
"""

def heights(tree):
    heightDict = {}
    height = 0
    queue = collections.deque()
    if not tree: 
        return heightDict
    
    queue.append(tree)

    while queue:
        currSize = len(queue)
        while currSize > 0:
            currNode = queue.popleft()
            currSize -= 1

            if currNode:
                heightDict[currNode[0]] = height

                if currNode[1] is not []:
                    queue.append(currNode[1])
                if currNode[2] is not []:
                    queue.append(currNode[2])
        height += 1

    return heightDict

"""
createTree() notes for technical understanding:
- when getting line from file in python there is 
a hidden \n charaacter at the end 
(unless it is the last line)
so if it exists, exclude that \n
- if the line is not a single int, raise ValueError
- ValueError raised because the type is correct (str)
but the string value is invalid.
- finally if it was a single int, try to insert it 
into the tree, if it's a dupliate entry print error
message.
"""

def createTree(tree, fileName):
    file = open(fileName)
    for line in file:
        if (line[-1] == "\n"):
            line = line[:-1] 
        try:
            if not line.isdigit():
                raise ValueError
        except ValueError:
            print("Invalid line: " + line)
        finally:
            if line.isdigit():
                try:
                    tree = insert(tree, (int)(line))
                except:
                    print("Duplicate value detected: " + line)
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