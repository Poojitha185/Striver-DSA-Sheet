#Time Complexity: O(N²) in the worst case. For each of the N nodes, its position may be searched linearly in the current inorder range. In a skewed tree, these searches can have sizes N, N-1, N-2, ..., resulting in quadratic time.
#Space Complexity: O(H), where H is the height of the constructed binary tree, due to the recursion stack. This becomes O(N) for a skewed tree and O(log N) for a balanced tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    # Builds the tree using the current inorder range.
    def build(
        self,
        preorder,
        inorder,
        in_start,
        in_end
    ):
        if in_start > in_end:
            return None

        # preorder[pre_index] is the root
        # of the current subtree.
        root_value = preorder[self.pre_index]
        self.pre_index += 1

        root = TreeNode(root_value)

        root_index = in_start

        # The root position splits inorder
        # into left and right subtree ranges.
        while (
            root_index <= in_end
            and inorder[root_index] != root_value
        ):
            root_index += 1

        root.left = self.build(
            preorder,
            inorder,
            in_start,
            root_index - 1
        )

        root.right = self.build(
            preorder,
            inorder,
            root_index + 1,
            in_end
        )

        return root

    # Reconstructs the binary tree from
    # preorder and inorder traversals.
    def build_tree(self, preorder, inorder):
        self.pre_index = 0

        return self.build(
            preorder,
            inorder,
            0,
            len(inorder) - 1
        )


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    solution = Solution()

    root = solution.build_tree(
        preorder,
        inorder
    )