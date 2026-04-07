## Лабораторная работа №4

## Задание А(1)
``` python
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    try:
        with open(p, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        return FileNotFoundError(f"File not found: {path}")
    except UnicodeDecodeError as e:
        return UnicodeDecodeError(
            f"Encoding error: cannot decode file '{path}' with encoding '{encoding}'",
            e.object, e.start, e.end
        )
```
## Тест-кейс
![Картинка 1](/src/lab04/images/01.04.png)

## Задание А(2)
```python
import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    try:
        p = Path(path)
        return p.read_text(encoding=encoding)
    except FileNotFoundError:
        return f"Ошибка: Файл {path} не найден"
    except UnicodeDecodeError as e:
        return f"Ошибка декодирования: {e}"

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | list[str] | None = None) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    if rows:
        first_row_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_row_len:
                raise ValueError(f"Несовпадение длины строк: строка 0 имеет {first_row_len} элементов, строка {i} имеет {len(row)}")
    
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow(header) 
        if rows:
            writer.writerows(rows)
```
## создаю файл и папку
```python
with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
```


## Тест-кейс для README 
```python
from src.io_txt_csv import read_text, write_csv
txt = read_text("data/input.txt")
write_csv([("word","count"),("test",3)], "data/check.csv")
```
## табличка csv
![картинка 2](/src/lab04/images/00.04.png)

## пустой файл с заголовком("a","b") 
![Картинка 3](/src/lab04/images/04.04.png)

## Задание В
```python
from pathlib import Path
import csv
import argparse
from function import normalize, tokenize, count_freq
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../lab03/lib'))

def read_csv_report(csv_file: str) -> None:
    input_path = Path(csv_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Ошибка: файл {csv_file} не существует")
    
    if not csv_file.lower().endswith('.csv'):
        raise ValueError(f"Ошибка: файл {csv_file} не является CSV файлом")

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                raise ValueError(f"Ошибка: CSV файл {csv_file} пуст")
            
            file.seek(0) 
            reader = csv.reader(file)
            
            try:
                header = next(reader)
            except StopIteration:
                raise ValueError(f"Ошибка: CSV файл {csv_file} не содержит данных")
            
            word_counts = {}
            total_words = 0
            
            for row in reader:
                if len(row) >= 2:
                    word = row[0]
                    count = int(row[1])
                    word_counts[word] = count
                    total_words += count

    except UnicodeDecodeError:
        raise ValueError(f"Ошибка: файл {csv_file} имеет неверную кодировку (требуется UTF-8)")
    except csv.Error as e:
        raise ValueError(f"Ошибка: невалидный CSV в файле {csv_file}: {e}")

    if not word_counts:
        raise ValueError(f"Ошибка: CSV файл {csv_file} не содержит данных о словах")

    unique_words = len(word_counts)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

def generate_csv_report(input_file: str, output_file: str) -> None:
    input_path = Path(input_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Ошибка: файл {input_file} не существует")
  
    if not input_file.lower().endswith('.txt'):
        raise ValueError(f"Ошибка: входной файл {input_file} не является TXT файлом")
    
    if not output_file.lower().endswith('.csv'):
        raise ValueError(f"Ошибка: выходной файл {output_file} не является CSV файлом")

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
            if not content:
                print("Пустой файл — создаю CSV только с заголовком.")
                output_path = Path(output_file)
                with open(output_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['word', 'count'])
                return
            text = content
    except UnicodeDecodeError:
        raise ValueError(f"Ошибка: файл {input_file} имеет неверную кодировку (требуется UTF-8)")

    norm_text = normalize(text)
    tokens = tokenize(norm_text)
    freqs = count_freq(tokens)
    output_path = Path(output_file)
    
    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['word', 'count'])  #заголовок
            for word, count in freqs.items():
                writer.writerow([word, count])
    except Exception as e:
        raise ValueError(f"Ошибка записи в файл {output_file}: {e}")
    print(f"Отчет сохранен в: {output_file}")
```
## Тест-кейс
![Картинка 3](/src/lab04/images/03.04.png)

## если наш файл пустой,то выводит:
![Картинка 4](/src/lab04/images/03(1).04.png)


![картианка 5](/src/lab04/images/02.04(1).png)

## Если файл не существует/не найден

![Картинка 5](/src/lab04/images/03(2).04.png)

### Если файл большой читается построчно