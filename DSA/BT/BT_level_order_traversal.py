#Queue
#first in, first out
class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self, traversal_type):
		# if traversal_type == "preorder":
		# 	return self.preorder_print(tree.root, "")
		# elif traversal_type == "inorder":
		# 	return self.inorder_print(tree.root, "")
		# elif traversal_type == "postorder":
		# 	return self.postorder_print(tree.root, "")
		if traversal_type == "levelorder":
			return self.levelorder_print(tree.root)

		else:
			print("Traversal type " + str(traversal_type) + " is not supported.")
			return False

	def levelorder_print(self, start):
		if start is None:
			return

		q = Queue()
		q.enqueue(start)
		traversal=''
		while len(q) > 0:
			traversal+=str(q.peek())+'-'
			node=q.dequeue()
			if node.left:
				q.enqueue(node.left)
				
			if node.right:
				q.enqueue(node.right)
		return traversal




tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.print_tree("levelorder"))

