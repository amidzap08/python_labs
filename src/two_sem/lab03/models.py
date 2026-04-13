# lab03/models.py
"""
Модуль с классами для ЛР-3
Содержит базовый класс Team и производные классы
"""

class Team:
    """Базовый класс - спортивная команда"""
    
    valid_divisions = ["beginner", "intermediate", "advanced", "professional"]
    
    def __init__(self, name: str, avg_weight: float, avg_height: float, total_points: float = 0.0):
        self._name = name
        self._avg_weight = avg_weight
        self._avg_height = avg_height
        self._total_points = total_points
        self._is_active = True
        self._division = "beginner"
    
    def avg_bmi(self) -> float:
        height_m = self._avg_height / 100
        return round(self._avg_weight / (height_m ** 2), 2)
    
    def performance_score(self) -> float:
        if not self._is_active:
            return 0.0
        return round((self._total_points * self.avg_bmi()) / 10, 2)
    
    def activate(self) -> None:
        self._is_active = True
        print(f"Команда '{self._name}' активирована")
    
    def deactivate(self) -> None:
        self._is_active = False
        print(f"Команда '{self._name}' деактивирована")
    
    def set_division(self, division: str) -> bool:
        if division.lower() in self.valid_divisions:
            self._division = division.lower()
            return True
        return False
    
    def add_points(self, points: float) -> None:
        if points > 0:
            self._total_points += points
    
    def __str__(self) -> str:
        status = "Активна" if self._is_active else "Неактивна"
        return (f"Команда: {self._name}\n"
                f"  Вес: {self._avg_weight} кг, Рост: {self._avg_height} см\n"
                f"  ИМТ: {self.avg_bmi()}, Очки: {self._total_points}\n"
                f"  Дивизион: {self._division}, Статус: {status}")
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def avg_weight(self) -> float:
        return self._avg_weight
    
    @property
    def avg_height(self) -> float:
        return self._avg_height
    
    @property
    def total_points(self) -> float:
        return self._total_points
    
    @property
    def is_active(self) -> bool:
        return self._is_active
    
    @property
    def division(self) -> str:
        return self._division


class ProfessionalTeam(Team):
    """Производный класс 1: Профессиональная команда"""
    
    min_budget = 100000
    sponsorship_tiers = ["Bronze", "Silver", "Gold", "Platinum"]
    
    def __init__(self, name: str, avg_weight: float, avg_height: float, 
                 total_points: float = 0.0, budget: float = 0.0, 
                 sponsor_tier: str = "Bronze", league: str = "National"):
        super().__init__(name, avg_weight, avg_height, total_points)
        self._budget = budget
        self._sponsor_tier = sponsor_tier
        self._league = league
        self._contract_bonus = 0.0
    
    def calculate_roi(self) -> float:
        if self._budget <= 0:
            return 0.0
        return (self.performance_score() * 10000) / self._budget
    
    def get_sponsorship_level(self) -> str:
        descriptions = {
            "Bronze": "Базовое спонсорство",
            "Silver": "Серебряный партнер",
            "Gold": "Золотой партнер",
            "Platinum": "Платиновый партнер"
        }
        return descriptions.get(self._sponsor_tier, "Без спонсора")
    
    def __str__(self) -> str:
        base_str = super().__str__()
        return (f"[PROFESSIONAL] {base_str}\n"
                f"  Лига: {self._league}, Бюджет: ${self._budget:,.2f}\n"
                f"  Спонсорство: {self.get_sponsorship_level()}")
    
    def performance_score(self) -> float:
        base_score = super().performance_score()
        budget_multiplier = 1.0 + (self._budget / 1000000) * 0.1
        tier_multipliers = {
            "Bronze": 1.0,
            "Silver": 1.1,
            "Gold": 1.2,
            "Platinum": 1.3
        }
        tier_multiplier = tier_multipliers.get(self._sponsor_tier, 1.0)
        return round(base_score * budget_multiplier * tier_multiplier, 2)
    
    def calculate_team_value(self) -> float:
        brand_value = self.performance_score() * 50000
        return self._budget * 1.5 + brand_value
    
    @property
    def budget(self) -> float:
        return self._budget
    
    @budget.setter
    def budget(self, value: float) -> None:
        if value < ProfessionalTeam.min_budget:
            print(f"Предупреждение: Бюджет ниже минимального ({ProfessionalTeam.min_budget})")
        self._budget = max(value, 0)
    
    @property
    def sponsor_tier(self) -> str:
        return self._sponsor_tier
    
    @sponsor_tier.setter
    def sponsor_tier(self, value: str) -> None:
        if value not in ProfessionalTeam.sponsorship_tiers:
            raise ValueError(f"Уровень спонсорства должен быть одним из: {ProfessionalTeam.sponsorship_tiers}")
        self._sponsor_tier = value
    
    @property
    def league(self) -> str:
        return self._league
    
    @property
    def contract_bonus(self) -> float:
        return self._contract_bonus
    
    @contract_bonus.setter
    def contract_bonus(self, value: float) -> None:
        if value < 0:
            raise ValueError("Бонус не может быть отрицательным")
        self._contract_bonus = value


