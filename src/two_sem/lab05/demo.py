"""
Демонстрация ЛР-5: Функции как аргументы. Стратегии и делегаты.
Работает с классами из lab03 без изменений в предыдущих ЛР.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from two_sem.lab03.models import ProfessionalTeam, AmateurTeam, YouthTeam
from two_sem.lab05.collection import FunctionalTeamCollection
import two_sem.lab05.strategies as strat


def print_collection(title: str, coll: FunctionalTeamCollection):
    """Вывод коллекции на экран."""

    print(f"  {title}")

    if len(coll) == 0:
        print("  (коллекция пуста)")
        return
    for i, team in enumerate(coll, 1):
        print(f"  {i}. {team.name:<20} | Дивизион: {team.division:<12} | "
              f"Очки: {team.total_points:>6.1f} | ИМТ: {team.avg_bmi():>5.2f} | "
              f"Произв.: {team.performance_score():>7.2f} | Активна: {'да' if team.is_active else 'нет'}")


def demo_score_3():
    """Задание на 3: сортировка и фильтрация."""

    print("  ЗАДАНИЕ НА 3: БАЗОВАЯ СОРТИРОВКА И ФИЛЬТРАЦИЯ")

    
    # Создаём коллекцию
    coll = FunctionalTeamCollection()
    
    # Добавляем команды разных типов
    teams = [
        ProfessionalTeam("Eagles", 82.0, 180.0, 400.0, 3000000.0, "Platinum", "Высшая лига"),
        ProfessionalTeam("Hawks", 88.0, 190.0, 380.0, 2500000.0, "Gold", "Первая лига"),
        AmateurTeam("Runners", 75.0, 175.0, 150.0, 300.0, 5, "Weekly"),
        AmateurTeam("Cyclists", 70.0, 172.0, 90.0, 200.0, 3, "Bi-weekly"),
        YouthTeam("Young Stars", 65.0, 170.0, 100.0, 200.0, 15, "Weekly", "U16", True),
        YouthTeam("Olympians", 70.0, 175.0, 180.0, 250.0, 20, "Bi-weekly", "U18", True),
    ]
    
    for team in teams:
        coll.add(team)
    
    # Установим дивизионы
    teams[0].set_division("professional")  # Eagles
    teams[1].set_division("professional")  # Hawks
    teams[2].set_division("beginner")      # Runners
    teams[3].set_division("intermediate")  # Cyclists
    teams[4].set_division("beginner")      # Young Stars
    teams[5].set_division("advanced")      # Olympians
    
    print_collection("Исходная коллекция", coll)
    
    # 1. Сортировка по имени
    coll.sort_by(strat.by_name)
    print_collection("Сортировка по имени (by_name)", coll)
    
    # 2. Сортировка по очкам (lambda)
    coll.sort_by(lambda t: -t.total_points)
    print_collection("Сортировка по очкам (lambda)", coll)
    
    # 3. Сортировка по дивизиону и имени
    coll.sort_by(strat.by_division_and_name)
    print_collection("Сортировка по дивизиону и имени", coll)
    
    # 4. Фильтрация: только активные
    active = coll.filter_by(strat.is_active)
    print_collection("Фильтр: активные команды", active)
    
    # 5. Фильтрация: высокая производительность
    high_perf = coll.filter_by(strat.has_high_performance)
    print_collection("Фильтр: производительность > 20", high_perf)


def demo_score_4():
    """Задание на 4: map, фабрика функций, методы коллекции."""
    print(" ЗАДАНИЕ НА 4: MAP, ФАБРИКИ, МЕТОДЫ КОЛЛЕКЦИИ")

    
    coll = FunctionalTeamCollection()
    teams = [
        ProfessionalTeam("Eagles", 82.0, 180.0, 400.0, 3000000.0, "Platinum", "Высшая лига"),
        AmateurTeam("Runners", 75.0, 175.0, 150.0, 300.0, 5, "Weekly"),
        YouthTeam("Olympians", 70.0, 175.0, 180.0, 250.0, 20, "Bi-weekly", "U18", True),
        ProfessionalTeam("Hawks", 88.0, 190.0, 380.0, 2500000.0, "Gold", "Первая лига"),
        YouthTeam("Young Stars", 65.0, 170.0, 100.0, 200.0, 15, "Weekly", "U16", True),
    ]
    for team in teams:
        coll.add(team)
    
    print_collection("Исходная коллекция", coll)
    
    # 1. map(): извлечение имён
    print("\n map(): извлечение имён ")
    names = list(map(strat.get_name, coll.get_items()))
    print(f"  {names}")
    
    # 2. map(): производительность
    print("\n map(): производительность ")
    performances = list(map(strat.get_performance, coll.get_items()))
    for name, perf in zip(names, performances):
        print(f"  {name}: {perf:.2f}")
    
    # 3. map(): сводка по командам
    print("\n map(): сводка по командам ")
    summaries = list(map(strat.get_team_summary, coll.get_items()))
    for s in summaries:
        print(f"  {s}")
    
    # 4. Фабрика функций: фильтр по дивизиону
    print("\n Фабрика: фильтр по дивизиону 'professional' ")
    pro_filter = strat.make_division_filter('professional')
    pros = coll.filter_by(pro_filter)
    print_collection("Команды в 'professional'", pros)
    
    # 5. Фабрика: фильтр по очкам
    print("\nФабрика: фильтр по очкам (>= 100) ")
    points_filter = strat.make_points_filter(100)
    strong = coll.filter_by(points_filter)
    print_collection("Команды с очками >= 100", strong)
    
    # 6. Методы коллекции в цепочке
    print("\n Цепочка: filter_by → sort_by ")
    result = (coll
              .filter_by(strat.is_active)
              .sort_by(strat.by_performance))
    print_collection("Активные, сортировка по производительности", result)
    
    # 7. Сравнение lambda vs именованная функция
    print("\nlambda vs именованная функция ")
    
    coll.sort_by(lambda t: t.avg_bmi())
    print_collection("Сортировка по ИМТ (lambda)", coll)
    
    coll.sort_by(strat.by_bmi)
    print_collection("Сортировка по ИМТ (функция by_bmi)", coll)


def demo_score_5():
    """Задание на 5: паттерн Стратегия, callable-объекты, цепочки."""
    print(" ЗАДАНИЕ НА 5: ПАТТЕРН СТРАТЕГИЯ, CALLABLE, ЦЕПОЧКИ")

    
    # ===== СЦЕНАРИЙ 1: Полная цепочка filter → sort → apply =====
    print("\n СЦЕНАРИЙ 1: Цепочка операций ")
    coll = FunctionalTeamCollection()
    teams = [
        ProfessionalTeam("Eagles", 82.0, 180.0, 400.0, 3000000.0, "Platinum", "Высшая лига"),
        ProfessionalTeam("Hawks", 88.0, 190.0, 380.0, 2500000.0, "Gold", "Первая лига"),
        AmateurTeam("Runners", 75.0, 175.0, 150.0, 300.0, 5, "Weekly"),
        AmateurTeam("Cyclists", 70.0, 172.0, 90.0, 200.0, 3, "Bi-weekly"),
        YouthTeam("Young Stars", 65.0, 170.0, 100.0, 200.0, 15, "Weekly", "U16", True),
    ]
    for team in teams:
        coll.add(team)
    
    # Деактивируем одну команду
    teams[2].deactivate()  # Runners
    
    print_collection("Исходная коллекция", coll)
    
    # Цепочка
    result = (coll
              .filter_by(strat.is_active)              # только активные
              .sort_by(strat.by_points)                 # сортировка по очкам
              .apply(strat.AddPointsStrategy(50))       # +50 очков
              )
    
    print_collection("filter(активные) → sort(очки) → apply(+50 очков)", result)
    
    # ===== СЦЕНАРИЙ 2: Замена стратегии =====
    print("\nСЦЕНАРИЙ 2: Замена стратегии ")
    
    coll2 = FunctionalTeamCollection()
    for team in teams[:4]:
        coll2.add(team)
    
    teams[0].set_division("intermediate")  # Меняем дивизион
    
    print_collection("Исходная коллекция", coll2)
    
    # Стратегия 1: активация
    print("\nПрименяем ActivateAllStrategy:")
    coll2.apply(strat.ActivateAllStrategy())
    print_collection("После активации", coll2)
    
    # Стратегия 2: смена дивизиона
    print("\nПрименяем SetDivisionStrategy('professional'):")
    coll2.apply(strat.SetDivisionStrategy('professional'))
    print_collection("После смены дивизиона на 'professional'", coll2)
    
    # ===== СЦЕНАРИЙ 3: Callable-объекты =====
    print("\n СЦЕНАРИЙ 3: Callable-объекты ")
    
    # Проверка callable
    info = strat.TeamInfoStrategy()
    print(f"\nTeamInfoStrategy callable? {callable(info)}")
    print("Применяем к команде:")
    info(teams[0])
    
    # Другой callable
    points = strat.AddPointsStrategy(75)
    print(f"\nAddPointsStrategy callable? {callable(points)}")
    test_team = AmateurTeam("Test", 78.0, 178.0, 120.0, 500.0, 8, "Weekly")
    print(f"  До: {test_team.name}, очки: {test_team.total_points}")
    points(test_team)
    print(f"  После: {test_team.name}, очки: {test_team.total_points}")


def main():
    """Главная функция."""
    demo_score_3()
    demo_score_4()
    demo_score_5()
    
    print("█  ДЕМОНСТРАЦИЯ ЛР-5 ЗАВЕРШЕНА")


if __name__ == "__main__":
    main()