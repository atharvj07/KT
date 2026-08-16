
import java.util.Scanner;

public class Main {
    private static long fastPow(long base, long index, long mod) {
        long res = 1l, tmp = base;
        while (index > 0) {
            if ((index & 1l) == 1l)
                res = res * tmp % mod;
            tmp = tmp * tmp % mod;
            index >>= 1;
        }
        return res;
    }

    private static long moduloReverse(long num, long mod) {
        return fastPow(num, mod - 2l, mod);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long a = input.nextLong();
        long b = input.nextLong();
        long p = input.nextLong();
        long x = input.nextLong();
        
        long arev = moduloReverse(a, p);

        long ans = 0l;
        for (long q = 0l; q < p - 1 && q <= x; ++q) {
            long k0 = ((q - b * fastPow(arev, q, p) % p) % p + p) % p;
            long tmp = (x - q) / (p - 1);
            if (k0 <= tmp)
                ans += (tmp - k0) / p + 1;
        }

        System.out.println(ans);
        input.close();
    }
}
