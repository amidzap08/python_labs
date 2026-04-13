# lab03/base.py
"""
Базовый класс для ЛР-3
Импортируется из ЛР-1 для переиспользования кода
"""
import sys
from pathlib import Path

# Добавляем путь к lab01 для импорта
sys.path.insert(0, str(Path(__file__).parent.parent))

# Импортируем класс Team из ЛР-1 как базовый
from two_sem.lab01.model import Team

# Реэкспортируем для использования в ЛР-3
__all__ = ['Team']