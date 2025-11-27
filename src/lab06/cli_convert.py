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

    # json2csv
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

    # csv2json
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

    # csv2xlsx
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

    # Проверка входного файла
    in_path = Path(args.input)
    if not in_path.exists():
        raise FileNotFoundError(f"Входной файл не найден: {args.input}")

    # Выполнение команд
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
