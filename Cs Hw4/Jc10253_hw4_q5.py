from LinkedBinaryTree import LinkedBinaryTree
def is_height_balanced(bin_tree):
    def is_subtree_balanced(root):
        if (root is None):
            return (True, 0)
        left_flag, left_height = is_subtree_balanced(root.left)
        right_flag, right_height = is_subtree_balanced(root.right)
        return left_flag and right_flag and abs(left_height - right_height) <= 1, max(left_height, right_height) + 1

    if bin_tree is None: raise Exception("Invalid Tree")
    return is_subtree_balanced(bin_tree.root)[0]
