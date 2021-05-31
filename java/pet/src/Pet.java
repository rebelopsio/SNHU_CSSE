public class Pet {
    private String petType;
    private String petName;
    private int petAge;
    private int dogSpaces;
    private int catSpaces;
    private int daysStay;
    private float amountDue;

    public Pet() {

    }

    public String getPetType() {
        return petType;
    }
    public float getAmountDue() {
        return amountDue;
    }
    public void setAmountDue(float amountDue) {
        this.amountDue = amountDue;
    }
    public int getDaysStay() {
        return daysStay;
    }
    public void setDaysStay(int daysStay) {
        this.daysStay = daysStay;
    }
    public int getCatSpaces() {
        return catSpaces;
    }
    public void setCatSpaces(int catSpaces) {
        this.catSpaces = catSpaces;
    }
    public int getDogSpaces() {
        return dogSpaces;
    }
    public void setDogSpaces(int dogSpaces) {
        this.dogSpaces = dogSpaces;
    }
    public int getPetAge() {
        return petAge;
    }
    public void setPetAge(int petAge) {
        this.petAge = petAge;
    }
    public String getPetName() {
        return petName;
    }
    public void setPetName(String petName) {
        this.petName = petName;
    }
    public void setPetType(String petType) {
        this.petType = petType;
    }
}
