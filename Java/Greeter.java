import java.util.Scanner;
public class Greeter{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("what is your name?");
        String name = input.next();
        greet(name);
    }
    public static void greet(String name){
        System.out.println("Hi "+name+", nice to meet you.");
    }
}