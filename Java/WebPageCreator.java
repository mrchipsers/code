import java.util.Scanner;
public class WebPageCreator{
    public static void main(String[] args) {
        createWebpage();
    }
    public static String surroundWithTag(String tag, String text){
        return "<"+tag+">"+text+"</"+tag+">";
    }
    public static String calculateAge(int age){
        int years = age/365;
        age = age%365;
        int months = age/30;
        age = age%30;
        return "I am "+years+" years, "+months+" months, and "+age+" days old";
    }
    public static String creatHead(String name){
        name = name+"'s website";
        String header = surroundWithTag("title", name);
        header = surroundWithTag("head", header);
        return header;
    }
    public static String createBody(String name, int age, String hobby){
        name = "welcome to "+name+"'s website";
        name = surroundWithTag("h1", name);
        String old = calculateAge(age);
        old = surroundWithTag("p", old);
        hobby = "my favourite hobby is "+hobby;
        hobby = surroundWithTag("p", hobby);
        String body = name+old+hobby;
        body = surroundWithTag("body", body);
        return body;
    }
    public static void createWebpage(){
        Scanner input = new Scanner(System.in);
        System.out.println("What is your name?");
        String name = input.next();
        System.out.println("What is your age in days?");
        int age = input.nextInt();
        System.out.println("What is your favourite hobby?");
        String hobby = input.next();
        String head = creatHead(name);
        String body = createBody(name, age, hobby);
        String html = head + body;
        html = surroundWithTag("html", html);
        System.out.println(html);
    }
}