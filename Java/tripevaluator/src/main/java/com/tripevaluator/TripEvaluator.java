package com.tripevaluator;
import java.util.Scanner;
public class TripEvaluator{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("how far are you going in km?");
        double distance = input.nextDouble();
        System.out.println("how much does it cost to take the ferry? (if you aren't taking the ferry or there is no cost, input 0)");
        double ferry = input.nextDouble();
        input.close();
        tripEval(distance, ferry);
        return;
    }

    public static String tripEval(double distance, double ferry){
        if (distance<0 || ferry<0) {
            System.out.println("Invalid Input");
            return null;
        }
        
        double[][] transport = {calculateCarCost(distance, ferry), calculateFlightCost(distance), calculateTrainCost(distance)};
        double[] cost = {0, 0, 0};
        double[] time = {0, 0, 0};
        double[] score = {0, 0, 0};

        for (int i = 0; i<3; i++){
            cost[i] = transport[i][0];
            time[i] = transport[i][1];
            score[i] = cost[i]+time[i];
        }
       
        if (score[0]<score[1] && score[0]<score[2]){
            long[] ctime = decimalTimeConvert(time[0]);
            System.out.println("You should take the car. it costs "+cost[0]+" and will take "+(ctime[0])+" hours and "+(ctime[1])+" minutes");
            return "You should take the car. it costs "+cost[0]+" and will take "+(ctime[0])+" hours and "+(ctime[1])+" minutes";
        }else if (score[1]<score[0] && score[1]<score[2]){
            long[] ptime = decimalTimeConvert(time[1]);
            System.out.println("You should take the plane. it costs "+cost[1]+" and will take "+(ptime[0])+" hours and "+(ptime[1])+" minutes");
            return "You should take the plane. it costs "+cost[1]+" and will take "+(ptime[0])+" hours and "+(ptime[1])+" minutes";
        }else{
            long[] ttime = decimalTimeConvert(time[2]);
            System.out.println("You should take the train. it costs "+cost[2]+" and will take "+(ttime[0])+" hours and "+(ttime[1])+" minutes");
            return "You should take the train. it costs "+cost[2]+" and will take "+(ttime[0])+" hours and "+(ttime[1])+" minutes";
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