def validate_name(name: str) -> None:
    """Проверяет, что имя - непустая строка."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Имя должно быть непустой строкой")
    if len(name.strip()) < 2:
        raise ValueError("Имя должно содержать минимум 2 символа")
    if len(name.strip()) > 50:
        raise ValueError("Имя не должно превышать 50 символов")

def validate_weight(weight: float) -> None:
    """Проверяет, что вес - положительное число."""
    if not isinstance(weight, (int, float)):
        raise TypeError("Вес должен быть числом")
    if weight <= 0:
        raise ValueError("Вес должен быть положительным числом")
    if weight > 300:
        raise ValueError("Вес не может превышать 300 кг")
    if weight < 20:
        raise ValueError("Вес не может быть меньше 20 кг")

def validate_height(height: float) -> None:
    """Проверяет, что рост - положительное число."""
    if not isinstance(height, (int, float)):
        raise TypeError("Рост должен быть числом")
    if height <= 0:
        raise ValueError("Рост должен быть положительным числом")
    if height > 280:
        raise ValueError("Рост не может превышать 280 см")
    if height < 50:
        raise ValueError("Рост не может быть меньше 50 см")

def validate_record(record: float) -> None:
    """Проверяет, что рекорд (очки) - неотрицательное число."""
    if not isinstance(record, (int, float)):
        raise TypeError("Рекорд должен быть числом")
    if record < 0:
        raise ValueError("Рекорд не может быть отрицательным")
    if record > 500:
        raise ValueError("Рекорд не может превышать 500")

def validate_health_status(status: str) -> None:
    """Проверяет, что статус здоровья допустим."""
    allowed = ("healthy", "injured", "recovering")
    if status not in allowed:
        raise ValueError(f"Статус здоровья должен быть одним из: {allowed}")

def validate_division(division: str) -> None:
    """Проверяет, что дивизион допустим."""
    allowed = ("beginner", "intermediate", "professional", "elite")
    if division not in allowed:
        raise ValueError(f"Дивизион должен быть одним из: {allowed}")

def validate_morale(morale: int) -> None:
    """Проверяет, что мораль - целое число от 0 до 10."""
    if not isinstance(morale, int):
        raise TypeError("Уровень мотивации должен быть целым числом")
    if morale < 0 or morale > 10:
        raise ValueError("Уровень мотивации должен быть от 0 до 10")