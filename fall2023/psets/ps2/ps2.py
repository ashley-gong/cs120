class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger=None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
        return self._size

    # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    """
    Calculates the size of the tree
    returns the size at a given node
    """

    def calculate_sizes(self, debugger=None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        # self.size += 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    """
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    """

    # Error -> traversing on the right subtree and failing to change index (since only checking left)
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        # print(left_size, ind)
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            # fix is with right subtrees -> must subtract (left_size + 1) from index when checking on right side
            return self.right.select(ind - left_size - 1)
        return None

    """
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    """

    # Correct
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None

    """
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    """

    # Too slow -> O(n) instead of O(h)
    # self.calculate_sizes is O(n) with recursive implementation, but only need
    # to update subtree size when traversing down to find where to place node
    # for calc_sizes, only increment nodes visited in search traversal to insert
    def insert(self, key):
        # print(self.key)
        if self.key is None:
            self.key = key
        else:
            # Increment size of a node visited in search traversal to insert
            self.size += 1
        if self.key > key:
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        # self.calculate_sizes()  # this is O(n) in current implementation
        return self

    ####### Part b #######

    """
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    """

    def getDir(self, node, direction, op):
        if direction == "R":
            if op:
                return node.left
            return node.right
        if direction == "L":
            if op:
                return node.right
            return node.left

    # O(1) to rearrange parent pointers
    # how to main size augmentation invariant
    def rotate(self, direction, child_side):
        if child_side == "R" and direction == "L":
            tree_child = self.right  # equal to child_side
            self.right = tree_child.right  # self.child_side -> tree_child.dirOPP
            tree_child.right = self.right.left  # TC.dirOPP -> self.dirOpp.dir
            self.right.left = tree_child  # self.child_side.dir -> TC
        if child_side == "L" and direction == "L":
            tree_child = self.left
            self.left = tree_child.right
            tree_child.right = self.right.left
            self.left.left = tree_child

        if child_side == "L" and direction == "R":
            tree_child = self.left
            self.left = tree_child.left
            tree_child.left = self.left.right
            self.left.right = tree_child
        if child_side == "R" and direction == "R":
            tree_child = self.right
            self.right = tree_child.left
            tree_child.left = self.left.right
            self.right.right = tree_child

        # tree_child = self.right if child_side == "R" else self.left
        # tc_dirOp = self.getDir(tree_child, direction, True)
        # if child_side == "R":
        #     self.right = tc_dirOp
        # if child_side == "L":
        #     self.left = tc_dirOp
        # tc_dirOp =

        # if child_side == "R":
        #     tree_child = self.right
        # if child_side == "L":
        #     tree_child = self.left

        # if direction == "L":
        #     self.right = tree_child.right
        #     tree_child.right = self.right.left
        #     self.right.left = tree_child
        # if direction == "R":
        #     self.left = tree_child.left
        #     tree_child.left = self.left.right
        #     self.left.right = tree_child

        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print(self.key),
        if self.right is not None:
            self.right.print_bst()
        return self
