# Middle of the Linked List
# Difficulty: Easy
# Category: Linked List, Two Pointers

"""
    Problem: We're given the head of a singly linked list, our job is to return the middle of the linked list.
    If there are two in the middle then we have to return the second one.

    e.g head = [1,2,3,4,5] output = [3,4,5]
    The output is [3,4,5] because the middle node is 3.

    Approach:
    Use two pointers on the same indicie, one slow pointer one fast pointer and move the fast pointer twice as fast as the slow one.

    1. Set the slow pointer and the fast pointer to the head of the linked list.
    2. While the fast pointer still exists and the next node after the fast pointer still exists
    3. Move the fast pointer twice (fast.next.next)
    4. Move the slow pointer once (slow.next)
    5. When the traversal is done fast will be at the end of the linked list and slow will be in the middle
    6. Return slow

    Time Complexity: O(n / 2) (O(n)) We drop constants in Big O
    Space Complexity: O(1)

    The time complexity of this approach is O(n) because there are n nodes and we go through half of them O(n/2) but in Big O we drop the constant.
    The space complexity of this approach is O(1) because we have only 2 variables throughout, we aren't creating an array or another linked list the extra memory stays constant.

"""

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

        slow = head
        fast = head

        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next

        return slow
        