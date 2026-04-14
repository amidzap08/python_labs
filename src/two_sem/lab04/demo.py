"""
Демонстрация работы интерфейсов.
"""

from two_sem.lab04.models import Team, Player, Match
from two_sem.lab04.interfaces import Printable, Comparable, Identifiable, Validatable


def demo_task_3():
    """Демонстрация задания на 3."""

    print("ЗАДАНИЕ НА 3: Базовые интерфейсы")

    team1 = Team("Lakers", "Pacific", total_points=52, wins=26, losses=12)
    team2 = Team("Warriors", "Pacific", total_points=44, wins=22, losses=16)
    
    print("\nИнтерфейс Printable")
    print(team1.to_string())
    print(team2.to_string())
    
    print("\n Интерфейс Comparable")
    result = team1.compare_to(team2)
    if result > 0:
        print(f"{team1.name} > {team2.name}")
    elif result < 0:
        print(f"{team1.name} < {team2.name}")
    else:
        print(f"{team1.name} == {team2.name}")
    
    print("\n Интерфейс Identifiable ")
    print(f"Team1 ID: {team1.get_id()}")
    print(f"Team2 ID: {team2.get_id()}")
    
    print("\n Интерфейс Validatable ")
    print(f"Team1 valid: {team1.is_valid()}")
    print(f"Team1 errors: {team1.get_validation_errors()}")


def demo_task_4():
    """Демонстрация задания на 4."""
    print()
    print("ЗАДАНИЕ НА 4: Интерфейс как тип, isinstance")
    print()
    
    team = Team("Celtics", "Atlantic", total_points=58, wins=29, losses=9)
    player = Player("LeBron James", "Forward", "Lakers", skill_rating=96)
    match = Match("Lakers", "Warriors", home_score=112, away_score=108, is_completed=True)
    
    objects = [team, player, match]
    
    # Универсальная функция, работающая через интерфейс Printable
    def print_all(items: list[Printable]):
        print("\n print_all() через интерфейс Printable ")
        for i, item in enumerate(items):
            print(f"{i+1}. {item.to_string()}")
    
    print_all(objects)
    
    # Проверка isinstance
    print("\nisinstance() проверка ")
    for obj in objects:
        name = obj.__class__.__name__
        print(f"{name}:")
        print(f"  Printable: {isinstance(obj, Printable)}")
        print(f"  Comparable: {isinstance(obj, Comparable)}")
        print(f"  Identifiable: {isinstance(obj, Identifiable)}")
        print(f"  Validatable: {isinstance(obj, Validatable)}")
    
    # Множественная реализация
    print("\n Множественная реализация ")
    print("Team: Printable, Comparable, Identifiable, Validatable")
    print("Player: Printable, Comparable, Identifiable")
    print("Match: Printable, Comparable")
    
    # Функция сортировки через Comparable (только для однотипных объектов)
    def sort_comparable(items: list) -> list:
        """Сортировка объектов через интерфейс Comparable (только однотипные)."""
        from functools import cmp_to_key
        
        # Группируем по типам
        by_type = {}
        for item in items:
            if isinstance(item, Comparable):
                t = type(item)
                if t not in by_type:
                    by_type[t] = []
                by_type[t].append(item)
        
        # Сортируем каждую группу
        result = []
        for t, group in by_type.items():
            result.extend(sorted(group, key=cmp_to_key(lambda a, b: a.compare_to(b))))
        
        return result
    
    print("\n Сортировка через Comparable (по типам) ")
    comparable_items = [obj for obj in objects if isinstance(obj, Comparable)]
    sorted_items = sort_comparable(comparable_items)
    for item in sorted_items:
        print(f"  {item.__class__.__name__}: {item.to_string()}")


