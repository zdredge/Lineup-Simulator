class Player:
    def __init__(self, name: str, positions: list, offensive_stats: dict, defensive_stats: dict):
        self.name = name
        self.positions = positions
        self.offensive_stats = offensive_stats
        self.defensive_stats = defensive_stats

    def __str__(self):
        return f"{self.name}: {self.positions}"

