import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        long a1;
        long a2;
        long d1;
        long d2;
        long L;
        long R;

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            a1 = in.nextLong();
            d1 = in.nextLong();
            a2 = in.nextLong();
            d2 = in.nextLong();
            L = in.nextLong();
            R = in.nextLong();


            if (d1 < d2) {
                long tmp = d2;
                d2 = d1;
                d1 = tmp;
                tmp = a2;
                a2 = a1;
                a1 = tmp;
            }

            long ans = bruteForce();
            if (ans == -1) {
                Pair solnPair = getAPairOfSoln(a1, a2, d1 - d2);
                ans = numOfSoln(a1, a2, d1, d2, solnPair);
            }
            out.print(ans);
            out.flush();
        }

        private long bruteForce() {
            long BF_THRES = 1000 * 1000;
            if (a1 < BF_THRES && a2 < BF_THRES) {
                return -1;
            }

            long A1 = d1, D1 = a1, A2 = d2, D2 = a2;
            if (D1 < D2) {
                A1 = d2;
                D1 = a2;
                A2 = d1;
                D2 = a1;
            }

            long num = A1, ans = 0;
            while (num <= R) {
                if (num >= L && num <= R && num >= A2 && (num - A2) % D2 == 0) {
                    ans++;
                }
                num += D1;
            }

            return ans;
        }

        private long numOfSoln(long a1, long a2, long d1, long d2, Pair solnPair) {
            if (solnPair == null) {
                return 0;
            }

            long _gcd = __gcd(a1, a2);
            long num = a1 * solnPair.x + d1;
            long period = (1L * a1 * a2) / _gcd;
            long D = Math.max(d1, d2);

            long afterD = getNextIntAfter(num, period, D);
            long afterL = getNextIntAfter(num, period, L);
            long afterR = getNextIntAfter(num, period, R + 1);

            afterL = Math.max(afterL, afterD);
            long ans = (afterR - afterL) / period;

            return Math.max(0, ans);
        }

        private long getNextIntAfter(long num, long period, long x) {
            long toAdd = (num - x) % period;
            if (toAdd < 0)
                toAdd += period;

            return x + toAdd;
        }

        private Pair getAPairOfSoln(long a1, long a2, long delta) {
            long _gcd = __gcd(a1, a2);
            if (delta % _gcd != 0) {
                return null;
            }

            a1 /= _gcd;
            a2 /= _gcd;
            delta /= _gcd;
            if (a2 == 1) {
                return new Pair(1, a1 + delta);
            } else if (a1 == 1) {
                return new Pair(a2 - delta, 1);
            }

            Pair returnPair = null;
            if (a1 > a2) {
                returnPair = getAPairOfSoln(a1 % a2, a2, delta);
                returnPair.change(0, a1 / a2);
            } else if (a2 > a1) {
                returnPair = getAPairOfSoln(a1, a2 % a1, delta);
                returnPair.change(a2 / a1, 0);
            }

            return returnPair;
        }

        private long __gcd(long a, long b) {
            return b == 0 ? a : __gcd(b, a % b);
        }

        public class Pair {
            long x;
            long y;

            Pair(long x, long y) {
                this.x = x;
                this.y = y;
            }

            void change(long x, long y) {
                this.x += x * this.y;
                this.y += y * this.x;
            }

        }

    }

    static class InputReader {
        private BufferedReader in;
        private StringTokenizer st;

        public InputReader(InputStream stream) {
            in = new BufferedReader(new InputStreamReader(stream));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    String rl = in.readLine();
                    if (rl == null) {
                        return null;
                    }
                    st = new StringTokenizer(rl);
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

    }
}

