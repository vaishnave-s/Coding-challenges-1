# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
		def removeNthFromEnd(self, head, n):
				"""
				:type head: Optional[ListNode]
				:type n: int
				:rtype: Optional[ListNode]
				"""
				curr = head
				l = 0
				while curr:
						curr = curr.next
						l+=1
				if l==n:
						return head.next
				ind = l-n+1
				counter = 0
				curr = head
				print(ind)
				while curr:
						counter+=1
						if counter == ind-1 and curr.next:
								curr.next = curr.next.next
								break
						curr = curr.next
				return head



