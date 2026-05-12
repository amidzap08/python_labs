"""
Демонстрационный скрипт для лабораторной работы №6
Показывает работу TypedCollection с классом Team и протоколами
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from two_sem.lab06.container import (
    TypedCollection, 
    Displayable, 
    Scorable, 
    D, 
    S,
    T
)
from two_sem.lab01.model import Team


def add_team_display(team_instance: Team) -> str:
    """Добавляет метод display() к Team, если его нет."""
    if not hasattr(Team, 'display'):
        def display(self) -> str:
            """Отображение информации о команде."""
            return (f"Команда '{self.name}': "
                    f"{self.division} дивизион, "
                    f"{'активна' if self.is_active else 'неактивна'}, "
                    f"здоровье: {self.health_status}, "
                    f"очки: {self.total_points}")
        Team.display = display


def add_team_score(team_instance: Team) -> str:
    """Добавляет метод score() к Team, если его нет."""
    if not hasattr(Team, 'score'):
        def score(self) -> float:
            """Оценка команды (использует performance_score)."""
            return self.performance_score()
        Team.score = score


def demo_task_3():
    """
    Демонстрация задания на 3:
    - Создание типизированной коллекции Team
    - Добавление объектов
    - Демонстрация валидации типов (mypy)
    - Получение всех элементов
    """
    print()
    print("ДЕМОНСТРАЦИЯ ЗАДАНИЯ НА 3: БАЗОВАЯ ТИПИЗАЦИЯ")
    print()
    
    teams: TypedCollection[Team] = TypedCollection()
    
    team1 = Team("Динамо", 75.5, 175.0, 85.0)
    team2 = Team("Спартак", 82.0, 180.0, 120.0)
    team3 = Team("ЦСКА", 70.0, 172.0, 65.0)
    
    print("Добавление команд в TypedCollection[Team]:")
    teams.add(team1)
    print(f"  Добавлена: {team1.name}")
    teams.add(team2)
    print(f"  Добавлена: {team2.name}")
    teams.add(team3)
    print(f"  Добавлена: {team3.name}")
    
    print(f"\nВсего команд в коллекции: {len(teams)}")
    
    print("\nСписок всех команд:")
    for team in teams.get_all():
        print(f"  - {team.name}: {team.division} дивизион, {team.total_points} очков")
    
    print("\nДемонстрация типобезопасности:")
    print("  При попытке добавить строку mypy выдаст ошибку:")
    print('  teams.add("не команда")  # error: Argument 1 has incompatible type "str"')
    
    print(f"\nУдаление команды '{team2.name}':")
    removed = teams.remove(team2)
    print(f"  Результат удаления: {removed}")
    print(f"  Осталось команд: {len(teams)}")


def demo_task_4():
    """
    Демонстрация задания на 4:
    - find() - поиск элемента
    - filter() - фильтрация
    - map() - преобразование с изменением типа
    """
    print()
    print("ДЕМОНСТРАЦИЯ ЗАДАНИЯ НА 4: ФУНКЦИИ ВЫСШЕГО ПОРЯДКА")
    print()
    
    teams: TypedCollection[Team] = TypedCollection()
    
    team1 = Team("Динамо", 75.5, 175.0, 85.0)
    team1.set_division("intermediate")
    
    team2 = Team("Спартак", 82.0, 180.0, 120.0)
    team2.set_division("professional")
    
    team3 = Team("ЦСКА", 70.0, 172.0, 65.0)
    team3.set_division("beginner")
    
    team4 = Team("Зенит", 78.0, 178.0, 150.0)
    team4.set_division("elite")
    
    team5 = Team("Локомотив", 68.0, 168.0, 45.0)
    team5.set_division("beginner")
    team5.deactivate()
    
    for t in [team1, team2, team3, team4, team5]:
        teams.add(t)
    
    print("Создана коллекция из 5 команд:")
    for t in teams:
        status = "активна" if t.is_active else "неактивна"
        print(f"  - {t.name}: {t.division} дивизион, {t.total_points} очков, {status}")
    
    print("\n--- find(): Поиск первого элемента ---")
    
    found = teams.find(lambda t: t.name == "Спартак")
    print("Поиск 'Спартак':")
    if found:
        print(f"  Найдена: {found.name}, {found.division} дивизион")
    else:
        print("  Не найдена")
    
    not_found = teams.find(lambda t: t.name == "Торпедо")
    print("Поиск 'Торпедо':")
    if not_found:
        print(f"  Найдена: {not_found.name}")
    else:
        print("  Команда не найдена (результат: None)")
    
    print("\n--- filter(): Фильтрация по условию ---")
    
    elite_teams = teams.filter(lambda t: t.division == "elite")
    print(f"Команды elite дивизиона ({len(elite_teams)}):")
    for t in elite_teams:
        print(f"  - {t.name}: {t.total_points} очков")
    
    active_teams = teams.filter(lambda t: t.is_active)
    print(f"\nАктивные команды ({len(active_teams)} из {len(teams)}):")
    for t in active_teams:
        print(f"  - {t.name}")
    
    high_score_teams = teams.filter(lambda t: t.total_points >= 100)
    print(f"\nКоманды с очками >= 100 ({len(high_score_teams)}):")
    for t in high_score_teams:
        print(f"  - {t.name}: {t.total_points} очков")
    
    print("\n--- map(): Преобразование с изменением типа результата ---")
    
    names: list[str] = teams.map(lambda t: t.name)
    print(f"Имена команд (list[str]): {names}")
    
    scores: list[float] = teams.map(lambda t: t.total_points)
    print(f"Очки команд (list[float]): {scores}")
    
    performances: list[float] = teams.map(lambda t: t.performance_score())
    print(f"Производительность (list[float]): {performances}")
    
    activity: list[bool] = teams.map(lambda t: t.is_active)
    print(f"Активность (list[bool]): {activity}")
    
    info: list[tuple[str, float]] = teams.map(lambda t: (t.name, t.total_points))
    print(f"Информация (list[tuple[str, float]]): {info}")
    
    print("\nМетод map() меняет тип результата в зависимости от переданной функции")


def demo_task_5_scenario_1():
    """
    Демонстрация задания на 5, Сценарий 1:
    TypedCollection[D] с ограничением Displayable
    """
    print()
    print("СЦЕНАРИЙ 1:")
    print("TypedCollection[D] с протоколом Displayable")
    print()
    
    add_team_display(None)
    
    displayable_teams: TypedCollection[D] = TypedCollection()
    
    team1 = Team("Динамо", 75.5, 175.0, 85.0)
    team1.set_division("intermediate")
    
    team2 = Team("Спартак", 82.0, 180.0, 120.0)
    team2.set_division("professional")
    
    team3 = Team("ЦСКА", 70.0, 172.0, 65.0)
    team3.set_division("beginner")
    
    print("Добавление Team в TypedCollection[D] (ограничение Displayable):")
    print("  Team не наследуется от Displayable явно")
    
    displayable_teams.add(team1)
    print(f"  Добавлена: {team1.name}")
    
    displayable_teams.add(team2)
    print(f"  Добавлена: {team2.name}")
    
    displayable_teams.add(team3)
    print(f"  Добавлена: {team3.name}")
    
    print(f"\nКоллекция содержит {len(displayable_teams)} элементов")
    
    print("\nВызов метода display() для всех элементов:")
    for i, team in enumerate(displayable_teams.get_all(), 1):
        print(f"  {i}. {team.display()}")
    
    print("\nОбъекты Team успешно работают с TypedCollection[D]")
    print("без явного наследования от Displayable")
    print("Достаточно наличия метода display() -> str")


def demo_task_5_scenario_2():
    """
    Демонстрация задания на 5, Сценарий 2:
    TypedCollection[S] с ограничением Scorable
    """
    print()
    print("СЦЕНАРИЙ 2:")
    print("TypedCollection[S] с протоколом Scorable")
    print()
    
    add_team_score(None)
    
    scorable_teams: TypedCollection[S] = TypedCollection()
    
    team1 = Team("Динамо", 75.5, 175.0, 85.0)
    team1.set_division("intermediate")
    team1.morale = 8
    
    team2 = Team("Спартак", 82.0, 180.0, 120.0)
    team2.set_division("professional")
    team2.morale = 10
    
    team3 = Team("ЦСКА", 70.0, 172.0, 65.0)
    team3.set_division("beginner")
    team3.morale = 5
    
    team4 = Team("Зенит", 78.0, 178.0, 150.0)
    team4.set_division("elite")
    team4.morale = 9
    
    print("Добавление Team в TypedCollection[S] (ограничение Scorable):")
    print("  Тот же класс Team, но другой протокол")
    
    for t in [team1, team2, team3, team4]:
        scorable_teams.add(t)
        print(f"  Добавлена: {t.name}")
    
    print(f"\nКоллекция содержит {len(scorable_teams)} элементов")
    
    print("\nВызов метода score() для всех элементов:")
    for i, team in enumerate(scorable_teams.get_all(), 1):
        print(f"  {i}. {team.name}: score = {team.score():.2f}")
    
    print("\nРейтинг команд по score():")
    sorted_teams = sorted(scorable_teams.get_all(), key=lambda t: t.score(), reverse=True)
    for i, team in enumerate(sorted_teams, 1):
        print(f"  {i}. {team.name} ({team.division}): {team.score():.2f}")
    
    print("\nИспользование map() на TypedCollection[S]:")
    scores = scorable_teams.map(lambda t: t.score())
    print(f"  Все оценки: {[f'{s:.2f}' for s in scores]}")
    
    print("\nОдин и тот же класс TypedCollection работает с разными протоколами")
    print("Team реализует структурную типизацию через наличие методов")
    print("Наследование от протоколов не требуется")


def demo_protocol_verification():
    """
    Проверка структурной типизации:
    демонстрация, что Team соответствует протоколам
    """
    print()
    print("ПРОВЕРКА СТРУКТУРНОЙ ТИПИЗАЦИИ")
    print()
    
    team = Team("Динамо", 75.0, 175.0, 100.0)
    
    add_team_display(None)
    add_team_score(None)
    
    print("Проверка соответствия Team протоколу Displayable:")
    print(f"  Наличие метода display(): {hasattr(team, 'display')}")
    print(f"  Результат display(): {team.display()}")
    print(f"  Тип результата: {type(team.display())}")
    print("  Team структурно соответствует Displayable")
    
    print("\nПроверка соответствия Team протоколу Scorable:")
    print(f"  Наличие метода score(): {hasattr(team, 'score')}")
    print(f"  Результат score(): {team.score()}")
    print(f"  Тип результата: {type(team.score())}")
    print("  Team структурно соответствует Scorable")


def main():
    """Главная функция демонстрации."""
    print()
    print("ЛАБОРАТОРНАЯ РАБОТА 6: GENERICS И TYPING")
    print()
    
    demo_task_3()
    demo_task_4()
    demo_task_5_scenario_1()
    demo_task_5_scenario_2()
    demo_protocol_verification()
    
    print("\nДемонстрация завершена успешно")


if __name__ == "__main__":
    main()