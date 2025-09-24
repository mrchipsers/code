import java.util.Scanner;
public class DayConverter{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("How many days?");
        int days = input.nextInt();
        int hours = daysToHours(days);
        int minutes = hoursToMinutes(hours);
        System.out.println(days+" days make "+minutes+" minutes");
        input.close();
    }
    public static int hoursToMinutes(int hours){
        return hours*60;
    }
    public static int daysToHours(int days){
        return days*24;
    }
}