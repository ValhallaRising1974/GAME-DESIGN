
class Champion:
    def __init__(self, name, champion_class, original_lane):
        self.name = name
        self.champion_class = champion_class
        self.original_lane = original_lane
        self.current_lane = original_lane
        self.penalty = 0

    def move_to_lane(self, new_lane, current_role=None):
        self.current_lane = new_lane
        self.apply_penalty(current_role)

    def apply_penalty(self, current_role):
        if self.champion_class == "Juggernaut":
            if self.original_lane == "Highland" and self.current_lane != "Highland":
                self.penalty = 60
        elif self.champion_class == "Slayer":
            if self.original_lane == "The Middle Way" and self.current_lane in ["Oblivion", "Firestarter"]:
                self.penalty = 80
            elif self.original_lane == "Oblivion" and self.current_lane != "Oblivion":
                self.penalty = 80
        elif self.champion_class == "Sniper":
            if self.original_lane != "Firestarter":
                self.penalty = 70
        elif self.champion_class == "Warlock":
            if current_role != "Damage":
                self.penalty = 70
        elif self.champion_class == "Bruiser":
            if self.original_lane == "Highland" and self.current_lane != "Highland":
                self.penalty = 40
            elif self.original_lane == "Oblivion" and self.current_lane != "Oblivion":
                self.penalty = 40
        else:
            self.penalty = 0

    def can_use_item(self, item_class):
        return self.champion_class == item_class

    def status(self):
        return {
            "Nome": self.name,
            "Classe": self.champion_class,
            "Rota Original": self.original_lane,
            "Rota Atual": self.current_lane,
            "Penalidade (%)": self.penalty
        }
