import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.insert_recursive(self.root, value)

    def insert_recursive(self, root, value):
        if root is None:
            return Node.Node(value)
        if value < root.value:
            root.leftChild = self.insert_recursive(root.leftChild, value)
        else:
            root.rightChild = self.insert_recursive(root.rightChild, value)
        return root

    def insert_iterative(self, value):
        if self.root is None:
            self.root = Node.Node(value)
            return
        current_node = self.root
        while current_node:
            if value < current_node.value:
                if current_node.leftChild is None:
                    current_node.leftChild = Node.Node(value)
                    return
                else:
                    current_node = current_node.leftChild
            else:
                if current_node.rightChild is None:
                    current_node.rightChild = Node.Node(value)
                    return
                else:
                    current_node = current_node.rightChild

    def search(self, value):
        return self.search_recursive(self.root, value)

    def search_recursive(self, root, value):
        if root is None:
            return f"{value } not found recursively"
        if root.value == value:
            return f"{value} is found recursively"
        elif value < root.value:
            return self.search_recursive(root.leftChild, value)
        else:
            return self.search_recursive(root.rightChild, value)

    def search_iterative(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return f"{value} if found iteratively"
            elif value > current_node.value:
                current_node = current_node.rightChild
            elif value < current_node.value:
                current_node = current_node.leftChild
        else:
            return f"{value} not found iteratively"

    def delete(self, value):
        self.root = self.delete_recursive(self.root, value)

    def delete_recursive(self, root, value):
        if root is None:
            return root
        if value < root.value:
            root.leftChild = self.delete_recursive(root.leftChild, value)
        elif value > root.value:
            root.rightChild = self.delete_recursive(root.rightChild, value)
        else:
            if root.leftChild is None:
                return root.rightChild
            elif root.rightChild is None:
                return root.leftChild

            inorder_successor = self.find_inorder_successor(root.rightChild)
            root.value = inorder_successor.value
            root.rightChild = self.delete_recursive(root.rightChild, inorder_successor.value)

        return root

    def find_inorder_successor(self, node):
        current_node = node
        while current_node.leftChild is not None:
            current_node = current_node.leftChild
        return current_node

    def traversals(self):
        print("Inorder traversal: ")
        self.inorder_traversal(self.root)
        print("\n Preorder traversal: ")
        self.preorder_traversal(self.root)
        print("\n Postorder traversal: ")
        self.postorder_traversal(self.root)

    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.leftChild)
            print(root.value, end=" ")
            self.inorder_traversal(root.rightChild)

    def preorder_traversal(self, root):
        if root is not None:
            print(root.value, end=" ")
            self.preorder_traversal(root.leftChild)
            self.preorder_traversal(root.rightChild)

    def postorder_traversal(self, root):
        if root is not None:
            self.postorder_traversal(root.leftChild)
            self.postorder_traversal(root.rightChild)
            print(root.value, end=" ")




