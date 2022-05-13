class Queue:
    def __init__(self,size =100):
        self.queue = [0 for _ in range(size)]

        self.rear = 0
        self.font = 0
        self.size = size

    def push(self,elem):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = elem

        else:
            raise IndexError("Queue is empty")


    def pop(self):
        if not self.is_empty():

            self.font = (self.font+1)%self.size
            return self.queue[self.font]
        else:

            raise IndexError('Queue is empty')
    def is_empty(self):
        return self.rear == self.font
    def is_full(self):
        return (self.rear+1)%self.size == self.font
a = Queue(10)
for i in range(9):
    a.push(i)
print(a.is_full())
print(a.pop())