from LinkedBinaryTree import LinkedBinaryTree
def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        if (root.left is None and root.right is None):
            return (root.data, root.data)
        cur_min = root.data
        cur_max = root.data
        min_left = root.data
        max_left = root.data
        min_right = root.data
        max_right = root.data

        if (root.left is not None):
            min_left, max_left = subtree_min_and_max(root.left)
        if (root.right is not None):
            min_right, max_right = subtree_min_and_max(root.right)
        return min([min_left, min_right, root.data]), max([max_left, max_right, root.data])

    if (bin_tree.is_empty()):
        raise Exception("Empty Tree")
    return subtree_min_and_max(bin_tree.root)
