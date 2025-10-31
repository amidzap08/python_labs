import json
import csv
import os

def json_to_csv(json_path: str, csv_path: str) -> None:
    # Проверка расширения файла
    if not json_path.lower().endswith('.json'):
        raise ValueError(f"Файл {json_path} не является JSON файлом")
    
    # Проверка существования файла
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    try:
        with open(json_path, 'r', encoding="UTF-8") as json_file:
            content = json_file.read().strip()
            
            # Проверка на пустой файл
            if not content:
                raise ValueError(f"JSON файл пуст: {json_path}")
            
            data = json.loads(content)
            
    except UnicodeDecodeError:
        raise ValueError(f"Файл {json_path} имеет неверную кодировку (требуется UTF-8)")
    except json.JSONDecodeError as e:
        raise ValueError(f"Невалидный JSON в файле {json_path}: {e}")
    
    # Проверка структуры данных
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список")
    
    if not data:
        raise ValueError("JSON должен содержать непустой список")
    
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Все элементы в JSON должны быть словарями")
    
    # Формирование и запись CSV
    all_columns = []
    for item in data:
        for key in item.keys():
            if key not in all_columns:
                all_columns.append(key)
    
    with open(csv_path, 'w', encoding="UTF-8", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=all_columns)
        writer.writeheader()
        for row in data:
            full_row = {}
            for column in all_columns:
                full_row[column] = row.get(column, '')
            writer.writerow(full_row)

def csv_to_json(csv_path: str, json_path: str) -> None:
    # Проверка расширения файла
    if not csv_path.lower().endswith('.csv'):
        raise ValueError(f"Файл {csv_path} не является CSV файлом")
    
    # Проверка существования файла
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    try:
        with open(csv_path, 'r', encoding="UTF-8") as csv_file:
            content = csv_file.read().strip()
            
            # Проверка на пустой файл
            if not content:
                raise ValueError(f"CSV файл пуст: {csv_path}")
            
            csv_file.seek(0)
            reader = csv.DictReader(csv_file)
            
            if not reader.fieldnames:
                raise ValueError("CSV файл не содержит заголовка")
            
            data = []
            for row in reader:
                str_row = {}
                for key, value in row.items():
                    str_row[key] = str(value)
                data.append(str_row)
            
            if not data:
                raise ValueError("CSV файл не содержит данных")
                
    except UnicodeDecodeError:
        raise ValueError(f"Файл {csv_path} имеет неверную кодировку (требуется UTF-8)")
    except csv.Error as e:
        raise ValueError(f"Невалидный CSV в файле {csv_path}: {e}")
    
    with open(json_path, 'w', encoding="UTF-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

# Тестирование ошибок
if __name__ == "__main__":
    test_cases = [
        # (функция, аргументы, ожидаемая_ошибка, описание)
        (json_to_csv, ("data/people.json", "data/people.csv"), None, "Нормальный JSON"),
        (json_to_csv, ("data/peopleempty.json", "data/people2.csv"), ValueError, "Пустой JSON"),
        (json_to_csv, ("data/peoplenotdict.json", "data/people2.csv"), ValueError, "JSON не словари"),
        (json_to_csv, ("data/peoplenotexist.json", "data/people2.csv"), FileNotFoundError, "Файл не существует"),
        (json_to_csv, ("data/people1251.json", "data/people2.csv"), ValueError, "Не UTF-8 кодировка"),
        (json_to_csv, ("data/people.txt", "data/people2.csv"), ValueError, "Не JSON расширение"),
        ]
    
    for func, args, expected_error, description in test_cases:
        print(f" {description}")
        try:
            func(*args)
            if expected_error is None:
                print("   ✓ Успешно")
            else:
                print("   ✗ ОШИБКА: ожидалась ошибка")
        except Exception as e:
            if expected_error and isinstance(e, expected_error):
                print(f"   ✓ Корректная ошибка: {e}")
            else:
                print(f"   ✗ Неожиданная ошибка: {e}")