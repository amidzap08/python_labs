# Лабораторная работа 6
### Задание 1
### CLI_TEXT.PY
```python
import sys
import argparse
from lab06.function import json_to_csv, csv_to_json
from lab06.function import csv_to_xlsx
from lab06.function import top_n


def setup_parser():
    parser = argparse.ArgumentParser(
        description="Утилита для обработки текстовых данных и конвертации форматов",
        prog="cli_tool",
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    cat_parser = subparsers.add_parser(
        "cat", help="Вывод содержимого файла с номерами строк"
    )
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument(
        "-n", "--number", action="store_true", help="Показать номера строк"
    )

    stats_parser = subparsers.add_parser("stats", help="Статистика по словам в файле")
    stats_parser.add_argument("--input", required=True, help="Входной файл")
    stats_parser.add_argument(
        "--top", type=int, default=10, help="Количество топ-слов для вывода"
    )

    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертация JSON в CSV")
    json2csv_parser.add_argument("--input", required=True, help="Входной JSON файл")
    json2csv_parser.add_argument("--output", required=True, help="Выходной CSV файл")

    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертация CSV в JSON")
    csv2json_parser.add_argument("--input", required=True, help="Входной CSV файл")
    csv2json_parser.add_argument("--output", required=True, help="Выходной JSON файл")

    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Конвертация CSV в XLSX")
    csv2xlsx_parser.add_argument("--input", required=True, help="Входной CSV файл")
    csv2xlsx_parser.add_argument("--output", required=True, help="Выходной XLSX файл")

    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    
    try:
        if args.command == "cat":
            cat_command(args)
        elif args.command == "stats":
            stats_command(args)
        elif args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
        else:
            print(f"Неизвестная команда: {args.command}")
            sys.exit(1)
    except Exception as e:
        print(f"Ошибка при выполнении команды: {e}")
        sys.exit(1)


def cat_command(args):
    try:
        with open(args.input, "r", encoding="utf-8") as file:
            for i, line in enumerate(file, 1):
                if args.number:
                    print(f"{i}. {line.rstrip()}")
                else:
                    print(line.rstrip())
    except Exception as e:
        print(f"Не удалось прочитать файл {args.input}: {e}")


def stats_command(args):
    try:
        with open(args.input, 'r', encoding='utf-8') as file:
            text = file.read()
        
        words = text.lower().split()
        freq = {}
        for word in words:
            word = word.strip('.,!?;:"()[]')
            if word:
                freq[word] = freq.get(word, 0) + 1
        n = args.top
        top_words = top_n(freq, n)
        
        print(f"Топ-{n} самых частых слов:")
        print("-" * 30)
        for i, (word, count) in enumerate(top_words, 1):
            print(f"{i:2}. {word:15} - {count:3} раз")
            
    except Exception as e:
        print(f"Ошибка при обработке файла {args.input}: {e}")


if __name__ == "__main__":
    main()
```
### Справка по программе 
```python
python -m src.lab06.cli_text -h
```
### Справка по команде cats
```python
python -m src.lab06.cli_text cat -h
```

### Справка по команде stats
```python
python -m src.lab06.cli_text stats -h
```


### Тест комманды cat
```python
python -m src.lab06.cli_text cat --input data/samples/input.txt -n
```
![Картинка 1](/src/lab06/images/catsout.png)

### Тест комманды stats
```python
python -m src.lab06.cli_text stats --input data/samples/input.txt

python -m src.lab06.cli_text stats --input data/samples/input.txt --top 5
```
![Картинка 2](/src/lab06/images/statsout.png)


## Задание 2
### CLI_CONVERT.PY
```python
import argparse
from pathlib import Path
import sys

current_file = Path(__file__)
parent_dir = current_file.parent.parent
sys.path.append(str(parent_dir))

from lab06.function import csv_to_json
from lab06.function import csv_to_xlsx
from lab06.function import json_to_csv


def main():
    parser = argparse.ArgumentParser(description="CLI конвертация файлов")
    subparsers = parser.add_subparsers(dest="command")

    json2csv_parser = subparsers.add_parser(
        "json2csv",
        help="Конвертировать JSON в CSV",
        description="Преобразовать JSON-файл (список объектов) в CSV с заголовком",
    )
    json2csv_parser.add_argument(
        "--in", dest="input", required=True, help="Входной JSON-файл"
    )
    json2csv_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной CSV-файл"
    )

    csv2json_parser = subparsers.add_parser(
        "csv2json",
        help="Конвертировать CSV в JSON",
        description="Преобразовать CSV-файл в JSON",
    )
    csv2json_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV-файл"
    )
    csv2json_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной JSON-файл"
    )

    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx",
        help="Конвертировать CSV в XLSX",
        description="Преобразовать CSV-файл в Excel",
    )
    csv2xlsx_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV-файл"
    )
    csv2xlsx_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной XLSX-файл"
    )

    args = parser.parse_args()

    if args.command is None:
        raise SystemExit(parser.format_help())

    in_path = Path(args.input)
    if not in_path.exists():
        raise FileNotFoundError(f"Входной файл не найден: {args.input}")

    if args.command == "json2csv":
        if in_path.suffix.lower() != ".json":
            raise ValueError("Ожидается входной файл .json для команды json2csv")
        if Path(args.output).suffix.lower() != ".csv":
            raise ValueError("Ожидается выходной файл .csv для команды json2csv")
        json_to_csv(args.input, args.output)
        print(f"Успешно: {args.input} -> {args.output}")

    elif args.command == "csv2json":
        if in_path.suffix.lower() != ".csv":
            raise ValueError("Ожидается входной файл .csv для команды csv2json")
        if Path(args.output).suffix.lower() != ".json":
            raise ValueError("Ожидается выходной файл .json для команды csv2json")
        csv_to_json(args.input, args.output)
        print(f"Успешно: {args.input} -> {args.output}")

    elif args.command == "csv2xlsx":
        if in_path.suffix.lower() != ".csv":
            raise ValueError("Ожидается входной файл .csv для команды csv2xlsx")
        if Path(args.output).suffix.lower() != ".xlsx":
            raise ValueError("Ожидается выходной файл .xlsx для команды csv2xlsx")
        csv_to_xlsx(args.input, args.output)
        print(f"Успешно: {args.input} -> {args.output}")


if __name__ == "__main__":
    main()
```

![Картинка 3](/src/lab06/images/out.png)

### Справки по коммандам 
```python
python -m src.lab06.cli_convert json2csv -h
python -m src.lab06.cli_convert csv2json -h
python -m src.lab06.cli_convert csv2xlsx -h
```
![Картинка 4](/src/lab06/images/command_test.png)

### Комманды для проверки программы
```python
python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people.json
python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv
python -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
```

![Картинка 5](/src/lab06/images/csvjson.png)

![Картинка 6](/src/lab06/images/jsoncsv.png)

![Картинка 7](/src/lab06/images/xlsx.png)