"""
Модуль demo.py - демонстрация работы класса Team
"""

from two_sem.lab01.model import Athlete
from two_sem.lab02.collection import Team


def print_separator(title: str = ""):
    """Печать разделителя"""
    print("\n" + "=" * 60)
    if title:
        print(f" {title} ")
        print("=" * 60)


def main():
    """Основная функция демонстрации"""
    
    # ========== Демонстрация задания на 3 ==========
    print_separator("ЗАДАНИЕ НА 3")
    
    # Создание спортсменов
    print("\n1. Создание спортсменов:")
    athlete1 = Athlete("Иван Петров", 75.5, 180, 120.0, "intermediate", "healthy", 8)
    athlete2 = Athlete("Мария Смирнова", 62.0, 165, 95.0, "beginner", "healthy", 7)
    athlete3 = Athlete("Алексей Иванов", 85.0, 190, 150.0, "advanced", "recovering", 6)
    athlete4 = Athlete("Елена Кузнецова", 58.5, 170, 110.0, "intermediate", "healthy", 9)
    
    print(f"  - {athlete1.name}")
    print(f"  - {athlete2.name}")
    print(f"  - {athlete3.name}")
    print(f"  - {athlete4.name}")
    
    # Создание команды и добавление спортсменов
    print("\n2. Создание команды 'Сборная России':")
    team = Team("Сборная России")
    
    print("   Добавление спортсменов:")
    for athlete in [athlete1, athlete2, athlete3, athlete4]:
        if team.add(athlete):
            print(f"   ✓ Добавлен: {athlete.name}")
        else:
            print(f"   ✗ Не добавлен: {athlete.name} (уже существует)")
    
    # Попытка добавить спортсмена с существующим именем
    print("\n3. Попытка добавить дубликат:")
    duplicate = Athlete("Иван Петров", 80.0, 185, 130.0, "advanced", "healthy", 7)
    if not team.add(duplicate):
        print(f"   ✗ Не удалось добавить: {duplicate.name} (спортсмен с таким именем уже есть)")
    
    # Попытка добавить объект неправильного типа
    print("\n4. Попытка добавить объект неправильного типа:")
    try:
        team.add("Это не спортсмен")
    except TypeError as e:
        print(f"   ✗ Ошибка: {e}")
    
    # Вывод всех спортсменов
    print("\n5. Все спортсмены в команде:")
    all_athletes = team.get_all()
    for athlete in all_athletes:
        print(f"   - {athlete.name}")
    
    # Удаление спортсмена
    print("\n6. Удаление спортсмена:")
    if team.remove(athlete3):
        print(f"   ✓ Удален: {athlete3.name}")
    
    print("\n7. Список после удаления:")
    for athlete in team.get_all():
        print(f"   - {athlete.name}")
    
    # ========== Демонстрация задания на 4 ==========
    print_separator("ЗАДАНИЕ НА 4")
    
    # Добавляем обратно удаленного спортсмена
    team.add(athlete3)
    
    # Поиск по имени
    print("\n1. Поиск спортсмена по имени:")
    found = team.find_by_name("Мария Смирнова")
    if found:
        print(f"   Найден: {found.name}")
    
    # Поиск по уровню подготовки
    print("\n2. Поиск спортсменов по уровню подготовки 'intermediate':")
    intermediates = team.find_by_training_level("intermediate")
    for athlete in intermediates:
        print(f"   - {athlete.name} (уровень: {athlete.training_level})")
    
    # Поиск по статусу здоровья
    print("\n3. Поиск спортсменов со статусом 'healthy':")
    healthy = team.find_by_health_status("healthy")
    for athlete in healthy:
        print(f"   - {athlete.name} (здоровье: {athlete.health_status})")
    
    # Поиск активных спортсменов
    print("\n4. Поиск активных спортсменов:")
    active = team.find_active()
    for athlete in active:
        print(f"   - {athlete.name} (активен: {athlete.is_active})")
    
    # Поиск по производительности
    print("\n5. Поиск спортсменов с производительностью > 100:")
    high_performance = team.find_by_performance(100)
    for athlete in high_performance:
        print(f"   - {athlete.name}: производительность = {athlete.performance_score():.1f}")
    
    # Демонстрация len()
    print(f"\n6. Количество спортсменов в команде: {len(team)}")
    
    # Демонстрация итерации
    print("\n7. Итерация по команде (for item in team):")
    for i, athlete in enumerate(team, 1):
        print(f"   {i}. {athlete.name} - {athlete.training_level}")
    
    # ========== Демонстрация задания на 5 ==========
    print_separator("ЗАДАНИЕ НА 5")
    
    # Индексация
    print("\n1. Доступ по индексу:")
    print(f"   team[0] = {team[0].name}")
    print(f"   team[1] = {team[1].name}")
    print(f"   team[2] = {team[2].name}")
    print(f"   team[-1] = {team[-1].name}")
    
    # Срез
    print("\n2. Срез team[1:3]:")
    for athlete in team[1:3]:
        print(f"   - {athlete.name}")
    
    # Удаление по индексу
    print("\n3. Удаление по индексу (team.remove_at(2)):")
    removed = team.remove_at(2)
    if removed:
        print(f"   Удален: {removed.name}")
    
    print(f"\n   После удаления (всего: {len(team)}):")
    for athlete in team:
        print(f"   - {athlete.name}")
    
    # Восстанавливаем удаленного спортсмена
    team.add(removed)
    
    # Сортировка по имени
    print("\n4. Сортировка по имени:")
    team.sort_by_name()
    for athlete in team:
        print(f"   - {athlete.name}")
    
    # Сортировка по рекорду
    print("\n5. Сортировка по личному рекорду (по убыванию):")
    team.sort_by_record(reverse=True)
    for athlete in team:
        print(f"   - {athlete.name}: рекорд = {athlete.personal_record}")
    
    # Сортировка по производительности
    print("\n6. Сортировка по производительности:")
    team.sort_by_performance(reverse=True)
    for athlete in team:
        print(f"   - {athlete.name}: производительность = {athlete.performance_score():.1f}")
    
    # Логические операции
    print("\n7. Логические операции над коллекцией:")
    
    # Активные спортсмены
    print("\n   Активные спортсмены:")
    active_team = team.get_active_athletes()
    for athlete in active_team:
        print(f"   - {athlete.name} (активен: {athlete.is_active})")
    
    # Деактивируем одного спортсмена
    team[0].deactivate()
    
    print("\n   После деактивации первого спортсмена:")
    print("   Все спортсмены:")
    for athlete in team:
        status = "активен" if athlete.is_active else "неактивен"
        print(f"   - {athlete.name}: {status}")
    
    print("\n   Только активные:")
    active_team = team.get_active_athletes()
    for athlete in active_team:
        print(f"   - {athlete.name}")
    
    # Здоровые спортсмены
    print("\n   Здоровые спортсмены:")
    healthy_team = team.get_healthy_athletes()
    for athlete in healthy_team:
        print(f"   - {athlete.name} (здоровье: {athlete.health_status})")
    
    # Спортсмены по уровню подготовки
    print("\n   Спортсмены уровня 'professional':")
    pro_team = team.get_by_training_level("professional")
    if len(pro_team) == 0:
        print("   Нет спортсменов уровня professional")
    else:
        for athlete in pro_team:
            print(f"   - {athlete.name}")
    
    # Финальный вывод
    print_separator("ИТОГОВАЯ ИНФОРМАЦИЯ")
    print(f"\n{team}")
    
    print("\nСписок всех спортсменов с детальной информацией:")
    for athlete in team:
        print(f"\n{athlete}")
        print(f"   Производительность: {athlete.performance_score():.2f}")
        print(f"   ИМТ: {athlete.bmi():.1f}")


if __name__ == "__main__":
    main()