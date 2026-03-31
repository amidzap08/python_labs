"""
Модуль collection.py - класс Team (коллекция спортсменов)
"""

from typing import List, Optional, Callable
from two_sem.lab01.model import Athlete


class Team:
    """
    Класс Team - коллекция спортсменов
    Управляет группой объектов Athlete
    """
    
    def __init__(self, name: str = ""):
        """
        Конструктор коллекции
        
        Args:
            name: Название команды
        """
        self._name = name
        self._items: List[Athlete] = []
    
    @property
    def name(self) -> str:
        """Получить название команды"""
        return self._name
    
    @name.setter
    def name(self, value: str):
        """Установить название команды"""
        self._name = value
    
    def add(self, athlete: Athlete) -> bool:
        """
        Добавить спортсмена в команду
        
        Args:
            athlete: Объект Athlete для добавления
            
        Returns:
            bool: True если добавление успешно, False если спортсмен уже существует
            
        Raises:
            TypeError: Если передан не объект Athlete
        """
        # Проверяем тип
        if not isinstance(athlete, Athlete):
            raise TypeError("Можно добавлять только объекты класса Athlete")
        
        # Проверка на дубликат по имени (как уникальному идентификатору)
        if self.find_by_name(athlete.name) is not None:
            return False
        
        self._items.append(athlete)
        return True
    
    def remove(self, athlete: Athlete) -> bool:
        """
        Удалить спортсмена из команды
        
        Args:
            athlete: Объект Athlete для удаления
            
        Returns:
            bool: True если удаление успешно, False если спортсмен не найден
        """
        if athlete in self._items:
            self._items.remove(athlete)
            return True
        return False
    
    def remove_at(self, index: int) -> Optional[Athlete]:
        """
        Удалить спортсмена по индексу
        
        Args:
            index: Индекс элемента для удаления
            
        Returns:
            Optional[Athlete]: Удаленный спортсмен или None если индекс недействителен
        """
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        return None
    
    def get_all(self) -> List[Athlete]:
        """
        Получить список всех спортсменов
        
        Returns:
            List[Athlete]: Копия списка спортсменов
        """
        return self._items.copy()
    
    def find_by_name(self, name: str) -> Optional[Athlete]:
        """
        Найти спортсмена по имени
        
        Args:
            name: Имя спортсмена
            
        Returns:
            Optional[Athlete]: Найденный спортсмен или None
        """
        for athlete in self._items:
            if athlete.name.lower() == name.lower():
                return athlete
        return None
    
    def find_by_training_level(self, level: str) -> List[Athlete]:
        """
        Найти спортсменов по уровню подготовки
        
        Args:
            level: Уровень подготовки
            
        Returns:
            List[Athlete]: Список найденных спортсменов
        """
        return [a for a in self._items if a.training_level == level]
    
    def find_by_health_status(self, status: str) -> List[Athlete]:
        """
        Найти спортсменов по статусу здоровья
        
        Args:
            status: Статус здоровья
            
        Returns:
            List[Athlete]: Список найденных спортсменов
        """
        return [a for a in self._items if a.health_status == status]
    
    def find_active(self) -> List[Athlete]:
        """
        Найти активных спортсменов
        
        Returns:
            List[Athlete]: Список активных спортсменов
        """
        return [a for a in self._items if a.is_active]
    
    def find_by_performance(self, min_score: float = 0) -> List[Athlete]:
        """
        Найти спортсменов с производительностью выше заданного порога
        
        Args:
            min_score: Минимальное значение производительности
            
        Returns:
            List[Athlete]: Список найденных спортсменов
        """
        return [a for a in self._items if a.performance_score() >= min_score]
    
    def __len__(self) -> int:
        """Возвращает количество спортсменов в команде"""
        return len(self._items)
    
    def __iter__(self):
        """Возвращает итератор по спортсменам"""
        return iter(self._items)
    
    def __getitem__(self, index):
        """
        Доступ к спортсмену по индексу
        
        Args:
            index: Индекс или срез
            
        Returns:
            Athlete или список спортсменов
        """
        return self._items[index]
    
    def __setitem__(self, index, value):
        """Установка спортсмена по индексу"""
        if not isinstance(value, Athlete):
            raise TypeError("Можно устанавливать только объекты класса Athlete")
        self._items[index] = value
    
    def sort(self, key: Optional[Callable] = None, reverse: bool = False):
        """
        Сортировка спортсменов
        
        Args:
            key: Функция для получения ключа сортировки
            reverse: Сортировать в обратном порядке
        """
        if key is None:
            self._items.sort(reverse=reverse)
        else:
            self._items.sort(key=key, reverse=reverse)
    
    def sort_by_name(self, reverse: bool = False):
        """Сортировка по имени"""
        self.sort(key=lambda a: a.name, reverse=reverse)
    
    def sort_by_record(self, reverse: bool = False):
        """Сортировка по личному рекорду"""
        self.sort(key=lambda a: a.personal_record, reverse=reverse)
    
    def sort_by_performance(self, reverse: bool = False):
        """Сортировка по производительности"""
        self.sort(key=lambda a: a.performance_score(), reverse=reverse)
    
    def sort_by_bmi(self, reverse: bool = False):
        """Сортировка по индексу массы тела"""
        self.sort(key=lambda a: a.bmi(), reverse=reverse)
    
    def get_active_athletes(self) -> 'Team':
        """
        Получить новую коллекцию только с активными спортсменами
        
        Returns:
            Team: Новая коллекция с активными спортсменами
        """
        active_team = Team(f"{self._name} (активные)")
        for athlete in self._items:
            if athlete.is_active:
                active_team.add(athlete)
        return active_team
    
    def get_healthy_athletes(self) -> 'Team':
        """
        Получить новую коллекцию только со здоровыми спортсменами
        
        Returns:
            Team: Новая коллекция со здоровыми спортсменами
        """
        healthy_team = Team(f"{self._name} (здоровые)")
        for athlete in self._items:
            if athlete.health_status == "healthy":
                healthy_team.add(athlete)
        return healthy_team
    
    def get_by_training_level(self, level: str) -> 'Team':
        """
        Получить новую коллекцию спортсменов с заданным уровнем подготовки
        
        Args:
            level: Уровень подготовки
            
        Returns:
            Team: Новая коллекция с отфильтрованными спортсменами
        """
        filtered_team = Team(f"{self._name} ({level})")
        for athlete in self._items:
            if athlete.training_level == level:
                filtered_team.add(athlete)
        return filtered_team
    
    def __str__(self) -> str:
        """Строковое представление коллекции"""
        if not self._items:
            return f"Команда '{self._name}' пуста"
        
        result = f"Команда '{self._name}' (всего: {len(self._items)} спортсменов):\n"
        for i, athlete in enumerate(self._items, 1):
            result += f"  {i}. {athlete.name} (рекорд: {athlete.personal_record}, "
            result += f"уровень: {athlete.training_level}, статус: {'активен' if athlete.is_active else 'неактивен'})\n"
        return result
    
    def __repr__(self) -> str:
        """Отладочное представление коллекции"""
        return f"Team(name='{self._name}', athletes={len(self._items)})"