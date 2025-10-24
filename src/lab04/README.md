## Лабораторная работа №4

## Задание А(1)
``` python
 from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    try:
        # Используем параметр encoding, а не локальную переменную
        with open(p, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        return FileNotFoundError(f"File not found: {path}")
    except UnicodeDecodeError as e:
        return UnicodeDecodeError(
            f"Encoding error: cannot decode file '{path}' with encoding '{encoding}'",
            e.object, e.start, e.end
        )

text1 = read_text(r"C:\Users\Comp\Desktop\python_labs\data\input.txt")
print(text1)
```
![Картинка 1](/src/lab04/images/01.04.png)

## Задание А(2)
```python
import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Чтение текстового файла с обработкой ошибок"""
    try:
        p = Path(path)
        return p.read_text(encoding=encoding)
    except FileNotFoundError:
        return f"Ошибка: Файл {path} не найден"
    except UnicodeDecodeError as e:
        return f"Ошибка декодирования: {e}"

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | list[str] | None = None) -> None:
    """Запись данных в CSV файл"""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    if rows:
        first_row_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_row_len:
                raise ValueError(f"Несовпадение длины строк: строка 0 имеет {first_row_len} элементов, строка {i} имеет {len(row)}")
    
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Запись заголовка
        if header:
            writer.writerow(header) 
        
        # Запись данных
        if rows:
            writer.writerows(rows)
   
if __name__ == "__main__":
    write_csv([("word", "count"), ("test", 3)], "data/check.csv")
     
    str_empty = read_text("data/input.txt")
    print("input.txt:", str_empty)
    
    strUTF = read_text("data/input.txt")
    print("input.txt (UTF):", strUTF)

    # ИСПРАВЛЕНИЕ: печатаем результат функции, а не класс исключения
    not_found = read_text("data/wexj.txt")
    print("Не найден:", not_found)  # Будет: "Ошибка: Файл data/wexj.txt не найден"
     
    strcp1251 = read_text("data/exg1251.txt", encoding='cp1251')
    print("CP1251:", strcp1251)  
```
## создаю файл и папку
![картинка 2](/src/lab04/images/02.04.png)

## Задание В
```python
import sys
from pathlib import Path
import csv
import argparse

def read_csv_report(csv_file: str) -> None:
#Чтение отчета из CSV файла и вывод в консоль
    input_path = Path(csv_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Ошибка: файл {csv_file} не существует")
    # Проверяем, что файл не пустой
    
    #Читаем CSV файл
    with open(input_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  #Пропускаем заголовок
        
        word_counts = {}
        total_words = 0
        
        for row in reader:
            if len(row) >= 2:
                word = row[0]
                count = int(row[1])
                word_counts[word] = count
                total_words += count
    
    #Выводим статистику
    unique_words = len(word_counts)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    
    #Сортируем по убыванию частоты
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_words:
        print(f"{word}:{count}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Чтение отчета из CSV файла')
    parser.add_argument('--csv', dest='csv_file', default='data/check.csv', help='Путь к CSV файлу с отчетом')
    
    args = parser.parse_args()
    
    try:
        read_csv_report(args.csv_file)
    except Exception as error:
        print(error)
        exit(1)
```
![Картинка 3](/src/lab04/images/03.04.png)
![Картинка 4](/src/lab04/images/03(1).04.png)
![Картинка 5](/src/lab04/images/03(2).04.png)