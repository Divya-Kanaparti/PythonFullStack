class Node:
    def __init__(self,data):
        self,data=data
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        new_node=Node(data)
        #CLL is empty
        if self.head is None:
            new_node.next=new_node
            self.head=new_node
            return 
        #CLL is not empty
        current=self.head
        while current.next!=self.head:
            current=current.next
        new_node.next=self.head
        current.next=new_node
        self.head=new_node
    
    def insert_at_end(self,data):
        new_node=Node(data)
        #CLL is empty
        if self.head is None:
            new_node.next=new_node
            self.head=new_node
            return
        #CLL is not empty
        current=self.head
        while current.next!=self.head:
            current=current.next
        #new node points to head
        new_node.next=self.head
        #current node points to new node
        current.next=new_node

    def insert_at_position(self,position,data):
        if position<0:
            print("invalid position")
            return
        if self.head is None:
            if position==0:
                new_node=Node(data)
                new_node.next=new_node
                self.head=new_node
            else:
                print("invalid position")
            return

        if position==0:
            self.insert_at_begining(data)
            return
        current=self.head
        for _ in range(position-1):
            current=current.next
        new_node=Node(data)
        new_node.next=current.next
        current.next=new_node

        