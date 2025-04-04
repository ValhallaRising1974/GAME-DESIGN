
public class Champion {
    private String name;
    private String championClass;
    private String originalLane;
    private String currentLane;
    private int penalty;

    public Champion(String name, String championClass, String originalLane) {
        this.name = name;
        this.championClass = championClass;
        this.originalLane = originalLane;
        this.currentLane = originalLane;
        this.penalty = 0;
    }

    public void moveToLane(String newLane, String currentRole) {
        this.currentLane = newLane;
        applyPenalty(currentRole);
    }

    public void applyPenalty(String currentRole) {
        if (championClass.equals("Juggernaut") && !currentLane.equals(originalLane) && originalLane.equals("Highland")) {
            penalty = 60;
        } else if (championClass.equals("Slayer")) {
            if (originalLane.equals("The Middle Way") && (currentLane.equals("Oblivion") || currentLane.equals("Firestarter"))) {
                penalty = 80;
            } else if (originalLane.equals("Oblivion") && !currentLane.equals("Oblivion")) {
                penalty = 80;
            }
        } else if (championClass.equals("Sniper") && !originalLane.equals("Firestarter")) {
            penalty = 70;
        } else if (championClass.equals("Warlock") && !"Damage".equals(currentRole)) {
            penalty = 70;
        } else if (championClass.equals("Bruiser")) {
            if (originalLane.equals("Highland") && !currentLane.equals("Highland")) {
                penalty = 40;
            } else if (originalLane.equals("Oblivion") && !currentLane.equals("Oblivion")) {
                penalty = 40;
            }
        } else {
            penalty = 0;
        }
    }

    public boolean canUseItem(String itemClass) {
        return championClass.equals(itemClass);
    }

    public String getStatus() {
        return String.format("Nome: %s, Classe: %s, Rota Original: %s, Rota Atual: %s, Penalidade: %d%%",
            name, championClass, originalLane, currentLane, penalty);
    }
}
