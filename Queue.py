class Queue:
	def __init__(self, capacity):
		self.capacity = capacity # the maximum number of items that can be stored in queue
		self.items = [None]*capacity
		self.num_in_queuee = 0
		self.front = 0
		self.rear = 0
	def is_empty(self):
		if self.num_in_queuee == 0:
			return True
		else:
			return False
	def is_full(self):
		if self.num_in_queuee == self.capacity:
			return True
		else:
			return False
	def enqueue(self, item):
		if(self.is_full() == True):
			raise IndexError("This Queue is full!")
		self.items[self.rear] = item 
		self.rear = (self.rear + 1)%self.capacity
		self.num_in_queuee += 1
	def dequeue(self):
		if(self.is_empty() == True):
			raise IndexError("This Queue is empty!") 
		temp = self.items[self.front]
		self.front = (self.front + 1)%self.capacity
		self.num_in_queuee -= 1
		return temp
	def num_in_queue(self):
		"""returns the number of items in the queue"""
		return self.num_in_queuee

#test cases
#is empty is full
#pops in correct order, enters in correct order
#NO OVERRRIDING!

class QueueLinked: #CAREFUL DEALING WITH EMPTY QUEUE??
	def __init__ (self, capacity):
		self.capacity = capacity # the maximum number of items that can be stored in queue
		self.num_in_queuee = 0
		self.front = None
		self.rear = None
	def is_empty(self):
		if self.num_in_queuee == 0:
			return True
		else:
			return False
	def is_full(self):
		if self.num_in_queuee == self.capacity:
			return True
		else:
			return False
	def enqueue(self, item):
		if(self.is_full() == True):
			raise IndexError("This LinkedList is full!")
		newone = Node(item)
		if (self.front == None):
			self.rear = newone
			self.front = newone
		else:
			(self.rear).set_next(newone)
			self.rear = newone
		self.num_in_queuee += 1
	def dequeue(self):
		if(self.is_empty() == True):
			raise IndexError("This LinkedList is empty!")
		prev = (self.front).get_data()
		self.front = (self.front).get_next()
		self.num_in_queuee -= 1
		return prev
	def num_in_queue(self):
		"""returns the number of items in the queue"""
		return self.num_in_queuee

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