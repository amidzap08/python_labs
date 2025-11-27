from pathlib import Path
import csv
import argparse
from function import normalize, tokenize, count_freq
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../lab03/lib"))


def read_csv_report(csv_file: str) -> None:
    """Читает и анализирует CSV отчет"""
    input_path = Path(csv_file)

    if not input_path.exists():
        raise FileNotFoundError(f"Ошибка: файл {csv_file} не существует")

    # ПРОВЕРКА РАСШИРЕНИЯ ФАЙЛА
    if not csv_file.lower().endswith(".csv"):
        raise ValueError(f"Ошибка: файл {csv_file} не является CSV файлом")

    try:
        with open(input_path, "r", encoding="utf-8") as file:
            # ПРОВЕРКА ПУСТОГО ФАЙЛА
            content = file.read().strip()
            if not content:
                raise ValueError(f"Ошибка: CSV файл {csv_file} пуст")

            file.seek(0)  # Возвращаемся к началу файла
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
        raise ValueError(
            f"Ошибка: файл {csv_file} имеет неверную кодировку (требуется UTF-8)"
        )
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

    # ПРОВЕРКА РАСШИРЕНИЯ ВХОДНОГО ФАЙЛА
    if not input_file.lower().endswith(".txt"):
        raise ValueError(f"Ошибка: входной файл {input_file} не является TXT файлом")

    # ПРОВЕРКА РАСШИРЕНИЯ ВЫХОДНОГО ФАЙЛА
    if not output_file.lower().endswith(".csv"):
        raise ValueError(f"Ошибка: выходной файл {output_file} не является CSV файлом")

    try:
        # читаем текстовый файл
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

            # ПРОВЕРКА ПУСТОГО ФАЙЛА
            if not content:
                print("Пустой файл — создаю CSV только с заголовком.")
                # создаем пустой CSV с заголовком
                output_path = Path(output_file)
                with open(output_path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["word", "count"])
                return

            text = content

    except UnicodeDecodeError:
        raise ValueError(
            f"Ошибка: файл {input_file} имеет неверную кодировку (требуется UTF-8)"
        )

    # обрабатываем текст
    norm_text = normalize(text)
    tokens = tokenize(norm_text)
    freqs = count_freq(tokens)

    # Сохраняем результат в CSV
    output_path = Path(output_file)
    try:
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["word", "count"])  # заголовок
            for word, count in freqs.items():
                writer.writerow([word, count])
    except Exception as e:
        raise ValueError(f"Ошибка записи в файл {output_file}: {e}")
    print(f"Отчет сохранен в: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Чтение отчета из CSV файла")
    parser.add_argument(
        "--csv",
        dest="csv_file",
        default="data/check.csv",
        help="Путь к CSV файлу с отчетом",
    )
    # создает парсер аргументов командной строки

    args = parser.parse_args()
    # разбирает аргументы, переданные скрипту при запуске

    try:
        read_csv_report(args.csv_file)
    except Exception as error:
        print(error)
        exit(1)
