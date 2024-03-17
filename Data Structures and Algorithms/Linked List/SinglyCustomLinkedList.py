class SingleNode:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data

class SinglyLinkedList:
    def __init__(self,circular) -> None:
        self.head = None
        self.circular = circular

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None") if not self.circular else nodes.append(str(self.head))
        return ' -> '.join(nodes)

# Using Custom Single LinkedList
llist = SinglyLinkedList(circular=True)

# Nodes
first_node = SingleNode("a")
second_node = SingleNode("b")
third_node = SingleNode("c")

llist.head = first_node
first_node.next = second_node
second_node.next = third_node

# LinkedList
if(llist.circular):
    print("Single Circular Linked List")
    print(llist)
else:
    print("Single Linked List")
    print(llist)
