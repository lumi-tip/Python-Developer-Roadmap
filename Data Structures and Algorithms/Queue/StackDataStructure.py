# FIFO Queue
class QueueFifoNode:
    def __init__(self, data) -> None:
        self.value = data
        self.next = None

class QueueFifo:
    def __init__(self,data) -> None:
        self.head = QueueFifoNode(data)
        self.count = 1

    def __str__(self) -> str:
        queue_str = ""
        node = self.head
        while node:
            queue_str += str(node.value) + '->'
            node = node.next
        return queue_str[:-2]
    
    def enqueue(self, value):
        new_node = QueueFifoNode(value)
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

    def dequeue(self):
        if self.queueLength() == 0:
            Exception("You cannot delete an element from an empty queue")
        removed = self.head.value
        self.head = self.head.next
        self.count -= 1
        return removed

if __name__ == "__main__":
    queue = QueueFifo(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print(queue)
    remove = queue.dequeue()
    
    print("Removing from queue: ")
    print(remove)
    
    print("NEW QUEUE")
    print(queue)

        
        