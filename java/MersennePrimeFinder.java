import java.util.Arrays;
import java.util.Scanner;
public class MersennePrimeFinder{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("how many primes would you like generated? (max of 8 unless you want things to slow down) ");
        int nOfPrimes = input.nextInt();
        System.out.println(Arrays.toString(primeFinder(nOfPrimes)));
        input.close();
    }

    public static long[] primeFinder(int n){
        long[] primes = new long[n];
        int p = 2;
        for (int i = 0; i<n;){
            long nthPrime = (long)Math.pow(2,p)-1;
            if (checker(nthPrime)){
                primes[i] = nthPrime;
                i++;
            }
            p++;
        }
        return primes;
    }

    public static boolean checker(long number){
        for (long i = 3; i<number; i++){
            if (number%i==0){
                return false;
            }
        }
        return true;
    }
}
