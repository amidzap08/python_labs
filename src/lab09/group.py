import csv
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Any
import json

# Предполагаем, что Student импортируется из предыдущей ЛР
try:
    from src.lab08.models import Student
except ImportError:
    # Заглушка для тестирования
    class Student:
        def __init__(self, fio: str, birthdate: str, group: str, gpa: float):
            self.fio = fio
            self.birthdate = birthdate
            self.group = group
            self.gpa = gpa
        
        def to_dict(self) -> Dict:
            return {
                "fio": self.fio,
                "birthdate": self.birthdate,
                "group": self.group,
                "gpa": self.gpa
            }
        
        @classmethod
        def from_dict(cls, data: Dict) -> 'Student':
            return cls(
                fio=data["fio"],
                birthdate=data["birthdate"],
                group=data["group"],
                gpa=float(data["gpa"])
            )
        
        def __repr__(self):
            return f"Student(fio='{self.fio}', group='{self.group}', gpa={self.gpa})"


class Group:
    """Класс для управления хранилищем студентов в CSV-файле"""
    
    HEADER = ["fio", "birthdate", "group", "gpa"]
    
    def __init__(self, storage_path: str):
        """
        Инициализация группы с указанием пути к CSV-файлу
        
        Args:
            storage_path: путь к CSV-файлу для хранения данных
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:
        """Создает файл с заголовком, если он не существует"""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.HEADER)
                writer.writeheader()
    
    def _read_all_raw(self) -> List[Dict[str, str]]:
        """
        Чтение всех записей из CSV в виде словарей
        
        Returns:
            Список словарей с данными студентов
        """
        if not self.path.exists() or self.path.stat().st_size == 0:
            return []
        
        with open(self.path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader if row]  # Пропускаем пустые строки
    
    def _write_all(self, data: List[Dict[str, str]]) -> None:
        """
        Запись всех записей в CSV
        
        Args:
            data: список словарей с данными студентов
        """
        with open(self.path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(data)
    
    def _validate_student_data(self, data: Dict) -> bool:
        """Валидация данных студента"""
        try:
            # Проверка обязательных полей
            if not all(key in data for key in self.HEADER):
                return False
            
            # Проверка GPA
            gpa = float(data["gpa"])
            if not (0.0 <= gpa <= 5.0):
                return False
            
            # Проверка даты (опционально, упрощенная)
            datetime.strptime(data["birthdate"], "%Y-%m-%d")
            
            return True
        except (ValueError, KeyError):
            return False
    
    def list(self) -> List[Student]:
        """
        Получение всех студентов в виде списка объектов Student
        
        Returns:
            Список объектов Student
        """
        raw_data = self._read_all_raw()
        students = []
        
        for row in raw_data:
            if self._validate_student_data(row):
                students.append(Student.from_dict(row))
        
        return students
    
    def add(self, student: Student) -> bool:
        """
        Добавление нового студента в CSV
        
        Args:
            student: объект Student для добавления
            
        Returns:
            True если добавление успешно, False в противном случае
        """
        try:
            # Проверяем, нет ли уже студента с таким ФИО
            existing = self._read_all_raw()
            for row in existing:
                if row["fio"] == student.fio:
                    print(f"Студент с ФИО '{student.fio}' уже существует")
                    return False
            
            # Добавляем нового студента
            existing.append(student.to_dict())
            self._write_all(existing)
            return True
            
        except Exception as e:
            print(f"Ошибка при добавлении студента: {e}")
            return False
    
    def find(self, substr: str) -> List[Student]:
        """
        Поиск студентов по подстроке в ФИО
        
        Args:
            substr: подстрока для поиска в поле fio
            
        Returns:
            Список найденных студентов
        """
        all_students = self.list()
        substr_lower = substr.lower()
        
        return [
            student for student in all_students
            if substr_lower in student.fio.lower()
        ]
    
    def remove(self, fio: str) -> bool:
        """
        Удаление записи(ей) по точному совпадению ФИО
        
        Args:
            fio: ФИО студента для удаления
            
        Returns:
            True если удаление успешно, False если студент не найден
        """
        raw_data = self._read_all_raw()
        initial_count = len(raw_data)
        
        # Удаляем всех студентов с указанным ФИО
        raw_data = [row for row in raw_data if row["fio"] != fio]
        
        if len(raw_data) == initial_count:
            print(f"Студент с ФИО '{fio}' не найден")
            return False
        
        self._write_all(raw_data)
        return True
    
    def update(self, fio: str, **fields) -> bool:
        if not fields:
            print("Не указаны поля для обновления")
            return False
        
        raw_data = self._read_all_raw()
        updated = False
        
        for row in raw_data:
            if row["fio"] == fio:
                # Обновляем только разрешенные поля
                for key, value in fields.items():
                    if key in self.HEADER and key != "fio":  # Нельзя менять ФИО
                        row[key] = str(value)
                updated = True
                break
        
        if not updated:
            print(f"Студент с ФИО '{fio}' не найден")
            return False
        
        self._write_all(raw_data)
        return True
    
    # ★ Дополнительное задание со звездочкой
    def stats(self) -> Dict[str, Any]:
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": []
            }
        
        # Основная статистика
        gpa_values = [student.gpa for student in students]
        groups_count = {}
        
        for student in students:
            groups_count[student.group] = groups_count.get(student.group, 0) + 1
        
        # Топ-5 студентов по GPA
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [
            {"fio": s.fio, "gpa": s.gpa}
            for s in sorted_students[:5]
        ]
        
        return {
            "count": len(students),
            "min_gpa": min(gpa_values),
            "max_gpa": max(gpa_values),
            "avg_gpa": sum(gpa_values) / len(gpa_values),
            "groups": groups_count,
            "top_5_students": top_5
        }


# Пример использования и тестирования
def test_group_operations():
    """Функция для тестирования работы класса Group"""
    
    # Создаем временный файл для тестирования
    test_file = "data/lab09/test_students.csv"
    group = Group(test_file)
    
    print("=== Тестирование CRUD операций ===")
    
    # 1. Добавление студентов
    print("\n1. Добавление студентов:")
    students_to_add = [
        Student("Иванов Иван Иванович", "2003-10-10", "БИВТ-21-1", 4.3),
        Student("Петрова Анна Сергеевна", "2002-05-15", "БИВТ-21-2", 4.7),
        Student("Сидоров Алексей Петрович", "2003-03-20", "БИВТ-21-1", 3.9),
        Student("Козлова Мария Владимировна", "2004-01-30", "БИВТ-21-3", 4.9),
        Student("Иванов Петр Сергеевич", "2003-08-12", "БИВТ-21-2", 4.1),
    ]
    
    for student in students_to_add:
        if group.add(student):
            print(f"Добавлен: {student.fio}")
    
    # 2. Вывод списка
    print("\n2. Список всех студентов:")
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"  {i}. {student.fio}, {student.group}, GPA: {student.gpa}")
    
    # 3. Поиск
    print("\n3. Поиск по подстроке 'Иванов':")
    found = group.find("Иванов")
    for student in found:
        print(f"  Найден: {student.fio}")
    
    # 4. Обновление
    print("\n4. Обновление GPA студента 'Иванов Иван Иванович':")
    if group.update("Иванов Иван Иванович", gpa=4.5):
        print("  GPA обновлен успешно")
    
    # 5. Получение статистики
    print("\n5. Статистика по группе:")
    stats = group.stats()
    print(f"  Количество студентов: {stats['count']}")
    print(f"  Средний GPA: {stats['avg_gpa']:.2f}")
    print(f"  Группы: {stats['groups']}")
    
    # 6. Удаление
    print("\n6. Удаление студента 'Петрова Анна Сергеевна':")
    if group.remove("Петрова Анна Сергеевна"):
        print("  Студент удален успешно")
    
    # 7. Итоговый список
    print("\n7. Итоговый список студентов:")
    final_students = group.list()
    for i, student in enumerate(final_students, 1):
        print(f"  {i}. {student.fio}, GPA: {student.gpa}")
    
    # Удаляем тестовый файл
    Path(test_file).unlink(missing_ok=True)
    print("\n=== Тестирование завершено ===")


if __name__ == "__main__":
    test_group_operations()