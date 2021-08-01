# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    # passing in the top only

    current = linkedList
    while current is not None:
        distinct = current.next
        # a none  value will also not have a property and that is why we have to perform a check heres
        # this will always be true and we should only keep iterating until we are not the same anymore
        while distinct is not None or distinct.value == current.value:
            distinct = distinct.next
        current.next = distinct
        current = distinct
    return linkedList
