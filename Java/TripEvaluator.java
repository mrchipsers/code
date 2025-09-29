import java.util.Scanner;
public class TripEvaluator{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("how far are you going in km?");
        double distance = input.nextDouble();
        System.out.println("how much does it cost to take the ferry? (if you aren't taking the ferry or there is no cost, input 0)");
        double ferry = input.nextDouble();
        if (distance<0) {
            System.out.println("Invalid Input");
        }else if (calculateFlightCost(distance)>calculateCarCost(distance, ferry)){
            System.out.println("You should take a car, the cost is: $"+calculateCarCost(distance, ferry));
        }else{
            System.out.println("You should take a plane, the cost is: $"+calculateFlightCost(distance));
        }
    }
    public static double calculateFlightCost(double distance){
        double cost = (distance*0.2)+200;
        return cost;
    }
    public static double calculateCarCost(double distance, double ferry){
        double cost = (distance*0.4)+ferry;
        return cost;
    }
}