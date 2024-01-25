class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
  
# n1 = Node(10)
# print(n1)
# n1.next = Node(20)
# n1.next.next = Node(30)
# print(f"{n1.data}-> {n1.next.data} -> {n1.next.next.data}")

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
        self.tail = None

    def __repr__(self) -> str:
        curr_node = self.head
        values = []
        while curr_node:
            values.append(str(curr_node.data))
            curr_node = curr_node.next
        return " -> ".join(values)
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head        
        else:
            curr_node = self.head
            while(curr_node.next):
                curr_node = curr_node.next
            curr_node.next = new_node
            self.tail = curr_node.next
        self.length += 1

    def insert_at_start(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
  #or##################################################################
    #   def insert_at_end(self, data):
    #     new_node = Node(data)
    #     if self.head == None:
    #         self.head = new_node
    #         self.tail = self.head
    #     else:
    #         self.tail.next = new_node
    #         self.tail = self.tail.next
    
    # def insert_at_start(self, data):
    #     new_node = Node(data)
    #     if self.head == None:
    #         self.head = new_node
    #         self.tail = self.head
    #     else:
    #         new_node.next = self.head
    #         self.head = new_node  
    
    
    
    
    def pop(self):
        if self.length == 1:
            deleted_node = self.head.data
            self.head = None
            self.tail = None
            return deleted_node
        
        curr_node = self.head
        while curr_node.next.next:
            curr_node = curr_node.next
        removed_ele = curr_node.next.data
        curr_node.next = None
        self.tail = curr_node
        self.length -= 1
        return removed_ele
    
    def delete(self,data):
        curr_node = self.head      
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
        while curr_node.next.data!= data:
            curr_node = curr_node.next
        if curr_node.next == self.tail:
            self.tail = curr_node
        curr_node.next =curr_node.next.next
        
        self.length -= 1

    def calculate_length(self):
        cnt = 0
        curr_node = self.head
        while curr_node:
            curr_node = curr_node.next
            cnt += 1
        return cnt
    
    def search_element(self,data):
        self.data = data
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                return True
            else:
                curr_node = curr_node.next
        return False

    def reverse(self):
        prev = None
        curr_node = self.head
        self.tail = self.head
        nextt = None
        while curr_node:
            nextt = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = nextt
        self.head = prev
s1 = SinglyLinkedList()
s1.insert_at_end(10)
s1.insert_at_end(20)
s1.insert_at_end(30)
s1.insert_at_end(50)
s1.insert_at_end(60)
s1.delete(60)
# print(f"{s1.head.data}->{s1.head.next.data} ->{s1.head.next.next} ")
print(s1)
s1.reverse()
print(s1)

        

