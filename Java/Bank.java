import java.util.Scanner;
public class Bank{
    public static void main(String[] args){
       Scanner input = new Scanner(System.in);
       System.out.println("Please input the value of the cheque: ");
       double cheque = input.nextDouble();
       double charge = 0;
       input.close();
       if (cheque<10){
        charge = cheque*0.01;
       }else if (cheque<100){
        charge = cheque*0.1;
       }else if (cheque<1000){
        charge = (cheque*0.05)+5;
       }else if (cheque>1000){
        charge = (cheque*0.01)+40;
       }
       System.out.println("your cheque value is "+cheque+", and the service charge is "+charge);
    }
}