import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.OutputStream;
import java.io.Writer;
import java.io.IOException;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author palayutm
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        ProblemGPartitions solver = new ProblemGPartitions();
        solver.solve(1, in, out);
        out.close();
    }

    static class ProblemGPartitions {
        final int mod = (int) 1e9 + 7;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.nextInt(), K = in.nextInt();
            long S = 0;
            for (int i = 0; i < n; i++) {
                S += in.nextInt();
            }
            S %= mod;
            Stirling stirling = new Stirling(K + 1, mod);
            out.println(S * (stirling.partitionNumber(n, K) + stirling.partitionNumber(n - 1, K) * (n - 1) % mod) % mod);
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] inbuf = new byte[1024];
        private int lenbuf = 0;
        private int ptrbuf = 0;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        private int readByte() {
            if (lenbuf == -1) throw new UnknownError();
            if (ptrbuf >= lenbuf) {
                ptrbuf = 0;
                try {
                    lenbuf = stream.read(inbuf);
                } catch (IOException e) {
                    throw new UnknownError();
                }
                if (lenbuf <= 0) return -1;
            }
            return inbuf[ptrbuf++];
        }

        public int nextInt() {
            int num = 0, b;
            boolean minus = false;
            while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
            if (b == '-') {
                minus = true;
                b = readByte();
            }

            while (true) {
                if (b >= '0' && b <= '9') {
                    num = num * 10 + (b - '0');
                } else {
                    return minus ? -num : num;
                }
                b = readByte();
            }
        }

    }

    static class OutputWriter extends PrintWriter {
        public OutputWriter(OutputStream out) {
            super(out);
        }

        public OutputWriter(Writer out) {
            super(out);
        }

        public void close() {
            super.close();
        }

    }

    static class BinomialMod {
        public long[] factorial;
        public long[] inv_factorial;
        private int md;

        public BinomialMod(int n, int mod) {
            this.md = mod;
            factorial = new long[n + 1];
            inv_factorial = IntegerUtils.preInverse(n, md);
            factorial[0] = inv_factorial[0] = 1;
            for (int i = 1; i <= n; i++) {
                factorial[i] = factorial[i - 1] * i % md;
                inv_factorial[i] = inv_factorial[i - 1] * inv_factorial[i] % md;
            }
        }

        public long choose(int n, int k) {
            if (k > n) return 0;
            return factorial[n] * inv_factorial[k] % md * inv_factorial[n - k] % md;
        }

    }

    static class Stirling {
        BinomialMod binomial;
        int mod;

        public Stirling(int n, int mod) {
            binomial = new BinomialMod(n, mod);
            this.mod = mod;
        }

        public long partitionNumber(int n, int k) {
            long ret = 0;
            for (int i = 0; i <= k; i++) {
                long v = binomial.choose(k, i) * IntegerUtils.powMod(i, n, mod) % mod;
                ret += ((k - i) % 2 == 1 ? -1 : 1) * v;
            }
            return ((ret % mod + mod) % mod * binomial.inv_factorial[k]) % mod;
        }

    }

    static class IntegerUtils {
        public static int powMod(long x, long y, int mod) {
            long ret = 1;
            x %= mod;
            for (; y > 0; y >>= 1, x = x * x % mod) {
                if ((y & 1) > 0) ret = ret * x % mod;
            }
            return (int) ret;
        }

        public static long[] preInverse(int n, int md) {
            long[] inv = new long[n + 1];
            inv[1] = 1;
            for (int i = 2; i <= n; ++i) {
                inv[i] = (md - md / i) * inv[md % i] % md;
            }
            return inv;
        }

    }
}

