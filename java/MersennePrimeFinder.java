import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;
/*program to generate and test possible primes using the Mersenne equation (2^(p)-1). 
if the number is prime it is printed and added to an array to printed at completion.
this program uses the Lucas-Lehmer test to determine priminality. (https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test)*/
public class MersennePrimeFinder{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("how many primes would you like generated? (max of 52 unless you want to be the proud owner of a position on a wikipedia page, max of 20 unless you want to be here forever) ");
        int nOfPrimes = input.nextInt();
        input.close();
        System.out.println(Arrays.toString(primeFinder(nOfPrimes)));
    }

    public static BigInteger[] primeFinder(int nOfPrimes){
        BigInteger[] primes = new BigInteger[nOfPrimes];
        int p = 2;
        for (int i = 0; i<nOfPrimes; p++){
            BigInteger possiblePrime = BigInteger.TWO.pow(p).subtract(BigInteger.ONE);
            if (lltChecker(possiblePrime, p)){
                primes[i]=possiblePrime;
                i++;
                System.out.println(possiblePrime.toString());
            }
        }
        return primes;
    }

    public static boolean lltChecker(BigInteger possiblePrime, int p){
        if (p==2){
            return true;
        }
        BigInteger s = new BigInteger("4");
        for (int i = 0; i<p-2;i++){
            s=s.multiply(s).subtract(BigInteger.TWO).mod(possiblePrime);
        }
        return s.equals(BigInteger.ZERO);
    }
}
