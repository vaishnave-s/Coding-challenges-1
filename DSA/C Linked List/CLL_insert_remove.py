class Node:
    def __init__(self, data):
      self.data = data
      self.next = None


class CircularLinkedList:
	def __init__(self):
		self.head = None 
	
	def prepend(self, data):
		current=self.head
		new_node=Node(data)
		while current.next!=self.head:
			current=current.next
		current.next=new_node
		new_node.next=self.head
		self.head=new_node
			
	def append(self, data):
		if not self.head:
			self.head = Node(data)
			self.head.next = self.head
		else:
			current=self.head
			new_node=Node(data)
			while current.next!=self.head:
				current=current.next
			current.next=new_node
			new_node.next=self.head

	def remove(self,key):
		if self.head:
			if self.head.data==key:
				next=self.head.next
				current=self.head
				while current.next!=self.head:
					current=current.next
				current.next=next
				self.head=next
			else:
				# current=self.head
				# while current.next and current.next!=self.head:
				# 	if current.next.data==key:
				# 		break
				# 	current=current.next
				# current.next=current.next.next
				curr=self.head
				prev=None
				while curr.next!=self.head:
					prev=curr
					curr=curr.next
					if curr.data==key:
						prev.next=curr.next
						curr=curr.next

						
	def print_list(self):
		current=self.head
		while current:
			print(current.data)
			current=current.next
			if current==self.head:
				break

cll=CircularLinkedList()
cll.append(3)
cll.append(3)
cll.append(4)
cll.append(6)
cll.prepend(2)
cll.append(5)
cll.prepend(0)
cll.print_list()

cll.remove(3)
print()
cll.print_list()