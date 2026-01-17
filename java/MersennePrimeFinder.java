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
            if (p<32 && checker(nthPrime)){
                primes[i] = nthPrime;
                i++;
            }else if (lltChecker(nthPrime, p)){
                primes[i] = nthPrime;
                i++;
            }
            p++;
        }
        return primes;
    }

    public static boolean checker(long number){
        if (number%2==0 || number%5==0){
            return false;
        }
        for (long i = 3; i<=number/2; i+=2){
            if (number%i==0){
                return false;
            }
        }
        return true;
    }

    public static boolean lltChecker(long number, int p){
        long s = 4;
        for (int i = 0; i<p-2;i++){
            s=((s*s)-2)%number;
        }
        return s==0;
    }
}
