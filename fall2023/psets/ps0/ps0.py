#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root


class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#


# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Set each node size to 1 to begin with
    v.size = 1
    # Base case is a leaf node - simply return size if no children
    if not v.left and not v.right:
        return v.size
    # Add current node to size calculation
    if v.left:
        v.size += calculate_sizes(v.left)
    if v.right:
        v.size += calculate_sizes(v.right)

    return v.size


#
# Problem 1c
#


# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r):
    total = r.size
    while r:
        left, right = None, None
        if r.left:
            left = r.left.size
        if r.right:
            right = r.right.size
        if left and left > total // 2:
            r = r.left
        elif right and right > total // 2:
            r = r.right
        else:
            return r
    return r
