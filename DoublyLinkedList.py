class Node:
    def __init__(self,data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        temp = self.head
        llstr = ''

        while temp:
            llstr = llstr + (str(temp.data) + "-->" if temp.next else str(temp.data))
            temp = temp.next
        print(llstr)

    def reverseDisplay(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        temp = self.head
        llstr = ''

        while temp.next:
            temp = temp.next

        while temp:
            llstr = llstr + (str(temp.data) + "-->" if temp.prev else str(temp.data))
            temp = temp.prev
        print(llstr)


    def insert_at_beg(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        node = Node(data,self.head)
        self.head.prev = node
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return

        temp = self.head
        while temp.next:
            temp =temp.next
        temp.next = Node(data,None,temp)

    def remove_by_data(self,data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp ==  self.head:
                    self.head = temp.next
                return
            temp = temp.next

        print("Given data is not found")


if __name__ == "__main__":
    obj = DoublyLinkedList()
    obj.insert_at_end(2)
    obj.insert_at_end(40)
    obj.insert_at_end(50)
    obj.insert_at_end(60)
    obj.insert_at_beg(1)
    obj.remove_by_data(10)
    obj.print()
    obj.reverseDisplay()