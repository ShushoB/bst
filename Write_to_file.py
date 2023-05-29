import BinaryTree



def write_to_file(root, file_path):
    with open(file_path, 'w') as file:
        _actual_writer(root, file)


def _actual_writer(root, file):
    if root is None:
        file.write('')
    else:
        file.write(str(root.value) + ' ')
        _actual_writer(root.leftChild, file)
        _actual_writer(root.rightChild, file)



