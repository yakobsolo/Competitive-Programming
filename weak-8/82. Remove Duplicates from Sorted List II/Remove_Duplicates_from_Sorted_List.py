class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        initial = ListNode()
        initial.val = 0
        initial.next = head
        prev = initial
        while head:
            if head.next is not None and head.val == head.next.val:
                while head.next != None and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            
            head = head.next
        return initial.next
