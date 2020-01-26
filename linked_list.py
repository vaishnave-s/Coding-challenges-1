class Node(object):
  def __init__(self,d,n=None):
    self.data = d
    self.next_node = n
  def get_next(self):
    return self.next_node
  def set_next(self,n):
    self.next_node = n
  def get_data(self):
    return self.data
  def set_data(self,d):
    self.data = d

class LinkedList(object):
  def __init__(self,r=None):
    self.root=r
    self.size=0
  def get_size(self):
    return self.size
  def add(self,d):
    for i in d:
      new_node=Node(i,self.root)
      self.root=new_node
      self.size+=1
  def remove (self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return "Removed"		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return "Couldn't find this number"  # data not found

  def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

myList = LinkedList()
# myList.add([5,8,7,8])
myList.add([5,8,7,8])

print("size="+str(myList.get_size()))
myList.remove(8)
print("size="+str(myList.get_size()))
print(myList.remove(12))
print("size="+str(myList.get_size()))
print(myList.find(5))
  




