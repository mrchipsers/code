public class TrianglePrinter{
    public static void main(String[] args){
        for(int i = 0; i<5; i++){//calls printTriangle() 5 times
            printTriangle();
        }
        }
    public static void printTriangle(){//method to print the triangle
        System.out.println("*");
        System.out.println("***");
        System.out.println("*****");//the prints
    }
}