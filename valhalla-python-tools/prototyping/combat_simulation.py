# 🛡Symbolic Combat Algorithm – Valhalla Rising: The Parchment

import random

# Example champions
defined_champions = {
    "Leila": {
        "class": "Warlock",
        "hp": 1200,
        "atk": 80,
        "def": 60,
        "magic": 130,
        "essence": "Protection and Redemption"
    },
    "Seth": {
        "class": "Slayer",
        "hp": 1400,
        "atk": 110,
        "def": 50,
        "magic": 60,
        "essence": "Chaos and Rupture"
    }
}

def symbolic_combat(champ1, champ2):
    c1 = defined_champions[champ1].copy()
    c2 = defined_champions[champ2].copy()

    turn = 1
    log = []

    log.append(f"🌌 {champ1} (Essence: {c1['essence']}) vs {champ2} (Essence: {c2['essence']})")
    log.append("--- Combat Begins ---")

    while c1["hp"] > 0 and c2["hp"] > 0:
        log.append(f"⚔️ Turn {turn}")

        # Champion 1 attacks
        damage1 = c1["atk"] + random.randint(-10, 10) + (c1["magic"] // 4)
        blocked1 = c2["def"] // 2
        final1 = max(0, damage1 - blocked1)
        c2["hp"] -= final1
        log.append(f"{champ1} attacks with {damage1} power, {champ2} blocks {blocked1}, final damage: {final1}. {champ2}'s HP: {c2['hp']}")

        if c2["hp"] <= 0:
            break

        # Champion 2 attacks
        damage2 = c2["atk"] + random.randint(-10, 10) + (c2["magic"] // 4)
        blocked2 = c1["def"] // 2
        final2 = max(0, damage2 - blocked2)
        c1["hp"] -= final2
        log.append(f"{champ2} attacks with {damage2} power, {champ1} blocks {blocked2}, final damage: {final2}. {champ1}'s HP: {c1['hp']}")

        turn += 1

    winner = champ1 if c1["hp"] > 0 else champ2
    log.append("--- Combat Ends ---")
    log.append(f"🏆 Winner: {winner} ✨")

    return log

# Sample duel
duel = symbolic_combat("Leila", "Seth")
for line in duel:
    print(line)
