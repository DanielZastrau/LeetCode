class ListNode():
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: 

        if l1.val == 0 and l1.next is None:
            return l2
        elif l2.val == 0 and l2.next is None:
            return l1

        initial_node = l1

        overflow = 0
        while True:
            
            print(l1.val, l2.val, overflow)
            l1.val = l1.val + l2.val + overflow
            overflow = l1.val // 10
            l1.val = l1.val % 10

            print(l1.val, overflow)

            if l1.next is None and l2.next is None:

                if overflow != 0:
                    l1.next = ListNode(overflow, None)

                return initial_node

            if l1.next is None:
                l1.next = ListNode(0, None)
            l1 = l1.next

            if l2.next is not None:
                l2 = l2.next
            else:
                l2 = ListNode(0, None)

def walk_linked_list(l: ListNode):

    while l.next is not None:
        print(l.val, end='')
        l = l.next
    print(l.val)

if __name__=='__main__':
    sol = Solution()

    # node1 = ListNode(2, ListNode(4, ListNode(3)))
    # node2 = ListNode(5, ListNode(6, ListNode(4)))

    # node1 = ListNode(0, ListNode(8, ListNode(6, ListNode(5, ListNode(6, ListNode(8, ListNode(3, ListNode(5, ListNode(7)))))))))
    # node2 = ListNode(6, ListNode(7, ListNode(8, ListNode(0, ListNode(8, ListNode(5, ListNode(8, ListNode(9, ListNode(7)))))))))

    node1 = ListNode(2, ListNode(4, ListNode(9)))
    node2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))

    walk_linked_list(sol.addTwoNumbers(node1, node2))