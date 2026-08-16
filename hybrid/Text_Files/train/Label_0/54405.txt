import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author warez80
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskA solver = new TaskA();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskA {
        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            int n = in.nextInt();
            int m = in.nextInt();
            long[] a = in.nextLongs(n);
            long[] b = in.nextLongs(m);
            long ans = Long.MAX_VALUE;
            for (int i = 0; i < n; ++i) {
                long x = Long.MIN_VALUE;
                for (int j = 0; j < n; ++j)
                    if (j != i) {
                        for (int k = 0; k < m; ++k) {
                            x = Math.max(x, a[j] * b[k]);
                        }
                    }
                ans = Math.min(ans, x);
            }
            out.println(ans);
        }

    }

    static class FastScanner {
        private byte[] buffer = new byte[1 << 10];
        private int bp;
        private int br;
        private InputStream is;
        private boolean empty;
        private boolean skipLF;

        public FastScanner(InputStream in) {
            is = in;
        }

        private byte r() {
            if (empty) throw new UnknownError();
            if (bp == br) try {
                br = is.read(buffer, bp = 0, 1 << 10);
                if (br == -1) buffer[0] = -1;
            } catch (Exception e) {
            }
            if (bp >= buffer.length || buffer[bp] == -1) {
                empty = true;
                return -1;
            }
            return buffer[bp++];
        }

        private byte rnw() {
            skipLF = false;
            byte c;
            do c = r(); while (c <= ' ');
            return c;
        }

        public int nextInt() {
            int ret = 0;
            byte c = rnw();
            boolean neg = c == '-';
            if (neg) c = r();
            do ret = (ret << 3) + (ret << 1) + c - '0'; while ((c = r()) >= '0' && c <= '9');
            if (neg) return -ret;
            return ret;
        }

        public long nextLong() {
            long ret = 0;
            byte c = rnw();
            boolean neg = c == '-';
            if (neg) c = r();
            do ret = (ret << 3) + (ret << 1) + c - '0'; while ((c = r()) >= '0' && c <= '9');
            if (neg) return -ret;
            return ret;
        }

        public long[] nextLongs(int count) {
            long[] xs = new long[count];
            for (int i = 0; i < count; i++) {
                xs[i] = nextLong();
            }
            return xs;
        }

    }
}

