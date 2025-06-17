#linked lIst

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        temp = self.head
        llstr = ''

        while temp:
            # llstr += str(temp.data)+'-->' if temp.next else str(temp.data)
            llstr = llstr + (str(temp.data) + '-->' if temp.next else str(temp.data))
            # print(temp.data)
            temp = temp.next
        print(llstr)


    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)


    def insert_at_beg(self,value):
        node = Node(value, self.head)
        self.head = node

    def insert_at_end(self,value):
        if self.head is None:
            self.head = Node(value,None)
            return

        temp = self.head
        while temp.next:
            temp= temp.next
        temp.next = Node(value,None)

    def insert_at_index(self,index,value):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beg(value)
            return

        prev = 0
        temp = self.head
        while temp:
            if prev == index -1:
                node = Node(value, temp.next)
                temp.next = node
                break

            temp = temp.next
            prev = prev +1


    def insert_after_data(self,data_after, data_to_insert):

        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head
        while temp:
            if temp.data == data_after:
                node = Node(data_to_insert,temp.next)
                temp.next = node
                return
            temp = temp.next

        print(f"Node with data {data_after} not found")

    def get_length(self):
        count =0
        temp = self.head

        while temp:
            count = count+1
            temp = temp.next
        return count

    def remove_first(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last(self):
        # if there is no node
        if self.head is None:
            return

        # If there's only one node
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next and current.next.next:
            current = current.next

        current.next = None

    def remove_at_index(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.remove_first()
            return

        prev = 0
        temp = self.head
        while temp:
            if prev == index -1:
                temp.next = temp.next.next
            temp = temp.next
            prev = prev+1

    def remove_by_data(self,data):
        temp = self.head

        if temp is not None and temp.data == data:
            self.remove_first()
            return

        while temp is not None and temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Given data is not found")



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beg(40)
    ll.insert_at_beg(28)
    ll.insert_at_beg(50)
    ll.insert_at_beg(20)
    ll.insert_at_beg(97)
    ll.insert_at_end(2)
    ll.insert_at_index(2,6)
    ll.print()

    ll.insert_after_data(50,0)
    ll.print()

    print(ll.get_length())

    ll.remove_first()
    ll.print()

    ll.remove_last()
    ll.print()

    ll.remove_at_index(2)
    ll.print()

    ll.remove_by_data(28)
    ll.print()

    ll.insert_values(["apple","banana","mango","orange","carrot"])
    ll.print()



