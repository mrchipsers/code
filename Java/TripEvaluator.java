import java.util.Scanner;
public class TripEvaluator{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("how far are you going in km?");
        double distance = input.nextDouble();
        System.out.println("how much does it cost to take the ferry? (if you aren't taking the ferry or there is no cost, input 0)");
        double ferry = input.nextDouble();
        input.close();
        
        if (distance<0) {
            System.out.println("Invalid Input");
            return;
        }
        
        double[] car = calculateCarCost(distance, ferry);
        double carcost = car[0];
        double cartime = car[1];
        double cscore = (0.5*carcost)+(0.5*cartime);
        
        double[] plane = calculateFlightCost(distance);
        double planecost = plane[0];
        double planetime = plane[1];
        double pscore = (0.7*planecost)+(0.3*planetime);
       
        double[] train = calculateTrainCost(distance);
        double traincost = train[0];
        double traintime = train[1];
        double tscore = (0.6*traincost)+(0.4*traintime);
       
        if (cscore<pscore && cscore<tscore){
            long[] time = decimalTimeConvert(cartime);
            System.out.println("You should take the car. it costs "+carcost+" and will take "+(time[0])+" hours and "+(time[1])+" minutes");
        }else if (pscore<cscore && pscore<tscore){
            long[] time = decimalTimeConvert(planetime);
            System.out.println("You should take the plane. it costs "+planecost+" and will take "+(time[0])+" hours and "+(time[1])+" minutes");
        }else{
            long[] time = decimalTimeConvert(traintime);
            System.out.println("You should take the train. it costs "+traincost+" and will take "+(time[0])+" hours and "+(time[1])+" minutes");
        }
    }

    public static double[] calculateFlightCost(double distance){
        double cost = (distance*0.2)+200;
        double time = (distance/900)+3;
        double[] list = {cost, time};
        return list;
    }

    public static double[] calculateCarCost(double distance, double ferry){
        double cost = (distance*0.4)+ferry;
        double time = distance/100;
        double[] list = {cost, time};
        return list;
    }

    public static double[] calculateTrainCost(double distance){
        double cost = distance*0.25;
        double time = (distance/350)+0.5;
        double[] list = {cost, time};
        return list;
    }
    public static long[] decimalTimeConvert(double time){
        double dtime = time%(time/time);
        time -= dtime;
        dtime = (dtime*60)/100;
        time += dtime;
        time = ((int)(time*100))/100.0;
        int hours = (int)time;
        long minutes = Math.round((time%(time/time))*100);
        long[] list = {hours, minutes};
        return list;
    }
}