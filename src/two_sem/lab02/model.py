"""
Модуль model.py - класс Athlete для ЛР-2
"""

class Athlete:
    """Класс, представляющий спортсмена"""
    
    # Атрибуты класса
    total_athletes = 0
    sport_type = "running"
    default_training_level = "beginner"
    max_morale = 10
    min_morale = 0
    weight_unit = "kg"
    height_unit = "cm"
    record_unit = "kg"
    
    # Допустимые значения
    VALID_TRAINING_LEVELS = ["beginner", "intermediate", "advanced", "professional"]
    VALID_HEALTH_STATUSES = ["healthy", "injured", "recovering"]
    
    # Максимальные рекорды по уровням подготовки
    MAX_RECORD_BY_LEVEL = {
        "beginner": 100,
        "intermediate": 200,
        "advanced": 350,
        "professional": 500
    }
    
    def __init__(self, name, weight, height, personal_record=0, 
                 training_level=None, health_status="healthy", morale=5):
        """
        Конструктор класса Athlete
        """
        # Валидация
        self._validate_name(name)
        self._validate_weight(weight)
        self._validate_height(height)
        self._validate_personal_record(personal_record)
        self._validate_training_level(training_level)
        self._validate_health_status(health_status)
        self._validate_morale(morale)
        
        # Присваивание значений
        self._name = name
        self._weight = weight
        self._height = height
        self._personal_record = personal_record
        self._training_level = training_level if training_level else self.default_training_level
        self._health_status = health_status
        self._morale = morale
        self._is_active = True
        
        # Увеличиваем счетчик
        Athlete.total_athletes += 1
    
    # Валидаторы
    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not name.strip():
            raise ValueError("Имя не может быть пустым")
        if len(name) < 2:
            raise ValueError("Имя должно содержать минимум 2 символа")
        if len(name) > 50:
            raise ValueError("Имя не должно превышать 50 символов")
    
    def _validate_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть числом")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        if weight < 20:
            raise ValueError("Вес не может быть меньше 20 кг")
        if weight > 300:
            raise ValueError("Вес не может превышать 300 кг")
    
    def _validate_height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError("Рост должен быть числом")
        if height <= 0:
            raise ValueError("Рост должен быть положительным числом")
        if height < 50:
            raise ValueError("Рост не может быть меньше 50 см")
        if height > 280:
            raise ValueError("Рост не может превышать 280 см")
    
    def _validate_personal_record(self, record):
        if not isinstance(record, (int, float)):
            raise TypeError("Рекорд должен быть числом")
        if record < 0:
            raise ValueError("Рекорд не может быть отрицательным")
        if record > 500:
            raise ValueError("Рекорд не может превышать 500")
    
    def _validate_training_level(self, level):
        if level is not None:
            if not isinstance(level, str):
                raise TypeError("Уровень подготовки должен быть строкой")
            if level not in self.VALID_TRAINING_LEVELS:
                raise ValueError(f"Уровень подготовки должен быть одним из: {self.VALID_TRAINING_LEVELS}")
    
    def _validate_health_status(self, status):
        if not isinstance(status, str):
            raise TypeError("Статус здоровья должен быть строкой")
        if status not in self.VALID_HEALTH_STATUSES:
            raise ValueError(f"Статус здоровья должен быть одним из: {self.VALID_HEALTH_STATUSES}")
    
    def _validate_morale(self, morale):
        if not isinstance(morale, int):
            raise TypeError("Мораль должна быть целым числом")
        if morale < self.min_morale or morale > self.max_morale:
            raise ValueError(f"Мораль должна быть от {self.min_morale} до {self.max_morale}")
    
    # Геттеры
    @property
    def name(self):
        return self._name
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def height(self):
        return self._height
    
    @property
    def personal_record(self):
        return self._personal_record
    
    @property
    def is_active(self):
        return self._is_active
    
    @property
    def health_status(self):
        return self._health_status
    
    @property
    def training_level(self):
        return self._training_level
    
    @property
    def morale(self):
        return self._morale
    
    # Сеттеры
    @weight.setter
    def weight(self, value):
        self._validate_weight(value)
        self._weight = value
    
    @height.setter
    def height(self, value):
        self._validate_height(value)
        self._height = value
    
    @personal_record.setter
    def personal_record(self, value):
        if not self._is_active:
            raise ValueError("Нельзя установить рекорд неактивному спортсмену")
        if self._health_status == "injured":
            raise ValueError("Нельзя установить рекорд при травме")
        if self._health_status == "recovering":
            print("Предупреждение: спортсмен восстанавливается, установка рекорда не рекомендуется")
        
        self._validate_personal_record(value)
        
        # Проверка максимального рекорда для уровня подготовки
        max_record = self.MAX_RECORD_BY_LEVEL[self._training_level]
        if value > max_record:
            raise ValueError(f"Рекорд не может превышать {max_record} для уровня {self._training_level}")
        
        self._personal_record = value
    
    @training_level.setter
    def training_level(self, value):
        if not self._is_active:
            raise ValueError("Нельзя изменить уровень подготовки неактивного спортсмена")
        self._validate_training_level(value)
        self._training_level = value
    
    @morale.setter
    def morale(self, value):
        self._validate_morale(value)
        self._morale = value
    
    @health_status.setter
    def health_status(self, value):
        self._validate_health_status(value)
        self._health_status = value
    
    # Бизнес-методы
    def bmi(self):
        """Расчет индекса массы тела"""
        height_m = self._height / 100
        return self._weight / (height_m ** 2)
    
    def performance_score(self):
        """Расчет производительности"""
        level_multiplier = {
            "beginner": 1.0,
            "intermediate": 1.5,
            "advanced": 2.0,
            "professional": 2.5
        }
        
        health_multiplier = {
            "healthy": 1.0,
            "recovering": 0.7,
            "injured": 0.3
        }
        
        base_score = self._personal_record
        level_bonus = level_multiplier[self._training_level]
        health_factor = health_multiplier[self._health_status]
        morale_factor = self._morale / 10
        
        return base_score * level_bonus * health_factor * morale_factor
    
    def set_record(self, new_record):
        """Обновление личного рекорда"""
        self.personal_record = new_record
    
    def set_training_level(self, level):
        """Изменение уровня подготовки"""
        self.training_level = level
    
    def deactivate(self):
        """Деактивация спортсмена"""
        self._is_active = False
    
    def activate(self):
        """Активация спортсмена"""
        self._is_active = True
    
    def injure(self):
        """Получение травмы"""
        self._health_status = "injured"
    
    def recover(self):
        """Начало восстановления"""
        self._health_status = "recovering"
    
    def heal(self):
        """Полное излечение"""
        self._health_status = "healthy"
    
    # Магические методы
    def __str__(self):
        status = "активен" if self._is_active else "неактивен"
        return (f"Спортсмен: {self._name}, вес: {self._weight} {self.weight_unit}, "
                f"рост: {self._height} {self.height_unit}, рекорд: {self._personal_record} {self.record_unit}, "
                f"ИМТ: {self.bmi():.1f}, здоровье: {self._health_status}, "
                f"уровень: {self._training_level}, мораль: {self._morale}/{self.max_morale}, "
                f"статус: {status}")
    
    def __repr__(self):
        return (f"Athlete(name='{self._name}', weight={self._weight}, "
                f"height={self._height}, record={self._personal_record})")
    
    def __eq__(self, other):
        if not isinstance(other, Athlete):
            return False
        return (self._name == other._name and 
                self._weight == other._weight and 
                self._height == other._height and 
                self._personal_record == other._personal_record)