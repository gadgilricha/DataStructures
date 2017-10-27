# final version for class notes

class BinarySearchTree:
    """Implement a Binary Search Tree with a root -- set root to first key value when created"""
    def __init__(self):
        self.root = None
    def insert(self, newkey):
        """Insert new key into BST -- in BST Class, pass key through left or right of root depending on value"""
        if self.root is None:			 
            self.root = TreeNode(newkey)
        else:
            p = self.root
            if p.key > newkey: #if key less than root, pass through left
                if p.left is None:
                    a = TreeNode(newkey)
                    p.left = a
                    a.set_parent(self.root)
                else:   
                    p.left.insert(newkey)
            else:
                if p.right is None:#if key greater than root, pass through right
                    a = TreeNode(newkey)
                    p.right = a
                    a.set_parent(self.root)
                else:
                    p.right.insert(newkey)
    def delete (self, key):
        """Delete node from BST -- adjust rest of nodes accordingly"""
        p = self.root # current root
        if self.find(key):
            while p is not None and p.get_key() != key: #find key node within BST
                if key < p.get_key():
                    p = p.left
                else:
                    p = p.right
            if p.right: #find successor of node, swap successor with node value
                succ = p.get_right()
                while succ.left is not None:
                    succ = succ.left
                key = succ.get_key()
                self.delete(key)
                p.set_key(key)
            elif p.get_left(): #find predeccesor of node, swap pre with node value
                succ = p.get_left()
                while succ.right is not None:
                    succ = succ.right
                key = succ.get_key()
                self.delete(key)
                p.set_key(key)
            else: 
                if p.parent and p.parent.left == p: #if no successor/predecess
                    p.parent.left = None
                elif p.parent:
                    p.parent.right = None
                else: 
                    self.root = None #if only 1 node -- root
        else:
            raise ValueError("This key is not in the Binary Search Tree") #errror! not there
    def is_empty(self): 
        """returns True if tree is empty, else False"""
        if self.root == None:
            return True
        else:
            return False
    def print_tree(self):
        """Print out the BST in order"""
        self.root.inorder_print_tree() 
    def find(self, key):
        """Find the node with the value of the key passed in """
        p = self.root      # current node
        while p is not None and p.key != key:
            if key < p.key:
                p = p.left
            else:
                p = p.right
        if p is None:
            return False        
        else:
            return True

class TreeNode:
    """Tree node: left and right child + data which can be any object"""
    def __init__(self,key,left=None,right=None, parent=None):
        self.key = key
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
    def set_key(self,key): #setters and getters
        self.key = key
    def set_left(self,key):
        self.left = TreeNode(key)
    def set_right(self,key):
        self.right = TreeNode(key)
    def set_parent(self, parent):
        self.parent = parent
    def get_key(self):
        return(self.key)
    def get_left(self):
        return(self.left)
    def get_right(self):
        return(self.right)
    def get_parent(self):
        return(self.parent)
    def insert(self, key):
        """  Insert new node with key, assumes data not present """
        if self.key != None:
            if key < self.key: #if less than tree node, pass through left 
                if self.left is None:
                    a = TreeNode(key)
                    a.parent = self
                    self.left = a
                else:
                    self.left.insert(key)
            else: #if greater than tree node, pass through right
                if self.right is None:
                    b = TreeNode(key)
                    b.parent = self
                    self.right = b
                else:
                    self.right.insert(key)
        else:
            self.key = key
    def inorder_print_tree(self): 
        """Print tree in order of values"""
        if (self.left != None):
            self.left.inorder_print_tree()
        if(self.key != None):
            print(self.key)
        if (self.right != None):
            self.right.inorder_print_tree()
    def find_min(self): # returns min value in the tree
        if self.left != None:
            self.left.find_min()
        elif self.left == None:
            print(self.key)
            return self.key 
    def find_max(self): #returns max value in tree
        if self.right == None:
            return self.key 
        if self.right != None:
            self.right.find_max()
    def find_successor(self): 
        """returns the node that is the inorder successor of the node"""
        if self.get_right():
            return self.right.find_min()
        p = self.parent
        while p != None:
            if self != p.right:
                return None
            self = p
            p = p.parent
        return p
    def print_levels(self):
        """print nodes in order as well as their level from root"""
        if (self.left != None):
            self.left.print_levels()
        print(self.key," ", self.node_level())
        if (self.right != None):
            self.right.print_levels()
    def node_level(self):
        """return level of node passed"""
        a = self
        count = -1
        while a != None:
            a = a.parent
            count += 1
        return count





