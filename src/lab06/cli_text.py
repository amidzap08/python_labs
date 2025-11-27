import sys
import argparse
from function import json_to_csv, csv_to_json
from function import csv_to_xlsx
from function import top_n


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
    json2csv_parser.add_argument("--output", help="Выходной CSV файл (опционально)")

    json2csv_parser.add_argument("--in", dest="input", required=True)
    json2csv_parser.add_argument("--out", dest="output", required=True)

    csv2json_parser = subparsers.add_parser("csv2json")
    csv2json_parser.add_argument("--in", dest="input", required=True)
    csv2json_parser.add_argument("--out", dest="output", required=True)

    csv2xlsx_parser = subparsers.add_parser("csv2xlsx")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True)
    csv2xlsx_parser.add_argument("--out", dest="output", required=True)
    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    commands = {
        "cat": cat_command,
        "stats": top_n,
        "json2csv": json_to_csv,
        "csv2json": csv_to_json,
        "csv2xlsx": csv_to_xlsx,
    }
    if args.command in commands:
        commands[args.command](args)
    else:
        print(f"Неизвестная команда: {args.command}")
        sys.exit(1)


def cat_command(args):

    try:
        with open(args.input, "r", encoding="utf-8") as file:
            for i, line in enumerate(file, 1):
                if args.number:
                    print(f"{i}. {line.rstrip()}")
                else:
                    print(line.rstrip())
    except:
        print(f"Не удалось прочитать файл {args.input}")


if __name__ == "__main__":
    main()
