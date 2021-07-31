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
// Prompt user to input wall's height
        do{
            System.out.println("Enter wall height (feet): ");
            wallHeight = scnr.nextDouble();

        }while(wallHeight<=0);

// Implement a do-while loop to ensure input is valid
// Prompt user to input wall's width
        do{
            System.out.println("Enter wall width (feet): ");
            wallWidth = scnr.nextDouble();
        }while(wallWidth<=0);
// Calculate and output wall area
        wallArea = wallHeight * wallWidth;
        System.out.println("Wall area: "+wallArea+" square feet");
// Calculate and output the amount of paint (in gallons) needed to paint the wall
        gallonsPaintNeeded = wallArea/squareFeetPerGallons;
        System.out.println("Paint needed: " + gallonsPaintNeeded + " gallons");
        //Only lines 33 and 34 have been added and the rest of the code is untouched.
        //We use Math.ceil() method of the Math class, this method gives us the ceiling value or the upper bond of a value.
        //For example for Math.ceil(3.1) will give us 4.0 and for Math.ceil(1.9) will give us 2.0.
        cansPaintNeeded = Math.ceil(gallonsPaintNeeded);
        System.out.println("Cans needed: "+cansPaintNeeded+" can(s)");  //we print the result.
    }
}