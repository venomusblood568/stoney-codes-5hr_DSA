# Question Link => https://leetcode.com/problems/remove-linked-list-elements/

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        node = head

        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        if head.val == val:
            head = head.next

        return head
