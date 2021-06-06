public class ItemToPurchase {
    String itemName;
    int itemPrice;
    int itemQuantity;
    public void setName(String name)
    {
        itemName = name;
    }

    public String getName() {
        return itemName;
    }

    public void setPrice(int value) {
        itemPrice = value;
    }

    public int getPrice() {
        return itemPrice;
    }

    public void setQuantity(int number) {
        itemQuantity = number;
    }

    public int getQuantity() {
        return itemQuantity;
    }
}