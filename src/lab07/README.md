# Лабораторная работа 7
## pyproject.py
```python
[project]
name = "lab07-tests"
version = "0.1.0"

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=4.0", 
    "black>=24.0",
    "ruff>=0.6",
]

[tool.black]
line-length = 88
target-version = ["py311"]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "--strict-markers --maxfail=1"
```

## Сборка пакета
![Картинка 1](/src/lab07/images/req.png)

## BLACK
![Картинка 2](/src/lab07/images/BLACK.png)

## CHECK ME
![Картинка 3](/src/lab07/images/check.png)

## Проверка тестов 
![Картинка 4](/src/lab07/images/prov.png)

![Картинка 5](/src/lab07/images/prov2.png)

![](/tests/test_csv_to_json.py)
![](/tests/test_text.py)