class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        self._size -= 1
        return temp.data

    def size(self):
        return self._size

if __name__ == "__main__":
    q = Queue()
    n = int(input())  # Number of operations

    for _ in range(n):
        operation = input().split()

        if operation[0] == "enqueue":
            q.enqueue(int(operation[1]))
        elif operation[0] == "dequeue":
            result = q.dequeue()
            if result is not None:
                print(result)
        elif operation[0] == "size":
            print(q.size())
