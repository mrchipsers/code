import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;
public class MersennePrimeFinder{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("how many primes would you like generated? (max of 52 unless you want to be the proud owner of a position on a wikipedia page,\n max of 20 unless you want to be here forever) ");
        int nOfPrimes = input.nextInt();
        System.out.println(Arrays.toString(primeFinder(nOfPrimes)));
        input.close();
    }



    public static BigInteger[] primeFinder(int n){
        BigInteger[] primes = new BigInteger[n];
        int p = 2;
        for (int i = 0; i<n;){
            
            BigInteger nthPrime = BigInteger.TWO.pow(p).subtract(BigInteger.ONE);
            if (lltChecker(nthPrime, p)){
                primes[i]=nthPrime;
                i++;
                System.out.println(nthPrime.toString());
            }
            p++;
        }
        return primes;
    }

    public static boolean lltChecker(BigInteger number, int p){
        if (p==2){
            return true;
        }
        BigInteger s = new BigInteger("4");
        for (int i = 0; i<p-2;i++){
            s=s.multiply(s).subtract(BigInteger.TWO).mod(number);
        }
        return s.equals(BigInteger.ZERO);
    }
}
