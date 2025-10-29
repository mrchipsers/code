import java.util.Scanner;
public class test{
    public static void main(String[] args){
        System.out.println(test());
    }

    public static int test(){
        Scanner input = new Scanner(System.in);
        System.out.println("enter a 3 digit number: ");
        int num;
        try {
            while (true){
                num = input.nextInt();
                String numLen = ""+num;
                if (numLen.length()==3){
                    return num;
                } 
                System.out.println("the number is not 3 digits long. please try again: "); 
            }
            
        } catch (Exception e) {
            System.out.println("bad input. please try agin.");
            return test();
        }
    }
}