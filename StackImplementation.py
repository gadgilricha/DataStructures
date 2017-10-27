class StackArray:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""
    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity= capacity
        self.items = [None]*capacity
        self.num_items = 0 
    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        if(self.num_items == 0):
            return True
        else:
            return False 
    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        if(self.num_items == self.capacity):
            return True
        else:
            return False
    def push(self, item):
        if(self.is_full() == True):
            raise IndexError("This Stack is full!")
        else:
            self.num_items+=1
            self.items[self.num_items - 1] = item
    def pop(self):
        """Returns item on the top of the stack and removes it"""
        if(self.is_empty() == True):
            raise IndexError("This Stack is empty!")
        else:
            temp = self.items[self.num_items-1]
            self.num_items-=1
            return temp
    def peek(self):
        """Returns item on the top of the stack but does not remove it"""
        if(self.size() != 0):
            return self.items[self.num_items-1] #add bounds checking 
    def size(self):
       """Returns the number of items in the stack"""
       return self.num_items

class StackLinked:
    """Implements an efficient last-in first-out Abstract Data Type using a LinkedList of seperate Nodes that contain values and references to the next Node"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = None
    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        if(self.size() == 0):
            return True 
        else:
            return False 
    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        if(self.size() == self.capacity):
            return True 
        else:
            return False
    def push(self, item):
        if(self.is_full() == True):
            raise IndexError("This LinkedList is full!")
        else:
            new = Node(item)
            new.set_next(self.top)
            self.top = new
    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        node = self.top
        count = 0
        while node != None:
            count+=1
            node = node.get_next()
        return count
    def pop(self):
        """Returns item on the top of the stack and removes it"""
        if(self.is_empty() == True):
            raise IndexError("This Stack is empty!")
        previous = self.top
        returned = previous.get_data()
        self.top = previous.get_next()
        return returned
        #whattodoifonly1iteminLIST??? #return VALUE?
    def peek(self):
        """Returns item on the top of the stack but does not remove it"""
        if(self.size() != 0):
            return (self.top).get_data()

class Node:
    """The Node class within the LinkedList that stores value and reference to the next node"""
    def __init__(self, value):
            self.value = value
            self.next = None
    def get_data(self):
        """returns data value of node"""
        return self.value
    def get_next(self):
        """returns reference to next node"""
        return self.next
    def set_data(newdata):
        """sets value of each node"""
        self.value = newdata
    def set_next(self,top): 
        """sets next reference of each node"""
        self.next = top


      # In the case when a user attempts to push an item on to a full stack, your
#push function (method) should raise an IndexError. Similarly if a user tries to pop an empty, your pop function
#(method) should raise an IndexError. 
