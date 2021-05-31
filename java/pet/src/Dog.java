public class Dog extends Pet {
    // Variables 
    private int dogSpaceNumber;
    private int dogWeight;
    private boolean grooming;

    // Constructor
    public Dog() {

    }

    // Methods
    public double getDogWeight() {
        return dogWeight;
    }
    public boolean getGrooming() {
        return grooming;
    }
    public void setGrooming(boolean grooming) {
        this.grooming = grooming;
    }
    public int getDogSpaceNumber() {
        return dogSpaceNumber;
    }
    public void setDogSpaceNumber(int dogSpaceNumber) {
        this.dogSpaceNumber = dogSpaceNumber;
    }
    public void setDogWeight(int dogWeight) {
        this.dogWeight = dogWeight;
    }

}