def demo_task_5():
    """Демонстрация задания на 5."""
    print()
    print("ЗАДАНИЕ НА 5: Полиморфизм и архитектура")
    print()
    
    # Создаем список разных объектов
    items = [
        Team("Lakers", "Pacific", total_points=52, wins=26, losses=12),
        Team("Warriors", "Pacific", total_points=44, wins=22, losses=16),
        Team("Celtics", "Atlantic", total_points=58, wins=29, losses=9),
        Player("LeBron James", "Forward", "Lakers", skill_rating=96),
        Player("Stephen Curry", "Guard", "Warriors", skill_rating=94),
        Player("Anthony Davis", "Center", "Lakers", skill_rating=91),
        Match("Lakers", "Warriors", 112, 108, True),
        Match("Celtics", "Nets", 98, 87, True),
        Match("Bulls", "Heat", 105, 110, True),
    ]
    
    # Сценарий 1: Фильтрация по интерфейсу
    print("\n Сценарий 1: Фильтрация по интерфейсу ")
    
    def filter_by_interface(items: list, interface_class) -> list:
        return [item for item in items if isinstance(item, interface_class)]
    
    printable_items = filter_by_interface(items, Printable)
    comparable_items = filter_by_interface(items, Comparable)
    identifiable_items = filter_by_interface(items, Identifiable)
    validatable_items = filter_by_interface(items, Validatable)
    
    print(f"Printable: {len(printable_items)} объектов")
    print(f"Comparable: {len(comparable_items)} объектов")
    print(f"Identifiable: {len(identifiable_items)} объектов")
    print(f"Validatable: {len(validatable_items)} объектов")
    
    # Сценарий 2: Полиморфизм без isinstance
    print("\nСценарий 2: Полиморфизм без isinstance ")
    print("Вызов to_string() напрямую:")
    for item in printable_items[:3]:
        print(f"  {item.to_string()}")
    
    # Сценарий 3: Сортировка через Comparable (только однотипные)
    print("\n Сценарий 3: Сортировка через Comparable ")
    
    from functools import cmp_to_key
    
    # Сортируем только Team
    teams = [item for item in items if isinstance(item, Team)]
    sorted_teams = sorted(teams, key=cmp_to_key(lambda a, b: a.compare_to(b)))
    
    print("Команды по возрастанию производительности:")
    for team in sorted_teams:
        print(f"  {team.name}: {team.performance_score():.1f}")
    
    # Сортируем только Player
    players = [item for item in items if isinstance(item, Player)]
    sorted_players = sorted(players, key=cmp_to_key(lambda a, b: a.compare_to(b)))
    
    print("\nИгроки по возрастанию рейтинга:")
    for player in sorted_players:
        print(f"  {player.name}: {player.skill_rating}")
    
    # Сортируем только Match
    matches = [item for item in items if isinstance(item, Match)]
    sorted_matches = sorted(matches, key=cmp_to_key(lambda a, b: a.compare_to(b)))
    
    print("\nМатчи по возрастанию голов:")
    for match in sorted_matches:
        print(f"  {match.home_team} vs {match.away_team}: {match.home_score + match.away_score} голов")
    
    # Сценарий 4: Валидация
    print("\n Сценарий 4: Валидация объектов ")
    
    # Создаем невалидную команду
    invalid_team = Team("", "Atlantic", total_points=-10, morale=150, health_status="unknown")
    validatable_all = [invalid_team] + [item for item in items if isinstance(item, Validatable)]
    
    for obj in validatable_all[:4]:
        name = getattr(obj, 'name', obj.__class__.__name__)
        if name == "":
            name = "<empty name>"
        if obj.is_valid():
            print(f"  {name}: валиден")
        else:
            print(f"  {name}: невалиден - {obj.get_validation_errors()}")
    
    # Сценарий 5: Поиск по ID
    print("\n Сценарий 5: Поиск по Identifiable ")
    
    def find_by_id(items: list, obj_id: str):
        for item in items:
            if isinstance(item, Identifiable) and item.get_id() == obj_id:
                return item
        return None
    
    # Показываем все ID
    print("Доступные ID:")
    for item in identifiable_items:
        print(f"  {item.get_id()}")
    
    target_id = "lakers_pacific"
    found = find_by_id(items, target_id)
    if found:
        print(f"\nНайден по ID '{target_id}': {found.to_string()}")
    else:
        print(f"\nОбъект с ID '{target_id}' не найден")


def main():
    """Главная функция."""
    print()
    print("ЛАБОРАТОРНАЯ РАБОТА №4")
    print("Интерфейсы и абстрактные классы")
    print()
    
    demo_task_3()
    demo_task_4()
    demo_task_5()
    
    print()
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print()


if __name__ == "__main__":
    main()