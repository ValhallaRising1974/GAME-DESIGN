#  Valhalla Rising – Territory System (Java Prototype)

This system introduces the symbolic exploration mechanics of **Valhalla Rising – The Parchment**.
In this prototype, players explore regions, unlock fragments of consciousness, and awaken forgotten truths.

---

## Overview

The system simulates a living world composed of symbolic regions. Each territory:

- Has a **name** and **poetic description**
- Belongs to a symbolic type: `Battlefield`, `Obelisk`, or `Sanctuary`
- Offers **interactive feedback** upon arrival
- May trigger **symbolic events** when visited for the first time

The player navigates through this map not to conquer, but to remember.

---

## Inner Progression System

When a player explores new territories, there's a chance to awaken a **Fragment of Consciousness**.

- Every 3 fragments, a whisper from the champions is revealed.
- These whispers are symbolic messages meant to reflect inner healing.

> Example: *“Even broken things remember how to shine.”*

There are no levels or experience bars — only remembrance.

---

## Sample Territories

- `Highland` – The path of vision and solitude
- `The Middle Way` – A neutral obelisk between logic and illusion
- `Firestarter` – The birthplace of rebellion
- `Oblivion` – A sanctuary where silence reigns

---

## How to Run

Compile and run via terminal:

```bash
javac MapExplorer.java
java MapExplorer
```

Then follow the prompts to explore regions and trigger symbolic events.

---

## Main Classes

- `Territory` – Abstract class for any region
- `Battlefield`, `Obelisk`, `Sanctuary` – Subclasses with unique interactions
- `Player` – Tracks symbolic progression
- `MapExplorer` – Entry point and navigation logic

---

##  Author

**Marcelo** (a.k.a. [Valhalla Rising](https://github.com/ValhallaRising1974))

> “In Valhalla Rising, we don’t level up — we remember who we were.”
