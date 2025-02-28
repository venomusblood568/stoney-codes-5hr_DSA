# Question Link => https://leetcode.com/problems/palindrome-linked-list/

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        # Find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        # Compare the first and second half nodes 
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True