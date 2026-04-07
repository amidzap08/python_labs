"""
Демонстрация работы контейнерного класса TeamCollection.
Показывает все возможности коллекции согласно требованиям ЛР-2.
"""

from two_sem.lab02.collection import TeamCollection
from two_sem.lab01.model import Team


def demonstrate_basic_operations():
    """Демонстрация базовых операций (Задание на 3)."""
    print("\nЗадание на 3 - Базовые операции")
    
    collection = TeamCollection()
    print(f"Создана пустая коллекция: {len(collection)} элементов")
    
    team1 = Team("Alpha", 72.5, 175.0, 150.0)
    team2 = Team("Beta", 68.0, 170.0, 120.0)
    team3 = Team("Gamma", 75.0, 180.0, 200.0)
    
    print(f"\nСозданы команды:")
    print(f"  - {team1.name}")
    print(f"  - {team2.name}")
    print(f"  - {team3.name}")
    
    print(f"\nДобавление команд в коллекцию:")
    collection.add(team1)
    print(f"  + Добавлена {team1.name}")
    collection.add(team2)
    print(f"  + Добавлена {team2.name}")
    collection.add(team3)
    print(f"  + Добавлена {team3.name}")
    
    print(f"\nВсе элементы коллекции ({len(collection)}):")
    all_teams = collection.get_all()
    for i, team in enumerate(all_teams, 1):
        print(f"  {i}. {team.name} (очки: {team.total_points})")
    
    print(f"\nУдаление команды {team2.name}:")
    collection.remove(team2)
    print(f"  - Удалена {team2.name}")
    
    print(f"\nКоллекция после удаления ({len(collection)}):")
    for i, team in enumerate(collection.get_all(), 1):
        print(f"  {i}. {team.name} (очки: {team.total_points})")
    
    print(f"\nПроверка валидации типа:")
    try:
        collection.add("не команда")
    except TypeError as e:
        print(f"  Ошибка (ожидаемо): {e}")
    
    print(f"\nПроверка на дубликаты:")
    try:
        collection.add(team1)
    except ValueError as e:
        print(f"  Ошибка (ожидаемо): {e}")


def demonstrate_search_and_iteration():
    """Демонстрация поиска и итерации (Задание на 4)."""
    print("\nЗадание на 4 - Поиск и итерация")
    
    collection = TeamCollection()
    
    teams_data = [
        ("Alpha", 72.5, 175.0, 150.0, "intermediate", "healthy"),
        ("Beta", 68.0, 170.0, 120.0, "beginner", "healthy"),
        ("Gamma", 75.0, 180.0, 200.0, "professional", "injured"),
        ("Delta", 70.0, 172.0, 180.0, "intermediate", "recovering"),
        ("Epsilon", 65.0, 168.0, 250.0, "elite", "healthy"),
    ]
    
    for name, weight, height, points, division, health in teams_data:
        team = Team(name, weight, height, points)
        if division != "beginner":
            team.set_division(division)
        if health == "injured":
            team.injure()
        elif health == "recovering":
            team.injure()
            team.recover()
        collection.add(team)
    
    print(f"Создана коллекция из {len(collection)} команд")
    
    print(f"\nПоиск по имени 'Gamma':")
    found = collection.find_by_name("Gamma")
    if found:
        print(f"  Найдена: {found.name} - {found.division} - статус: {found.health_status}")
    
    print(f"\nПоиск по дивизиону 'intermediate':")
    intermediate_teams = collection.find_by_division("intermediate")
    for team in intermediate_teams:
        print(f"  - {team.name} (очки: {team.total_points})")
    
    print(f"\nПоиск здоровых команд:")
    healthy_teams = collection.find_by_health_status("healthy")
    for team in healthy_teams:
        print(f"  - {team.name} (статус: {team.health_status})")
    
    print(f"\nИспользование len(): {len(collection)} команд в коллекции")
    
    print(f"\nИтерация по коллекции с помощью for:")
    for i, team in enumerate(collection, 1):
        print(f"  {i}. {team.name} - производительность: {team.performance_score()}")


