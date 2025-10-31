from pathlib import Path
import csv
import argparse
from function import normalize, tokenize, count_freq
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../lab03/lib'))

def read_csv_report(csv_file: str) -> None:
    """Читает и анализирует CSV отчет"""
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
    for i, (word, count) in enumerate(sorted_words[:5], 1):
        print(f"{i}. {word}: {count}")

def generate_csv_report(input_file: str, output_file: str) -> None:
    """Генерирует CSV отчет из текстового файла"""
    input_path = Path(input_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Ошибка: файл {input_file} не существует")
    
    # Читаем текстовый файл
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if not text.strip():
        print("Пустой файл — создаю CSV только с заголовком.")
        # Создаем пустой CSV с заголовком
        output_path = Path(output_file)
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['word', 'count'])
        return

    # Обрабатываем текст
    norm_text = normalize(text)
    tokens = tokenize(norm_text)
    freqs = count_freq(tokens)
    
    # Сохраняем результат в CSV
    output_path = Path(output_file)
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'count'])  # заголовок
        for word, count in freqs.items():
            writer.writerow([word, count])
    
    print(f"Отчет сохранен в: {output_file}")

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
