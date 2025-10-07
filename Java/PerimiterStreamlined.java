import java.util.Scanner;
public class PerimiterStreamlined{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Please input a side legnth: ");
        double sidel = input.nextDouble();
        System.out.println("Please enter a number of sides; ");
        int siden = input.nextInt();
        input.close();
        System.out.println("The perimeter of the shape is "+perimeter(sidel, siden));
    }
    public static double perimeter(double sidel, int siden){
        double perimeter = sidel*siden;
        return perimeter;
    }
}