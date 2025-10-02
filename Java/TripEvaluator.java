import java.util.Scanner;
public class TripEvaluator{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("how far are you going in km?");
        double distance = input.nextDouble();
        
        if (distance<0) {
            System.out.println("Invalid Input");
            input.close();
            return;
        }else if (distance<1000){
            System.out.println("how much does it cost to take the ferry? (if you aren't taking the ferry or there is no cost, input 0)");
            double ferry = input.nextDouble();

            double[] car = calculateCarCost(distance, ferry);
            double carcost = car[0];
            double cartime = car[1];
            long carhours = Math.round(cartime-(cartime%(cartime/cartime)));
            long carminutes = Math.round((cartime%(cartime/cartime))*100);
            double cscore;
            
            double[] train = calculateTrainCost(distance);
            double traincost = train[0];
            double traintime = train[1];
            long trainhours = Math.round(traintime-(traintime%(traintime/traintime)));
            long trainminutes = Math.round((traintime%(traintime/traintime))*100);
            double tscore;
            
            if (distance > 500) {
                cscore = (0.7*carcost)+(0.3*cartime); // Penalize car for long trips
                tscore = (0.4*traincost)+(0.6*traintime); // Favor train for long trips
            } else {
                cscore = (0.4*carcost)+(0.6*cartime); // Favor car for short trips
                tscore = (0.7*traincost)+(0.3*traintime); // Penalize train for short trips
            }

            if  (cscore<tscore){
                System.out.println("You should take the car. it costs "+carcost+" and will take "+carhours+" hours and "+carminutes+" minutes");
            }else{
                System.out.println("You should take the train. it costs "+traincost+" and will take "+trainhours+" hours and "+trainminutes+" minutes");
            }
        }else{
            double[] plane = calculateFlightCost(distance);
            double planecost = plane[0];
            double planetime = plane[1];
            long planehours = Math.round(planetime-(planetime%(planetime/planetime)));
            long planeminutes = Math.round((planetime%(planetime/planetime))*100);
            double pscore = (0.7*planecost)+(0.3*planetime);
        
            double[] train = calculateTrainCost(distance);
            double traincost = train[0];
            double traintime = train[1];
            long trainhours = Math.round(traintime-(traintime%(traintime/traintime)));
            long trainminutes = Math.round((traintime%(traintime/traintime))*100);
            double tscore = (0.7*traincost)+(0.3*traintime);

            if (pscore<tscore){
                System.out.println("You should take the plane. it costs "+planecost+" and will take "+planehours+" hours and "+planeminutes+" minutes");
            }else{
                System.out.println("You should take the train. it costs "+traincost+" and will take "+trainhours+" hours and "+trainminutes+" minutes");
            }
        }
        input.close();
    }

    public static double[] calculateFlightCost(double distance){
        double cost = (distance*0.2)+200;
        double time = (distance/900)+3;
        double dtime = time%(time/time);
        time -= dtime;
        dtime = (dtime*60)/100;
        time += dtime;
        time = ((int)(time*100))/100.0;
        double[] list = {cost, time};
        return list;
    }

    public static double[] calculateCarCost(double distance, double ferry){
        double cost = (distance*0.4)+ferry;
        double time = distance/100;
        double dtime = time%(time/time);
        time -= dtime;
        dtime = (dtime*60)/100;
        time += dtime;
        time = ((int)(time*100))/100.0;
        double[] list = {cost, time};
        return list;
    }

    public static double[] calculateTrainCost(double distance){
        double cost = distance*0.25;
        double time = (distance/350)+0.5;
        double dtime = time%(time/time);
        time -= dtime;
        dtime = (dtime*60)/100;
        time += dtime;
        time = ((int)(time*100))/100.0;
        double[] list = {cost, time};
        return list;
    }
}