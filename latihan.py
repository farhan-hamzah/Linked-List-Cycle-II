# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        # Langkah 1: deteksi apakah ada siklus
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Ketemu siklus
                break
        else:
            return None  # Tidak ada siklus
        
        # Langkah 2: cari node awal siklus
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow  # Node awal siklus
