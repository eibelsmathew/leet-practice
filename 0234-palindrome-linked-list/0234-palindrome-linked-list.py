# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr       
            curr = nxt
        second_half = prev

        first_half = head
        palin = True
        while second_half:
            if first_half.val != second_half.val:
                palin = False
                break
            first_half = first_half.next
            second_half = second_half.next
        return palin