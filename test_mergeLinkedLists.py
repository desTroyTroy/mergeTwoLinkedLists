from mergeTwoLinkedLists import ListNode, Solution

def buildLinkedList(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head

def toList(node):
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values

tests = [
    ([1, 4, 7], [2, 3, 6]),
    ([], [2, 3, 6]),
    ([1, 3, 5], []),
    ([], []),
    ([1, 2, 3], [4, 5, 6]),
    ([4, 5, 6], [1, 2, 3]),
]

solution = Solution()

for values1, values2 in tests:
    list1 = buildLinkedList(values1)
    list2 = buildLinkedList(values2)

    merged = solution.mergeTwoLists(list1, list2)

    print(f"{values1} + {values2} -> {toList(merged)}")