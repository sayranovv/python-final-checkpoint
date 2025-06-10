class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value): # Добавить элемент в конец очереди
        node = Node(value)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node

    def dequeue(self): # Удалить элемент из начала очереди и вернуть его
        if self.is_empty():
            raise IndexError("Удаление из пустой очереди")
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value

    def peek(self): # Вернуть начало очереди без удаления
        if self.is_empty():
            raise IndexError("Peek из пустой очереди")
        return self.head.value

class UglyNumbersGenerator:
    # Инициализируем три очереди для множителей 2, 3 и 5
    def __init__(self):
        self.queue2 = Queue()
        self.queue3 = Queue()
        self.queue5 = Queue()

    def get_numbers(self, n):
        # Возвращает список из первых n чисел, простые множители которых – только 2,3,5.
        # Бросает ValueError при некорректном n.
        if not isinstance(n, int):
            raise ValueError("n должно быть целым числом")
        if n <= 0:
            raise ValueError("n должно быть положительным")

        self.queue2 = Queue()
        self.queue3 = Queue()
        self.queue5 = Queue()

        numbers = []
        current = 1
        numbers.append(current)

        # Инициализируем очереди первыми умноженными значениями
        self.queue2.enqueue(current * 2)
        self.queue3.enqueue(current * 3)
        self.queue5.enqueue(current * 5)

        # Генерируем оставшиеся n-1 чисел
        while len(numbers) < n:
            # Берем наименьшее число из трех очередей
            next_val = min(self.queue2.peek(), self.queue3.peek(), self.queue5.peek())
            numbers.append(next_val)

            # Убираем совпадения из всех очередей и добавляем новые элементы
            if next_val == self.queue2.peek():
                self.queue2.dequeue()
            if next_val == self.queue3.peek():
                self.queue3.dequeue()
            if next_val == self.queue5.peek():
                self.queue5.dequeue()

            # Генерируем новые кандидаты на основе next_val
            self.queue2.enqueue(next_val * 2)
            self.queue3.enqueue(next_val * 3)
            self.queue5.enqueue(next_val * 5)

        return numbers

def main():
    gen = UglyNumbersGenerator()
    try:
        n_input = input("Введите количество чисел n: ")
        n = int(n_input)
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    if n <= 0:
        print("Ошибка: n должно быть положительным.")
        return

    try:
        result = gen.get_numbers(n)
        print("\nПервые", n, "чисел (с простыми множителями только 2,3,5):")
        print(' '.join(map(str, result)))
    except Exception as e:
        print("Ошибка:", e)

if __name__ == '__main__':
    main()