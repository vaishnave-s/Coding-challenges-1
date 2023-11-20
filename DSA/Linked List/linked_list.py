#Linked lists have two components - data, next
#Implementations - node class (data and next), linked list class (head)

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList():
	def __init__(self):
		self.head=None

	#add new node
	def append(self,data):
		new_node=Node(data)
		#empty linked list case - assigning top element to the newest node
		if self.head==None:
			self.head = new_node
			return
		#non empty linked list case - head node is constantly looped till the last node and then the new node is added to last node
		last_node=self.head
		while last_node.next:
			last_node=last_node.next
		last_node.next=new_node
	
	def print_list(self):
		current = self.head
		while current:
			print(current.data)
			print("^")
			current=current.next
		print("None")
	
	#add new node first
	def prepend(self,data):
		new_node=Node(data)
		new_node.next=self.head
		self.head=new_node
	
	#insert after a spefific node
	def insert_after_node(self,prev_node,data):
		if not prev_node:
			print("Previous node doesnt exist!")
			return
		new_node=Node(data)
		new_node.next=prev_node.next
		prev_node.next=new_node

	#length of linked list
	def length_ll(self):
		curr_node=self.head
		count=0
		while curr_node:
			curr_node=curr_node.next
			count+=1
		return count
	
	#check if palindrome
	def is_palindrome(self):
		curr_node=self.head
		ls = []
		while curr_node:
			ls.append(curr_node.data)
			curr_node=curr_node.next

		curr_node=self.head
		while curr_node:
			if curr_node.data!=ls.pop():
				return
			curr_node=curr_node.next
		return True

	#rotate - 1-2-3-4-5-none with pivot 3 becomes 4-5-1-2-3-none
	def rotate(self,pivot):
		curr=self.head
		pivot_node=self.head
		#assign last node to point to first one
		while curr.next:
			curr=curr.next
		curr.next=self.head
		#find pivot data
		while pivot_node:
			if pivot_node.data==pivot:
				break
			pivot_node=pivot_node.next
		#assign pivot to point to none
		if pivot_node and pivot_node.next!=None:
			self.head=pivot_node.next
			pivot_node.next=None
	
	#5-4-3-none + 3-2-1-none = 8-6-4-none with the first node being tens and last node being hundreds/ thousands...
	def sum_ll(self,ll):
		curr1=self.head
		curr2=ll.head
		s1=''
		s2=''
		while curr1:
			s1+=str(curr1.data)
			curr1=curr1.next
		s1=s1[::-1]
		i1=int(s1)

		while curr2:
			s2+=str(curr2.data)
			curr2=curr2.next
		s2=s2[::-1]
		i2=int(s2)
		sum_i=i1+i2
		sum_s=str(sum_i)
		sum_s=sum_s[::-1]
		sum_ll=LinkedList()
		for i in sum_s:
			sum_ll.append(int(i))
		return sum_ll


llist = LinkedList()
llist2 = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("B")
# llist.append("A")
# llist.insert_after_node(llist.head.next, "D")
# llist.print_list() 
# print(llist.length_ll())
# print(llist.is_palindrome())

llist.append(1)
llist.append(2)
llist.append(3)
llist2.append(4)
llist2.append(5)
llist2.append(9)
summed_ll=llist.sum_ll(llist2)
summed_ll.print_list()


# llist.print_list() 
# print("-------")
# llist.rotate(4)
# llist.print_list() 


