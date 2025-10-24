## Лабораторная работа №4

## Задание А(1)
``` python
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

## Задание В
```python
def read_csv_report(csv_file: str) -> None:
    input_path = Path(csv_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Ошибка: файл {csv_file} не существует")
    with open(input_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader) 
        
        word_counts = {}
        total_words = 0
        
        for row in reader:
            if len(row) >= 2:
                word = row[0]
                count = int(row[1])
                word_counts[word] = count
                total_words += count
    unique_words = len(word_counts)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
   
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_words:
        print(f"{word}:{count}")
```
## Тест-кейс
![Картинка 3](/src/lab04/images/03.04.png)

## если наш файл пустой,то выводит:
![Картинка 4](/src/lab04/images/03(1).04.png)
![картианка 5](/src/lab04/images/02.04(1).png)

## Если файл не существует/не найден
![Картинка 5](/src/lab04/images/03(2).04.png)