# npc_group_simulator.py – SymbolicBot Emotional Group Simulation

from symbolic_bot_ai import SymbolicBot

# Create a small team of bots with unique essences
bots = [
    SymbolicBot("Nahlia", "Serenity and Vision", base_aggression=30, base_caution=20),
    SymbolicBot("Dravok", "Wrath and Ashes", base_aggression=70, base_caution=15),
    SymbolicBot("Selun", "Doubt and Fog", base_aggression=40, base_caution=60),
    SymbolicBot("Vael", "Harmony and Pulse", base_aggression=45, base_caution=35),
    SymbolicBot("Zaruk", "Vengeance and Flame", base_aggression=65, base_caution=25)
]

# Simulate different environments for each bot
scenarios = [
    {"cosmic_energy_level": 60, "nearby_enemies": ["Leila"], "map_fog": True},
    {"cosmic_energy_level": 85, "nearby_enemies": ["Seth", "Lara"], "map_fog": False},
    {"cosmic_energy_level": 30, "nearby_enemies": [], "map_fog": True},
    {"cosmic_energy_level": 95, "nearby_enemies": ["Bjorn"], "map_fog": False},
    {"cosmic_energy_level": 50, "nearby_enemies": ["Tuane", "Hogan"], "map_fog": True},
]

# Run the simulation
for i, bot in enumerate(bots):
    print(f"\n🌌 Simulation for {bot.name} – Essence: {bot.essence}")
    scenario = scenarios[i]
    bot.perceive_environment(**scenario)
    print(bot.act())
