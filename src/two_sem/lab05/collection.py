"""
Расширенная коллекция команд с поддержкой функций высшего порядка.
Работает с любыми объектами, имеющими интерфейс Team.
"""
from typing import Callable, List, Any


class FunctionalTeamCollection:
    """
    Автономная коллекция с методами функционального программирования.
    Не зависит от TeamCollection из lab02, но совместима с объектами из lab03.
    """
    
    def __init__(self):
        self._items = []
    
    def add(self, team) -> None:
        """
        Добавить команду в коллекцию (без проверки типов).
        
        Args:
            team: Объект команды
        """
        self._items.append(team)
    
    def sort_by(self, key_func: Callable) -> 'FunctionalTeamCollection':
        """
        Сортирует коллекцию на месте по ключевой функции.
        
        Args:
            key_func: Функция, принимающая объект и возвращающая ключ сортировки
        
        Returns:
            self для цепочки вызовов
        """
        self._items.sort(key=key_func)
        return self
    
    def filter_by(self, predicate: Callable) -> 'FunctionalTeamCollection':
        """
        Создаёт новую коллекцию из объектов, удовлетворяющих предикату.
        
        Args:
            predicate: Функция, принимающая объект и возвращающая bool
        
        Returns:
            FunctionalTeamCollection с отфильтрованными объектами
        """
        filtered = FunctionalTeamCollection()
        for item in self._items:
            if predicate(item):
                filtered._items.append(item)
        return filtered
    
    def apply(self, func: Callable) -> 'FunctionalTeamCollection':
        """
        Применяет функцию ко всем объектам в коллекции.
        
        Args:
            func: Функция, принимающая объект
        
        Returns:
            self для цепочки вызовов
        """
        for item in self._items:
            func(item)
        return self
    
    def get_items(self) -> List:
        """Получить список всех объектов."""
        return self._items.copy()
    
    def __iter__(self):
        return iter(self._items)
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __getitem__(self, index: int):
        return self._items[index]