from pathlib import Path
import pytest
import json
import csv
import os
import sys

# Правильное определение путей
current_dir = os.path.dirname(__file__)  # получаем директорию текущего файла
src_path = os.path.join(
    current_dir, "..", "src"
)  # поднимаемся на уровень выше и входим в src
sys.path.insert(0, os.path.abspath(src_path))

from lab05.json_to_csv import json_to_csv, csv_to_json


class TestCsvToJson:
    """Тесты для функции csv_to_json"""

    def test_basic_conversion(self, tmp_path: Path):
        """Позитивный сценарий: корректная конвертация CSV → JSON"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"

        # Создаем тестовый CSV файл
        csv_data = [
            ["name", "age", "city"],
            ["Alice", "25", "Moscow"],
            ["Bob", "30", "SPb"],
            ["Charlie", "35", "Kazan"],
        ]

        with open(csv_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)

        # Выполняем конвертацию
        csv_to_json(str(csv_file), str(json_file))

        # Проверяем результат
        assert json_file.exists()

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

            # Проверяем количество записей
            assert len(data) == 3

            # Проверяем структуру данных
            for item in data:
                assert isinstance(item, dict)
                assert set(item.keys()) == {"name", "age", "city"}

            # Проверяем значения
            assert data[0]["name"] == "Alice"
            assert data[0]["age"] == "25"  # В CSV все строки, в JSON остаются строками
            assert data[0]["city"] == "Moscow"

    def test_csv_with_special_characters(self, tmp_path: Path):
        """Позитивный сценарий: CSV со специальными символами"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"

        csv_data = [
            ["name", "message", "value"],
            ["Анна", "Hello, World!", "100€"],
            ["John", "Test;with;semicolons", "50%"],
        ]

        with open(csv_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)

        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

            assert len(data) == 2
            assert data[0]["name"] == "Анна"
            assert data[0]["message"] == "Hello, World!"
            assert data[0]["value"] == "100€"

    def test_csv_with_quotes_and_commas(self, tmp_path: Path):
        """Позитивный сценарий: CSV с кавычками и запятыми в данных"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"

        # CSV с данными, содержащими запятые (должны быть в кавычках)
        csv_content = """name,description,value
"Alice","Description, with, commas",100
"Bob","Normal description",200"""

        csv_file.write_text(csv_content, encoding="utf-8")

        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

            assert len(data) == 2
            assert data[0]["name"] == "Alice"
            assert data[0]["description"] == "Description, with, commas"
            assert data[0]["value"] == "100"

    def test_empty_csv_file(self, tmp_path: Path):
        """Негативный сценарий: пустой CSV файл"""
        csv_file = tmp_path / "empty.csv"
        json_file = tmp_path / "output.json"

        csv_file.write_text("", encoding="utf-8")

        with pytest.raises(ValueError, match="CSV файл пуст"):
            csv_to_json(str(csv_file), str(json_file))

    def test_csv_without_headers(self, tmp_path: Path):
        """CSV без явных заголовков - DictReader создает заголовки из данных"""
        csv_file = tmp_path / "no_headers.csv"
        json_file = tmp_path / "output.json"

        csv_content = """Alice,25,Moscow
Bob,30,SPb"""

        csv_file.write_text(csv_content, encoding="utf-8")

        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # DictReader создаст заголовки из первой строки
        assert len(data) == 1  # Только вторая строка станет данными
        assert isinstance(data[0], dict)
        # Проверяем что ключи взяты из первой строки
        assert "Alice" in data[0]
        assert "25" in data[0]
        assert "Moscow" in data[0]

    def test_csv_with_empty_headers(self, tmp_path: Path):
        """Негативный сценарий: CSV с пустыми заголовками"""
        csv_file = tmp_path / "empty_headers.csv"
        json_file = tmp_path / "output.json"

        # CSV с пустыми именами колонок
        csv_content = """,,,
Alice,25,Moscow,IT
Bob,30,SPb,HR"""

        csv_file.write_text(csv_content, encoding="utf-8")

        # DictReader создаст fieldnames, но они будут пустыми
        # Проверяем что функция корректно обрабатывает этот случай
        try:
            csv_to_json(str(csv_file), str(json_file))
            # Если не упало, проверяем результат
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Должны быть созданы ключи с пустыми именами
            assert len(data) == 2
        except ValueError as e:
            # Или возникает ошибка - это тоже допустимо
            assert "заголовк" in str(e).lower() or "header" in str(e).lower()

    def test_csv_with_partial_headers(self, tmp_path: Path):
        """Тест CSV с частичными заголовками"""
        csv_file = tmp_path / "partial_headers.csv"
        json_file = tmp_path / "output.json"

        # Некоторые заголовки пустые
        csv_content = """name,,city
