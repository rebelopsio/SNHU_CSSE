import java.util.Scanner;

public class Paint1 {

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        double wallHeight = 0.0;
        double wallWidth = 0.0;
        double wallArea = 0.0;
        double gallonsPaintNeeded = 0.0;
        double cansPaintNeeded = 0.0;
        final double squareFeetPerGallons = 350.0;

        // Implement a do-while loop to ensure input is valid
        do {
            try {

                // Prompt user to input wall's height
                System.out.println("Enter wall height (feet): ");
                wallHeight = scnr.nextDouble();

                if (wallHeight <= 0) {
                    throw new Exception();
                }

            }

            catch (Exception expt) {
                System.out.println("Invalid input");
                scnr.next();
            }
        } while (wallHeight <= 0);

        // Implement a do-while loop to ensure input is valid
        do {
            try {
                // Prompt user to input wall's width
                System.out.println("Enter wall width (feet): ");
                wallWidth = scnr.nextDouble();

                if (wallWidth <= 0) {
                    throw new Exception();
                }

            } catch (Exception expt) {
                System.out.println("Invalid input");
                scnr.next();
            }
        } while (wallWidth <= 0);

        // Calculate and output wall area
        wallArea = wallHeight * wallWidth;
        System.out.println("Wall area: " + wallArea + " square feet");

        // Calculate and output the amount of paint (in gallons) needed to paint the
        // wall
        gallonsPaintNeeded = wallArea / squareFeetPerGallons;
        System.out.println("Paint needed: " + gallonsPaintNeeded + " gallons");

        // Calculate and output the number of paint cans needed to paint the wall,
        // rounded up to nearest integer
        // Complete this code block
        cansPaintNeeded = Math.ceil(gallonsPaintNeeded);
        System.out.println("Cans needed: " + cansPaintNeeded + " can(s)");

    }
}
