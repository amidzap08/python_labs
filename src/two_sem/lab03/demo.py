# lab03/demo.py
"""
Демонстрация работы иерархии классов для ЛР-3
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from two_sem.lab03.models import ProfessionalTeam, AmateurTeam, YouthTeam


class TeamCollection:
    """Коллекция для управления командами"""
    
    def __init__(self):
        self._teams = []
    
    def add_team(self, team):
        self._teams.append(team)
        print(f"Команда '{team.name}' добавлена в коллекцию")
    
    def get_professional_teams(self):
        return [t for t in self._teams if isinstance(t, ProfessionalTeam)]
    
    def get_amateur_teams(self):
        return [t for t in self._teams if isinstance(t, AmateurTeam) 
                and not isinstance(t, YouthTeam)]
    
    def get_youth_teams(self):
        return [t for t in self._teams if isinstance(t, YouthTeam)]
    
    def get_statistics(self):
        return {
            "total": len(self._teams),
            "professional": len(self.get_professional_teams()),
            "amateur": len(self.get_amateur_teams()),
            "youth": len(self.get_youth_teams())
        }
    
    def __iter__(self):
        return iter(self._teams)
    
    def __len__(self):
        return len(self._teams)


def main():

    print("ЗАДАНИЕ 3: БАЗОВОЕ НАСЛЕДОВАНИЕ")

    pro_team = ProfessionalTeam(
        name="Чемпионы Про",
        avg_weight=85.5,
        avg_height=185.0,
        total_points=350.0,
        budget=2000000.0,
        sponsor_tier="Gold",
        league="Премьер-лига"
    )
    
    amateur_team = AmateurTeam(
        name="Любители Выходного Дня",
        avg_weight=78.0,
        avg_height=178.0,
        total_points=120.0,
        membership_fee=500.0,
        volunteer_count=8,
        practice_frequency="Weekly"
    )
    
    print("\nДемонстрация методов базового класса:")
    print(f"Профессиональная команда '{pro_team.name}':")
    print(f"  ИМТ команды: {pro_team.avg_bmi():.2f}")
    print(f"  Производительность: {pro_team.performance_score():.2f}")
    print(f"  Статус: {'активна' if pro_team.is_active else 'неактивна'}")
    
    print(f"\nЛюбительская команда '{amateur_team.name}':")
    print(f"  ИМТ команды: {amateur_team.avg_bmi():.2f}")
    print(f"  Производительность: {amateur_team.performance_score():.2f}")
    print(f"  Дивизион: {amateur_team.division}")
    
    print("\nДемонстрация новых методов дочерних классов:")
    print(f"Профессиональная команда:")
    print(f"  ROI: {pro_team.calculate_roi():.2f}")
    print(f"  Уровень спонсорства: {pro_team.get_sponsorship_level()}")
    
    print(f"\nЛюбительская команда:")
    print(f"  Месячный доход: ${amateur_team.calculate_monthly_income():.2f}")
    print(f"  Расписание: {amateur_team.get_practice_schedule()}")
    amateur_team.add_community_event()
    

    print("ЗАДАНИЕ 4: ПОЛИМОРФИЗМ И ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДОВ")

    collection = TeamCollection()
    
    teams = [
        ProfessionalTeam("Орлы", 82.0, 180.0, 400.0, 3000000.0, "Platinum", "Высшая лига"),
        ProfessionalTeam("Ястребы", 88.0, 190.0, 380.0, 2500000.0, "Gold", "Первая лига"),
        AmateurTeam("Бегуны", 75.0, 175.0, 150.0, 300.0, 5, "Weekly"),
        AmateurTeam("Волейболисты", 80.0, 182.0, 130.0, 400.0, 12, "Bi-weekly"),
        YouthTeam("Юные Звезды", 65.0, 170.0, 100.0, 200.0, 15, "Weekly", "U16", True),
    ]
    
    print("\nДобавление команд в коллекцию:")
    for team in teams:
        collection.add_team(team)
    
    print("\nПроверка типов через isinstance():")
    for team in collection:
        if isinstance(team, ProfessionalTeam):
            print(f"  {team.name}: ПРОФЕССИОНАЛЬНАЯ (лига: {team.league})")
        elif isinstance(team, YouthTeam):
            print(f"  {team.name}: МОЛОДЕЖНАЯ (группа: {team.age_group})")
        elif isinstance(team, AmateurTeam):
            print(f"  {team.name}: ЛЮБИТЕЛЬСКАЯ (волонтеров: {team.volunteer_count})")
    
    print("\nПереопределенный __str__():")
    for i, team in enumerate(collection, 1):
        print(f"\nКоманда {i}")
        print(team)
    
# lab03/demo.py (исправленная часть для Задания 5)

    print()
    print("ЗАДАНИЕ 5: ПОЛИМОРФИЗМ БЕЗ УСЛОВИЙ И ИНТЕРФЕЙС")
    print()
  
    # ===== СЦЕНАРИЙ 1: Полиморфный вызов calculate_team_value() =====

    print("СЦЕНАРИЙ 1: Полиморфизм — разная стоимость команд")

    print("Вызов calculate_team_value() для всех типов команд:")
    for team in collection:
        value = team.calculate_team_value()
        team_type = type(team).__name__
        print(f"  [{team_type}] {team.name}: ${value:,.2f}")
    
    # ===== СЦЕНАРИЙ 2: Полиморфный вызов performance_score() =====
    print()
    print("СЦЕНАРИЙ 2: Полиморфизм — разный расчет производительности")

    print("Вызов performance_score() для всех типов команд:")
    for team in collection:
        score = team.performance_score()
        team_type = type(team).__name__
        print(f"  [{team_type}] {team.name}: {score:.2f}")
        print()
    
    # ===== СЦЕНАРИЙ 3: Фильтрация по типам =====
    print("СЦЕНАРИЙ 3: Фильтрация коллекции по типам")

    
    pro_teams = collection.get_professional_teams()
    print(f"\nПрофессиональные команды ({len(pro_teams)}):")
    for team in pro_teams:
        print(f"  {team.name} - бюджет: ${team.budget:,.0f}, ROI: {team.calculate_roi():.2f}")
    
    amateur_teams = collection.get_amateur_teams()
    print(f"\nЛюбительские команды ({len(amateur_teams)}):")
    for team in amateur_teams:
        print(f"  {team.name} - волонтеров: {team.volunteer_count}, взнос: ${team.membership_fee}")
    
    youth_teams = collection.get_youth_teams()
    print(f"\nМолодежные команды ({len(youth_teams)}):")
    for team in youth_teams:
        team.award_scholarship()
        print(f"  {team.name} - группа: {team.age_group}, стипендий: {team.scholarship_count}")
    

    print()

    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")

if __name__ == "__main__":
    main()