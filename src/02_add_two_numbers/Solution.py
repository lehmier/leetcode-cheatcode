# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        return str(self.val) if self.next is None else str(self.val) + ' -> ' + str(self.next)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sumList = ListNode(0)
        currentNode = sumList
        carryOver = 0
        while l1 is not None or l2 is not None:
            currentVal = 0
            currentNode.next = ListNode(0)
            currentNode = currentNode.next

            if l1 is not None:
                currentVal = l1.val
                l1 = l1.next
            if l2 is not None:
                currentVal += l2.val
                l2 = l2.next

            currentVal += carryOver
            carryOver = 0 if currentVal < 10 else 1
            currentNode.val = currentVal if currentVal < 10 else currentVal - 10

        currentNode.next = ListNode(carryOver) if carryOver != 0 else None
        return sumList.next

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
print Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), \
                               ListNode(5, ListNode(6, ListNode(4))))
# 7 -> 0 -> 8
