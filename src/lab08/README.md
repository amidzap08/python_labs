## Лабораторная работа 8
### models.py
```python
from dataclasses import dataclass
from datetime import datetime, date
import re


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается: YYYY-MM-DD")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть в диапазоне 0-5, получено: {self.gpa}")
        
        if not re.match(r'^[A-Za-zА-Яа-яЁё\s]+$', self.fio):
            raise ValueError("ФИО должно содержать только буквы и пробелы")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        age = today.year - birth_date.year
        
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
            
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
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
            gpa=float(data["gpa"]) 
        )

    def __str__(self) -> str:
        return f"Student {self.fio},{self.group},{self.gpa}"

```

### serialize.py
```python
import json
from typing import List
from lab08.models import Student


def students_to_json(students: List[Student], path: str):
    data = [student.to_dict() for student in students]
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Данные успешно сохранены в {path}")


def students_from_json(path: str) -> List[Student]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            raise TypeError("JSON должен содержать список объектов")
        
        students = []
        for item in data:
            try:
                if not isinstance(item, dict):
                    raise TypeError("Каждый элемент должен быть словарем")

                if not isinstance(item.get("fio"), str):
                    raise TypeError("Поле 'fio' должно быть строкой")

                if not isinstance(item.get("birthdate"), str):
                    raise TypeError("Поле 'birthdate' должно быть строкой")

                if not isinstance(item.get("group"), str):
                    raise TypeError("Поле 'group' должно быть строкой")

                if not isinstance(item.get("gpa"), (float, int)):
                    raise TypeError("Поле 'gpa' должно быть числом (int или float)")
                
                required_fields = ["fio", "birthdate", "group", "gpa"]
                for field in required_fields:
                    if field not in item:
                        raise ValueError(f"Отсутствует обязательное поле: {field}")
                student = Student.from_dict(item)
                students.append(student)
                
            except (ValueError, TypeError) as e:
                print(f"Ошибка при создании студента из данных: {item}")
                print(f"Ошибка: {e}")
                continue
            except Exception as e:
                print(f"Неожиданная ошибка при создании студента: {e}")
                continue
        
        print(f"Успешно загружено {len(students)} студентов из {path}")
        return students
        
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON в файле {path}: {e}")
        return []
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")
        return []

```

### Файл students_input.json до
![Картинка 1](/src/lab08/images/fileoutbef.png)

### Файл students_input.json после
![Картинка 2](/src/lab08/images/fileoutaft.png)

### Валидация ошибок 
![Картинка 3](/src/lab08/images/ERRORSS.png)

### Вывод models.py
![Картинка 4](/src/lab08/images/itog.png)

### Вывод serialize.py
![Картинка 5](/src/lab08/images/itogser.png)

#### все выполнено успешно(5)