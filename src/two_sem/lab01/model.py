from two_sem.lab01 import validate

class Athlete:
    total_athletes = 0
    sport_type = "running"
    default_training_level = "beginner"
    max_morale = 10
    min_morale = 0
    weight_unit = "kg"
    height_unit = "cm"
    record_unit = "kg"

    def __init__(self, name: str, weight: float, height: float, record: float = 0.0):
        # Валидация входных данных
        validate.validate_name(name)
        validate.validate_weight(weight)
        validate.validate_height(height)
        validate.validate_record(record)

        self._name = name.strip()
        self._weight = weight
        self._height = height
        self._personal_record = record

        # Состояния
        self._is_active = True
        self._health_status = "healthy"
        self._training_level = Athlete.default_training_level
        self._morale = Athlete.max_morale

        Athlete.total_athletes += 1

    # Свойства (геттеры) для всех атрибутов
    @property
    def name(self) -> str:
        return self._name

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        validate.validate_weight(value)
        self._weight = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        validate.validate_height(value)
        self._height = value

    @property
    def personal_record(self) -> float:
        return self._personal_record

    @personal_record.setter
    def personal_record(self, value: float) -> None:
        # Проверка состояния здоровья и активности
        if not self._is_active:
            raise RuntimeError("Нельзя изменить рекорд неактивного спортсмена")
        if self._health_status == "injured":
            raise RuntimeError("Нельзя изменить рекорд при травме")
        if self._health_status == "recovering":
            print("Предупреждение: Спортсмен восстанавливается, установка рекорда может быть рискованной")

        # Проверка ограничений по уровню подготовки
        max_record = self._max_record_for_level()
        if value > max_record:
            raise ValueError(f"Рекорд {value} превышает максимально допустимый для уровня {self._training_level} ({max_record})")

        validate.validate_record(value)
        self._personal_record = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def health_status(self) -> str:
        return self._health_status

    @property
    def training_level(self) -> str:
        return self._training_level

    @property
    def morale(self) -> int:
        return self._morale

    @morale.setter
    def morale(self, value: int) -> None:
        validate.validate_morale(value)
        self._morale = value

    # Методы изменения состояний
    def activate(self) -> None:
        if not self._is_active:
            self._is_active = True
            print(f"{self._name} активирован")

    def deactivate(self) -> None:
        if self._is_active:
            self._is_active = False
            print(f"{self._name} деактивирован")

    def injure(self) -> None:
        if self._health_status != "injured":
            self._health_status = "injured"
            print(f"{self._name} получил травму")

    def recover(self) -> None:
        if self._health_status == "injured":
            self._health_status = "recovering"
            print(f"{self._name} начал восстановление")
        else:
            print(f"{self._name} не травмирован. Текущий статус: {self._health_status}")

    def heal(self) -> None:
        """Полное излечение (становится здоровым)."""
        self._health_status = "healthy"
        print(f"{self._name} полностью здоров")

    def set_training_level(self, level: str) -> None:
        validate.validate_training_level(level)
        self._training_level = level
        print(f"Уровень подготовки {self._name} изменен на {level}")

    # Вспомогательные методы
    def _max_record_for_level(self) -> float:
        limits = {
            "beginner": 100,
            "intermediate": 200,
            "advanced": 350,
            "professional": 500
        }
        return limits[self._training_level]

    # Бизнес-методы
    def set_record(self, new_record: float) -> None:
        """Установить новый личный рекорд (использует сеттер)."""
        self.personal_record = new_record

    def bmi(self) -> float:
        """Расчет индекса массы тела."""
        height_m = self._height / 100
        return round(self._weight / (height_m ** 2), 2)

    def performance_score(self) -> float:
        """Расчет показателя производительности."""
        if not self._is_active:
            return 0.0
        
        level_multipliers = {
            "beginner": 1.0,
            "intermediate": 1.5,
            "advanced": 2.0,
            "professional": 3.0
        }
        
        health_penalty = {
            "healthy": 1.0,
            "recovering": 0.7,
            "injured": 0.0
        }
        
        multiplier = level_multipliers[self._training_level]
        health_factor = health_penalty[self._health_status]
        morale_factor = self._morale / Athlete.max_morale
        
        score = self._personal_record * multiplier * health_factor * morale_factor
        return round(score, 2)

    # Магические методы
    def __str__(self) -> str:
        status = "активен" if self._is_active else "неактивен"
        return (f"Спортсмен: {self._name}, вес: {self._weight}{Athlete.weight_unit}, "
                f"рост: {self._height}{Athlete.height_unit}, "
                f"рекорд: {self._personal_record}{Athlete.record_unit}, ИМТ: {self.bmi()}, "
                f"здоровье: {self._health_status}, уровень: {self._training_level}, "
                f"Уровень мотивации: {self._morale}/{Athlete.max_morale}, статус: {status}")

    def __repr__(self) -> str:
        return (f"Athlete(name='{self._name}', weight={self._weight}, "
                f"height={self._height}, record={self._personal_record})")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Athlete):
            return False
        return (self._name == other._name and
                self._weight == other._weight and
                self._height == other._height and
                self._personal_record == other._personal_record)