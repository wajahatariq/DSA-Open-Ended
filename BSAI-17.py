class node:
    def __init__(self, value):  # Initialize the node with a value
        self.value = value
        self.next = None

class singlylinkedlist:
    def __init__(self):  # Initialize the linked list
        self.head = None

    def append(self, value):
        new_node = node(value)  # create a new node
        if not self.head:
            self.head = new_node  # set it as the head if the list is empty
            return
        last_node = self.head
        while last_node.next:  # traverse the list to find the last node
            last_node = last_node.next
        last_node.next = new_node  # link the new node at the end

    def display(self):
        current_node = self.head
        while current_node:  # print each node's value followed by "|" if there is a next node
            print(current_node.value, end=" | " if current_node.next else "\n")
            current_node = current_node.next

    def removeNAfterM(self, m, n):
        current_node = self.head
        while current_node:
            # skip the first m nodes
            for _ in range(m - 1):
                if not current_node:
                    return
                current_node = current_node.next

            if not current_node:
                return
            
            # remove the next n nodes
            temp_node = current_node.next
            for _ in range(n):
                if not temp_node:
                    break
                temp_node = temp_node.next

            current_node.next = temp_node  # link the current node to the node after the deleted ones
            current_node = temp_node


linked_list = singlylinkedlist()
values = [0, 5, 4, 3, 8, 1, 19, 1]  # sample data for the linked list
for value in values:
    linked_list.append(value)

print("original linked list:") 
linked_list.display()

m, n = 2, 1  # skip and remove n nodes
linked_list.removeNAfterM(m, n)

print(f"modified linked list")
linked_list.display()
