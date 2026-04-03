class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k              # Запоминаем максимальный размер
        self.queue = []        

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.k

    def enQueue(self, value: int) -> bool:
        # Если мест нет - отказываем
        if self.isFull():
            return False
        
        # Если места есть - просто добавляем в конец
        self.queue.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
            
        # Удаляем первого человека из очереди
        self.queue.pop(0)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[-1]