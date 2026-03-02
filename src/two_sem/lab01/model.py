from datetime import datetime
from two_sem.lab01.validate import AthleteValidator  # Импортируем валидатор


class Athlete:
    """Класс, представляющий спортсмена"""
    
    # Атрибуты класса теперь берутся из валидатора
    sport_type_list = AthleteValidator.ALLOWED_SPORT_TYPES
    min_age = AthleteValidator.MIN_AGE
    max_age = AthleteValidator.MAX_AGE
    
    def __init__(self, name: str, age: int, sport_type: str, weight: float, personal_record: float = 0):
        """Конструктор с проверкой данных через валидатор"""
        # Закрытые атрибуты
        self._name = None
        self._age = None
        self._sport_type = None
        self._weight = None
        self._personal_record = None
        self._is_active = True  # по умолчанию спортсмен активен
        
        # Используем свойства для установки значений с валидацией через валидатор
        self.name = name
        self.age = age
        self.sport_type = sport_type
        self.weight = weight
        self.personal_record = personal_record
    
    # Методы валидации теперь используют валидатор
    def _validate_name(self, name: str) -> None:
        """Проверка корректности имени через валидатор"""
        AthleteValidator.check_name(name)
    
    def _validate_age(self, age: int) -> None:
        """Проверка корректности возраста через валидатор"""
        AthleteValidator.check_age(age)
    
    def _validate_sport_type(self, sport_type: str) -> None:
        """Проверка корректности вида спорта через валидатор"""
        AthleteValidator.check_sport_type(sport_type)
    
    def _validate_weight(self, weight: float) -> None:
        """Проверка корректности веса через валидатор"""
        AthleteValidator.check_weight(weight)
    
    def _validate_personal_record(self, record: float) -> None:
        """Проверка корректности личного рекорда через валидатор"""
        AthleteValidator.check_personal_record(record)
    
    # Свойства (геттеры и сеттеры)
    @property
    def name(self) -> str:
        """Геттер для имени"""
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        """Сеттер для имени с валидацией"""
        self._validate_name(value)
        self._name = value.strip()
    
    @property
    def age(self) -> int:
        """Геттер для возраста"""
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        """Сеттер для возраста с валидацией"""
        self._validate_age(value)
        self._age = value
    
    @property
    def sport_type(self) -> str:
        """Геттер для вида спорта"""
        return self._sport_type
    
    @sport_type.setter
    def sport_type(self, value: str) -> None:
        """Сеттер для вида спорта с валидацией"""
        self._validate_sport_type(value)
        self._sport_type = value
    
    @property
    def weight(self) -> float:
        """Геттер для веса"""
        return self._weight
    
    @weight.setter
    def weight(self, value: float) -> None:
        """Сеттер для веса с валидацией"""
        self._validate_weight(value)
        self._weight = float(value)
    
    @property
    def personal_record(self) -> float:
        """Геттер для личного рекорда"""
        return self._personal_record
    
    @personal_record.setter
    def personal_record(self, value: float) -> None:
        """Сеттер для личного рекорда с валидацией"""
        self._validate_personal_record(value)
        self._personal_record = float(value)
    
    @property
    def is_active(self) -> bool:
        """Геттер для статуса активности"""
        return self._is_active
    
    # Бизнес-методы
    def update_record(self, new_record: float) -> str:
        """Обновление личного рекорда"""
        if not self._is_active:
            raise ValueError("Нельзя обновить рекорд неактивного спортсмена")
        
        # Используем валидатор для проверки нового рекорда
        AthleteValidator.check_personal_record(new_record)
        
        if new_record > self._personal_record:
            old_record = self._personal_record
            self._personal_record = new_record
            return f"Рекорд улучшен! Был: {old_record:.2f}, стал: {new_record:.2f}"
        elif new_record < self._personal_record:
            return f"Новый результат ({new_record:.2f}) хуже текущего рекорда ({self._personal_record:.2f})"
        else:
            return f"Результат равен текущему рекорду ({self._personal_record:.2f})"
    
    def train(self, hours: float) -> str:
        """Метод тренировки с проверкой через валидатор"""
        if not self._is_active:
            raise ValueError("Нельзя тренировать неактивного спортсмена")
        
        # Используем специальный метод валидатора для тренировок с учетом возраста
        warning = AthleteValidator.check_junior_training_hours(hours, self._age)
        
        # Расчет сожженных калорий (упрощенно)
        calories_per_hour = 300 + (self._weight * 2)
        total_calories = calories_per_hour * hours
        
        result = (f"{self._name} провел тренировку длительностью {hours} ч. "
                  f"Сожжено примерно {total_calories:.0f} ккал.")
        
        if warning:
            result = f"ПРЕДУПРЕЖДЕНИЕ: {warning}\n  {result}"
        
        return result
    
    def deactivate(self) -> None:
        """Деактивация спортсмена"""
        if not self._is_active:
            raise ValueError("Спортсмен уже неактивен")
        self._is_active = False
    
    def activate(self) -> None:
        """Активация спортсмена"""
        if self._is_active:
            raise ValueError("Спортсмен уже активен")
        self._is_active = True
    
    def get_bmi(self) -> float:
        """Расчет индекса массы тела"""
        height = 1.75  # условный средний рост
        bmi = self._weight / (height ** 2)
        return round(bmi, 2)
    
    def get_age_category(self) -> str:
        """Определение возрастной категории"""
        if self._age < 18:
            return "Юниор"
        elif self._age < 35:
            return "Взрослый"
        else:
            return "Ветеран"
    
    # Магические методы
    def __str__(self) -> str:
        """Строковое представление для пользователей"""
        status = "активен" if self._is_active else "неактивен"
        return (f"Спортсмен: {self._name} | Возраст: {self._age} | "
                f"Вид спорта: {self._sport_type} | Вес: {self._weight:.1f} кг | "
                f"Рекорд: {self._personal_record:.2f} | Статус: {status}")
    
    def __repr__(self) -> str:
        """Официальное строковое представление для разработчиков"""
        return (f"Athlete(name='{self._name}', age={self._age}, "
                f"sport_type='{self._sport_type}', weight={self._weight}, "
                f"personal_record={self._personal_record})")
    
    def __eq__(self, other) -> bool:
        """Сравнение по имени и виду спорта"""
        if not isinstance(other, Athlete):
            return False
        return (self._name == other._name and 
                self._sport_type == other._sport_type)