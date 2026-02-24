# Лабораторная работа 1!!!
### model.py
```python
from datetime import datetime


class Athlete: #1 Один пользовательский класс 

    # Атрибуты класса
    sport_type_list = ["Футбол", "Баскетбол", "Плавание", "Легкая атлетика", "Теннис", "Бокс"]
    min_age = 14
    max_age = 50
    
    def __init__(self, name: str, age: int, sport_type: str, weight: float, personal_record: float = 0):#3/ конструктор с проверкой
#2/ 6 закрытых атрибутов 
        self._name = None
        self._age = None
        self._sport_type = None
        self._weight = None
        self._personal_record = None
        self._is_active = True  #по умолчанию спортсмен активен
        
        # Используем свойства для установки значений с валидацией 
        self.name = name
        self.age = age
        self.sport_type = sport_type
        self.weight = weight
        self.personal_record = personal_record
    
    # Валидация отдельных полей
    def _validate_name(self, name: str) -> None:
        #проверка корректности имени
        if not isinstance(name, str):
            raise ValueError("Имя должно быть строкой")
        if not name.strip():
            raise ValueError("Имя не может быть пустым")
        if len(name) < 2:
            raise ValueError("Имя должно содержать минимум 2 символа")
        if len(name) > 50:
            raise ValueError("Имя не может быть длиннее 50 символов")
    
    def _validate_age(self, age: int) -> None:
        #Проверка корректности возраста
        if not isinstance(age, int):
            raise ValueError("Возраст должен быть целым числом")
        if age < Athlete.min_age or age > Athlete.max_age:
            raise ValueError(f"Возраст должен быть от {Athlete.min_age} до {Athlete.max_age} лет")
    
    def _validate_sport_type(self, sport_type: str) -> None:
        #Проверка корректности вида спорта
        if not isinstance(sport_type, str):
            raise ValueError("Вид спорта должен быть строкой")
        if sport_type not in Athlete.sport_type_list:
            raise ValueError(f"Вид спорта должен быть одним из: {', '.join(Athlete.sport_type_list)}")
    
    def _validate_weight(self, weight: float) -> None:
        #Проверка корректности веса
        if not isinstance(weight, (int, float)):
            raise ValueError("Вес должен быть числом")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        if weight > 200:
            raise ValueError("Вес не может превышать 200 кг")
    
    def _validate_personal_record(self, record: float) -> None:
        #Проверка корректности личного рекорда
        if not isinstance(record, (int, float)):
            raise ValueError("Личный рекорд должен быть числом")
        if record < 0:
            raise ValueError("Личный рекорд не может быть отрицательным")
    
    # Свойства (геттеры и сеттеры)
    @property #4 Свойства для чтения Геттеры для доступа к данным
    def name(self) -> str:
        #Геттер для имени
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        #Сеттер для имени с валидацией
        self._validate_name(value)
        self._name = value.strip()
    
    @property
    def age(self) -> int:
        #Геттер для возраста
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        #Сеттер для возраста с валидацией
        self._validate_age(value)
        self._age = value
    
    @property
    def sport_type(self) -> str:
        #Геттер для вида спорт
        return self._sport_type
    
    @sport_type.setter
    def sport_type(self, value: str) -> None:
        #Сеттер для вида спорта с валидацией
        self._validate_sport_type(value)
        self._sport_type = value
    
    @property
    def weight(self) -> float:
        #Геттер для веса
        return self._weight
    
    @weight.setter
    def weight(self, value: float) -> None: #4 cеттеры с валидацией 
        #Сеттер для веса с валидацией
        self._validate_weight(value)
        self._weight = float(value)
    
    @property
    def personal_record(self) -> float:
        #Геттер для личного рекорда
        return self._personal_record
    
    @personal_record.setter
    def personal_record(self, value: float) -> None:
        #Сеттер для личного рекорда с валидацией
        self._validate_personal_record(value)
        self._personal_record = float(value)
    
    @property
    def is_active(self) -> bool:
        #Геттер для статуса активности
        return self._is_active
    
    # Бизнес-методы
    def update_record(self, new_record: float) -> str:
        if not self._is_active:
            raise ValueError("Нельзя обновить рекорд неактивного спортсмена")
        
        self._validate_personal_record(new_record)
        
        if new_record > self._personal_record:
            old_record = self._personal_record
            self._personal_record = new_record
            return f"Рекорд улучшен! Был: {old_record:.2f}, стал: {new_record:.2f}"
        elif new_record < self._personal_record:
            return f"Новый результат ({new_record:.2f}) хуже текущего рекорда ({self._personal_record:.2f})"
        else:
            return f"Результат равен текущему рекорду ({self._personal_record:.2f})"
    
    def train(self, hours: float) -> str: #7 бизнес-метод, метод тренировки
        if not self._is_active:
            raise ValueError("Нельзя тренировать неактивного спортсмена")
        
        if not isinstance(hours, (int, float)):
            raise ValueError("Количество часов должно быть числом")
        if hours <= 0:
            raise ValueError("Количество часов должно быть положительным")
        if hours > 8:
            raise ValueError("Тренировка не может длиться более 8 часов")
        
        # Логика, зависящая от состояния (возраста)
        if self._age < 18:
            max_hours = 4
            if hours > max_hours:
                return f"Спортсмену до 18 лет рекомендуется тренироваться не более {max_hours} часов. Вы указали {hours} ч."
        
        # Расчет сожженных калорий (упрощенно)
        calories_per_hour = 300 + (self._weight * 2)
        total_calories = calories_per_hour * hours
        
        return (f"{self._name} провел тренировку длительностью {hours} ч. "
                f"Сожжено примерно {total_calories:.0f} ккал.")
    
    def deactivate(self) -> None:
        #Деактивация спортсмена
        if not self._is_active:
            raise ValueError("Спортсмен уже неактивен")
        self._is_active = False
    
    def activate(self) -> None:
        #Активация спортсмена
        if self._is_active:
            raise ValueError("Спортсмен уже активен")
        self._is_active = True
    
    def get_bmi(self) -> float:
        height = 1.75  # условный средний рост
        bmi = self._weight / (height ** 2)
        return round(bmi, 2)
    
    def get_age_category(self) -> str:
        if self._age < 18:
            return "Юниор"
        elif self._age < 35:
            return "Взрослый"
        else:
            return "Ветеран"
    
    # Магические методы
    def __str__(self) -> str: #5/ cтроковое представление

        #Строковое представление для пользователей

        status = "активен" if self._is_active else "неактивен"
        return (f"Спортсмен: {self._name} | Возраст: {self._age} | "
                f"Вид спорта: {self._sport_type} | Вес: {self._weight:.1f} кг | "
                f"Рекорд: {self._personal_record:.2f} | Статус: {status}")
    
    def __repr__(self) -> str:  #4  Официальное строковое представление для разработчиков

        return (f"Athlete(name='{self._name}', age={self._age}, "
                f"sport_type='{self._sport_type}', weight={self._weight}, "
                f"personal_record={self._personal_record})")
    
    def __eq__(self, other) -> bool: #6 /cравнение по имени и виду спорта
        if not isinstance(other, Athlete):
            return False
        return (self._name == other._name and 
                self._sport_type == other._sport_type)
```
### demo.py
```python
from two_sem.lab01.model import Athlete


def print_header(text):
    #вывод заголовка
    print(f"\n{text}")



def print_result(text):
    #Вывод результата с отступом
    print(f"  {text}")


def main():
    #Основная функция демонстрации
    
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
```

