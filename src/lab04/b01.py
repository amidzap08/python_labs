import sys
from pathlib import Path
import csv
import argparse

def read_csv_report(csv_file: str) -> None:
#Чтение отчета из CSV файла и вывод в консоль
    input_path = Path(csv_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Ошибка: файл {csv_file} не существует")
    # Проверяем, что файл не пустой
    
    #Читаем CSV файл
    with open(input_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  #Пропускаем заголовок
        
        word_counts = {}
        total_words = 0
        
        for row in reader:
            if len(row) >= 2:
                word = row[0]
                count = int(row[1])
                word_counts[word] = count
                total_words += count
    
    #Выводим статистику
    unique_words = len(word_counts)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    
    #Сортируем по убыванию частоты
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_words:
        print(f"{word}:{count}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Чтение отчета из CSV файла')
    parser.add_argument('--csv', dest='csv_file', default='data/check.csv', help='Путь к CSV файлу с отчетом')
    
    args = parser.parse_args()
    
    try:
        read_csv_report(args.csv_file)
    except Exception as error:
        print(error)
        exit(1)