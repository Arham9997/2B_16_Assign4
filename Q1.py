class Solution:
    def sortedInsert(self, head, x):
        current=head 
        while(current):
            if current.data>=x and current.prev==None:
                node=Node(x)
                node.next=current
                current.prev=node
                return node
            elif current.data<=x and current.next==None :
                node=Node(x)
                node.prev=current
                current.next=node 
                return head
            elif current.data<=x and current.next.data>=x:
                node=Node(x)
                node.prev=current
                node.next=current.next
                current.next.prev=node 
                current.next=node
                return head
            current=current.next
