from two_sem.lab01.model import Athlete
from two_sem.lab01.validate import AthleteValidator  # Импортируем валидатор для демонстрации


def print_header(text):
    """Вывод заголовка"""
    print(f" {text}")


def print_result(text):
    """Вывод результата с отступом"""
    print(f"  {text}")


def demonstrate_validator():
    """Демонстрация работы валидатора отдельно"""
    print_header("Демонстрация работы валидатора")
    
    print_result("Проверка корректных данных:")
    try:
        AthleteValidator.check_all("Иван Петров", 25, "Футбол", 75.5, 12.5)
        print_result("Все проверки пройдены успешно")
    except (TypeError, ValueError) as e:
        print_result(f" Ошибка: {e}")
    
    print_result("\nПроверка некорректных данных:")
    try:
        AthleteValidator.check_all("A", 10, "Хоккей", -70, -5)
    except (TypeError, ValueError) as e:
        print_result(f"ошибка: {e}")
    
    print_result("\nПроверка тренировочных часов для юниора:")
    warning = AthleteValidator.check_junior_training_hours(5.0, 16)
    if warning:
        print_result(f"{warning}")


def main():
    """Основная функция демонстрации"""
    
    print_header("Демонстрация класса ATHLETE")
    
    # Сначала покажем работу валидатора
    demonstrate_validator()
    
    # 1. Создание объектов
    print_header("1. Создание объектов")
    
    try:
        athlete1 = Athlete("Иван Петров", 25, "Футбол", 75.5, 12.5)
        athlete2 = Athlete("Мария Сидорова", 22, "Плавание", 60.0, 45.3)
        
        print_result("athlete1 создан")
        print_result(" athlete2 создан")
        print_result(f"athlete1: {athlete1}")
        print_result(f"athlete2: {athlete2}")
        
    except (TypeError, ValueError) as e:
        print_result(f" Ошибка: {e}")
    
    # 2. Сравнение объектов
    print_header("2. Сравнение объектов")
    
    try:
        athlete3 = Athlete("Иван Петров", 30, "Футбол", 80.0, 13.0)
        athlete4 = Athlete("Анна Иванова", 28, "Теннис", 62.0, 10.5)
        
        print_result(f"athlete1 == athlete3: {athlete1 == athlete3} (одинаковые имя и спорт)")
        print_result(f"athlete1 == athlete4: {athlete1 == athlete4} (разные)")
    except Exception as e:
        print_result(f"Ошибка: {e}")
    
    # 3. Некорректное создание (try/except)
    print_header("3. Некорректное создание")
    
    try:
        athlete_invalid = Athlete("A", 10, "Хоккей", -70, -5)
        print_result(f"Создан: {athlete_invalid}")
    except (TypeError, ValueError) as e:
        print_result(f" Ошибка: {e}")
        print_result("  Валидатор успешно предотвратил создание некорректного объекта")
    
    # 4. Использование сеттеров
    print_header("4. Использование сеттеров")
    
    try:
        print_result(f"Текущий вес athlete1: {athlete1.weight} кг")
        athlete1.weight = 80.5
        print_result(f"Новый вес после установки: {athlete1.weight} кг")
        # Попытка установить некорректный вес
        print_result("\nПопытка установить вес -10 кг (через валидатор):")
        athlete1.weight = -10
    except (TypeError, ValueError) as e:
        print_result(f" Ошибка: {e}")
    
    # 5. Атрибуты класса (теперь из валидатора)
    print_header("5. Атрибуты класса")
    
    print_result(f"Допустимые виды спорта: {Athlete.sport_type_list}")
    print_result(f"Минимальный возраст: {Athlete.min_age}")
    print_result(f"Максимальный возраст: {Athlete.max_age}")
    
    # 6. Магические методы
    print_header("6. Магические методы")
    
    print_result(f"__str__: {athlete1}")
    print_result(f"__repr__: {repr(athlete1)}")
    
    # 7. Бизнес-методы
    print_header("7. Бизнес-методы")
    
    try:
        # Тренировка
        print_result(athlete1.train(2.5))
        
        # Обновление рекорда
        print_result(athlete2.update_record(46.8))
        
        # ИМТ и возрастная категория
        print_result(f"ИМТ athlete1: {athlete1.get_bmi()}")
        print_result(f"Возрастная категория athlete1: {athlete1.get_age_category()}")
    except (TypeError, ValueError) as e:
        print_result(f"Ошибка: {e}")
    
    # 8. Логические состояния
    print_header("8. Логические состояния")
    
    try:
        print_result(f"Текущий статус athlete2: {athlete2.is_active}")
        
        # Деактивация
        athlete2.deactivate()
        print_result("athlete2 деактивирован")
        print_result(f"Статус после деактивации: {athlete2.is_active}")
        
        # Попытка тренировки неактивного спортсмена
        print_result("\nПопытка тренировки неактивного спортсмена:")
        print_result(athlete2.train(1.0))
    except ValueError as e:
        print_result(f"Ошибка: {e}")
    
    try:
        # Активация
        athlete2.activate()
        print_result("\nathlete2 реактивирован")
        print_result(f"Статус после активации: {athlete2.is_active}")
        print_result(athlete2.train(1.5))
    except (TypeError, ValueError) as e:
        print_result(f" Ошибка: {e}")
    
    # 9. Три сценария работы
    print_header("9. Три сценария работы")
    
    # Сценарий 1: Юный спортсмен (с проверкой через валидатор)
    print_result("СЦЕНАРИЙ 1: Юный спортсмен")
    try:
        young = Athlete("Петр Сидоров", 16, "Теннис", 55.0, 8.2)
        print_result(f"  {young}")
        print_result(f"  {young.train(5.0)}")  # Здесь сработает предупреждение валидатора
        print_result(f"  Категория: {young.get_age_category()}")
    except (TypeError, ValueError) as e:
        print_result(f"   Ошибка: {e}")
    
    print_result("")
    
    # Сценарий 2: Улучшение рекорда
    print_result("СЦЕНАРИЙ 2: Постепенное улучшение рекорда")
    try:
        runner = Athlete("Алексей Бегун", 28, "Легкая атлетика", 70.0, 10.2)
        print_result(f"  Начальный рекорд: {runner.personal_record}")
        print_result(f"  {runner.update_record(10.5)}")
        print_result(f"  {runner.update_record(10.3)}")
        print_result(f"  {runner.update_record(10.8)}")
        print_result(f"  Итоговый рекорд: {runner.personal_record}")
    except (TypeError, ValueError) as e:
        print_result(f"   Ошибка: {e}")
    
    print_result("")
    
    # Сценарий 3: Спортсмен-ветеран
    print_result("СЦЕНАРИЙ 3: Спортсмен-ветеран")
    try:
        veteran = Athlete("Борис Старков", 45, "Плавание", 85.0, 30.5)
        print_result(f"  {veteran}")
        print_result(f"  Категория: {veteran.get_age_category()}")
        print_result(f"  ИМТ: {veteran.get_bmi()}")
    except (TypeError, ValueError) as e:
        print_result(f"   Ошибка: {e}")
    
    print_header("конец")

    # ============= ДОБАВЛЕННЫЕ ПРОВЕРКИ ВСЕХ ОШИБОК =============
    
    print("\n")
    print_header("ОШИБКИ ВАЛИДАЦИИ ПРИ СОЗДАНИИ (через Validator):")
    
    # Проверка имени
    print("\nПопытка: тип имени (не строка)")
    try:
        AthleteValidator.check_name(123)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: пустое имя")
    try:
        AthleteValidator.check_name("")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: слишком короткое имя")
    try:
        AthleteValidator.check_name("A")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: слишком длинное имя")
    try:
        AthleteValidator.check_name("A" * 51)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    # Проверка возраста
    print("\nПопытка: тип возраста (не число)")
    try:
        AthleteValidator.check_age("двадцать")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: возраст меньше минимального")
    try:
        AthleteValidator.check_age(10)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: возраст больше максимального")
    try:
        AthleteValidator.check_age(60)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: возраст не целое число")
    try:
        AthleteValidator.check_age(25.5)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    # Проверка вида спорта
    print("\nПопытка: тип вида спорта (не строка)")
    try:
        AthleteValidator.check_sport_type(123)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: некорректный вид спорта")
    try:
        AthleteValidator.check_sport_type("Хоккей")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    # Проверка веса
    print("\nПопытка: тип веса (не число)")
    try:
        AthleteValidator.check_weight("семьдесят")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: отрицательный вес")
    try:
        AthleteValidator.check_weight(-10)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: вес слишком большой")
    try:
        AthleteValidator.check_weight(250)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    # Проверка личного рекорда
    print("\nПопытка: тип рекорда (не число)")
    try:
        AthleteValidator.check_personal_record("десять")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: отрицательный рекорд")
    try:
        AthleteValidator.check_personal_record(-5)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    # Проверка тренировочных часов
    print("\nПопытка: тип часов (не число)")
    try:
        AthleteValidator.check_training_hours("пять")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: отрицательные часы")
    try:
        AthleteValidator.check_training_hours(-2)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: часы слишком большие")
    try:
        AthleteValidator.check_training_hours(10)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    # Проверка статуса активности
    print("\nПопытка: тип статуса (не bool)")
    try:
        AthleteValidator.check_is_active("да")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print_header("ОШИБКИ ПРИ СОЗДАНИИ ОБЪЕКТА (через конструктор):")
    
    print("\nПопытка: все поля некорректны")
    try:
        athlete_invalid_full = Athlete("A", 10, "Хоккей", -70, -5)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: имя слишком короткое")
    try:
        athlete_invalid_name = Athlete("A", 25, "Футбол", 75, 10)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: возраст меньше минимального")
    try:
        athlete_invalid_age = Athlete("Иван", 10, "Футбол", 75, 10)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: возраст больше максимального")
    try:
        athlete_invalid_age_max = Athlete("Иван", 60, "Футбол", 75, 10)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: некорректный вид спорта")
    try:
        athlete_invalid_sport = Athlete("Иван", 25, "Хоккей", 75, 10)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: отрицательный вес")
    try:
        athlete_invalid_weight = Athlete("Иван", 25, "Футбол", -70, 10)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: вес слишком большой")
    try:
        athlete_invalid_weight_max = Athlete("Иван", 25, "Футбол", 250, 10)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: отрицательный рекорд")
    try:
        athlete_invalid_record = Athlete("Иван", 25, "Футбол", 75, -5)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print_header("ОШИБКИ ПРИ ИСПОЛЬЗОВАНИИ СЕТТЕРОВ:")
    
    # Создаем корректного спортсмена для тестов сеттеров
    test_athlete = Athlete("Тест Тестов", 25, "Футбол", 75.5, 12.5)
    
    print("\nПопытка: установить некорректное имя")
    try:
        test_athlete.name = "A"
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: установить некорректный возраст")
    try:
        test_athlete.age = 10
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: установить некорректный вид спорта")
    try:
        test_athlete.sport_type = "Хоккей"
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: установить отрицательный вес")
    try:
        test_athlete.weight = -10
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: установить отрицательный рекорд")
    try:
        test_athlete.personal_record = -5
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print_header("ОШИБКИ В БИЗНЕС-МЕТОДАХ:")
    
    print("\nПопытка: тренировка с отрицательными часами")
    try:
        test_athlete.train(-2)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: тренировка с часами больше максимума")
    try:
        test_athlete.train(10)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: тренировка с нечисловыми часами")
    try:
        test_athlete.train("пять")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: обновление рекорда с отрицательным значением")
    try:
        test_athlete.update_record(-5)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: обновление рекорда с нечисловым значением")
    try:
        test_athlete.update_record("десять")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    
    print_header("ОШИБКИ С ЛОГИЧЕСКИМ СОСТОЯНИЕМ:")
    
    # Деактивируем спортсмена
    test_athlete.deactivate()
    
    print("\nПопытка: тренировка неактивного спортсмена")
    try:
        test_athlete.train(2)
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    print("\nПопытка: обновление рекорда неактивного спортсмена")
    try:
        test_athlete.update_record(15)
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    # Активируем обратно
    test_athlete.activate()
    
    print("\nПопытка: повторная активация активного спортсмена")
    try:
        test_athlete.activate()
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    # Деактивируем
    test_athlete.deactivate()
    
    print("\nПопытка: повторная деактивация неактивного спортсмена")
    try:
        test_athlete.deactivate()
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    print_header("ПРЕДУПРЕЖДЕНИЯ ДЛЯ ЮНИОРОВ:")
    
    young_test = Athlete("Юный Спортсмен", 16, "Теннис", 55.0, 8.2)
    
    print("\nПопытка: тренировка юниора 5 часов")
    result = young_test.train(5)
    print(f"Результат: {result}")
    
    print_header("ИТОГ: Все возможные ошибки проверены и перехвачены")


if __name__ == "__main__":
    main()