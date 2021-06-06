import java.util.*;

public class ShoppingCartPrinter {
 
    public static void main(String[] args) throws java.lang.Exception {
        String name;
        int value = 0;
        int number = 0;

        ItemToPurchase Item1 = new ItemToPurchase();
        Scanner scnr = new Scanner(System.in);
        System.out.println("Item 1\nEnter the item name: ");
        name = scnr.nextLine();
        Item1.setName(name);
        System.out.println("Enter the item price: ");
        // Scanner scin = new Scanner(System.in);
        value = scnr.nextInt();
        Item1.setPrice(value);
        System.out.println("Enter the item quantity: ");
        number = scnr.nextInt();
        Item1.setQuantity(number);
        scnr.close();

        ItemToPurchase Item2 = new ItemToPurchase();
        Scanner scnr1 = new Scanner(System.in);
        System.out.println("Item 2\nEnter the item name: ");
        name = scnr1.nextLine();
        Item2.setName(name);
        System.out.println("Enter the item price: ");
        value = scnr1.nextInt();
        Item2.setPrice(value);
        System.out.println("Enter the item quantity: ");
        number = scnr1.nextInt();
        Item2.setQuantity(number);
        System.out.println("TOTAL COST " + Item1.getName() + " " + Item1.getQuantity() + " @ $" + Item1.getPrice()
                + " = $" + Item1.getPrice() * Item1.getQuantity());
        System.out.println("TOTAL COST " + Item2.getName() + " " + Item2.getQuantity() + " @ $" + Item2.getPrice()
                + " = $" + Item2.getPrice() * Item2.getQuantity());
        System.out.println(
                "Total: $" + (Item1.getPrice() * Item1.getQuantity() + Item2.getPrice() * Item2.getQuantity()));
        scnr.close();
    }

}