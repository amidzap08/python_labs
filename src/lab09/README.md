## Лабораторная работа 9 
### Задание А

```python
import csv
from pathlib import Path
from typing import List, Dict


class Student:
    def __init__(self, fio: str, birthdate: str, group: str, gpa: float):
        self.fio = fio.strip()
        self.birthdate = birthdate.strip()
        self.group = group.strip()
        self.gpa = float(gpa)
    
    def to_dict(self) -> Dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": str(self.gpa)
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Student':
        return cls(**data)
    
    def __repr__(self):
        return f"Student(fio='{self.fio}', group='{self.group}', gpa={self.gpa})"
    
    def as_dict(self) -> Dict:
        """Возвращает данные студента в виде словаря"""
        return {
            "ФИО": self.fio,
            "Дата рождения": self.birthdate,
            "Группа": self.group,
            "Средний балл": self.gpa
        }


class Group:
    """Класс для управления хранилищем студентов в CSV-файле"""
    
    HEADER = ["fio", "birthdate", "group", "gpa"]
    
    def __init__(self, storage_path: str = "data/lab09/students.csv"):
        self.path = Path(storage_path)
        
        # Создаем файл только если он не существует
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.HEADER)
                writer.writeheader()
    
    def _read_all_raw(self) -> List[Dict[str, str]]:
        """Чтение всех записей из CSV в виде словарей"""
        if not self.path.exists() or self.path.stat().st_size == 0:
            return []
        
        with open(self.path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                if row and any(row.values()):
                    rows.append(row)
            return rows
    
    def _write_all(self, data: List[Dict[str, str]]) -> None:
        """Запись всех записей в CSV"""
        with open(self.path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(data)
    
    def list(self) -> List[Student]:
        """Получение всех студентов в виде объектов Student"""
        raw_data = self._read_all_raw()
        students = []
        
        for row in raw_data:
            try:
                student_data = {
                    'fio': row.get('fio', '').strip(),
                    'birthdate': row.get('birthdate', '').strip(),
                    'group': row.get('group', '').strip(),
                    'gpa': float(row.get('gpa', 0))
                }
                students.append(Student(**student_data))
            except (ValueError, KeyError):
                continue
        
        return students
    
    def add(self, student: Student) -> bool:
        """Добавление нового студента"""
        if not student.fio or not student.fio.strip():
            return False
        
        if student.gpa < 0 or student.gpa > 5:
            return False
        
        try:
            existing_data = self._read_all_raw()
            student_fio_normalized = student.fio.strip().lower()
            
            for row in existing_data:
                existing_fio = row.get("fio", "").strip().lower()
                if existing_fio == student_fio_normalized:
                    return False
            
            with open(self.path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.HEADER)
                writer.writerow(student.to_dict())
            
            return True
            
        except Exception:
            return False
    
    def find(self, substr: str) -> List[Dict]:
        """Поиск студентов по подстроке в ФИО, возвращает словари"""
        if not substr or not substr.strip():
            return []
        
        all_students = self.list()
        substr_lower = substr.strip().lower()
        
        found_students = [
            s for s in all_students 
            if substr_lower in s.fio.lower()
        ]
        
        # Возвращаем список словарей с данными студентов
        return [student.as_dict() for student in found_students]
    
    def _get_student_data(self, fio: str) -> Dict:
        """Получение данных студента по ФИО"""
        fio_normalized = fio.strip().lower()
        for student in self.list():
            if student.fio.strip().lower() == fio_normalized:
                return student.as_dict()
        return {}
    
    def remove(self, fio: str) -> bool:
        """Удаление ВСЕХ записей по точному совпадению ФИО"""
        if not fio or not fio.strip():
            return False
        
        # Получаем данные студента перед удалением
        student_data = self._get_student_data(fio)
        if not student_data:
            return False
        
        raw_data = self._read_all_raw()
        initial_count = len(raw_data)
        
        fio_normalized = fio.strip().lower()
        filtered_data = [
            row for row in raw_data 
            if row.get("fio", "").strip().lower() != fio_normalized
        ]
        
        if len(filtered_data) == initial_count:
            return False
        
        self._write_all(filtered_data)
        
        # Возвращаем данные удаленного студента
        self._last_removed_student = student_data
        return True
    
    def get_last_removed_student(self) -> Dict:
        """Получение данных последнего удаленного студента"""
        return getattr(self, '_last_removed_student', {})
    
    def update(self, fio: str, **fields) -> bool:
        """Обновление полей существующего студента"""
        if not fio or not fio.strip():
            return False
        
        if not fields:
            return False
        
        valid_fields = [f for f in fields.keys() if f in self.HEADER and f != "fio"]
        if not valid_fields:
            return False
        
        raw_data = self._read_all_raw()
        fio_normalized = fio.strip().lower()
        updated = False
        updated_student_data = {}
        
        for row in raw_data:
            if row.get("fio", "").strip().lower() == fio_normalized:
                # Сохраняем исходные данные перед обновлением
                old_data = {
                    "fio": row.get("fio", ""),
                    "birthdate": row.get("birthdate", ""),
                    "group": row.get("group", ""),
                    "gpa": row.get("gpa", "0")
                }
                
                # Обновляем поля
                for field in valid_fields:
                    value = fields[field]
                    if field == "gpa":
                        try:
                            gpa_value = float(value)
                            if gpa_value < 0 or gpa_value > 5:
                                return False
                            row[field] = str(gpa_value)
                        except ValueError:
                            return False
                    else:
                        row[field] = str(value).strip()
                
                updated = True
                
                # Сохраняем обновленные данные для вывода
                updated_student_data = {
                    "ФИО": fio,
                    "Дата рождения": row.get("birthdate", ""),
                    "Группа": row.get("group", ""),
                    "Средний балл": float(row.get("gpa", "0"))
                }
                break
        
        if not updated:
            return False
        
        self._write_all(raw_data)
        
        # Сохраняем обновленные данные студента
        self._last_updated_student = updated_student_data
        return True
    
    def get_last_updated_student(self) -> Dict:
        """Получение данных последнего обновленного студента"""
        return getattr(self, '_last_updated_student', {})
    
    def count(self) -> int:
        """Возвращает количество студентов в группе"""
        return len(self.list())
    
    def clear(self) -> bool:
        """Очищает все данные, оставляя только заголовок"""
        try:
            self._write_all([])
            return True
        except Exception:
            return False


# Создаем файл с начальными данными если его нет
def create_initial_file():
    """Создает файл с начальными данными"""
    initial_data = [
        {"fio": "Иванов Иван Иванович", "birthdate": "2000-01-15", "group": "БИВТ-21-1", "gpa": "4.5"},
        {"fio": "Петров Петр Петрович", "birthdate": "2001-03-20", "group": "БИВТ-21-2", "gpa": "3.8"},
        {"fio": "Сидорова Мария Сергеевна", "birthdate": "2000-07-10", "group": "БИВТ-21-1", "gpa": "4.9"},
        {"fio": "Кузнецов Алексей Владимирович", "birthdate": "2001-11-05", "group": "БИВТ-21-3", "gpa": "3.2"},
        {"fio": "Ильин Никита Денисович", "birthdate": "2005-02-09", "group": "ПИ-21-1", "gpa": "2.1"},
        {"fio": "Феодосьевна Руслана Владимировна", "birthdate": "2007-05-18", "group": "БИВТ-25-7", "gpa": "4.3"},
        {"fio": "Смирнов Алексей Петрович", "birthdate": "2006-09-25", "group": "БИВТ-24-3", "gpa": "4.2"},
        {"fio": "Васильева Мария Игоревна", "birthdate": "2005-12-15", "group": "ПИ-22-2", "gpa": "4.8"},
        {"fio": "Кузнецов Дмитрий Сергеевич", "birthdate": "2008-03-30", "group": "БИВТ-26-1", "gpa": "3.9"}
    ]
    
    file_path = Path("data/lab09/students.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["fio", "birthdate", "group", "gpa"])
        writer.writeheader()
        writer.writerows(initial_data)


# Вспомогательная функция для красивого вывода словаря
def print_dict(data: Dict, title: str = ""):
    """Красивый вывод словаря"""
    if title:
        print(f"\n{title}:")
    
    if not data:
        print("  Нет данных")
        return
    
    for key, value in data.items():
        print(f"  {key}: {value}")


```
### print(people.list())
![Картинка 1](/src/lab09/images/list.png)

### people.add(Student("Дзяпшба Амина Астамуровна", "2008-08-15", "БИВТ-25-7", 5.0))
###  people.update("Дзяпшба Амина Астамуровна", birthdate='2008-08-14', gpa=4.6)
![Картинка 2](/src/lab09/images/dannie.png)

### students.csv и добавленный people
![Картинка 3](/src/lab09/images/добавила.png)

### people.remove('Кудрявцева Анастасия Олеговна'):
![Картинка 4](/src/lab09/images/remove.png)

### print(people.find('Смир'))
![Картинка 5](/src/lab09/images/find.png)