### результат 
```python

 Демонстрация класса ATHLETE

1. создание объектов
  athlete1 создан
  athlete2 создан
  athlete1: Спортсмен: Иван Петров | Возраст: 25 | Вид спорта: Футбол | Вес: 75.5 кг | Рекорд: 12.50 | Статус: активен
  athlete2: Спортсмен: Мария Сидорова | Возраст: 22 | Вид спорта: Плавание | Вес: 60.0 кг | Рекорд: 45.30 | Статус: активен

2. сравнение объектов
  athlete1 == athlete3: True
  athlete1 == athlete4: False

3. некорректное создание
  ошибка: Имя должно содержать минимум 2 символа

4. использование сеттеров
  Текущий вес athlete1: 75.5 кг
  Новый вес после установки: 80.5 кг
  Попытка установить вес -10 кг:
   ошибка: Вес должен быть положительным числом

5. атрибуты класса
  Через класс: ['Футбол', 'Баскетбол', 'Плавание', 'Легкая атлетика', 'Теннис', 'Бокс']
  Через экземпляр: ['Футбол', 'Баскетбол', 'Плавание', 'Легкая атлетика', 'Теннис', 'Бокс']
  Минимальный возраст: 14
  Максимальный возраст: 50

6. магические методы
  __str__: Спортсмен: Иван Петров | Возраст: 25 | Вид спорта: Футбол | Вес: 80.5 кг | Рекорд: 12.50 | Статус: активен
  __repr__: Athlete(name='Иван Петров', age=25, sport_type='Футбол', weight=80.5, personal_record=12.5)

7. бизнес-методы
  Иван Петров провел тренировку длительностью 2.5 ч. Сожжено примерно 1152 ккал.
  Рекорд улучшен! Был: 45.30, стал: 46.80
  ИМТ athlete1: 26.29
  Возрастная категория athlete1: Взрослый

8. логические состояния
  Текущий статус athlete2: True
   athlete2 деактивирован
  Статус после деактивации: False
  Попытка тренировки неактивного спортсмена:
  ошибка: Нельзя тренировать неактивного спортсмена

 athlete2 реактивирован
  Статус после активации: True
  Мария Сидорова провел тренировку длительностью 1.5 ч. Сожжено примерно 630 ккал.

9. три сценария работы
  Сценарий 1: Юный спортсмен
    Спортсмен: Петр Сидоров | Возраст: 16 | Вид спорта: Теннис | Вес: 55.0 кг | Рекорд: 8.20 | Статус: активен
    Спортсмену до 18 лет рекомендуется тренироваться не более 4 часов. Вы указали 5.0 ч.
    Категория: Юниор

  Сценарий 2: Постепенное улучшение рекорда
    Начальный рекорд: 10.2
    Рекорд улучшен! Был: 10.20, стал: 10.50
    Новый результат (10.30) хуже текущего рекорда (10.50)
    Рекорд улучшен! Был: 10.50, стал: 10.80
    Итоговый рекорд: 10.8

  Сценарий 3: Спортсмен-ветеран
    Спортсмен: Борис Старков | Возраст: 45 | Вид спорта: Плавание | Вес: 85.0 кг | Рекорд: 30.50 | Статус: активен
    Категория: Ветеран
    ИМТ: 27.76
конец
```