import sys
import argparse
from lab06.function import json_to_csv, csv_to_json
from lab06.function import csv_to_xlsx
from lab06.function import top_n

##CLI‑программы позволяют вызывать функции программы через команды и флаги
##Модуль argparse — стандартный инструмент Python для парсинга аргументов командной строки.


def setup_parser():
    parser = argparse.ArgumentParser(
        description="Утилита для обработки текстовых данных и конвертации форматов",
        prog="cli_tool",
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # Команда cat
    cat_parser = subparsers.add_parser(
        "cat", help="Вывод содержимого файла с номерами строк"
    )
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument(
        "-n", "--number", action="store_true", help="Показать номера строк"
    )

    # Команда stats
    stats_parser = subparsers.add_parser("stats", help="Статистика по словам в файле")
    stats_parser.add_argument("--input", required=True, help="Входной файл")
    stats_parser.add_argument(
        "--top", type=int, default=10, help="Количество топ-слов для вывода"
    )

    # Команда json2csv
    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертация JSON в CSV")
    json2csv_parser.add_argument("--input", required=True, help="Входной JSON файл")
    json2csv_parser.add_argument("--output", required=True, help="Выходной CSV файл")

    # Команда csv2json
    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертация CSV в JSON")
    csv2json_parser.add_argument("--input", required=True, help="Входной CSV файл")
    csv2json_parser.add_argument("--output", required=True, help="Выходной JSON файл")

    # Команда csv2xlsx
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
    """Обработчик команды stats"""
    try:
        with open(args.input, "r", encoding="utf-8") as file:
            text = file.read()

        # Подсчет частоты слов
        words = text.lower().split()
        freq = {}
        for word in words:
            word = word.strip('.,!?;:"()[]')
            if word:
                freq[word] = freq.get(word, 0) + 1

        # Используем функцию top_n
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

