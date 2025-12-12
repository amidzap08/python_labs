from lab09.group import Group

# Попытка импортировать настоящий Student
try:
    from lab08.models import Student
    print("Используется импортированный Student")
except ImportError:
    from lab09.group import Student
    print("Используется локальный Student")

def main():
    # Тестирование
    pass

if __name__ == "__main__":
    main()