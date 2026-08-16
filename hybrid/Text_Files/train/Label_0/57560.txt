import java.math.BigDecimal;
import java.util.*;

public class Main {

    private static Scanner sc = new Scanner(System.in);

    private static final BigDecimal mod = new BigDecimal(1000000007);

    public static void main(String[] args) {

        int n = sc.nextInt();
        int m = sc.nextInt();

        PrimeFact p = new PrimeFact(m);

        System.out.println(ans(p, n));
    }

    private static long ans(PrimeFact p, int n) {
        BigDecimal ret = new BigDecimal(1);
        for (Map.Entry<Long, Integer> e : p.factorization.entrySet()) {
            ret = ret.multiply(
                    combination(n + e.getValue() - 1, e.getValue())
            );

            ret = ret.remainder(mod);
        }
        return ret.longValue();
    }

    public static BigDecimal combination(int a, int b) {
        BigDecimal ret = new BigDecimal(1);
        for (int i=a; i > a-b; i--) {
            ret = ret.multiply(new BigDecimal(i));
        }
        for (int i=1; i <= b; i++) {
            ret = ret.divide(new BigDecimal(i));
        }
        return ret;
    }

    public static class PrimeFact {
        private final Long orig;
        private LinkedHashMap<Long, Integer> factorization;

        public PrimeFact(long num) {
            orig = num;
            factorization = factorize(num);
        }

        public PrimeFact(int num) {
            orig = (long) num;
            factorization = factorize(num);
        }
    }

    private static LinkedHashMap<Long, Integer> factorize(long num) {

        LinkedHashMap<Long, Integer> fact;

        if (num == 1L) return new LinkedHashMap<>();

        long sqrt = (long) Math.floor(Math.sqrt(num));

        for (long p : getPrimes(sqrt)) {
            if (num % p == 0) {
                fact = factorize(num/p);
                if (fact.containsKey(p)) fact.put(p, fact.get(p) + 1);
                else fact.put(p, 1);
                return fact;
            }
        }

        fact = new LinkedHashMap<>();
        fact.put(num, 1);
        return fact;
    }

    private static LinkedList<Long> primes;

    static {
        primes = new LinkedList<>();
        primes.add(2L);
    }

    public static List<Long> getPrimes(long min) {

        if (primes.getLast() < min)
            genPrime(min);

        int index = 0;
        for (long p : primes) {
            if (p > min) break;
            index++;
        }

        return primes.subList(0, index);
    }

    private static void genPrime(long min) {
        for (long biggestKnown = primes.getLast() + 1; biggestKnown <= min; biggestKnown++) {
            if (isPrime(biggestKnown)) primes.add(biggestKnown);
        }
    }

    private static boolean isPrime(long num) {
        int sqrt = (int) Math.floor(Math.sqrt(num));

        for (long p : primes) {
            if (p > sqrt) break;
            if (num % p == 0) return false;
        }

        return true;
    }

}
