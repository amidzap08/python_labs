from two_sem.lab01.model import Athlete

def demo_validation():
    """Сценарий 1: базовая валидация."""
    print("Сценарий 1: Валидация данных")
    
    try:
        a = Athlete("", 70, 175)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")

    try:
        a = Athlete("Иван", -70, 175)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")

    try:
        a = Athlete("Иван", 350, 175)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")

    a = Athlete("Иван", 70, 175, 100)
    print(f"Создан спортсмен: {a}")

    try:
        a.weight = -80
    except ValueError as e:
        print(f"Ошибка при изменении веса: {e}")
    
    a.weight = 72
    print(f"Вес изменен на {a.weight}{Athlete.weight_unit}")
    print()

def demo_state_changes():
    """Сценарий 2: логическое состояние is_active."""
    print("Сценарий 2: Логическое состояние")
    
    a = Athlete("Мария", 65, 170, 80)
    print(f"Начальное состояние: {a}")

    a.deactivate()
    try:
        a.set_record(85)
    except RuntimeError as e:
        print(f"Ошибка при установке рекорда: {e}")

    a.activate()
    a.set_record(85)
    print(f"После активации: {a}")
    print()

def demo_equality():
    """Сценарий 3: сравнение объектов."""
    print("Сценарий 3: Сравнение объектов")
    
    a1 = Athlete("Петр", 80, 180, 120)
    a2 = Athlete("Петр", 80, 180, 120)
    a3 = Athlete("Петр", 80, 180, 130)

    print(f"a1: {repr(a1)}")
    print(f"a2: {repr(a2)}")
    print(f"a3: {repr(a3)}")
    print(f"a1 == a2: {a1 == a2}")
    print(f"a1 == a3: {a1 == a3}")

    a2.deactivate()
    print(f"a2 деактивирован, но сравнение a1 == a2: {a1 == a2}")
    print()

def demo_class_attribute():
    """Сценарий 4: атрибуты класса."""
    print("Сценарий 4: Атрибуты класса")
    
    print(f"Athlete.total_athletes = {Athlete.total_athletes}")
    print(f"Athlete.sport_type = {Athlete.sport_type}")
    print(f"Athlete.default_training_level = {Athlete.default_training_level}")
    print(f"Athlete.max_morale = {Athlete.max_morale}")
    print(f"Athlete.min_morale = {Athlete.min_morale}")
    print(f"Athlete.weight_unit = {Athlete.weight_unit}")
    print(f"Athlete.height_unit = {Athlete.height_unit}")
    print(f"Athlete.record_unit = {Athlete.record_unit}")

    a1 = Athlete("Олег", 75, 182, 110)
    a2 = Athlete("Анна", 62, 168, 95)
    print(f"\nСоздано два спортсмена: {a1.name} и {a2.name}")
    print(f"Через экземпляр a1: a1.sport_type = {a1.sport_type}")
    print(f"Через экземпляр a2: a2.max_morale = {a2.max_morale}")
    print(f"Теперь Athlete.total_athletes = {Athlete.total_athletes}")
    print()

def demo_multiple_states():
    """Сценарий 5: множественные состояния."""
    print("Сценарий 5: Множественные состояния")
    
    a = Athlete("Алексей", 78, 185, 140)
    a.set_training_level("intermediate")
    
    try:
        a.set_record(220)
    except ValueError as e:
        print(f"Ошибка: {e}")

    a.set_training_level("advanced")
    a.set_record(220)
    print(f"Уровень advanced, рекорд: {a.personal_record}")

    a.injure()
    try:
        a.set_record(230)
    except RuntimeError as e:
        print(f"При травме: {e}")

    a.recover()
    a.set_record(230)
    print(f"Восстановление, рекорд: {a.personal_record}")

    try:
        a.morale = 15
    except ValueError as e:
        print(f"Уровень мотивации: {e}")
    
    a.morale = 5
    print(f"Уровень мотивации: {a.morale}")
    print()

def demo_performance():
    """Сценарий 6: расчет производительности."""
    print("Сценарий 6: Расчет производительности")
    
    athletes = [
        Athlete("Начинающий", 70, 175, 80),
        Athlete("Продвинутый", 75, 180, 150),
        Athlete("Профессионал", 80, 185, 250)
    ]
    
    athletes[0].set_training_level("beginner")
    athletes[1].set_training_level("advanced")
    athletes[2].set_training_level("professional")
    
    athletes[0].morale = 8
    athletes[1].morale = 6
    athletes[2].morale = 10
    
    for athlete in athletes:
        print(f"{athlete.name}:")
        print(f"  Уровень: {athlete.training_level}")
        print(f"  Рекорд: {athlete.personal_record} {Athlete.record_unit}")
        print(f"  Уровень мотивации: {athlete.morale}/{Athlete.max_morale}")
        print(f"  ИМТ: {athlete.bmi()}")
        print(f"  Производительность: {athlete.performance_score()}")
        print()

if __name__ == "__main__":
    print("Демонстрация класса ATHLETE")
    print()
    
    demo_validation()
    demo_state_changes()
    demo_equality()
    demo_class_attribute()
    demo_multiple_states()
    demo_performance()
    
    print("конец")