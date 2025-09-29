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
            if (calculateCarCost(distance, ferry)>calculateTrainCost(distance)){
                System.out.println("You should take the train, the cost is: "+calculateTrainCost(distance));
            }else{
                System.out.println("You should take the car, the cost is: "+calculateCarCost(distance, ferry));
            }
        }else{
            if (calculateFlightCost(distance)>calculateTrainCost(distance)){
                System.out.println("You should take the train, the cost is: "+calculateTrainCost(distance));
            }else{
                System.out.println("You should take the plane, the cost is: "+calculateFlightCost(distance));
            }
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
    public static double calculateTrainCost(double distance){
        double cost = distance*0.25;
        return cost;
    }
}