def demonstrate_advanced_features():
    """Демонстрация расширенных возможностей (Задание на 5)."""
    print("\nЗадание на 5 - Индексация, сортировка и фильтрация")
    
    collection = TeamCollection()
    
    teams = [
        Team("Zeta", 74.0, 178.0, 180.0),
        Team("Alpha", 70.0, 173.0, 150.0),
        Team("Delta", 72.0, 176.0, 200.0),
        Team("Beta", 68.0, 170.0, 120.0),
        Team("Gamma", 76.0, 182.0, 250.0),
    ]
    
    for team in teams:
        collection.add(team)
    
    print(f"Исходная коллекция ({len(collection)} команд):")
    for i, team in enumerate(collection, 1):
        print(f"  {i}. {team.name} (очки: {team.total_points})")
    
    print(f"\nИндексация коллекции:")
    print(f"  collection[0] = {collection[0].name}")
    print(f"  collection[2] = {collection[2].name}")
    print(f"  collection[-1] = {collection[-1].name} (последний элемент)")
    print(f"  collection[-2] = {collection[-2].name} (предпоследний элемент)")
    
    try:
        print(f"  Попытка доступа к collection[10]...")
        print(collection[10])
    except IndexError as e:
        print(f"  Ошибка (ожидаемо): {e}")
    
    print(f"\nУдаление по индексу:")
    removed = collection.remove_at(2)
    print(f"  Удалена команда: {removed.name} (индекс 2)")
    print(f"  Осталось команд: {len(collection)}")
    
    print(f"\nСортировка по имени:")
    collection.sort_by_name()
    for i, team in enumerate(collection, 1):
        print(f"  {i}. {team.name}")
    
    print(f"\nСортировка по очкам (по убыванию):")
    collection.sort_by_points(reverse=True)
    for i, team in enumerate(collection, 1):
        print(f"  {i}. {team.name}: {team.total_points} очков")
    
    print(f"\nФильтрация - активные команды:")
    if len(collection) > 0:
        collection[0].deactivate()
    active_collection = collection.get_active_teams()
    print(f"  Активных команд: {len(active_collection)} из {len(collection)}")
    for team in active_collection:
        print(f"  - {team.name} (активна: {team.is_active})")
    
    print(f"\nФильтрация - здоровые команды:")
    healthy_collection = collection.get_healthy_teams()
    print(f"  Здоровых команд: {len(healthy_collection)} из {len(collection)}")
    for team in healthy_collection:
        print(f"  - {team.name} (здоровье: {team.health_status})")
    
    print("\nСценарии использования")
    
    print("\nСценарий 1: Управление турнирной таблицей")
    tournament = TeamCollection()
    
    tournament_teams = [
        Team("Titans", 75.0, 180.0, 100.0),
        Team("Warriors", 72.0, 177.0, 95.0),
        Team("Gladiators", 78.0, 183.0, 110.0),
        Team("Spartans", 70.0, 175.0, 88.0),
    ]
    
    for team in tournament_teams:
        tournament.add(team)
    
    print("Турнирная таблица (до сортировки):")
    for team in tournament:
        print(f"  - {team.name}: {team.total_points} очков")
    
    tournament.sort_by_points(reverse=True)
    print("\nТурнирная таблица (после сортировки по очкам):")
    for i, team in enumerate(tournament, 1):
        print(f"  {i}. {team.name}: {team.total_points} очков")
    
    print("\nСценарий 2: Управление травмами и восстановлением")
    league = TeamCollection()
    
    team_a = Team("Aces", 71.0, 174.0, 150.0)
    team_b = Team("Bulls", 73.0, 178.0, 140.0)
    
    league.add(team_a)
    league.add(team_b)
    
    print("Исходное состояние:")
    for team in league:
        print(f"  - {team.name}: здоровье={team.health_status}, очки={team.total_points}")
    
    print("\nКоманда Aces получает травму")
    team_a.injure()
    
    print("\nПопытка изменить очки травмированной команды:")
    try:
        team_a.total_points = 160.0
    except RuntimeError as e:
        print(f"  Ошибка: {e}")
    
    print("\nПроцесс восстановления:")
    team_a.recover()
    print(f"  Команда {team_a.name} в статусе: {team_a.health_status}")
    
    team_a.heal()
    print(f"  Команда {team_a.name} полностью здорова: {team_a.health_status}")
    
    print("\nСценарий 3: Анализ производительности команд")
    analysis = TeamCollection()
    
    performance_teams = [
        Team("Speed", 68.0, 170.0, 180.0),
        Team("Power", 85.0, 185.0, 150.0),
        Team("Agility", 62.0, 165.0, 220.0),
        Team("Endurance", 75.0, 178.0, 195.0),
    ]
    
    performance_teams[0].set_division("elite")
    performance_teams[2].set_division("professional")
    
    for team in performance_teams:
        analysis.add(team)
    
    print("Анализ производительности команд:")
    for team in analysis:
        performance = team.performance_score()
        if performance > 200:
            rating = "Высокая"
        elif performance > 100:
            rating = "Средняя"
        else:
            rating = "Низкая"
        print(f"  - {team.name}: {performance} очков производительности ({rating})")
    
    high_perf = analysis.get_high_performance_teams(threshold=150)
    print(f"\nКоманды с высокой производительностью (>150):")
    for team in high_perf:
        print(f"  - {team.name}: {team.performance_score()} очков")
    
    print("\nДемонстрация завершена")


if __name__ == "__main__":
    demonstrate_basic_operations()
    demonstrate_search_and_iteration()
    demonstrate_advanced_features()