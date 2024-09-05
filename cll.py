class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head

    def display(self):
        temp=self.head
        while True:
            print(temp.data, end=' ')
            temp = temp.next
            if temp == self.head:
                break
        print()

    def insert_at_front(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head
        else:
            newnode.next = self.head
            self.head = newnode
            self.tail.next = self.head

    def insert_at_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head

    def insert_at_mid(self, data, pos):
        newnode = Node(data)
        temp = self.head
        i = 1
        while i < pos - 1:
            temp = temp.next
            if temp == self.head:
                print("Position out of bounds")
                return
            i += 1
        newnode.next = temp.next
        temp.next = newnode
        if newnode.next == self.head:
            self.tail = newnode

    def delete_at_front(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

    def delete_at_end(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp

    def delete_at_mid(self, pos):
        temp = self.head
        i = 1
        while i < pos - 1:
            temp = temp.next
            if temp.next == self.head:
                print("Position out of bounds")
                return
            i += 1
        temp.next = temp.next.next
        if temp.next == self.head:
            self.tail = temp
obj = CLL()
while True:
    print("1. Create 2. Display 3. Insert at front 4. Insert at mid 5. Insert at end 6. Delete at front 7. Delete at end 8. Delete at mid")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        data = int(input("Enter the data: "))
        obj.create(data)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        data = int(input("Enter the data: "))
        obj.insert_at_front(data)
    elif choice == 4:
        data = int(input("Enter the data: "))
        pos = int(input("Enter the position: "))
        obj.insert_at_mid(data, pos)
    elif choice == 5:
        data = int(input("Enter the data: "))
        obj.insert_at_end(data)
    elif choice == 6:
        obj.delete_at_front()
    elif choice == 7:
        obj.delete_at_end()
    elif choice == 8:
        pos = int(input("Enter the position: "))
        obj.delete_at_mid(pos)
    else:
        print("Invalid choice")
