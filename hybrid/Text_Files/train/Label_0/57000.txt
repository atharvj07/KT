import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.FilterInputStream;
import java.io.BufferedInputStream;
import java.io.InputStream;

/**
 * @author khokharnikunj8
 */

public class Main {
    public static void main(String[] args) {
        new Thread(null, new Runnable() {
            public void run() {
                new Main().solve();
            }
        }, "1", 1 << 26).start();
    }

    void solve() {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        ScanReader in = new ScanReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        DNumbers solver = new DNumbers();
        solver.solve(1, in, out);
        out.close();
    }

    static class DNumbers {
        int[] primes;
        int a;
        int b;
        int k;
        long ans;

        public void dfs(long val, int current, boolean sign) {
            if (val > b) return;
            if (sign) ans += ((b / val) - (a - 1) / val);
            else ans -= ((b / val) - (a - 1) / val);
            while (current < primes.length) {
                dfs(val * primes[current], current + 1, sign ^ true);
                current++;
            }
        }

        public void solve(int testNumber, ScanReader in, PrintWriter out) {
            a = in.scanInt();
            b = in.scanInt();
            k = in.scanInt();
            if (!CodeHash.isPrime(k)) {
                out.println(0);
                return;
            }
            if (k >= 45000) {
                long min = ((a - 1) / k + 1) * k;
                ans = 0;
                while (min <= b) {
                    boolean flag = true;
                    for (int i = 2; i * i <= min && flag; i++) {
                        if (min % i == 0) {
                            if (i < k || min / i < k) flag = false;
                        }
                    }
                    if (flag) ans++;
                    min += k;
                }
                out.println(ans);
            } else {
                primes = CodeHash.sieveEratosthenes(k - 1);
                dfs(k, 0, true);
                out.println(ans);
            }
        }

    }

    static class CodeHash {
        public static int[] sieveEratosthenes(int n) {
            if (n <= 32) {
                int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
                for (int i = 0; i < primes.length; i++) {
                    if (n < primes[i]) {
                        return Arrays.copyOf(primes, i);
                    }
                }
                return primes;
            }

            int u = n + 32;
            double lu = Math.log(u);
            int[] ret = new int[(int) (u / lu + u / lu / lu * 1.5)];
            ret[0] = 2;
            int pos = 1;

            int[] isp = new int[(n + 1) / 32 / 2 + 1];
            int sup = (n + 1) / 32 / 2 + 1;

            int[] tprimes = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
            for (int tp : tprimes) {
                ret[pos++] = tp;
                int[] ptn = new int[tp];
                for (int i = (tp - 3) / 2; i < tp << 5; i += tp)
                    ptn[i >> 5] |= 1 << (i & 31);
                for (int i = 0; i < tp; i++) {
                    for (int j = i; j < sup; j += tp)
                        isp[j] |= ptn[i];
                }
            }

            // 3,5,7
            // 2x+3=n
            int[] magic = {0, 1, 23, 2, 29, 24, 19, 3, 30, 27, 25, 11, 20, 8, 4,
                    13, 31, 22, 28, 18, 26, 10, 7, 12, 21, 17, 9, 6, 16, 5, 15, 14};
            int h = n / 2;
            for (int i = 0; i < sup; i++) {
                for (int j = ~isp[i]; j != 0; j &= j - 1) {
                    int pp = i << 5 | magic[(j & -j) * 0x076be629 >>> 27];
                    int p = 2 * pp + 3;
                    if (p > n)
                        break;
                    ret[pos++] = p;
                    for (int q = pp; q <= h; q += p)
                        isp[q >> 5] |= 1 << (q & 31);
                }
            }

            return Arrays.copyOf(ret, pos);
        }

        public static boolean isPrime(long n) {
            if (n < 2) return false;
            if (n == 2 || n == 3) return true;
            if (n % 2 == 0 || n % 3 == 0) return false;
            long sqrtN = (long) Math.sqrt(n) + 1;
            for (long i = 6L; i <= sqrtN; i += 6) {
                if (n % (i - 1) == 0 || n % (i + 1) == 0) return false;
            }
            return true;
        }

    }

    static class ScanReader {
        private byte[] buf = new byte[4 * 1024];
        private int index;
        private BufferedInputStream in;
        private int total;

        public ScanReader(InputStream inputStream) {
            in = new BufferedInputStream(inputStream);
        }

        private int scan() {
            if (index >= total) {
                index = 0;
                try {
                    total = in.read(buf);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                if (total <= 0) return -1;
            }
            return buf[index++];
        }

        public int scanInt() {
            int integer = 0;
            int n = scan();
            while (isWhiteSpace(n)) n = scan();
            int neg = 1;
            if (n == '-') {
                neg = -1;
                n = scan();
            }
            while (!isWhiteSpace(n)) {
                if (n >= '0' && n <= '9') {
                    integer *= 10;
                    integer += n - '0';
                    n = scan();
                }
            }
            return neg * integer;
        }

        private boolean isWhiteSpace(int n) {
            if (n == ' ' || n == '\n' || n == '\r' || n == '\t' || n == -1) return true;
            else return false;
        }

    }
}