class AmateurTeam(Team):
    """Производный класс 2: Любительская команда"""
    
    max_membership_fee = 1000
    volunteer_roles = ["Coach", "Assistant", "Manager", "Supporter"]
    
    def __init__(self, name: str, avg_weight: float, avg_height: float, 
                 total_points: float = 0.0, membership_fee: float = 0.0, 
                 volunteer_count: int = 0, practice_frequency: str = "Weekly"):
        super().__init__(name, avg_weight, avg_height, total_points)
        self._membership_fee = membership_fee
        self._volunteer_count = volunteer_count
        self._practice_frequency = practice_frequency
        self._community_events = 0
        
        if self._division not in ["beginner", "intermediate"]:
            self.set_division("beginner")
    
    def calculate_monthly_income(self) -> float:
        return self._membership_fee
    
    def get_practice_schedule(self) -> str:
        schedules = {
            "Daily": "Каждый день в 18:00",
            "Weekly": "По субботам в 10:00",
            "Bi-weekly": "Два раза в неделю",
            "Monthly": "Раз в месяц"
        }
        return schedules.get(self._practice_frequency, "По договоренности")
    
    def add_community_event(self) -> None:
        self._community_events += 1
        print(f"{self._name} провела общественное мероприятие. Всего: {self._community_events}")
    
    def __str__(self) -> str:
        base_str = super().__str__()
        return (f"[AMATEUR] {base_str}\n"
                f"  Взнос: ${self._membership_fee:.2f}, Волонтеры: {self._volunteer_count}\n"
                f"  Тренировки: {self.get_practice_schedule()}")
    
    def performance_score(self) -> float:
        base_score = super().performance_score()
        volunteer_bonus = 1.0 + (self._volunteer_count * 0.02)
        event_bonus = 1.0 + (self._community_events * 0.05)
        return round(base_score * volunteer_bonus * event_bonus, 2)
    
    def calculate_team_value(self) -> float:
        volunteer_value = self._volunteer_count * 1000
        community_value = self._community_events * 500
        performance_value = self.performance_score() * 1000
        return volunteer_value + community_value + performance_value
    
    @property
    def membership_fee(self) -> float:
        return self._membership_fee
    
    @membership_fee.setter
    def membership_fee(self, value: float) -> None:
        if value > AmateurTeam.max_membership_fee:
            print(f"Предупреждение: Взнос превышает максимальный ({AmateurTeam.max_membership_fee})")
        self._membership_fee = max(value, 0)
    
    @property
    def volunteer_count(self) -> int:
        return self._volunteer_count
    
    @volunteer_count.setter
    def volunteer_count(self, value: int) -> None:
        if value < 0:
            raise ValueError("Количество волонтеров не может быть отрицательным")
        self._volunteer_count = value
    
    @property
    def practice_frequency(self) -> str:
        return self._practice_frequency
    
    @property
    def community_events(self) -> int:
        return self._community_events


class YouthTeam(AmateurTeam):
    """Производный класс 3: Молодежная команда"""
    
    def __init__(self, name: str, avg_weight: float, avg_height: float, 
                 total_points: float = 0.0, membership_fee: float = 0.0, 
                 volunteer_count: int = 0, practice_frequency: str = "Weekly",
                 age_group: str = "U18", school_program: bool = False):
        super().__init__(name, avg_weight, avg_height, total_points, 
                        membership_fee, volunteer_count, practice_frequency)
        self._age_group = age_group
        self._school_program = school_program
        self._scholarship_count = 0
    
    def __str__(self) -> str:
        base_str = super().__str__()
        school_status = "Да" if self._school_program else "Нет"
        return (f"{base_str}\n"
                f"  [YOUTH] Возрастная группа: {self._age_group}, "
                f"Школьная программа: {school_status}")
    
    def calculate_team_value(self) -> float:
        base_value = super().calculate_team_value()
        return base_value * 1.3
    
    def award_scholarship(self) -> None:
        self._scholarship_count += 1
        print(f"{self._name}: Выдана стипендия #{self._scholarship_count}")
    
    @property
    def age_group(self) -> str:
        return self._age_group
    
    @property
    def scholarship_count(self) -> int:
        return self._scholarship_count