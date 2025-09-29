public class TriangleMath{
    public static void main(String[] args){
        java.util.Scanner reader = new java.util.Scanner(System.in);
        
        System.out.println("Enter side a: ");
        double sideA = reader.nextDouble();
        System.out.println("Enter side b: ");
        double sideB = reader.nextDouble();
        System.out.println("Enter the angle between side a and b: ");
        double angle = reader.nextDouble();
        double perimeter = TriangleMath.computeTrianglePerimeter(sideA, sideB, angle);
        System.out.println("The perimeter is: " + perimeter);
        reader.close(); 
    }
        
    public static double computeTrianglePerimeter(double sideA, double sideB, double angle){
        angle = Math.toRadians(angle);
        double sideC = Math.sqrt(sideB*sideB + sideA*sideA - 2*sideA*sideB*Math.cos(angle));
        double perimeter = sideC+sideA+sideB;
        return perimeter;
    }
}