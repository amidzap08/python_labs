"""
Модуль содержит классы моделей, реализующие интерфейсы.
"""

from dataclasses import dataclass
from two_sem.lab04.interfaces import Printable, Comparable, Identifiable, Validatable


@dataclass
class Team(Printable, Comparable, Identifiable, Validatable):
    """Класс спортивной команды."""
    
    name: str
    division: str
    is_active: bool = True
    health_status: str = "healthy"
    total_points: int = 0
    morale: float = 100.0
    wins: int = 0
    losses: int = 0
    
    # Printable
    def to_string(self) -> str:
        return f"Team: {self.name} ({self.division}) | Points: {self.total_points} | Active: {self.is_active}"
    
    # Comparable
    def compare_to(self, other: 'Team') -> int:
        if not isinstance(other, Team):
            raise TypeError(f"Cannot compare Team with {type(other).__name__}")
        
        self_perf = self.performance_score()
        other_perf = other.performance_score()
        
        if self_perf < other_perf:
            return -1
        elif self_perf > other_perf:
            return 1
        return 0
    
    # Identifiable
    def get_id(self) -> str:
        return f"{self.name}_{self.division}".lower().replace(" ", "_")
    
    # Validatable
    def is_valid(self) -> bool:
        return len(self.get_validation_errors()) == 0
    
    def get_validation_errors(self) -> list:
        errors = []
        if not self.name:
            errors.append("Name is required")
        if not self.division:
            errors.append("Division is required")
        if self.health_status not in ["healthy", "recovering", "injured"]:
            errors.append(f"Invalid health status: {self.health_status}")
        if self.total_points < 0:
            errors.append("Total points cannot be negative")
        if self.morale < 0 or self.morale > 100:
            errors.append("Morale must be between 0 and 100")
        return errors
    
    # Business methods
    def performance_score(self) -> float:
        """Расчет производительности команды."""
        win_rate = self.wins / (self.wins + self.losses) if (self.wins + self.losses) > 0 else 0
        activity_multiplier = 1.0 if self.is_active else 0.5
        health_multipliers = {"healthy": 1.0, "recovering": 0.7, "injured": 0.4}
        health_multiplier = health_multipliers.get(self.health_status, 0.5)
        
        return self.total_points * win_rate * activity_multiplier * health_multiplier * (self.morale / 100)


@dataclass
class Player(Printable, Comparable, Identifiable):
    """Класс игрока."""
    
    name: str
    position: str
    team_name: str
    skill_rating: int = 50
    is_active: bool = True
    
    # Printable
    def to_string(self) -> str:
        status = "Active" if self.is_active else "Inactive"
        return f"Player: {self.name} | Pos: {self.position} | Team: {self.team_name} | Rating: {self.skill_rating} | {status}"
    
    # Comparable
    def compare_to(self, other: 'Player') -> int:
        if not isinstance(other, Player):
            raise TypeError(f"Cannot compare Player with {type(other).__name__}")
        
        if self.skill_rating < other.skill_rating:
            return -1
        elif self.skill_rating > other.skill_rating:
            return 1
        return 0
    
    # Identifiable
    def get_id(self) -> str:
        return f"{self.name}_{self.team_name}".lower().replace(" ", "_")


@dataclass
class Match(Printable, Comparable):
    """Класс матча."""
    
    home_team: str
    away_team: str
    home_score: int = 0
    away_score: int = 0
    is_completed: bool = False
    
    # Printable
    def to_string(self) -> str:
        if self.is_completed:
            return f"Match: {self.home_team} {self.home_score} - {self.away_score} {self.away_team} (FINAL)"
        return f"Match: {self.home_team} vs {self.away_team} (Upcoming)"
    
    # Comparable
    def compare_to(self, other: 'Match') -> int:
        if not isinstance(other, Match):
            raise TypeError(f"Cannot compare Match with {type(other).__name__}")
        
        self_goals = self.home_score + self.away_score
        other_goals = other.home_score + other.away_score
        
        if self_goals < other_goals:
            return -1
        elif self_goals > other_goals:
            return 1
        return 0