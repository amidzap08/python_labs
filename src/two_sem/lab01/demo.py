from two_sem.lab01.model import Team

def demo_validation():
    """Сценарий 1: базовая валидация."""
    print("Сценарий 1: Валидация данных")
    
    try:
        t = Team("", 70, 175)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")

    try:
        t = Team("Спартак", -70, 175)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")

    try:
        t = Team("Спартак", 350, 175)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")

    t = Team("Спартак", 70, 175, 100)
    print(f"Создана команда: {t}")

    try:
        t.avg_weight = -80
    except ValueError as e:
        print(f"Ошибка при изменении веса: {e}")
    
    t.avg_weight = 72
    print(f"Средний вес изменен на {t.avg_weight}{Team.weight_unit}")
    print()

def demo_state_changes():
    """Сценарий 2: логическое состояние is_active."""
    print("Сценарий 2: Логическое состояние")
    
    t = Team("Динамо", 65, 170, 80)
    print(f"Начальное состояние: {t}")

    t.deactivate()
    try:
        t.set_points(85)
    except RuntimeError as e:
        print(f"Ошибка при установке очков: {e}")

    t.activate()
    t.set_points(85)
    print(f"После активации: {t}")
    print()

def demo_equality():
    """Сценарий 3: сравнение объектов."""
    print("Сценарий 3: Сравнение объектов")
    
    t1 = Team("Локомотив", 80, 180, 120)
    t2 = Team("Локомотив", 80, 180, 120)
    t3 = Team("Локомотив", 80, 180, 130)

    print(f"t1: {repr(t1)}")
    print(f"t2: {repr(t2)}")
    print(f"t3: {repr(t3)}")
    print(f"t1 == t2: {t1 == t2}")
    print(f"t1 == t3: {t1 == t3}")

    t2.deactivate()
    print(f"t2 деактивирована, но сравнение t1 == t2: {t1 == t2}")
    print()

def demo_class_attribute():
    """Сценарий 4: атрибуты класса."""
    print("Сценарий 4: Атрибуты класса")
    
    print(f"Team.total_teams = {Team.total_teams}")
    print(f"Team.sport_type = {Team.sport_type}")
    print(f"Team.default_division = {Team.default_division}")
    print(f"Team.max_morale = {Team.max_morale}")
    print(f"Team.min_morale = {Team.min_morale}")
    print(f"Team.weight_unit = {Team.weight_unit}")
    print(f"Team.height_unit = {Team.height_unit}")
    print(f"Team.record_unit = {Team.record_unit}")

    t1 = Team("Зенит", 75, 182, 110)
    t2 = Team("ЦСКА", 62, 168, 95)
    print(f"\nСоздано две команды: {t1.name} и {t2.name}")
    print(f"Через экземпляр t1: t1.sport_type = {t1.sport_type}")
    print(f"Через экземпляр t2: t2.max_morale = {t2.max_morale}")
    print(f"Теперь Team.total_teams = {Team.total_teams}")
    print()

def demo_multiple_states():
    """Сценарий 5: множественные состояния."""
    print("Сценарий 5: Множественные состояния")
    
    t = Team("Рубин", 78, 185, 140)
    t.set_division("intermediate")
    
    try:
        t.set_points(220)
    except ValueError as e:
        print(f"Ошибка: {e}")

    t.set_division("professional")
    t.set_points(220)
    print(f"Дивизион professional, очки: {t.total_points}")

    t.injure()
    try:
        t.set_points(230)
    except RuntimeError as e:
        print(f"При травмах: {e}")

    t.recover()
    t.set_points(230)
    print(f"Восстановление, очки: {t.total_points}")

    try:
        t.morale = 15
    except ValueError as e:
        print(f"Уровень мотивации: {e}")
    
    t.morale = 5
    print(f"Уровень мотивации: {t.morale}")
    print()

def demo_performance():
    """Сценарий 6: расчет производительности."""
    print("Сценарий 6: Расчет производительности")
    
    teams = [
        Team("Любитель", 70, 175, 80),
        Team("Полупрофи", 75, 180, 150),
        Team("Профи", 80, 185, 250)
    ]
    
    teams[0].set_division("beginner")
    teams[1].set_division("intermediate")
    teams[2].set_division("professional")
    
    teams[0].morale = 8
    teams[1].morale = 6
    teams[2].morale = 10
    
    for team in teams:
        print(f"{team.name}:")
        print(f"  Дивизион: {team.division}")
        print(f"  Очки: {team.total_points} {Team.record_unit}")
        print(f"  Уровень мотивации: {team.morale}/{Team.max_morale}")
        print(f"  Средний ИМТ: {team.avg_bmi()}")
        print(f"  Производительность: {team.performance_score()}")
        print()

if __name__ == "__main__":
    print("Демонстрация класса TEAM")
    print()
    
    demo_validation()
    demo_state_changes()
    demo_equality()
    demo_class_attribute()
    demo_multiple_states()
    demo_performance()
    
    print("конец")