class AthleteValidator:

    # Допустимые виды спорта (атрибут класса из model.py)
    ALLOWED_SPORT_TYPES = ["Футбол", "Баскетбол", "Плавание", "Легкая атлетика", "Теннис", "Бокс"]

    # Ограничения для полей (атрибуты класса из model.py)
    MIN_AGE = 14
    MAX_AGE = 50
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 50
    MAX_WEIGHT = 200
    MAX_TRAINING_HOURS = 8
    MAX_TRAINING_HOURS_JUNIOR = 4

    @classmethod
    def check_name(cls, name: str) -> None:

       # Проверка имени спортсмена.
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not name.strip():
            raise ValueError("Имя не может быть пустым")
        if len(name) < cls.MIN_NAME_LENGTH:
            raise ValueError(f"Имя должно содержать минимум {cls.MIN_NAME_LENGTH} символа")
        if len(name) > cls.MAX_NAME_LENGTH:
            raise ValueError(f"Имя не может быть длиннее {cls.MAX_NAME_LENGTH} символов")

    @classmethod
    def check_age(cls, age: int) -> None:

      #  Проверка возраста спортсмена.

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age < cls.MIN_AGE or age > cls.MAX_AGE:
            raise ValueError(f"Возраст должен быть от {cls.MIN_AGE} до {cls.MAX_AGE} лет")

    @classmethod
    def check_sport_type(cls, sport_type: str) -> None:

       # Проверка вида спорта.

        if not isinstance(sport_type, str):
            raise TypeError("Вид спорта должен быть строкой")
        if sport_type not in cls.ALLOWED_SPORT_TYPES:
            raise ValueError(f"Вид спорта должен быть одним из: {', '.join(cls.ALLOWED_SPORT_TYPES)}")

    @classmethod
    def check_weight(cls, weight: float) -> None:

      #Проверка веса спортсмена.

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть числом")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        if weight > cls.MAX_WEIGHT:
            raise ValueError(f"Вес не может превышать {cls.MAX_WEIGHT} кг")

    @classmethod
    def check_personal_record(cls, record: float) -> None:

       # Проверка личного рекорда спортсмена.

        if not isinstance(record, (int, float)):
            raise TypeError("Личный рекорд должен быть числом")
        if record < 0:
            raise ValueError("Личный рекорд не может быть отрицательным")

    @staticmethod
    def check_is_active(status: bool) -> None:

      #  Проверка, что статус активности является булевым значением.

        if not isinstance(status, bool):
            raise TypeError("Статус активности должен быть булевым значением")

    @classmethod
    def check_training_hours(cls, hours: float) -> None:

        #Проверка количества часов для тренировки (базовая проверка).
        if not isinstance(hours, (int, float)):
            raise TypeError("Количество часов должно быть числом")
        if hours <= 0:
            raise ValueError("Количество часов должно быть положительным")
        if hours > cls.MAX_TRAINING_HOURS:
            raise ValueError(f"Тренировка не может длиться более {cls.MAX_TRAINING_HOURS} часов")

    @classmethod
    def check_junior_training_hours(cls, hours: float, age: int) -> None:
        cls.check_training_hours(hours)
        
        if age < 18 and hours > cls.MAX_TRAINING_HOURS_JUNIOR:
            return (f"Спортсмену до 18 лет рекомендуется тренироваться "
                    f"не более {cls.MAX_TRAINING_HOURS_JUNIOR} часов. Вы указали {hours} ч.")
        return ""

    @classmethod
    def check_all(cls, name: str, age: int, sport_type: str, weight: float, personal_record: float) -> None:
        cls.check_name(name)
        cls.check_age(age)
        cls.check_sport_type(sport_type)
        cls.check_weight(weight)
        cls.check_personal_record(personal_record)