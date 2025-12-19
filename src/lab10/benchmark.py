import time
import random
from lab10.structures import Stack, Queue
from lab10.linked_list import SinglyLinkedList


def benchmark_push_pop(n: int = 100000) -> dict:
    """Бенчмарк для операций push/pop (стек)"""
    stack = Stack()
    
    # Замер push
    start = time.time()
    for i in range(n):
        stack.push(i)
    push_time = time.time() - start
    
    # Замер pop
    start = time.time()
    for _ in range(n):
        stack.pop()
    pop_time = time.time() - start
    
    return {"push": push_time, "pop": pop_time}


def benchmark_enqueue_dequeue(n: int = 100000) -> dict:
    """Бенчмарк для операций enqueue/dequeue (очередь)"""
    queue = Queue()
    
    # Замер enqueue
    start = time.time()
    for i in range(n):
        queue.enqueue(i)
    enqueue_time = time.time() - start
    
    # Замер dequeue
    start = time.time()
    for _ in range(n):
        queue.dequeue()
    dequeue_time = time.time() - start
    
    return {"enqueue": enqueue_time, "dequeue": dequeue_time}


def benchmark_linked_list_append(n: int = 10000) -> float:
    """Бенчмарк для операции append (связный список)"""
    linked_list = SinglyLinkedList()
    
    start = time.time()
    for i in range(n):
        linked_list.append(i)
    
    return time.time() - start


def benchmark_list_append(n: int = 10000) -> float:
    """Бенчмарк для операции append (встроенный список)"""
    lst = []
    
    start = time.time()
    for i in range(n):
        lst.append(i)
    
    return time.time() - start


def run_benchmarks():
    """Запуск всех бенчмарков"""
    n = 10000
    
    print("=== Бенчмарки структур данных ===")
    print(f"Количество операций: {n}")
    print()
    
    # Стек
    stack_results = benchmark_push_pop(n)
    print(f"Stack.push(): {stack_results['push']:.6f} сек")
    print(f"Stack.pop():  {stack_results['pop']:.6f} сек")
    print()
    
    # Очередь
    queue_results = benchmark_enqueue_dequeue(n)
    print(f"Queue.enqueue(): {queue_results['enqueue']:.6f} сек")
    print(f"Queue.dequeue(): {queue_results['dequeue']:.6f} сек")
    print()
    
    # Связный список vs встроенный список
    ll_time = benchmark_linked_list_append(n)
    list_time = benchmark_list_append(n)
    print(f"SinglyLinkedList.append(): {ll_time:.6f} сек")
    print(f"list.append():            {list_time:.6f} сек")
    print(f"Отношение (linked_list / list): {ll_time / list_time:.2f}")
    print()
    
    # Сравнение insert в начало
    print("=== Вставка в начало ===")
    
    # SinglyLinkedList
    ll = SinglyLinkedList()
    start = time.time()
    for i in range(1000):
        ll.prepend(i)
    ll_prepend_time = time.time() - start
    
    # list
    lst = []
    start = time.time()
    for i in range(1000):
        lst.insert(0, i)  # O(n) операция!
    list_insert0_time = time.time() - start
    
    print(f"SinglyLinkedList.prepend(): {ll_prepend_time:.6f} сек")
    print(f"list.insert(0, item):       {list_insert0_time:.6f} сек")
    print(f"Отношение (list / linked_list): {list_insert0_time / ll_prepend_time:.2f}")


if __name__ == "__main__":
    run_benchmarks()