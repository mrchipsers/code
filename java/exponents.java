public class exponents {
    public static void main(String[] args) {
        long base=2;
        long power=61;
        long result=base;
        for (int i = 0; i<power;i++){
            result*=base;
        }
        System.out.println(result);
    }
}
