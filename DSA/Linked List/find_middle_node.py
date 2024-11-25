# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
		def middleNode(self, head):
				"""
				:type head: Optional[ListNode]
				:rtype: Optional[ListNode]
				"""
				l = 0
				curr = head
				while curr:
						l+=1
						curr = curr.next
				middle_ind = l/2 if l/2==0 else l/2+1
				curr = head
				if l<=1:
						return curr
				for i in range(middle_ind):
						if i == middle_ind-1:
								return curr
						curr = curr.next




