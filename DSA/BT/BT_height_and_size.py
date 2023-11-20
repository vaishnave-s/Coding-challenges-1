

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)
	
	def height(self, node):
		if node is None:
			return -1
		left_height = self.height(node.left)
		right_height = self.height(node.right)
		return 1 + max(left_height, right_height)
		
	def size_(self, node):
		if node is None:
			return 0
		val_l = self.size_(node.left)
		val_r = self.size_(node.right)
		return 1+val_l+val_r


# Calculate height of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5
# 
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Height") 	
print(tree.height(tree.root)) 	
print("Size") 	
print(tree.size_(tree.root)) 	