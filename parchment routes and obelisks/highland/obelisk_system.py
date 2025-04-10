class Obelisk:
    def __init__(self, is_base=False):
        self.is_base = is_base
        self.health = 2000 if is_base else 1200
        self.damage = 200 if is_base else 120

    def attack(self):
        print("Obelisk fires a magical beam!")
