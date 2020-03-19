class Node: 

	# Class to create nodes of linked list 
	# constucter initializes node automatically 
	def __init__(self,data): 
		self.data = data 
		self.next = None

class Stack: 
	
	# head is default NULL 
	def __init__(self): 
		self.head = None
    
    # Checks if stack is empty 
	def isempty(self): 
		if self.head == None: 
			return True
		else: 
			return False
    
    # adds to the start of the stack 
	def push(self,data): 
		
		if self.head == None: 
			self.head=Node(data) 
			
		else: 
			newnode = Node(data) 
			newnode.next = self.head 
			self.head = newnode 