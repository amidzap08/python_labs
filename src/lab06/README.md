# Лабораторная работа 6
### Задание 1
```python
import sys
import argparse
from function import json_to_csv, csv_to_json
from function import csv_to_xlsx
from function import top_n
from pathlib import Path
from collections import Counter
import re

def cat_command(args):
    """Команда cat - вывод содержимого файла"""
    try:
        with open(args.input, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file, 1):
                if args.number:
                    print(f"{i:6}  {line}", end='')
                else:
                    print(line, end='')
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден - {args.input}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла {args.input}: {e}", file=sys.stderr)
        sys.exit(1)

def clean_word(word):
    """Очистка слова от знаков препинания"""
    return re.sub(r'[^\w\s]', '', word).lower()

def stats_command(args):
    """Команда stats - анализ частот слов в тексте"""
    try:
        # Читаем файл и анализируем слова
        with open(args.input, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Разбиваем текст на слова и очищаем их
        words = text.split()
        cleaned_words = [clean_word(word) for word in words if clean_word(word)]
        
        # Подсчитываем частоту
        word_freq = Counter(cleaned_words)
        
        # Используем функцию top_n из function.py
        from function import top_n
        top_words = top_n(dict(word_freq), args.top)
        
        print(f"Топ-{args.top} самых частых слов в файле {args.input}:")
        print("-" * 40)
        for word, count in top_words:
            print(f"{word:<20} : {count:>3}")
            
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден - {args.input}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при анализе файла {args.input}: {e}", file=sys.stderr)
        sys.exit(1)

def setup_parser():
    """Настройка парсера аргументов для текстовых утилит"""
    parser = argparse.ArgumentParser(
        description="Утилита для обработки текстовых данных",
        prog="text_tools"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')

    # Парсер для команды cat
    cat_parser = subparsers.add_parser('cat', help='Вывод содержимого файла с номерами строк')
    cat_parser.add_argument('--input', required=True, help='Входной файл')
    cat_parser.add_argument('-n', '--number', action='store_true', help='Показать номера строк')
    cat_parser.set_defaults(func=cat_command)

    # Парсер для команды stats
    stats_parser = subparsers.add_parser('stats', help='Статистика по словам в файле')
    stats_parser.add_argument('--input', required=True, help='Входной текстовый файл')
    stats_parser.add_argument('--top', type=int, default=5, help='Количество топ-слов для вывода (по умолчанию: 5)')
    stats_parser.set_defaults(func=stats_command)

    return parser

def main():
    """Основная функция для текстовых утилит"""
    parser = setup_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Вызываем соответствующую функцию команды
    args.func(args)

if __name__ == "__main__":
    main()
```

## Задание 2
```python
import argparse
import sys
import os
from pathlib import Path

def json2csv_command(args):
    try:
        from function import json_to_csv
        
        # Создаем директорию для выходного файла если нужно
        output_dir = os.path.dirname(args.output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        # Вызываем функцию конвертации
        json_to_csv(args.input, args.output)
        print(f"Успешно сконвертировано: {args.input} -> {args.output}")
        
    except ImportError:
        print("Ошибка: Не найдена функция json_to_csv из модуля function", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неизвестная ошибка при конвертации: {e}", file=sys.stderr)
        sys.exit(1)

def csv2json_command(args):
    try:
        from function import csv_to_json
        
        # Создаем директорию для выходного файла если нужно
        output_dir = os.path.dirname(args.output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        # Вызываем функцию конвертации
        csv_to_json(args.input, args.output)
        print(f"Успешно сконвертировано: {args.input} -> {args.output}")
        
    except ImportError:
        print("Ошибка: Не найдена функция csv_to_json из модуля function", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неизвестная ошибка при конвертации: {e}", file=sys.stderr)
        sys.exit(1)

def csv2xlsx_command(args):
    """Команда конвертации CSV в XLSX"""
    try:
        from function import csv_to_xlsx
        
        # Создаем директорию для выходного файла если нужно
        output_dir = os.path.dirname(args.output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        # Вызываем функцию конвертации
        csv_to_xlsx(args.input, args.output)
        print(f"Успешно сконвертировано: {args.input} -> {args.output}")
        
    except ImportError:
        print("Ошибка: Не найдена функция csv_to_xlsx из модуля function", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неизвестная ошибка при конвертации: {e}", file=sys.stderr)
        sys.exit(1)

def setup_parser():
    parser = argparse.ArgumentParser(
        description="Утилита для конвертации данных между форматами",
        prog="convert_tools"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')

    json2csv_parser = subparsers.add_parser('json2csv', help='Конвертация JSON в CSV')
    json2csv_parser.add_argument("--in", dest="input", required=True, help='Входной JSON файл')
    json2csv_parser.add_argument("--out", dest="output", required=True, help='Выходной CSV файл')
    json2csv_parser.set_defaults(func=json2csv_command)

    csv2json_parser = subparsers.add_parser("csv2json", help='Конвертация CSV в JSON')
    csv2json_parser.add_argument("--in", dest="input", required=True, help='Входной CSV файл')
    csv2json_parser.add_argument("--out", dest="output", required=True, help='Выходной JSON файл')
    csv2json_parser.set_defaults(func=csv2json_command)

    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help='Конвертация CSV в XLSX')
    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help='Входной CSV файл')
    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help='Выходной XLSX файл')
    csv2xlsx_parser.set_defaults(func=csv2xlsx_command)

    return parser

def main():
    parser = setup_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    args.func(args)

if __name__ == "__main__":
    main()
```

![Картинка 1]()