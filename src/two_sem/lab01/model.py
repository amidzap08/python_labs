from datetime import datetime


class Athlete: #1 Один пользовательский класс 

    # Атрибуты класса
    sport_type_list = ["Футбол", "Баскетбол", "Плавание", "Легкая атлетика", "Теннис", "Бокс"]
    min_age = 14
    max_age = 50
    
    def __init__(self, name: str, age: int, sport_type: str, weight: float, personal_record: float = 0):#3/ конструктор с проверкой
#2/ 6 закрытых атрибутов 
        self._name = None
        self._age = None
        self._sport_type = None
        self._weight = None
        self._personal_record = None
        self._is_active = True  #по умолчанию спортсмен активен
        
        # Используем свойства для установки значений с валидацией 
        self.name = name
        self.age = age
        self.sport_type = sport_type
        self.weight = weight
        self.personal_record = personal_record
    
    # Валидация отдельных полей
    def _validate_name(self, name: str) -> None:
        #проверка корректности имени
        if not isinstance(name, str):
            raise ValueError("Имя должно быть строкой")
        if not name.strip():
            raise ValueError("Имя не может быть пустым")
        if len(name) < 2:
            raise ValueError("Имя должно содержать минимум 2 символа")
        if len(name) > 50:
            raise ValueError("Имя не может быть длиннее 50 символов")
    
    def _validate_age(self, age: int) -> None:
        """Проверка корректности возраста"""
        if not isinstance(age, int):
            raise ValueError("Возраст должен быть целым числом")
        if age < Athlete.min_age or age > Athlete.max_age:
            raise ValueError(f"Возраст должен быть от {Athlete.min_age} до {Athlete.max_age} лет")
    
    def _validate_sport_type(self, sport_type: str) -> None:
        """Проверка корректности вида спорта"""
        if not isinstance(sport_type, str):
            raise ValueError("Вид спорта должен быть строкой")
        if sport_type not in Athlete.sport_type_list:
            raise ValueError(f"Вид спорта должен быть одним из: {', '.join(Athlete.sport_type_list)}")
    
    def _validate_weight(self, weight: float) -> None:
        """Проверка корректности веса"""
        if not isinstance(weight, (int, float)):
            raise ValueError("Вес должен быть числом")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        if weight > 200:
            raise ValueError("Вес не может превышать 200 кг")
    
    def _validate_personal_record(self, record: float) -> None:
        """Проверка корректности личного рекорда"""
        if not isinstance(record, (int, float)):
            raise ValueError("Личный рекорд должен быть числом")
        if record < 0:
            raise ValueError("Личный рекорд не может быть отрицательным")
    
    # Свойства (геттеры и сеттеры)
    @property #4 Свойства для чтения Геттеры для доступа к данным
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
    def weight(self, value: float) -> None: #4 cеттеры с валидацией 
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
        if not self._is_active:
            raise ValueError("Нельзя обновить рекорд неактивного спортсмена")
        
        self._validate_personal_record(new_record)
        
        if new_record > self._personal_record:
            old_record = self._personal_record
            self._personal_record = new_record
            return f"Рекорд улучшен! Был: {old_record:.2f}, стал: {new_record:.2f}"
        elif new_record < self._personal_record:
            return f"Новый результат ({new_record:.2f}) хуже текущего рекорда ({self._personal_record:.2f})"
        else:
            return f"Результат равен текущему рекорду ({self._personal_record:.2f})"
    
    def train(self, hours: float) -> str: #7 бизнес-метод, метод тренировки
        if not self._is_active:
            raise ValueError("Нельзя тренировать неактивного спортсмена")
        
        if not isinstance(hours, (int, float)):
            raise ValueError("Количество часов должно быть числом")
        if hours <= 0:
            raise ValueError("Количество часов должно быть положительным")
        if hours > 8:
            raise ValueError("Тренировка не может длиться более 8 часов")
        
        # Логика, зависящая от состояния (возраста)
        if self._age < 18:
            max_hours = 4
            if hours > max_hours:
                return f"Спортсмену до 18 лет рекомендуется тренироваться не более {max_hours} часов. Вы указали {hours} ч."
        
        # Расчет сожженных калорий (упрощенно)
        calories_per_hour = 300 + (self._weight * 2)
        total_calories = calories_per_hour * hours
        
        return (f"{self._name} провел тренировку длительностью {hours} ч. "
                f"Сожжено примерно {total_calories:.0f} ккал.")
    
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

        # Для расчета ИМТ нужен рост, но у нас его нет, поэтому используем упрощенную формулу
        height = 1.75  # условный средний рост
        bmi = self._weight / (height ** 2)
        return round(bmi, 2)
    
    def get_age_category(self) -> str:

        if self._age < 18:
            return "Юниор"
        elif self._age < 35:
            return "Взрослый"
        else:
            return "Ветеран"
    
    # Магические методы
    def __str__(self) -> str: #5/ cтроковое представление
        """
        Строковое представление для пользователей
        """
        status = "активен" if self._is_active else "неактивен"
        return (f"Спортсмен: {self._name} | Возраст: {self._age} | "
                f"Вид спорта: {self._sport_type} | Вес: {self._weight:.1f} кг | "
                f"Рекорд: {self._personal_record:.2f} | Статус: {status}")
    
    def __repr__(self) -> str:  #4  Официальное строковое представление для разработчиков

        return (f"Athlete(name='{self._name}', age={self._age}, "
                f"sport_type='{self._sport_type}', weight={self._weight}, "
                f"personal_record={self._personal_record})")
    
    def __eq__(self, other) -> bool: #6 /cравнение по имени и виду спорта
        if not isinstance(other, Athlete):
            return False
        return (self._name == other._name and 
                self._sport_type == other._sport_type)