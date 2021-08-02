# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
	f = head
	s = head
	i = 1
	while i <= k:
		s = s.next
		i += 1
	if s is None:
		head.value = f.next.value
		head.next = f.next.next
		return
	while s.next is not None:
		f = f.next
		s = s.next
	f.next = f.next.next
