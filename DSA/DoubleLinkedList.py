class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_at_begining(self,data):
        new_node=Node(data)
        #list is empty
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        #List is not empty
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    
    def insert_at_ending(self,data):
        new_node=Node(data)
        #list is empty
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        #list is not empty
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node

    def insert_at_position(self,position,data):
        #if position is less than 0
        if position<0:
            print("Invalid position")
            return
        if position==0:
            self.insert_at_begining(data)
            return
        #position gretaer than 0
        new_node=Node(data)
        current=self.head
        for _ in range(position-1):
            if current is None:
                print("Invalid position")
                return
            current=current.next
        new_node.next=current.next
        new_node.prev=current

        if current.next is not None:
            current.next.prev=new_node
        else:
            self.tail=new_node
        current.next=new_node

    def delete_from_begining(self):
        #list is empty
        if self.head is None:
            print("list is empty")
            return
        #list has only one element
        if self.head==self.tail:
            self.head=None
            self.tail=None
        #list has more than one element
        self.head=self.head.next
        self.head.prev=None

    def delete_from_end(self):
        #list is empty
        if self.head is None:
            print("list is empty")
            return
        #list has only one element
        if self.head==self.tail:
            self.head=None
            self.tail=None
        #list has more than one element
        self.tail=self.tail.prev
        self.tail.next=None

    def delete_by_value(self,value):
        if self.head is None:
            print("list is empty")
            return
        current=self.head
        while current is not None:
            if current.data==value:
                if current==self.head:
                    self.delete_from_begining()
                    return
                if current==self.tail:
                    self.delete_from_end()
                    return
                current.prev.next=current.next
                current.next.prev=current.prev
                return
            current=current.next
        print("Value not found")

    def delete_by_position(self,position):
        if self.head is None:
            print("list is empty")
            return
        if position<0:
            print("invalid")
            return
        if position==0:
            self.delete_from_begining()
        current=self.head
        for _ in range(position):
            current=current.next
        current.prev.next=current.next
        current.next.prev=current.prev

    def update(self,index,new_value):
        if index<0:
            return False
        current=self.head
        count=0
        while current is not None:
            if count==index:
                current.data=new_value
                return True
            current=current.next
            count+=1
        return False

    def search(self,value):
        current=self.head
        index=0
        while current is not None:
            if current.data==value:
                return index
            current=current.next
            index+=1
        return -1

    def reverse(self):
        current=self.head
        while current is not None:
            current.prev,current.next=current.next,current.prev
            current=current.prev
        self.head,self.tail=self.tail,self.head

    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end="<->")
            current=current.next
        print("None")
dll = DoublyLinkedList()

# Insert at beginning
dll.insert_at_begining(20)
dll.insert_at_begining(10)

# Insert at ending
dll.insert_at_ending(30)
dll.insert_at_ending(40)

print("After inserting:")
dll.display()

# Insert at position
dll.insert_at_position(2, 25)

print("After inserting 25 at position 2:")
dll.display()

# Delete from beginning
dll.delete_from_begining()

print("After deleting from beginning:")
dll.display()

# Delete from end
dll.delete_from_end()

print("After deleting from end:")
dll.display()

# Delete by value
dll.delete_by_value(25)

print("After deleting value 25:")
dll.display()

# Insert some more values
dll.insert_at_ending(50)
dll.insert_at_ending(60)

print("After adding 50 and 60:")
dll.display()

# Delete by position
dll.delete_by_position(1)

print("After deleting position 1:")
dll.display()

# Update
dll.update(1, 100)

print("After updating position 1 to 100:")
dll.display()

# Search
print("Index of 100:", dll.search(100))
print("Index of 500:", dll.search(500))

# Reverse
dll.reverse()

print("After reversing:")
dll.display()