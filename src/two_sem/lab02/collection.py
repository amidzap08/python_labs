from typing import List, Optional, Iterator, Callable
from two_sem.lab01.model import Team


class TeamCollection:
    """
    Контейнерный класс для хранения объектов Team.
    Реализует основные операции управления коллекцией.
    """
    
    def __init__(self):
        """Инициализация пустой коллекции."""
        self._items: List[Team] = []
    
    # ============= Задание на 3 =============
    
    def add(self, team: Team) -> None:
        """
        Добавить объект Team в коллекцию.
        
        Args:
            team: Объект Team для добавления
            
        Raises:
            TypeError: Если добавляемый объект не является Team
            ValueError: Если команда с таким именем уже существует
        """
        # Проверка типа
        if not isinstance(team, Team):
            raise TypeError(f"Можно добавлять только объекты Team, получен {type(team).__name__}")
        
        # Проверка на дубликат по имени (задание на 4)
        if self._find_by_name(team.name) is not None:
            raise ValueError(f"Команда с именем '{team.name}' уже существует в коллекции")
        
        self._items.append(team)
    
    def remove(self, team: Team) -> bool:
        """
        Удалить объект Team из коллекции.
        
        Args:
            team: Объект Team для удаления
            
        Returns:
            bool: True если удаление успешно, False если объект не найден
        """
        try:
            self._items.remove(team)
            return True
        except ValueError:
            return False
    
    def get_all(self) -> List[Team]:
        """
        Вернуть список всех объектов в коллекции.
        
        Returns:
            List[Team]: Копия списка объектов
        """
        return self._items.copy()
    
    # ============= Задание на 4 =============
    
    def _find_by_name(self, name: str) -> Optional[Team]:
        """Внутренний метод поиска по имени."""
        for team in self._items:
            if team.name == name:
                return team
        return None
    
    def find_by_name(self, name: str) -> Optional[Team]:
        """
        Поиск команды по имени.
        
        Args:
            name: Имя команды
            
        Returns:
            Optional[Team]: Найденная команда или None
        """
        return self._find_by_name(name)
    
    def find_by_division(self, division: str) -> List[Team]:
        """
        Поиск команд по дивизиону.
        
        Args:
            division: Название дивизиона
            
        Returns:
            List[Team]: Список команд в указанном дивизионе
        """
        return [team for team in self._items if team.division == division]
    
    def find_by_health_status(self, status: str) -> List[Team]:
        """
        Поиск команд по статусу здоровья.
        
        Args:
            status: Статус здоровья (healthy, recovering, injured)
            
        Returns:
            List[Team]: Список команд с указанным статусом здоровья
        """
        return [team for team in self._items if team.health_status == status]
    
    def find_active(self) -> List[Team]:
        """
        Поиск активных команд.
        
        Returns:
            List[Team]: Список активных команд
        """
        return [team for team in self._items if team.is_active]
    
    def __len__(self) -> int:
        """
        Возвращает количество объектов в коллекции.
        
        Returns:
            int: Размер коллекции
        """
        return len(self._items)
    
    def __iter__(self) -> Iterator[Team]:
        """
        Возвращает итератор для обхода коллекции.
        
        Returns:
            Iterator[Team]: Итератор по объектам Team
        """
        return iter(self._items)
    
    # ============= Задание на 5 =============
    
    def __getitem__(self, index: int) -> Team:
        """
        Индексация коллекции с поддержкой отрицательных индексов.
        
        Args:
            index: Индекс элемента (может быть отрицательным)
            
        Returns:
            Team: Объект Team по указанному индексу
            
        Raises:
            IndexError: Если индекс вне диапазона
            TypeError: Если индекс не целое число
        """
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        
        # Преобразуем отрицательный индекс в положительный
        if index < 0:
            index = len(self._items) + index
        
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Индекс {index} вне диапазона (0-{len(self._items)-1})")
        
        return self._items[index]
    
    def remove_at(self, index: int) -> Team:
        """
        Удаление объекта по индексу (с поддержкой отрицательных индексов).
        
        Args:
            index: Индекс элемента для удаления (может быть отрицательным)
            
        Returns:
            Team: Удаленный объект
            
        Raises:
            IndexError: Если индекс вне диапазона
        """
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        
        # Преобразуем отрицательный индекс в положительный
        if index < 0:
            index = len(self._items) + index
        
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Индекс {index} вне диапазона (0-{len(self._items)-1})")
        
        return self._items.pop(index)
    
    def sort(self, key: Optional[Callable[[Team], any]] = None, reverse: bool = False) -> None:
        """
        Сортировка коллекции.
        
        Args:
            key: Функция для получения ключа сортировки
            reverse: Сортировка в обратном порядке
        """
        if key is None:
            # Сортировка по умолчанию по имени
            self._items.sort(key=lambda team: team.name, reverse=reverse)
        else:
            self._items.sort(key=key, reverse=reverse)
    
    def sort_by_name(self, reverse: bool = False) -> None:
        """Сортировка по имени команды."""
        self.sort(key=lambda team: team.name, reverse=reverse)
    
    def sort_by_points(self, reverse: bool = False) -> None:
        """Сортировка по количеству очков."""
        self.sort(key=lambda team: team.total_points, reverse=reverse)
    
    def sort_by_performance(self, reverse: bool = False) -> None:
        """Сортировка по производительности."""
        self.sort(key=lambda team: team.performance_score(), reverse=reverse)
    
    def sort_by_morale(self, reverse: bool = False) -> None:
        """Сортировка по уровню мотивации."""
        self.sort(key=lambda team: team.morale, reverse=reverse)
    
    # Логические операции над коллекцией
    
    def get_active_teams(self) -> 'TeamCollection':
        """
        Получить новую коллекцию только с активными командами.
        
        Returns:
            TeamCollection: Новая коллекция с активными командами
        """
        new_collection = TeamCollection()
        for team in self._items:
            if team.is_active:
                new_collection.add(team)
        return new_collection
    
    def get_healthy_teams(self) -> 'TeamCollection':
        """
        Получить новую коллекцию только со здоровыми командами.
        
        Returns:
            TeamCollection: Новая коллекция со здоровыми командами
        """
        new_collection = TeamCollection()
        for team in self._items:
            if team.health_status == "healthy":
                new_collection.add(team)
        return new_collection
    
    def get_high_performance_teams(self, threshold: float = 100.0) -> 'TeamCollection':
        """
        Получить новую коллекцию команд с производительностью выше порога.
        
        Args:
            threshold: Пороговое значение производительности
            
        Returns:
            TeamCollection: Новая коллекция с высокопроизводительными командами
        """
        new_collection = TeamCollection()
        for team in self._items:
            if team.performance_score() >= threshold:
                new_collection.add(team)
        return new_collection
    
    def get_teams_in_division(self, division: str) -> 'TeamCollection':
        """
        Получить новую коллекцию команд из указанного дивизиона.
        
        Args:
            division: Название дивизиона
            
        Returns:
            TeamCollection: Новая коллекция команд из дивизиона
        """
        new_collection = TeamCollection()
        for team in self._items:
            if team.division == division:
                new_collection.add(team)
        return new_collection
    
    # Дополнительные методы для удобства
    
    def clear(self) -> None:
        """Очистить коллекцию."""
        self._items.clear()
    
    def is_empty(self) -> bool:
        """Проверить, пуста ли коллекция."""
        return len(self._items) == 0
    
    def __contains__(self, team: Team) -> bool:
        """
        Проверка наличия объекта в коллекции.
        
        Args:
            team: Объект Team для проверки
            
        Returns:
            bool: True если объект присутствует в коллекции
        """
        return team in self._items
    
    def __str__(self) -> str:
        """Строковое представление коллекции."""
        if not self._items:
            return "TeamCollection: пусто"
        
        result = f"TeamCollection ({len(self._items)} команд):\n"
        for i, team in enumerate(self._items, 1):
            result += f"{i}. {team.name} - {team.division} - {team.performance_score()} очков производительности\n"
        return result
    
    def __repr__(self) -> str:
        """Подробное строковое представление коллекции."""
        return f"TeamCollection({repr(self._items)})"