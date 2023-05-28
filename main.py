import BinaryTree


binaryTree = BinaryTree.BinarySearchTree()
root = 5
binaryTree.insert(root)
binaryTree.insert(3)
binaryTree.insert(9)
binaryTree.insert(4)
binaryTree.insert(2)
binaryTree.insert(11)
binaryTree.insert(7)
print(binaryTree.search(11))
print(binaryTree.search(13))
print(binaryTree.search_iterative(11))
print(binaryTree.search_iterative(13))
binaryTree.traversals()