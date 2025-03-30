# SymbolicBot AI – Valhalla Rising: The Parchment

import random

class SymbolicBot:
    def __init__(self, name, essence, base_aggression, base_caution):
        self.name = name
        self.essence = essence  # Symbolic essence: "Mystery", "Vengeance", "Balance"
        self.aggression = base_aggression  # 0 to 100
        self.caution = base_caution  # 0 to 100
        self.state = "neutral"

    def perceive_environment(self, cosmic_energy_level, nearby_enemies, map_fog):
        """
        Evaluate surroundings and adjust emotional state
        """
        if cosmic_energy_level > 70:
            self.aggression += 10
        if len(nearby_enemies) > 2:
            self.caution += 15
        if not map_fog:
            self.caution += 5

        # Boundaries
        self.aggression = min(self.aggression, 100)
        self.caution = min(self.caution, 100)

        self.update_state()

    def update_state(self):
        if self.caution > 80:
            self.state = "avoid"
        elif self.aggression > 70:
            self.state = "engage"
        else:
            self.state = "observe"

    def act(self):
        if self.state == "engage":
            return f"{self.name} charges into battle, essence of {self.essence} pulsing."
        elif self.state == "avoid":
            return f"{self.name} retreats to the shadows, seeking signs beyond sight."
        else:
            return f"{self.name} waits, watching silently... the winds are uncertain."

# Example Usage
bot = SymbolicBot("Morgun", "Doubt and Mystery", base_aggression=50, base_caution=40)
bot.perceive_environment(cosmic_energy_level=75, nearby_enemies=["Leila", "Seth"], map_fog=False)
print(bot.act())
