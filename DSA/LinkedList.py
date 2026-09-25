class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    #time complexity=O(1)
    #space complexity=O(1)
    def insert_at_begining(self,data):
        new_node=Node(data)
        # if linked list is empty
        if self.head is None:
            self.head=new_node
            return
        #if linked list is not empty
        new_node.next=self.head
        self.head=new_node

    #time complexity=O(n)-->because you traverse till end
    def insert_at_ending(self,data):
        new_node=Node(data)
        #Linked list is empty
        if self.head is None:
            self.head=new_node
            return
        #linked list is not empty
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node

    def insert_at_position(self,data,position):
        if position<0:
            print("Invalid Position")
            return
        if position==0:
            self.insert_at_begining(data)
            return
        new_node=Node(data)
        current=self.head
        for i in range(position-1):
            #current is none
            if current is None:
                print("Invalid position")
                return
            #current is not none
            current=current.next
        new_node.next=current.next
        current.next=new_node

    def delete_from_begining(self):
        #linked list is empty
        if self.head is None:
            print("list is empty")
            return
        #linked list has only one element
        if self.head.next is None:
            self.head=None
            return
        #linked list is not empty
        self.head=self.head.next

    def delete_from_end(self):
        #linked list is empty
        if self.head is None:
            print("list is empty")
            return
        #linked list has only one element
        if self.head.next is None:
            self.head=None
            return
        #linked list has more than one element
        current=self.head
        while current.next.next is not None:
            current=current.next
        current.next=None
             