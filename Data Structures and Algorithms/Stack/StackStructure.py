# Stacks follow LIFO rules last in first out
    
class QueueLifoNode:
    def __init__(self,data):
        self.value = data
        self.next = None

class QueueLifo:
    def __init__(self,data):
        self.head = QueueLifoNode(data)
        self.count = 1

    def __str__(self) -> str:
        queue_str = ""
        node = self.head
        while node:
            queue_str += str(node.value) + "-->"
            node = node.next
        return queue_str[:-3]
    
    def push(self, value):
        new_node = QueueLifoNode(value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
        self.count += 1

    def queueLength(self):
        return self.count
    
    def pop(self):
        if self.queueLength() == 0:
            raise Exception("You cannot delete something from an empty queue")
    
        if self.head.next is None:  # Si solo hay un elemento en la cola
            removed = self.head.value
            self.head = None
        else:
            prev_node = None
            current_node = self.head
            while current_node.next:
                prev_node = current_node
                current_node = current_node.next
            removed = current_node.value
            prev_node.next = None

        self.count -= 1
        return removed

if __name__ == "__main__":
    queue = QueueLifo(1)
    queue.push(2)
    queue.push(3)
    
    print(queue)
    remove = queue.pop()
    
    print("Removing from queue: ")
    print(remove)
    
    print("NEW QUEUE")
    print(queue)
