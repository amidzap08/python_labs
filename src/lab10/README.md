# Лабораторная работа 10!!!
## Теоретическая часть

### Стек (Stack)
#### Стек - структура данных типа LIFO (Last In First Out), где последний добавленный элемент извлекается первым.

### Основные операции:

#### push(item) - добавить элемент на вершину стека (O(1))
#### pop() - удалить и вернуть верхний элемент (O(1))
#### peek() - посмотреть верхний элемент без удаления (O(1))
#### is_empty() - проверить пустоту стека (O(1)) 

### Типичные применения:

#### история действий (undo/redo);
#### обход графа/дерева в глубину (DFS);
#### парсинг выражений, проверка скобок.




## Очередь (Queue)
### Очередь - структура данных типа FIFO (First In First Out), где первый добавленный элемент извлекается первым.

### Основные операции:

#### enqueue(item) - добавить элемент в конец очереди (O(1))
#### dequeue() - удалить и вернуть первый элемент (O(1))
#### peek() - посмотреть первый элемент без удаления (O(1))
#### is_empty() - проверить пустоту очереди (O(1))

### Типичные применения:

#### обработка задач по очереди (job queue);
#### обход графа/дерева в ширину (BFS);
#### буферы (сетевые, файловые, очереди сообщений).


## Односвязный список (Singly Linked List)
### Динамическая структура данных, состоящая из узлов, каждый из которых содержит значение и ссылку на следующий узел.

### Основные операции:

#### append(value) - добавить в конец (O(1) с tail, O(n) без)
#### prepend(value) - добавить в начало (O(1))
#### insert(idx, value) - вставить по индексу (O(n))
#### remove(value) - удалить первое вхождение (O(n))
#### search(value) - поиск элемента (O(n))
#### get(idx) - получение по индексу (O(n))

### Основные идеи:

#### элементы не хранятся подряд в памяти, как в массиве;
#### каждый элемент знает только «следующего соседа».

## Двусвязный список (Doubly Linked List)
### Структура:
#### value — значение элемента;
#### next — ссылку на следующий узел;
#### prev — ссылку на предыдущий узел.
### Основные идеи:

### можно двигаться как вперёд, так и назад по цепочке узлов;
### удобно хранить ссылки на оба конца: head и tail.

## Реализация
## Структуры данных
### 1. Stack (structures.py)
### Реализован на базе списка Python:

#### push() использует list.append() (O(1) амортизированно)
#### pop() использует list.pop() (O(1))
#### При пустом стеке выбрасывается IndexError
### 2. Queue (structures.py)
### Реализован на базе collections.deque:

#### enqueue() использует deque.append() (O(1))
#### dequeue() использует deque.popleft() (O(1))
### При пустой очереди выбрасывается IndexError
## 3. SinglyLinkedList (linked_list.py)
### Реализован с поддержкой tail для ускорения append():

### Хранит ссылки на head и tail
### Поддерживает счетчик элементов _size для O(1) определения длины
### Имеет красивое строковое представление в виде цепи узлов

## Примеры использования
### Стек (LIFO)
```python 
s = Stack()
s.push(1)       # [1]
s.push(2)       # [1, 2]
print(s.pop())  # 2
print(s.pop())  # 1
```
### Очередь (FIFO)
```python
q = Queue()
q.enqueue(1)    # [1]
q.enqueue(2)    # [1, 2]
print(q.dequeue())  # 1
print(q.dequeue())  # 2
```
### Связный список
```python
lst = SinglyLinkedList()
lst.append(1)   # [1]
lst.append(2)   # [1, 2]
lst.prepend(0)  # [0, 1, 2]
print(list(lst))  # [0, 1, 2]
```

## Задание А - Реализовать Stack и Queue (structures.py)
```python
from collections import deque
from typing import Any, Optional


class Stack:
    __slots__ = ("_data",)

    def __init__(self, iterable=None) -> None:
        self._data: list[Any] = list(iterable) if iterable is not None else []

    def push(self, item: Any) -> None: 
        self._data.append(item)

    def pop(self) -> Any:
        if not self._data:
            raise IndexError("pop from empty Stack")
        return self._data.pop()

    def peek(self) -> Optional[Any]:
        return self._data[-1] if self._data else None

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data!r})"


class Queue:

    __slots__ = ("_data",)

    def __init__(self, iterable=None) -> None:
        self._data: deque[Any] = deque(iterable) if iterable is not None else deque()

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if not self._data:
            raise IndexError("dequeue from empty Queue")
        return self._data.popleft()

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
```
![](/src/lab10/images/01.10.png)

## Задание B - Реализовать SinglyLinkedList (linked_list.py)
```python
from typing import Any, Iterator, Optional


class Node:
    __slots__ = ("value", "next")

    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


class SinglyLinkedList:
    __slots__ = ("head", "tail", "_size")

    def __init__(self, iterable=None) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
        if iterable:
            for v in iterable:
                self.append(v)

    def append(self, value: Any) -> None:
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            assert self.tail is not None
            self.tail.next = node
            self.tail = node
        self._size += 1

    def prepend(self, value: Any) -> None:
        node = Node(value, next=self.head)
        self.head = node
        if self._size == 0:
            self.tail = node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("insert index out of range")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return

        prev = self.head
        for _ in range(idx - 1):
            assert prev is not None
            prev = prev.next
        assert prev is not None
        node = Node(value, next=prev.next)
        prev.next = node
        self._size += 1

    def remove(self, value: Any) -> None:
        prev: Optional[Node] = None
        cur = self.head
        idx = 0
        while cur:
            if cur.value == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev
                self._size -= 1
                return
            prev, cur = cur, cur.next
            idx += 1
        raise ValueError("remove: value not found in SinglyLinkedList")

    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError("remove_at index out of range")
        prev: Optional[Node] = None
        cur = self.head
        for _ in range(idx):
            prev, cur = cur, cur.next  # type: ignore
        assert cur is not None
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next
        if cur is self.tail:
            self.tail = prev
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(repr(x) for x in self)}])"

    def __str__(self) -> str:
        parts = []
        cur = self.head
        while cur:
            parts.append(f"[{cur.value!s}]")
            cur = cur.next
        parts.append("None")
        return " -> ".join(parts)

sll = SinglyLinkedList()
print(f'Длина нашего односвязанного списка : {len(sll)}')

sll.append(1)
sll.append(2)
sll.prepend(0)
print(f'Наша ныняшняя длина списка после добавления эллементов : {len(sll)}') 
print(f'Односвязаный список : {list(sll)}')

sll.insert(1, 0.5)
print(f'Длина списка после добавления на 1 индекс числа 0.5 : {len(sll)}')
print(f'Односвязаный список : {list(sll)}')
sll.append(52)
print(f'Односвязанный список после добавления числа в конец : {list(sll)}')

print(sll) 
```
![](/src/lab10/images/02.10.png)

## спасибо за курс ура