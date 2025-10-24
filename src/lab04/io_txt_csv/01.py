from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    try:
        # Используем параметр encoding, а не локальную переменную
        with open(p, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        return FileNotFoundError(f"File not found: {path}")
    except UnicodeDecodeError as e:
        return UnicodeDecodeError(
            f"Encoding error: cannot decode file '{path}' with encoding '{encoding}'",
            e.object, e.start, e.end
        )

text1 = read_text(r"C:\Users\Comp\Desktop\python_labs\data\input.txt")
print(text1)

  