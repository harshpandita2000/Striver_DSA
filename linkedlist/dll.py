class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __repr__(self) -> str:
        curr_node = self.head
        data_list = []
        while curr_node:
            data_list.append(str(curr_node.data))
            curr_node = curr_node.next
        return "->".join(data_list)
    
    def insert_at_end(self,data): #10 20 30 40
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        # 10 < > 20 < >
        #30   10 ,,20

    def insert_at_start(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop(self):
        curr_node = self.head
        if self.head == self.tail:
            ele = curr_node.data
            self.head = None
            self.tail = None
            return ele
        # while curr_node.next.next:
        #     curr_node = curr_node.next
        # curr_node.next = None
        # self.tail = curr_node
        removed_ele = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return removed_ele
    
    #10 20 30
    def delete(self,data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
                return
            else:
                curr_node = curr_node.next

    def search(self, data):
        curr_node = self.head
        while curr_node:

            if curr_node.data == data:
                return True
            curr_node = curr_node.next
            
        return False
    
    #100 200 300 400
    #400 300 200 100
    def reverse(self):
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            prev_node = curr_node.prev
            curr_node.next = prev_node
            curr_node.prev = next_node
            curr_node = next_node
        self.tail,self.head = self.head,self.tail                      

s1 = DoublyLinkedList()
s1.insert_at_end(10)
s1.insert_at_end(20)
s1.insert_at_end(30)
s1.reverse()
print(s1)
        
