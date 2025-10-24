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