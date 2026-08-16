import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Arrays;
import java.io.IOException;
import java.util.Random;
import java.io.UncheckedIOException;
import java.io.Closeable;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Thread thread = new Thread(null, new TaskAdapter(), "", 1 << 27);
        thread.start();
        thread.join();
    }

    static class TaskAdapter implements Runnable {
        @Override
        public void run() {
            InputStream inputStream = System.in;
            OutputStream outputStream = System.out;
            FastInput in = new FastInput(inputStream);
            FastOutput out = new FastOutput(outputStream);
            TaskF solver = new TaskF();
            solver.solve(1, in, out);
            out.close();
        }
    }

    static class TaskF {
        public void solve(int testNumber, FastInput in, FastOutput out) {
            int n = in.readInt();
            int k = in.readInt();
            int[] hs = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                hs[i] = in.readInt();
            }

            DiscreteMap dm = new DiscreteMap(hs.clone());
            for (int i = 0; i <= n; i++) {
                hs[i] = dm.rankOf(hs[i]);
            }

            int m = dm.maxRank();
            long[][][] dp = new long[n + 1][k + 1][m + 1];
            SequenceUtils.deepFill(dp, (long) 1e13);
            dp[0][0][0] = 0;
            long[][][] prefix = new long[n + 1][k + 1][m + 1];
            long[][][] suffix = new long[n + 1][k + 1][m + 1];
            for (int i = 0; i <= k; i++) {
                for (int j = 0; j <= m; j++) {
                    if (j == 0) {
                        prefix[0][i][j] = dp[0][i][j];
                    } else {
                        prefix[0][i][j] = Math.min(prefix[0][i][j - 1] + dm.iThElement(j) - dm.iThElement(j - 1), dp[0][i][j]);
                    }
                }

                for (int j = m; j >= 0; j--) {
                    if (j == m) {
                        suffix[0][i][j] = dp[0][i][j];
                    } else {
                        suffix[0][i][j] = Math.min(suffix[0][i][j + 1], dp[0][i][j]);
                    }
                }
            }
            for (int i = 1; i <= n; i++) {
                int h = hs[i];
                for (int j = 0; j <= k; j++) {
                    for (int t = 0; t <= m; t++) {
                        if (t != h) {
                            if (j > 0) {
                                dp[i][j][t] = Math.min(prefix[i - 1][j - 1][t], dp[i][j][t]);
                                dp[i][j][t] = Math.min(suffix[i - 1][j - 1][t], dp[i][j][t]);
                            } else {

                            }
                        } else {
                            dp[i][j][t] = Math.min(prefix[i - 1][j][t], dp[i][j][t]);
                            dp[i][j][t] = Math.min(suffix[i - 1][j][t], dp[i][j][t]);
                        }
                    }
                }

                for (int ii = 0; ii <= k; ii++) {
                    for (int jj = 0; jj <= m; jj++) {
                        if (jj == 0) {
                            prefix[i][ii][jj] = dp[i][ii][jj];
                        } else {
                            prefix[i][ii][jj] = Math.min(prefix[i][ii][jj - 1] + dm.iThElement(jj) - dm.iThElement(jj - 1), dp[i][ii][jj]);
                        }
                    }
                    for (int jj = m; jj >= 0; jj--) {
                        if (jj == m) {
                            suffix[i][ii][jj] = dp[i][ii][jj];
                        } else {
                            suffix[i][ii][jj] = Math.min(suffix[i][ii][jj + 1], dp[i][ii][jj]);
                        }
                    }


                }
            }

            long ans = (long) 1e18;
            for (int i = 0; i <= k; i++) {
                for (int j = 0; j <= m; j++) {
                    ans = Math.min(ans, dp[n][i][j]);
                }
            }

            out.println(ans);
        }

    }

    static class FastOutput implements AutoCloseable, Closeable {
        private StringBuilder cache = new StringBuilder(10 << 20);
        private final Writer os;

        public FastOutput(Writer os) {
            this.os = os;
        }

        public FastOutput(OutputStream os) {
            this(new OutputStreamWriter(os));
        }

        public FastOutput println(long c) {
            cache.append(c).append('\n');
            return this;
        }

        public FastOutput flush() {
            try {
                os.append(cache);
                os.flush();
                cache.setLength(0);
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
            return this;
        }

        public void close() {
            flush();
            try {
                os.close();
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }

        public String toString() {
            return cache.toString();
        }

    }

    static class Randomized {
        static Random random = new Random();

        public static void randomizedArray(int[] data, int from, int to) {
            to--;
            for (int i = from; i <= to; i++) {
                int s = nextInt(i, to);
                int tmp = data[i];
                data[i] = data[s];
                data[s] = tmp;
            }
        }

        public static int nextInt(int l, int r) {
            return random.nextInt(r - l + 1) + l;
        }

    }

    static class DiscreteMap {
        int[] val;
        int f;
        int t;

        public DiscreteMap(int[] val) {
            this(val, 0, val.length);
        }

        public DiscreteMap(int[] val, int f, int t) {
            Randomized.randomizedArray(val, f, t);
            Arrays.sort(val, f, t);
            int wpos = f + 1;
            for (int i = f + 1; i < t; i++) {
                if (val[i] == val[i - 1]) {
                    continue;
                }
                val[wpos++] = val[i];
            }
            this.val = val;
            this.f = f;
            this.t = wpos;
        }

        public int rankOf(int x) {
            return Arrays.binarySearch(val, f, t, x) - f;
        }

        public int iThElement(int i) {
            return val[f + i];
        }

        public int maxRank() {
            return t - f - 1;
        }

        public String toString() {
            return Arrays.toString(Arrays.copyOfRange(val, f, t));
        }

    }

    static class FastInput {
        private final InputStream is;
        private byte[] buf = new byte[1 << 13];
        private int bufLen;
        private int bufOffset;
        private int next;

        public FastInput(InputStream is) {
            this.is = is;
        }

        private int read() {
            while (bufLen == bufOffset) {
                bufOffset = 0;
                try {
                    bufLen = is.read(buf);
                } catch (IOException e) {
                    bufLen = -1;
                }
                if (bufLen == -1) {
                    return -1;
                }
            }
            return buf[bufOffset++];
        }

        public void skipBlank() {
            while (next >= 0 && next <= 32) {
                next = read();
            }
        }

        public int readInt() {
            int sign = 1;

            skipBlank();
            if (next == '+' || next == '-') {
                sign = next == '+' ? 1 : -1;
                next = read();
            }

            int val = 0;
            if (sign == 1) {
                while (next >= '0' && next <= '9') {
                    val = val * 10 + next - '0';
                    next = read();
                }
            } else {
                while (next >= '0' && next <= '9') {
                    val = val * 10 - next + '0';
                    next = read();
                }
            }

            return val;
        }

    }

    static class SequenceUtils {
        public static void deepFill(Object array, long val) {
            if (!array.getClass().isArray()) {
                throw new IllegalArgumentException();
            }
            if (array instanceof long[]) {
                long[] longArray = (long[]) array;
                Arrays.fill(longArray, val);
            } else {
                Object[] objArray = (Object[]) array;
                for (Object obj : objArray) {
                    deepFill(obj, val);
                }
            }
        }

    }
}

