"""
Модуль strategies.py
Содержит стратегии сортировки, фильтрации и обработки объектов.
Работает с классами из lab03 (ProfessionalTeam, AmateurTeam, YouthTeam).
Все функции и классы задокументированы.
"""


# ===== СТРАТЕГИИ СОРТИРОВКИ =====

def by_name(team) -> str:
    """
    Стратегия сортировки по имени команды (регистронезависимо).
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        str: Имя в нижнем регистре
    """
    return team.name.lower()


def by_points(team) -> float:
    """
    Стратегия сортировки по очкам (по убыванию).
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        float: Отрицательные очки для сортировки по убыванию
    """
    return -team.total_points


def by_bmi(team) -> float:
    """
    Стратегия сортировки по ИМТ (по возрастанию).
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        float: Значение ИМТ
    """
    return team.avg_bmi()


def by_performance(team) -> float:
    """
    Стратегия сортировки по производительности (по убыванию).
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        float: Отрицательная производительность
    """
    return -team.performance_score()


def by_division_and_name(team) -> tuple:
    """
    Стратегия сортировки: сначала по дивизиону, затем по имени.
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        tuple: (дивизион, имя в нижнем регистре)
    """
    return (team.division, team.name.lower())


# ===== ФУНКЦИИ-ФИЛЬТРЫ =====

def is_active(team) -> bool:
    """
    Фильтр: активные команды.
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        bool: True если команда активна
    """
    return team.is_active


def is_beginner(team) -> bool:
    """
    Фильтр: команды из дивизиона 'beginner'.
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        bool: True если division == 'beginner'
    """
    return team.division == "beginner"


def has_high_performance(team) -> bool:
    """
    Фильтр: команды с производительностью > 20.
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        bool: True если performance_score() > 20
    """
    return team.performance_score() > 20


def is_professional(team) -> bool:
    """
    Фильтр: профессиональные команды.
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        bool: True если ProfessionalTeam
    """
    from two_sem.lab03.models import ProfessionalTeam
    return isinstance(team, ProfessionalTeam)


def is_youth(team) -> bool:
    """
    Фильтр: молодёжные команды.
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        bool: True если YouthTeam
    """
    from two_sem.lab03.models import YouthTeam
    return isinstance(team, YouthTeam)


# ===== ФУНКЦИИ ДЛЯ map =====

def get_name(team) -> str:
    """
    Извлекает имя команды.
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        str: Имя команды
    """
    return team.name


def get_performance(team) -> float:
    """
    Извлекает производительность команды.
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        float: Значение performance_score()
    """
    return team.performance_score()


def get_team_summary(team) -> str:
    """
    Создаёт краткую сводку по команде.
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        str: Строка с информацией
    """
    return f"{team.name} ({team.division}) - Очки: {team.total_points}, Произв.: {team.performance_score():.2f}"


def get_team_dict(team) -> dict:
    """
    Преобразует команду в словарь.
    
    Args:
        team: Объект команды из lab03
    
    Returns:
        dict: Словарь с данными
    """
    return {
        "name": team.name,
        "type": type(team).__name__,
        "division": team.division,
        "points": team.total_points,
        "bmi": team.avg_bmi(),
        "performance": team.performance_score(),
        "active": team.is_active
    }


# ===== ФАБРИКА ФУНКЦИЙ =====

def make_division_filter(division: str):
    """
    Фабричная функция: создаёт фильтр по дивизиону.
    
    Args:
        division: Название дивизиона
    
    Returns:
        function: Функция-фильтр
    """
    def filter_fn(team) -> bool:
        return team.division == division
    filter_fn.__doc__ = f"Фильтр: команды в дивизионе '{division}'"
    return filter_fn


def make_points_filter(min_points: float):
    """
    Фабричная функция: создаёт фильтр по минимальным очкам.
    
    Args:
        min_points: Минимальное значение очков
    
    Returns:
        function: Функция-фильтр
    """
    def filter_fn(team) -> bool:
        return team.total_points >= min_points
    filter_fn.__doc__ = f"Фильтр: команды с очками >= {min_points}"
    return filter_fn


# ===== CALLABLE-ОБЪЕКТЫ (ПАТТЕРН СТРАТЕГИЯ) =====

class ActivateAllStrategy:
    """
    Стратегия: активация всех команд.
    Использует метод activate().
    """
    
    def __call__(self, team) -> object:
        """
        Активирует команду, если она неактивна.
        
        Args:
            team: Объект команды
        
        Returns:
            Та же команда
        """
        if not team.is_active:
            team.activate()
        return team


class SetDivisionStrategy:
    """
    Стратегия: перевод команд в указанный дивизион.
    """
    
    def __init__(self, target_division: str):
        """
        Args:
            target_division: Целевой дивизион
        """
        self.target_division = target_division
    
    def __call__(self, team) -> object:
        """
        Переводит команду в другой дивизион.
        
        Args:
            team: Объект команды
        
        Returns:
            Та же команда
        """
        if team.division != self.target_division:
            team.set_division(self.target_division)
        return team


class AddPointsStrategy:
    """
    Стратегия: добавление очков командам.
    """
    
    def __init__(self, points: float):
        """
        Args:
            points: Количество очков для добавления
        """
        self.points = points
    
    def __call__(self, team) -> object:
        """
        Добавляет очки команде.
        
        Args:
            team: Объект команды
        
        Returns:
            Та же команда
        """
        team.add_points(self.points)
        return team


class TeamInfoStrategy:
    """
    Стратегия: вывод информации о команде.
    Не модифицирует команду.
    """
    
    def __call__(self, team) -> object:
        """
        Выводит информацию о команде.
        
        Args:
            team: Объект команды
        
        Returns:
            Та же команда без изменений
        """
        print(f"\n{'='*40}")
        print(f"  Команда: {team.name}")
        print(f"  Тип: {type(team).__name__}")
        print(f"  Дивизион: {team.division}")
        print(f"  Очки: {team.total_points}")
        print(f"  ИМТ: {team.avg_bmi()}")
        print(f"  Производительность: {team.performance_score():.2f}")
        print(f"  Активна: {'да' if team.is_active else 'нет'}")
        print(f"{'='*40}")
        return team