import java.math.BigInteger;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;
public class MersennePrimeFinder{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("how many primes would you like generated? (max of 8 unless you want things to slow down) ");
        int nOfPrimes = input.nextInt();
        System.out.println(Arrays.toString(primeFinder(nOfPrimes)));
        input.close();
    }

    public static int p = 2;

    public static BigInteger[] primeFinder(int n){
        BigInteger[] primes = new BigInteger[n];
        for (int i = 0; i<n;){
            BigInteger nthPrime = BigInteger.TWO.pow(p).subtract(BigInteger.ONE);

            if (p<32 && checker(nthPrime)){
                primes[i] = nthPrime;
                i++;
                System.out.println(nthPrime.toString());

            }else if (mrtChecker(nthPrime) && lltChecker(nthPrime, p)){
                primes[i] = nthPrime;
                i++;
                System.out.println(nthPrime.toString());
            }

            p++;
        }
        return primes;
    }

    public static boolean checker(BigInteger number){
        BigInteger five = new BigInteger("5");
        if (number.mod(BigInteger.TWO).equals(BigInteger.ZERO) || number.mod(five).equals(BigInteger.ZERO)){
            return false;
        }
        for (BigInteger i = new BigInteger("3"); i.compareTo(number.divide(BigInteger.TWO))==-1; i.add(BigInteger.TWO)){
            if (number.mod(i).equals(BigInteger.ZERO)){
                return false;
            }
        }
        return true;
    }

    public static boolean lltChecker(BigInteger number, int p){
        BigInteger s = new BigInteger("4");
        for (int i = 0; i<p-2;i++){
            s=(s.multiply(s)).mod(number);
        }
        return s.equals(BigInteger.ZERO);
    }

    public static boolean mrtChecker(BigInteger number){
        Random random = new Random();
        long s=0;
        BigInteger d=number.subtract(BigInteger.ONE);
        while (d.mod(BigInteger.ONE).equals(BigInteger.ZERO)){
            d=d.divide(BigInteger.TWO);
            s++;
        }

        for (int k = 0; k<10;k++){
            BigInteger a=BigInteger.ZERO;
            while (a.compareTo(number.subtract(BigInteger.TWO))>0){
                a = new BigInteger(number.subtract(BigInteger.TWO).bitLength(), random);
                a.add(BigInteger.TWO);
            }
            BigInteger x=a.pow(d).mod(number);
            BigInteger y=BigInteger.ZERO;
            for(long i=0; i<s; i++){
                y = x.multiply(x).mod(number);
                if (y.equals(BigInteger.ONE) && !x.equals(BigInteger.ONE) && !x.equals(number.subtract(BigInteger.ONE))){
                    System.out.println("MRT returned false. first check. p value "+p);
                    return false;
                }
                x=y;
            }
            if (!y.equals(BigInteger.ONE)){
                System.out.println("MRT returned false. second check. p value "+p);
                return false;
            }
        }
        System.out.println("MRT returned true");
        return true;
    }
}
