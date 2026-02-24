from two_sem.lab01.model import Athlete


def print_header(text):
    """Вывод заголовка"""
    print(f"\n{text}")



def print_result(text):
    """Вывод результата с отступом"""
    print(f"  {text}")


def main():
    """Основная функция демонстрации"""
    
    print("\n Демонстрация класса ATHLETE")
   
    
    # 1. Создание объектов
    print_header("1. создание объектов")
    
    try:
        athlete1 = Athlete("Иван Петров", 25, "Футбол", 75.5, 12.5)
        athlete2 = Athlete("Мария Сидорова", 22, "Плавание", 60.0, 45.3)
        
        print_result("athlete1 создан")
        print_result("athlete2 создан")
        print_result(f"athlete1: {athlete1}")
        print_result(f"athlete2: {athlete2}")
        
    except ValueError as e:
        print_result(f"Ошибка: {e}")
    
    # 2. Сравнение объектов
    print_header("2. сравнение объектов")
    
    try:
        athlete3 = Athlete("Иван Петров", 30, "Футбол", 80.0, 13.0)
        athlete4 = Athlete("Анна Иванова", 28, "Теннис", 62.0, 10.5)
        
        print_result(f"athlete1 == athlete3: {athlete1 == athlete3}")
        print_result(f"athlete1 == athlete4: {athlete1 == athlete4}")
    except Exception as e:
        print_result(f"Ошибка: {e}")
    
    # 3. Некорректное создание (try/except)
    print_header("3. некорректное создание")
    
    try:
        athlete_invalid = Athlete("A", 10, "Хоккей", -70, -5)
        print_result(f"Создан: {athlete_invalid}")
    except ValueError as e:
        print_result(f"ошибка: {e}")
    
    # 4. Использование сеттеров
    print_header("4. использование сеттеров")
    
    try:
        print_result(f"Текущий вес athlete1: {athlete1.weight} кг")
        athlete1.weight = 80.5
        print_result(f"Новый вес после установки: {athlete1.weight} кг")
        
        # Попытка установить некорректный вес
        print_result("Попытка установить вес -10 кг:")
        athlete1.weight = -10
    except ValueError as e:
        print_result(f" ошибка: {e}")
    
    # 5. Атрибуты класса
    print_header("5. атрибуты класса")
    
    print_result(f"Через класс: {Athlete.sport_type_list}")
    print_result(f"Через экземпляр: {athlete1.sport_type_list}")
    print_result(f"Минимальный возраст: {Athlete.min_age}")
    print_result(f"Максимальный возраст: {Athlete.max_age}")
    
    # 6. Магические методы
    print_header("6. магические методы")
    
    print_result(f"__str__: {athlete1}")
    print_result(f"__repr__: {repr(athlete1)}")
    
    # 7. Бизнес-методы
    print_header("7. бизнес-методы")
    
    try:
        # Тренировка
        print_result(athlete1.train(2.5))
        
        # Обновление рекорда
        print_result(athlete2.update_record(46.8))
        
        # ИМТ и возрастная категория
        print_result(f"ИМТ athlete1: {athlete1.get_bmi()}")
        print_result(f"Возрастная категория athlete1: {athlete1.get_age_category()}")
    except ValueError as e:
        print_result(f" Ошибка: {e}")
    
    # 8. Логические состояния
    print_header("8. логические состояния")
    
    try:
        print_result(f"Текущий статус athlete2: {athlete2.is_active}")
        
        # Деактивация
        athlete2.deactivate()
        print_result(" athlete2 деактивирован")
        print_result(f"Статус после деактивации: {athlete2.is_active}")
        
        # Попытка тренировки неактивного спортсмена
        print_result("Попытка тренировки неактивного спортсмена:")
        print_result(athlete2.train(1.0))
    except ValueError as e:
        print_result(f"ошибка: {e}")
    
    try:
        # Активация
        athlete2.activate()
        print_result("\n athlete2 реактивирован")
        print_result(f"Статус после активации: {athlete2.is_active}")
        print_result(athlete2.train(1.5))
    except ValueError as e:
        print_result(f"Ошибка: {e}")
    
    # 9. Три сценария работы
    print_header("9. три сценария работы")
    
    # Сценарий 1: Юный спортсмен
    print_result("Сценарий 1: Юный спортсмен")
    try:
        young = Athlete("Петр Сидоров", 16, "Теннис", 55.0, 8.2)
        print_result(f"  {young}")
        print_result(f"  {young.train(5.0)}")
        print_result(f"  Категория: {young.get_age_category()}")
    except ValueError as e:
        print_result(f"  Ошибка: {e}")
    
    print_result("")
    
    # Сценарий 2: Улучшение рекорда
    print_result("Сценарий 2: Постепенное улучшение рекорда")
    try:
        runner = Athlete("Алексей Бегун", 28, "Легкая атлетика", 70.0, 10.2)
        print_result(f"  Начальный рекорд: {runner.personal_record}")
        print_result(f"  {runner.update_record(10.5)}")
        print_result(f"  {runner.update_record(10.3)}")
        print_result(f"  {runner.update_record(10.8)}")
        print_result(f"  Итоговый рекорд: {runner.personal_record}")
    except ValueError as e:
        print_result(f"  Ошибка: {e}")
    
    print_result("")
    
    # Сценарий 3: Спортсмен-ветеран
    print_result("Сценарий 3: Спортсмен-ветеран")
    try:
        veteran = Athlete("Борис Старков", 45, "Плавание", 85.0, 30.5)
        print_result(f"  {veteran}")
        print_result(f"  Категория: {veteran.get_age_category()}")
        print_result(f"  ИМТ: {veteran.get_bmi()}")
    except ValueError as e:
        print_result(f"  Ошибка: {e}")
    
    print("конец")


if __name__ == "__main__":
    main()