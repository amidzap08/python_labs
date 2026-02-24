from collections import deque
from typing import Any, Optional
# pop(0) был бы O(n) (нужно сдвигать все элементы)
#O(1) означает, что время выполнения операции не зависит от размера данных.

class Stack:
    #cтек (LIFO) на базе list. как стопка тарелок
    __slots__ = ("_data",)

    def __init__(self, iterable=None) -> None:
        self._data: list[Any] = list(iterable) if iterable is not None else []

    def push(self, item: Any) -> None: 
        self._data.append(item)

    #добавляет элемент в конец списка
    def pop(self) -> Any:
        if not self._data:
            raise IndexError("pop from empty Stack")
        return self._data.pop()
    #удаление и возврат элемента

  #метод просмотра верхнего элемента без удаления
  #возвращает последний элемент или None, если стек пуст
    def peek(self) -> Optional[Any]:
        return self._data[-1] if self._data else None

    #метод проверки стека на пустоту
    def is_empty(self) -> bool:
        return not self._data

#возвращает количество элементов
    def __len__(self) -> int:
        return len(self._data)
#строковое представление для отладки
    def __repr__(self) -> str:
        return f"Stack({self._data!r})"


class Queue:
    #oчередь (FIFO) на базе collections.deque.как очередь в магазине
#Использует collections.deque — двустороннюю очередь
#deque оптимизирован для быстрых операций с обоих концов

    __slots__ = ("_data",)

    def __init__(self, iterable=None) -> None:
        self._data: deque[Any] = deque(iterable) if iterable is not None else deque()
#добавление в очередь
    def enqueue(self, item: Any) -> None:
        self._data.append(item)
#удаление из очереди/Удаляет элемент из начала очереди
    def dequeue(self) -> Any:
        if not self._data:
            raise IndexError("dequeue from empty Queue")
        return self._data.popleft()
# просмотр первого элемента
    def peek(self) -> Optional[Any]:
        return self._data[0] if self._data else None

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)!r})"

print('Stack')

stack = Stack([1,2,3,4])
print(f'Снятие верхнего элемента стека : {stack.pop()}')
print(f'Пустой ли стек? {stack.is_empty()}')
print(f'Число сверху : {stack.peek()}')
stack.push(1)
print(f'Значение сверху после добавления числа в стек : {stack.peek()}')
print(f'Длина стека : {len(stack)}')
print(f'Стек : {stack._data}')

print('Deque')

q = Queue([1,2,3,4])

print(f'Значение первого эллемента : {q.peek()}')
q.dequeue()
print(f'Значение первого эллемента после удаления числа : {q.peek()}')
q.enqueue(52)
print(f'Значение первого эллемента после добавления числа : {q.peek()}')
print(f'Пустая ли очередь? {q.is_empty()}')
print(f'Количество элементов в очереди : {len(q)}')