
public class ChangeGiver{
    public static void main(String[]args){
        java.util.Scanner reader = new java.util.Scanner(System.in);
        
        System.out.println("Please input your change");
        
        float change = (reader.nextFloat())*100; // ex 545 (5.45$), or 4056 (40.56$)
        
        if (change<0) {
            change *= -1;  
        }
        
        int ichange = (int) change;
        // ichange = ichange - twoonies*200  --->  ichange = ichange % 200
        
        int twenty = ichange/2000;
        ichange = ichange % 2000;
        
        int ten = ichange/1000;
        ichange = ichange % 1000;
        
        int five = ichange/500;
        ichange = ichange % 500;
        
        int twoonies = ichange/200; // 545 / 200 = 2
        ichange = ichange % 200;
        
        int loonies = ichange/100;
        ichange = ichange % 100;
        
        int quarters = ichange/25;
        ichange = ichange % 25;
        
        int dimes = ichange/10;
        ichange = ichange % 10;
        
        int nickels = ichange/5;
        ichange = ichange % 5;
        
        int pennies = ichange;
        ichange = ichange % 1;
        
        System.out.println("Twenty dollar bills: " + twenty + 
        " Ten dollar bills: " + ten + 
        " Five dollar bills: " + five +
        " Twoonies: " + twoonies +
        " Loonies: " + loonies +
        " Quarters: " + quarters +
        " Dimes: " + dimes +
        " Nickels: " + nickels +
        " Pennies: " + pennies);
    }
}