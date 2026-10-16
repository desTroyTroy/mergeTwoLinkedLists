class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create 2 dummy nodes
        dummy1 = ListNode(0, list1)
        dummy2 = ListNode(0, list2)
        # Create 2 pointers and point them at the dummy nodes
        current1 = dummy1
        current2 = dummy2

        # If list1 empty, return list2
        if dummy1.next == None:
            dummy1 = dummy2

        else:
            # Else iterate through both lists until one runs out
            while current1.next != None and current2.next != None:

                # If the value of the next node in list1 is less than
                # that of list2, simply advance the 1st pointer
                if current1.next.val < current2.next.val:
                    current1 = current1.next
                
                else:
                    # Else list2's next node's value is smaller; therefore,
                    # temporarily store the 1st pointers next location,
                    temp = current1.next
                    
                    # redirect the chain of list1 to the next node of 
                    # list2
                    current1.next = current2.next

                    # Advance the 2nd pointer 2 locations to indicate 
                    # the new starting position of list2 before breaking
                    # the chain
                    dummy2.next = current2.next.next
                    current2 = dummy2

                    # Then reattach the rest of list1 starting at the 
                    # temporarily store location
                    current1.next.next = temp

                    # Finally, advance the 1st pointer to the next node
                    # before the next comparison
                    current1 = current1.next

            # If list1 ran out first, attach the rest of list2
            if current2.next != None:
                current1.next = current2.next

        # Return the original starting position of list 1       
        return dummy1.next

''' Commented out once test module was uploaded
def print_list(node):
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    print(values)

# List 1: 1 -> 4 -> 7
list1 = None

# List 2: 2 -> 3 -> 6
list2 = ListNode(2, ListNode(3, ListNode(6)))

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

print_list(merged)
'''
