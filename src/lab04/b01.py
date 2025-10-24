import sys
from pathlib import Path
import csv
import argparse

def read_csv_report(csv_file: str) -> None:
    input_path = Path(csv_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Ошибка: файл {csv_file} не существует")


    with open(input_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file) # интерирует сsv файл по строкам
        header = next(reader) # первая строка из файла- заголовок
        
        word_counts = {} # пустой словарь
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
    # ключ для сортировки, х- пара(слово,количество),-х[1]-сортирует по кол-ву
    # в убывающем порядке
    for word, count in sorted_words:
        print(f"{word}:{count}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Чтение отчета из CSV файла')
    parser.add_argument('--csv', dest='csv_file', default='data/check.csv', help='Путь к CSV файлу с отчетом')
    # создает аргумент ArgumentParser


    args = parser.parse_args()
    # разбивает аргументы, переданные скрипту при запуске
    
    try:
        read_csv_report(args.csv_file)
    except Exception as error:
        print(error)
        exit(1)