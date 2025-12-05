from dataclasses import dataclass
from datetime import datetime, date
import re


@dataclass
class Student:
    """Класс Student для представления студента"""
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        """Валидация данных после инициализации"""
        # Валидация даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается: YYYY-MM-DD")
        
        # Валидация GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть в диапазоне 0-5, получено: {self.gpa}")
        
        # Валидация ФИО (должно содержать только буквы и пробелы)
        if not re.match(r'^[A-Za-zА-Яа-яЁё\s]+$', self.fio):
            raise ValueError("ФИО должно содержать только буквы и пробелы")

    def age(self) -> int:
        """Вычисляет возраст студента в полных годах"""
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        age = today.year - birth_date.year
        
        # Проверяем, был ли уже день рождения в этом году
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
            
        return age

    def to_dict(self) -> dict:
        """Сериализует объект Student в словарь"""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Десериализует словарь в объект Student с валидацией"""
        # Дополнительная проверка типов перед созданием объекта
        if not isinstance(data.get("fio"), str):
            raise TypeError("fio должен быть строкой")
        if not isinstance(data.get("birthdate"), str):
            raise TypeError("birthdate должен быть строкой")
        if not isinstance(data.get("group"), str):
            raise TypeError("group должен быть строкой")
        if not isinstance(data.get("gpa"), (int, float)):
            raise TypeError("gpa должен быть числом")
    
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"])  # Преобразуем к float для единообразия
        )

    def __str__(self) -> str:
        """Строковое представление студента как на картинке"""
        return f"Student {self.fio},{self.group},{self.gpa}"


# Демонстрация работы класса
if __name__ == "__main__":
    # Создание студентов как на картинке
    student1 = Student(
        fio="Иванов Иван Иванович",
        birthdate="2000-05-15",
        group="БИВТ-25-1",
        gpa=4.5
    )
    
    student2 = Student(
        fio="Сидоров Петр Петрович", 
        birthdate="2001-12-03",
        group="БИВТ-25-2", 
        gpa=3.8
    )

    student3 = Student(
        fio="Сидорова Анна Сергеевна",
        birthdate="2002-03-10",
        group="БИВТ-25-3",
        gpa=4.9
    )
    
    print("Демонстрация работы класса Student:")
    print(student1)
    print(student2)
    print(student3)

    print("\nСериализация в словарь:")
    print(student1.to_dict())