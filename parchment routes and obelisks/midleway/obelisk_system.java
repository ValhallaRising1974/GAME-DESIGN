public class Obelisk {
    private int health;
    private int damage;
    private boolean isBaseObelisk;

    public Obelisk(boolean isBase) {
        this.isBaseObelisk = isBase;
        this.health = isBase ? 2000 : 1200;
        this.damage = isBase ? 200 : 120;
    }

    public void attack() {
        System.out.println("Obelisk fires a magical beam!");
    }
}
