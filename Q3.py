class Solution:
    def reverseDLL(self, head):
        temp=head
        while temp.next!=None:
            temp=temp.next
        reversed=DLLNode(temp.data)                                
        reversed.prev=None
        head1=reversed
        temp1=head1
        temp=temp.prev
        while temp!=None:
            curr=DLLNode(temp.data)    
            temp1.next=curr
            curr.prev=temp1
            temp1=curr 
            curr=None
            temp=temp.prev  
        return head1
