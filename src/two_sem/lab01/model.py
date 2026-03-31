from two_sem.lab01 import validate

class Team:
    total_teams = 0
    sport_type = "running"
    default_division = "beginner"
    max_morale = 10
    min_morale = 0
    weight_unit = "kg"
    height_unit = "cm"
    record_unit = "points"

    def __init__(self, name: str, avg_weight: float, avg_height: float, total_points: float = 0.0):
        # Валидация входных данных
        validate.validate_name(name)
        validate.validate_weight(avg_weight)
        validate.validate_height(avg_height)
        validate.validate_record(total_points)

        self._name = name.strip()
        self._avg_weight = avg_weight
        self._avg_height = avg_height
        self._total_points = total_points

        # Состояния
        self._is_active = True
        self._health_status = "healthy"
        self._division = Team.default_division
        self._morale = Team.max_morale

        Team.total_teams += 1

    # Свойства (геттеры) для всех атрибутов
    @property
    def name(self) -> str:
        return self._name

    @property
    def avg_weight(self) -> float:
        return self._avg_weight

    @avg_weight.setter
    def avg_weight(self, value: float) -> None:
        validate.validate_weight(value)
        self._avg_weight = value

    @property
    def avg_height(self) -> float:
        return self._avg_height

    @avg_height.setter
    def avg_height(self, value: float) -> None:
        validate.validate_height(value)
        self._avg_height = value

    @property
    def total_points(self) -> float:
        return self._total_points

    @total_points.setter
    def total_points(self, value: float) -> None:
        # Проверка состояния здоровья и активности
        if not self._is_active:
            raise RuntimeError("Нельзя изменить очки неактивной команды")
        if self._health_status == "injured":
            raise RuntimeError("Нельзя изменить очки при травмах в команде")
        if self._health_status == "recovering":
            print("Предупреждение: Команда восстанавливается, изменение очков может быть рискованным")

        # Проверка ограничений по дивизиону
        max_points = self._max_points_for_division()
        if value > max_points:
            raise ValueError(f"Очки {value} превышают максимально допустимые для дивизиона {self._division} ({max_points})")

        validate.validate_record(value)
        self._total_points = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def health_status(self) -> str:
        return self._health_status

    @property
    def division(self) -> str:
        return self._division

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
            print(f"{self._name} активирована")

    def deactivate(self) -> None:
        if self._is_active:
            self._is_active = False
            print(f"{self._name} деактивирована")

    def injure(self) -> None:
        if self._health_status != "injured":
            self._health_status = "injured"
            print(f"{self._name} получила травмы в команде")

    def recover(self) -> None:
        if self._health_status == "injured":
            self._health_status = "recovering"
            print(f"{self._name} начала восстановление")
        else:
            print(f"{self._name} не травмирована. Текущий статус: {self._health_status}")

    def heal(self) -> None:
        """Полное излечение (становится здоровой)."""
        self._health_status = "healthy"
        print(f"{self._name} полностью здорова")

    def set_division(self, division: str) -> None:
        validate.validate_division(division)
        self._division = division
        print(f"Дивизион {self._name} изменен на {division}")

    # Вспомогательные методы
    def _max_points_for_division(self) -> float:
        limits = {
            "beginner": 100,
            "intermediate": 200,
            "professional": 350,
            "elite": 500
        }
        return limits[self._division]

    # Бизнес-методы
    def set_points(self, new_points: float) -> None:
        """Установить новые очки команды (использует сеттер)."""
        self.total_points = new_points

    def avg_bmi(self) -> float:
        """Расчет среднего индекса массы тела команды."""
        height_m = self._avg_height / 100
        return round(self._avg_weight / (height_m ** 2), 2)

    def performance_score(self) -> float:
        """Расчет показателя производительности команды."""
        if not self._is_active:
            return 0.0
        
        division_multipliers = {
            "beginner": 1.0,
            "intermediate": 1.5,
            "professional": 2.0,
            "elite": 3.0
        }
        
        health_penalty = {
            "healthy": 1.0,
            "recovering": 0.7,
            "injured": 0.0
        }
        
        multiplier = division_multipliers.get(self._division, 1.0)
        health_factor = health_penalty.get(self._health_status, 1.0)
        morale_factor = self._morale / Team.max_morale
        
        score = self._total_points * multiplier * health_factor * morale_factor
        return round(score, 2)

    # Магические методы
    def __str__(self) -> str:
        status = "активна" if self._is_active else "неактивна"
        return (f"Команда: {self._name}, средний вес: {self._avg_weight}{Team.weight_unit}, "
                f"средний рост: {self._avg_height}{Team.height_unit}, "
                f"очки: {self._total_points}{Team.record_unit}, средний ИМТ: {self.avg_bmi()}, "
                f"здоровье: {self._health_status}, дивизион: {self._division}, "
                f"уровень мотивации: {self._morale}/{Team.max_morale}, статус: {status}")

    def __repr__(self) -> str:
        return (f"Team(name='{self._name}', avg_weight={self._avg_weight}, "
                f"avg_height={self._avg_height}, total_points={self._total_points})")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Team):
            return False
        return (self._name == other._name and
                self._avg_weight == other._avg_weight and
                self._avg_height == other._avg_height and
                self._total_points == other._total_points)