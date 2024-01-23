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
        else:
            curr_node = self.head
            while(curr_node.next):
                curr_node = curr_node.next
            curr_node.next = new_node
    # def insert_at_start(self, data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node

    # def pop(self):
    #     curr_node = self.head
    #     while curr_node.next.next:
    #         curr_node = curr_node.next
    #     removed_ele = curr_node.next.data
    #     curr_node.next = None
    #     return removed_ele
    
    def delete(self,data):
        curr_node = self.head      
        if self.head.data == data:
            self.head = self.head.next
            return
        while curr_node.next.data!= data:
            curr_node = curr_node.next
        curr_node.next =curr_node.next.next
    


        
s1 = SinglyLinkedList()
s1.insert_at_end(10)
s1.insert_at_end(20)
s1.insert_at_end(30)
s1.insert_at_end(50)
s1.insert_at_end(60)
s1.delete(10)

# print(f"{s1.head.data}->{s1.head.next.data} ->{s1.head.next.next} ")
print(s1)

        