Alice,25,Moscow
Bob,30,SPb"""

        csv_file.write_text(csv_content, encoding="utf-8")

        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert len(data) == 2
        # Проверяем что пустые заголовки стали пустыми ключами
        assert "" in data[0].keys() or "1" in data[0].keys()

    def test_csv_without_data(self, tmp_path: Path):
        """Негативный сценарий: CSV только с заголовками, без данных"""
        csv_file = tmp_path / "headers_only.csv"
        json_file = tmp_path / "output.json"

        csv_content = "name,age,city"
        csv_file.write_text(csv_content, encoding="utf-8")

        with pytest.raises(ValueError, match="не содержит данных"):
            csv_to_json(str(csv_file), str(json_file))

    def test_invalid_csv_syntax(self, tmp_path):
        csv_file = tmp_path / "complex.csv"
        json_file = tmp_path / "output.json"

        # CSV с различными сложными случаями
        csv_content = """name,description,value
"Alice,Smith","Description with, commas",100
"Bob","Text with ""quotes"" inside",200
"Charlie","Normal text",300"""

        csv_file.write_text(csv_content, encoding="utf-8")

        # Этот CSV должен обработаться корректно
        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert len(data) == 3
        assert data[0]["name"] == "Alice,Smith"
        assert data[1]["description"] == 'Text with "quotes" inside'

    def test_csv_file_not_found(self, tmp_path: Path):
        """Негативный сценарий: файл не существует"""
        csv_file = tmp_path / "nonexistent.csv"
        json_file = tmp_path / "output.json"

        with pytest.raises(FileNotFoundError, match="CSV файл не найден"):
            csv_to_json(str(csv_file), str(json_file))

    def test_wrong_csv_extension(self, tmp_path: Path):
        """Негативный сценарий: неверное расширение файла"""
        txt_file = tmp_path / "test.txt"
        json_file = tmp_path / "output.json"

        txt_file.write_text("name,age\nAlice,25", encoding="utf-8")

        with pytest.raises(ValueError, match="не является CSV файлом"):
            csv_to_json(str(txt_file), str(json_file))

    def test_csv_wrong_encoding(self, tmp_path: Path):
        """Негативный сценарий: неверная кодировка CSV файла"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"

        # Записываем в кодировке, отличной от UTF-8
        with open(csv_file, "w", encoding="cp1251") as f:
            f.write("name,age\nАнна,25")  # кириллица в cp1251

        with pytest.raises(ValueError, match="неверную кодировку"):
            csv_to_json(str(csv_file), str(json_file))


class TestIntegration:
    """Интеграционные тесты: JSON → CSV → JSON"""

    def test_round_trip_conversion(self, tmp_path: Path):
        """Интеграционный тест: JSON → CSV → JSON"""
        # Исходные данные
        original_data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"},
            {"name": "Charlie", "age": 35, "city": "Kazan", "country": "Russia"},
        ]

        json_file1 = tmp_path / "original.json"
        csv_file = tmp_path / "converted.csv"
        json_file2 = tmp_path / "final.json"

        # Сохраняем исходный JSON
        with open(json_file1, "w", encoding="utf-8") as f:
            json.dump(original_data, f, ensure_ascii=False, indent=2)

        # Конвертируем JSON → CSV
        json_to_csv(str(json_file1), str(csv_file))

        # Конвертируем CSV → JSON
        csv_to_json(str(csv_file), str(json_file2))

        # Загружаем конечный JSON
        with open(json_file2, "r", encoding="utf-8") as f:
            final_data = json.load(f)

        # Проверяем что количество записей совпадает
        assert len(final_data) == len(original_data)

        # Проверяем что все поля присутствуют (CSV добавит пустые поля для отсутствующих значений)
        all_keys = set()
        for item in original_data:
            all_keys.update(item.keys())

        for item in final_data:
            assert set(item.keys()) == all_keys

        # Проверяем значения (учитываем что в CSV все становится строками)
        for i, original_item in enumerate(original_data):
            final_item = final_data[i]
            for key in all_keys:
                original_value = original_item.get(key, "")
                final_value = final_item.get(key, "")
                assert str(original_value) == final_value


if __name__ == "__main__":
    # Правильный запуск тестов
    pytest.main([__file__, "-v"])
