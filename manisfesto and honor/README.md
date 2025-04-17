# Valhalla Rising - The Parchment
# Core Design Manifesto - Honor System and Community Culture
# Author: Valhalla Rising (Marcelo dos Santos Prado)
# Created - April 2025

"""
This document defines the essential values, behavioral principles, and narrative-driven mechanics that guide the
community structure and player interaction model of Valhalla Rising – The Parchment.

Our mission is to build a competitive, beautiful, and ethical space — where fun is sacred, communication is celebrated,
and respect is the foundation.
"""

# === CORE OBJECTIVES ===

objectives = [
    "Foster a welcoming competitive environment focused on joy, mutual growth, and strategy.",
    "Discourage toxicity and penalize harmful communication and behavior.",
    "Encourage collaboration and healthy communication before, during, and after matches.",
    "Reward players for empathy, guidance, and community support (beyond kill count).",
    "Embed respect and honor into champion narratives, voice lines, and match intros.",
    "Use narrative events to reinforce values such as humility, protection, and growth.",
    "Ensure that even losses contribute to player growth, emotionally and strategically."
]

# === PLAYER HONOR SYSTEM (Pseudocode) ===

def award_honor_points(player, behavior):
    if behavior == "encouraging_ally":
        player.honor += 2
    elif behavior == "respects_enemy":
        player.honor += 1
    elif behavior == "toxic_chat":
        player.honor -= 3
    elif behavior == "team_griefing":
        player.honor -= 5
    elif behavior == "uplifts_team_after_loss":
        player.honor += 3
    else:
        player.honor += 0  # Neutral behavior

    # Trigger champion response
    trigger_champion_interaction(player, behavior)

# === CHAMPION-DRIVEN NARRATIVES ===

champion_lines = {
    "Rayzel": {
        "on_honor_gained": "Let the strength of spirit lead more than the swing of your blade.",
        "on_toxic_behavior": "Victory means nothing if earned without dignity."
    },
    "Yara": {
        "on_honor_gained": "You watered someone’s hope today. That is a rare gift.",
        "on_toxic_behavior": "Even the earth recoils at cruel words."
    },
    "Seth": {
        "on_honor_gained": "Justice without cruelty. You chose wisely.",
        "on_toxic_behavior": "Be careful. Darkness can start with a whisper."
    }
}

def trigger_champion_interaction(player, behavior):
    if behavior in ["encouraging_ally", "respects_enemy", "uplifts_team_after_loss"]:
        print(champion_lines[player.champion]["on_honor_gained"])
    elif behavior in ["toxic_chat", "team_griefing"]:
        print(champion_lines[player.champion]["on_toxic_behavior"])

# === SUMMARY ===

"""
Valhalla Rising - The Parchment is more than a game. It is a movement — one that redefines how players relate
to each other and to the universe of combat. With competitive integrity and emotional wisdom, we rise.

This file will evolve with each patch and social discovery.
"""

# END OF MANIFESTO
