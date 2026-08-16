import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Pradyumn
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastReader in = new FastReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskE solver = new TaskE();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskE {
        static final int MODULO = (int) (1e6 + 3);

        public void solve(int testNumber, FastReader in, PrintWriter out) {
            Debug debug = new Debug(out);
            long n = in.nextLong();
            long K = in.nextLong();
            if (n < 64 && 1L << n < K) {
                out.println("1 1");
                return;
            }
            long commonPower = 0;
            for (long i = 1; i < 64; ++i)
                commonPower += (K - 1) / (1L << i);

            long _2n = powerMod(2, n);
            long gcd = powerMod(powerMod(2, commonPower), MODULO - 2);
            long den = powerMod(_2n, K - 1) * gcd % MODULO;

            long num = 0;
            if (K - 1 < MODULO) {
                num = 1;
                for (int i = 1; i < K; ++i) {
                    num = num * (_2n - i + MODULO) % MODULO;
                }
                num = num * gcd % MODULO;
            }
            out.println((den - num + MODULO) % MODULO + " " + den);
        }

        public static long powerMod(long a, long n) {
            a %= MODULO;
            long ret = 1;
            int x = 63 - Long.numberOfLeadingZeros(n);
            for (; x >= 0; --x) {
                ret = ret * ret % MODULO;
                if (n << ~x < 0) ret = ret * a % MODULO;
            }
            return ret;
        }

    }

    static class Debug {
        PrintWriter out;
        boolean oj;
        long timeBegin;
        Runtime runtime;

        public Debug(PrintWriter out) {
            oj = System.getProperty("ONLINE_JUDGE") != null;
            this.out = out;
            this.timeBegin = System.currentTimeMillis();
            this.runtime = Runtime.getRuntime();
        }

    }

    static class FastReader {
        private InputStream stream;
        private byte[] buf = new byte[8192];
        private int curChar;
        private int pnumChars;

        public FastReader(InputStream stream) {
            this.stream = stream;
        }

        private int pread() {
            if (pnumChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= pnumChars) {
                curChar = 0;
                try {
                    pnumChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (pnumChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }

        public long nextLong() {
            int c = pread();
            while (isSpaceChar(c))
                c = pread();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = pread();
            }
            long res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = pread();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        private boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

    }
}

