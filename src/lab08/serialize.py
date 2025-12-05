import json
from typing import List
from lab08.models import Student


def students_to_json(students: List[Student], path: str):
    data = [student.to_dict() for student in students]
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Данные успешно сохранены в {path}")


def students_from_json(path: str) -> List[Student]:
    """
    Читает JSON файл и создает список объектов Student
    
    Args:
        path: путь к JSON файлу
        
    Returns:
        List[Student]: список объектов Student
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Проверка что data является списком
        if not isinstance(data, list):
            raise TypeError("JSON должен содержать список объектов")
        
        students = []
        for item in data:
            try:
                # Подробная проверка типов данных как в примере
                if not isinstance(item, dict):
                    raise TypeError("Каждый элемент должен быть словарем")
                
                # Проверка обязательных полей и их типов
                if not isinstance(item.get("fio"), str):
                    raise TypeError("Поле 'fio' должно быть строкой")
                if not isinstance(item.get("birthdate"), str):
                    raise TypeError("Поле 'birthdate' должно быть строкой")
                if not isinstance(item.get("group"), str):
                    raise TypeError("Поле 'group' должно быть строкой")
                if not isinstance(item.get("gpa"), (float, int)):
                    raise TypeError("Поле 'gpa' должно быть числом (int или float)")
                
                # Проверка что все обязательные поля присутствуют
                required_fields = ["fio", "birthdate", "group", "gpa"]
                for field in required_fields:
                    if field not in item:
                        raise ValueError(f"Отсутствует обязательное поле: {field}")
                
                # Создание студента (внутри Student.from_dict тоже есть валидация)
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


# Демонстрация работы функций
if __name__ == "__main__":
    # Создание тестовых данных
    students = [
        Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.5),
        Student("Петрова Анна Сергеевна", "2001-12-03", "SE-02", 3.8),
        Student("Дзяпшба Амина Астамуровна", "2008-08-14", "BIVT-25-7", 4.9)
    ]
    
    # Сохранение в JSON
    students_to_json(students, "data/lab08/students_output.json")
    
    # Загрузка из JSON
    loaded_students = students_from_json("data/lab08/students_input.json")

    print("\nЗагруженные студенты:")
    for student in loaded_students:
        print(student)