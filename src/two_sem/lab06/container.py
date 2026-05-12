"""
Модуль container.py для лабораторной работы №6
Реализация Generic-коллекции TypedCollection с поддержкой протоколов
Основана на TeamCollection из ЛР-2
"""

from typing import TypeVar, Generic, Callable, Optional, List, Protocol, Iterator, Union, Any


# ============ Определение TypeVar ============

T = TypeVar('T')
R = TypeVar('R')


# ============ Определение Protocol (Задание на 5) ============

class Displayable(Protocol):
    """Протокол для объектов, которые можно отобразить."""
    def display(self) -> str:
        ...


class Scorable(Protocol):
    """Протокол для объектов, которые можно оценить."""
    def score(self) -> float:
        ...


# TypeVar с ограничениями на протоколы
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)


# ============ Класс TypedCollection ============

class TypedCollection(Generic[T]):
    """
    Generic-версия коллекции для хранения объектов любого типа T.
    Повторяет интерфейс TeamCollection из ЛР-2, но теперь знает тип хранимых элементов.
    Поддерживает операции добавления, удаления, поиска, фильтрации и трансформации.
    """
    
    def __init__(self) -> None:
        """Инициализация пустой коллекции."""
        self._items: List[T] = []
    
    # ============= Задание на 3: Базовые методы с аннотациями типов =============
    
    def add(self, item: T) -> None:
        """
        Добавить элемент в коллекцию.
        
        Args:
            item: Объект типа T для добавления
            
        Raises:
            TypeError: Если добавляемый объект не соответствует типу T
        """
        self._items.append(item)
    
    def remove(self, item: T) -> bool:
        """
        Удалить элемент из коллекции.
        
        Args:
            item: Объект типа T для удаления
            
        Returns:
            bool: True если удаление успешно, False если элемент не найден
        """
        try:
            self._items.remove(item)
            return True
        except ValueError:
            return False
    
    def get_all(self) -> List[T]:
        """
        Вернуть список всех элементов коллекции.
        
        Returns:
            List[T]: Копия списка элементов
        """
        return self._items.copy()
    
    # ============= Методы из TeamCollection ЛР-2 =============
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в коллекции.
        
        Returns:
            int: Размер коллекции
        """
        return len(self._items)
    
    def __iter__(self) -> Iterator[T]:
        """
        Возвращает итератор для обхода коллекции.
        
        Returns:
            Iterator[T]: Итератор по элементам типа T
        """
        return iter(self._items)
    
    def __contains__(self, item: T) -> bool:
        """
        Проверка наличия элемента в коллекции.
        
        Args:
            item: Объект типа T для проверки
            
        Returns:
            bool: True если элемент присутствует в коллекции
        """
        return item in self._items
    
    def clear(self) -> None:
        """Очистить коллекцию."""
        self._items.clear()
    
    def is_empty(self) -> bool:
        """
        Проверить, пуста ли коллекция.
        
        Returns:
            bool: True если коллекция пуста
        """
        return len(self._items) == 0
    
    # ============= Задание на 4: Методы с функциями высшего порядка =============
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """
        Поиск первого элемента, удовлетворяющего условию.
        
        Args:
            predicate: Функция-условие, принимающая элемент типа T и возвращающая bool
            
        Returns:
            Optional[T]: Первый подходящий элемент или None, если ничего не найдено
            
        Example:
            team = collection.find(lambda t: t.name == "Чемпионы")
        """
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """
        Фильтрация элементов по условию.
        
        Args:
            predicate: Функция-условие, принимающая элемент типа T и возвращающая bool
            
        Returns:
            List[T]: Список элементов, удовлетворяющих условию
            
        Example:
            active_teams = collection.filter(lambda t: t.is_active)
        """
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        """
        Применение функции-преобразования к каждому элементу.
        Тип результата может отличаться от типа элементов коллекции.
        
        Args:
            transform: Функция-преобразование, принимающая T и возвращающая R
            
        Returns:
            List[R]: Список результатов преобразования (тип R может отличаться от T)
            
        Example:
            names = collection.map(lambda t: t.name)  # List[str]
            scores = collection.map(lambda t: t.performance_score())  # List[float]
        """
        return [transform(item) for item in self._items]
    
    # ============= Строковые представления =============
    
    def __str__(self) -> str:
        """Строковое представление коллекции."""
        if not self._items:
            return "TypedCollection: пусто"
        
        result = f"TypedCollection ({len(self._items)} элементов):\n"
        for i, item in enumerate(self._items, 1):
            result += f"  {i}. {item}\n"
        return result
    
    def __repr__(self) -> str:
        """Подробное строковое представление коллекции."""
        return f"TypedCollection({repr(self._items)})"