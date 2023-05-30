import BinaryTree
import Read_from_file
import Write_to_file

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
path = "test.txt"
Write_to_file.write_to_file(binaryTree.root, path)
new_tree = Read_from_file.read_from_file(path)
print("\nNew tree: ")
new_tree.traversals()

