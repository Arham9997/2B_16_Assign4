class Solution:
    def delete_node(self, head, x):
        if x==1:
            new_head=head.next
            if new_head:
                new_head.prev=None
            return new_head
         
        curr=head  
        count=1
        while curr and count < x:
            curr = curr.next
            count += 1
        
        if not curr:
            return head
        
        if curr.next:
            curr.next.prev = curr.prev
        if curr.prev:
            curr.prev.next = curr.next
        
        return head
