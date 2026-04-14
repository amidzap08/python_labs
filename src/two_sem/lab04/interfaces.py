"""
Модуль содержит абстрактные базовые классы (интерфейсы).
Определяет контракты поведения для классов.
"""

from abc import ABC, abstractmethod
from typing import Any


class Printable(ABC):
    """Интерфейс для объектов с строковым представлением."""

    @abstractmethod
    def to_string(self) -> str:
        """Возвращает строковое представление объекта."""
        pass


class Comparable(ABC):
    """Интерфейс для сравнения объектов."""

    @abstractmethod
    def compare_to(self, other: Any) -> int:
        """
        Сравнивает текущий объект с другим.
        
        Returns:
            -1 если self < other, 0 если равны, 1 если self > other
        """
        pass


class Identifiable(ABC):
    """Интерфейс для объектов с уникальным идентификатором."""

    @abstractmethod
    def get_id(self) -> str:
        """Возвращает уникальный идентификатор."""
        pass


class Validatable(ABC):
    """Интерфейс для валидации объектов."""

    @abstractmethod
    def is_valid(self) -> bool:
        """Проверяет валидность объекта."""
        pass

    @abstractmethod
    def get_validation_errors(self) -> list:
        """Возвращает список ошибок валидации."""
        pass