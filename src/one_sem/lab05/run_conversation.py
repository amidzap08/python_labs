import os
import sys

# Добавляем текущую директорию в путь для импорта
sys.path.append(".")

from src.lab05.json_to_csv import json_to_csv, csv_to_json
from src.lab05.csv_to_xlsx import csv_to_xlsx


def main():
    """Запускает все конвертации и создает файлы в data/out/"""

    # Создаем папку out если её нет
    os.makedirs("data/out", exist_ok=True)

    print("=== ЗАПУСК КОНВЕРТАЦИЙ ===")

    try:
        # 1. JSON → CSV
        print(
            "1. Конвертируем data/samples/people.json → data/out/people_from_json.csv"
        )
        json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
        print("   ✓ Успешно")

        # 2. CSV → JSON
        print("2. Конвертируем data/samples/people.csv → data/out/people_from_csv.json")
        csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
        print("   ✓ Успешно")

        # 3. CSV → XLSX (из оригинального people.csv)
        print("3. Конвертируем data/samples/people.csv → data/out/people.xlsx")
        csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
        print("   ✓ Успешно")

        # 4. Дополнительно: cities.csv → XLSX
        print("4. Конвертируем data/samples/cities.csv → data/out/cities.xlsx")
        csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")
        print("   ✓ Успешно")

        print("\n ВСЕ КОНВЕРТАЦИИ ЗАВЕРШЕНЫ!")
        print(" Результаты сохранены в data/out/")

        # Показываем созданные файлы
        print("\n Созданные файлы:")
        for file in os.listdir("data/out"):
            print(f"   - {file}")

    except Exception as e:
        print(f" Ошибка: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
