class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)  # Dummy node to simplify the code
    curr = dummy
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        # Calculate the sum and carry
        sum_val = x + y + carry
        carry = sum_val // 10
        curr.next = ListNode(sum_val % 10)

        # Move to the next nodes
        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # Handle the remaining carry
    if carry:
        curr.next = ListNode(carry)

    return dummy.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next


