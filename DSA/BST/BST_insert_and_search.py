class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BST(object):
	def __init__(self, root):
		self.root = Node(root)
	
	def insert(self,new_val):
		return self.insert_helper(self.root, new_val)
		
	def insert_helper(self,current,new_val):
		if current.data<new_val:
			if current.right:
				self.insert_helper(current.right,new_val)
			else:
				current.right=Node(new_val)
		else:
			if current.left:
				self.insert_helper(current.left,new_val)
			else:
				current.left=Node(new_val)

	def search(self,val):
		return self.search_helper(self.root,val)

	def search_helper(self,current,val):
		if current:
			if current.data==val:
				return True
			elif current.data<val:
				return self.search_helper(current.right, val)
			elif current.data>val:
				return self.search_helper(current.left, val)
		else:
				return False
					

bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print("search")
print(bst.search(9))
print(bst.search(14))