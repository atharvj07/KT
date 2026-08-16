import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    private static final long m = (int) 1e9 + 7;

    public static void main(String args[]) {
        try (Scanner in = new Scanner(System.in)) {
            int n = in.nextInt();

            int[] a = new int[n + 1];
            int[] count = new int[n + 1];
            int index2 = -1;
            int value = -1;
            for (int i = 0; i < a.length; i++) {
                a[i] = in.nextInt();
                count[a[i]]++;
                if (count[a[i]] > 1) {
                    index2 = i;
                    value = a[i];
                }
            }

            int index1 = -1;
            for (int i = 0; i < index2; i++) {
                if (a[i] == value) {
                    index1 = i;
                }
            }

            // Utils.debug("value", value, "index1", index1, "index2", index2);

            StringBuilder res = new StringBuilder();
            for (int k = 1; k <= n + 1; k++) {
                // modC(index1, k, m);
                // modC(index2 - index1 - 1, k, m);
                // Utils.debug("modC(" + n + ", " + k + ", m)", modC(n, k, m));
                // Utils.debug(k, modComb((n + 1), k, m) - modComb((index1) + (n + 1 - (index2 + 1)), k - 1, m));
                // Utils.debug(k, modComb((n + 1), k, m) - modComb((n + 1) - (index2 - index1 + 1), k - 1, m));
                // Utils.debug(k, modComb((n + 1), k, m), modComb((n + 1) - (index2 - index1 + 1), k - 1, m));
                // System.out.println((modComb((n + 1), k, m) - modComb((n + 1) - (index2 - index1 + 1), k - 1, m) + m) % m);
                res.append(((modComb((n + 1), k, m) - modComb((n + 1) - (index2 - index1 + 1), k - 1, m) + m) % m) + "\n");
            }

            System.out.println(res.toString());
        }
    }

    // p119
    public static final int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    // p120
    public static final int extgcd(int a, int b, int[] x, int[] y) {
        int d = a;
        if (b != 0) {
            d = extgcd(b, a % b, y, x);
            y[0] -= (a / b) * x[0];
        } else {
            x[0] = 1;
            y[0] = 0;
        }
        return d;
    }

    public static final long extgcd(long a, long b, long[] x, long[] y) {
        long d = a;
        if (b != 0) {
            d = extgcd(b, a % b, y, x);
            y[0] -= (a / b) * x[0];
        } else {
            x[0] = 1;
            y[0] = 0;
        }
        return d;
    }

    // p122
    /** 素数判定O(n^(1/2)) */
    public static final boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return n != 1;
    }

    public static final boolean isPrime(long n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return n != 1;
    }

    /** 約数の列挙O(n^(1/2)) */
    public static final ArrayList<Integer> divisor(int n) {
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                res.add(i);
                if (n / i != i) {
                    res.add(n / i);
                }
            }
        }
        return res;
    }

    /** 素因数分解O(n^(1/2)) */
    public static final Map<Integer, Integer> primeFactor(int n) {
        HashMap<Integer, Integer> res = new HashMap<>();
        for (int i = 2; i * i <= n; i++) {
            while (n % i == 0) {
                int count = res.get(i) == null ? 0 : res.get(i).intValue();
                res.put(i, count + 1);
                n /= i;
            }
        }
        if (n != 1) {
            int count = res.get(n) == null ? 0 : res.get(n).intValue();
            res.put(n, count + 1);
        }
        return res;
    }

    // p123
    private static final int MAX_N = (int) 1e5;
    /** i 番目の素数 */
    private static final int[] prime = new int[MAX_N];
    /** isPrime[i] が true なら i は素数 */
    private static final boolean[] isPrime = new boolean[MAX_N + 1];

    /** n以下の素数の数を返す */
    public static final int sieve(int n) {
        int p = 0;
        for (int i = 0; i <= n; i++) {
            isPrime[i] = true;
        }
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                prime[p++] = i;
                for (int j = 2 * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        return p;
    }

    public static final long modAdd(long a, long b, long modulo) {
        a %= modulo;
        b %= modulo;
        return (a + b) % modulo;
    }

    public static final long modSubtract(long a, long b, long modulo) {
        a %= modulo;
        b %= modulo;
        return (a - b + modulo) % modulo;
    }

    public static final long modMultiply(long a, long b, long modulo) {
        a %= modulo;
        b %= modulo;
        return (a * b) % modulo;
    }

    // p126
    public static final int modPow(long x, int n, int modulo) {
        long res = 1;
        while (n > 0) {
            if ((n & 1) != 0) {
                res = res * x % modulo;
            }
            x = x * x % modulo;
            n >>= 1;
        }
        return (int) res;
    }

    public static final long modPow(long x, long n, long modulo) {
        long res = 1L;
        while (n > 0) {
            if ((n & 1L) != 0) {
                res = res * x % modulo;
            }
            x = x * x % modulo;
            n >>= 1;
        }
        return res;
    }

    // p127
    public static final long modPow2(long x, long n, long modulo) {
        if (n == 0) {
            return 1L;
        }
        long res = modPow2(x * x % modulo, n / 2, modulo);
        if ((n & 1L) != 0) {
            res = res * x % modulo;
        }
        return res;
    }

    // p242
    public static final int modInverse(int a, int modulo) {
        int[] x = new int[1];
        int[] y = new int[1];
        int gcd = extgcd(a, modulo, x, y);
        assert gcd == 1;
        return (modulo + x[0] % modulo) % modulo;
    }

    public static final long modInverse(long a, long modulo) {
        long[] x = new long[1];
        long[] y = new long[1];
        long gcd = extgcd(a, modulo, x, y);
        assert gcd == 1;
        return (modulo + x[0] % modulo) % modulo;
    }

    // p242
    // By Fermat's little theorem
    private static int modInverseByFermatsLittleTheorem(int x, int modulo) {
        if (!isPrime(modulo)) {
            throw new IllegalArgumentException("modulo is not prime.");
        }
        return modPow(x, modulo - 2, modulo);
    }

    private static long modInverseByFermatsLittleTheorem(long x, long modulo) {
        // if (!isPrime(modulo)) {
        // throw new IllegalArgumentException("modulo is not prime.");
        // }
        return modPow(x, modulo - 2, modulo);
    }

    // p245
    private static final int MAX_P = (int) 1e5 + 2;
    private static final long[] fact = new long[MAX_P];
    private static final boolean[] first = new boolean[] { true, };

    // public static final int modFact(int n, int p, int[] e) {
    // if (first[0]) {
    // first[0] = false;
    // fact[0] = 1;
    // for (int i = 1; i < fact.length; i++) {
    // // fact[i] = i * fact[i - 1] % p;
    // fact[i] = modFact(i, p, e);
    // }
    // }
    //
    // e[0] = 0;
    // if (n == 0) {
    // return 1;
    // }
    //
    // int res = modFact(n / p, p, e);
    // e[0] += n / p;
    //
    // if (n / p % 2 == 0) {
    // return res * (p - fact[n % p]) % p;
    // // return res * (p - modFact(n % p, p, new int[1])) % p;
    // }
    //
    // return res * fact[n % p] % p;
    // // return res * modFact(n % p, p, new int[1]) % p;
    // }

    public static final long modFact(long n, long p, long[] e) {
        if (first[0]) {
            first[0] = false;
            fact[0] = 1;
            for (int i = 1; i < fact.length; i++) {
                // fact[i] = (int) modFact(i, p, e);
                fact[i] = (int) ((i * fact[i - 1]) % p);
            }
        }

        e[0] = 0;
        if (n == 0) {
            Utils.debug("modFact(long " + n + ", long " + p + ", long[] " + e[0] + ") = " + 1);
            return 1;
        }

        long res = modFact(n / p, p, e);
        e[0] += n / p;

        if ((n / p) % 2 != 0) {
            Utils.debug("modFact(long " + n + ", long " + p + ", long[] " + e[0] + ") = " + (res * (p - fact[(int) (n % p)]) % p));
            return res * (p - fact[(int) (n % p)]) % p;
            // return res * (p - modFact(n % p, p, new long[1])) % p;
        }

        Utils.debug("modFact(long " + n + ", long " + p + ", long[] " + e[0] + ") = " + (res * fact[(int) (n % p)] % p));
        return res * fact[(int) (n % p)] % p;
        // return res * modFact(n % p, p, new long[1]) % p;
    }

    // p245
    // public static final int modComb(int n, int k, int p) {
    // if (n < 0 || k < 0 || n < k) {
    // return 0;
    // }
    // int[] e1 = new int[1];
    // int[] e2 = new int[1];
    // int[] e3 = new int[1];
    // int a1 = modFact(n, p, e1);
    // int a2 = modFact(k, p, e2);
    // int a3 = modFact(n - k, p, e3);
    // if (e1[0] > e2[0] + e3[0]) {
    // return 0;
    // }
    // return a1 * modInverseByFermatsLittleTheorem(a2 * a3 % p, p) % p;
    // }

    public static final long modComb(long n, long k, long p) {
        if (n < 0 || k < 0 || n < k) {
            Utils.debug("modComb(long " + n + ", long " + k + ", long " + p + ") = " + 0);
            return 0;
        }
        long[] e1 = new long[1];
        long[] e2 = new long[1];
        long[] e3 = new long[1];
        long a1 = modFact(n, p, e1);
        long a2 = modFact(k, p, e2);
        long a3 = modFact(n - k, p, e3);
        if (e1[0] > e2[0] + e3[0]) {
            Utils.debug("modComb(long " + n + ", long " + k + ", long " + p + ") = " + 0);
            return 0;
        }
        Utils.debug("modComb(long " + n + ", long " + k + ", long " + p + ") = " + "" + a1 + " / (" + a2 + "*" + a3 + ")" + " = " + ((a1 * modInverseByFermatsLittleTheorem((a2 * a3) % p, p)) % p));
        return (a1 * modInverseByFermatsLittleTheorem((a2 * a3) % p, p)) % p;
    }
}

final class Utils {
    private Utils() {
    }

    public static final void debug(Object... o) {
        // System.err.println(toString(o));
    }

    public static final String toString(Object... o) {
        return Arrays.deepToString(o);
    }

}
