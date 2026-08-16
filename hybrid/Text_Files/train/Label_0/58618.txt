import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Arrays;
import java.io.IOException;
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
        Thread thread = new Thread(null, new TaskAdapter(), "", 1 << 29);
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
            EMsSolution solver = new EMsSolution();
            solver.solve(1, in, out);
            out.close();
        }
    }

    static class EMsSolution {
        Point[] pts;

        public void solve(int testNumber, FastInput in, FastOutput out) {
            int n = in.readInt();
            pts = new Point[n];

            for (int i = 0; i < n; i++) {
                pts[i] = new Point();
                pts[i].x = in.readInt();
                pts[i].y = in.readInt();
                pts[i].w = in.readInt();
            }
            Arrays.sort(pts, (a, b) -> Integer.compare(a.y, b.y));


            long[][] dp = new long[n][n + 1];
            long inf = (long) 1e18;


            long[] ans = new long[n + 1];
            Arrays.fill(ans, inf);
            for (int i = 0; i < 1 << n; i++) {
                for (int j = 0; j < n; j++) {
                    pts[j].minNow = Math.min(Math.abs(pts[j].x), Math.abs(pts[j].y));
                }


                for (int j = 0; j < n; j++) {
                    if (Bits.get(i, j) == 0) {
                        continue;
                    }
                    for (int k = 0; k < n; k++) {
                        pts[k].minNow = Math.min(pts[k].minNow, Math.abs(pts[k].x - pts[j].x));
                    }
                }
                long sum = 0;
                for (Point point : pts) {
                    sum += point.minNow * point.w;
                }
                int bitCount = Integer.bitCount(i);
                ans[bitCount] = Math.min(ans[bitCount], sum);

                //dp
                SequenceUtils.deepFill(dp, inf);
                for (int j = 0; j < n; j++) {
                    dp[j][1] = 0;
                    for (int k = 0; k <= j; k++) {
                        long cost = Math.min(pts[k].minNow, pts[j].y - pts[k].y);
                        dp[j][1] += cost * pts[k].w;
                    }

                    for (int t = 0; t < j; t++) {
                        //t + 1 to j
                        long cost = 0;
                        for (int k = t + 1; k <= j; k++) {
                            cost += Math.min(pts[k].minNow, Math.min(pts[j].y - pts[k].y, pts[k].y - pts[t].y)) * pts[k].w;
                        }
                        for (int k = 2; k <= n; k++) {
                            dp[j][k] = Math.min(dp[j][k], dp[t][k - 1] + cost);
                        }
                    }

                    //if it's the last one
                    long cost = 0;
                    for (int k = j + 1; k < n; k++) {
                        cost += Math.min(pts[k].minNow, pts[k].y - pts[j].y) * pts[k].w;
                    }
                    for (int k = 1; k + bitCount <= n; k++) {
                        ans[k + bitCount] = Math.min(ans[k + bitCount], cost + dp[j][k]);
                    }
                }
            }

            for (int i = 0; i <= n; i++) {
                out.println(ans[i]);
            }
        }

    }

    static class Bits {
        private Bits() {
        }

        public static int get(int x, int i) {
            return (x >>> i) & 1;
        }

    }

    static class Point {
        int x;
        int y;
        int minNow;
        long w;

    }

    static class FastOutput implements AutoCloseable, Closeable, Appendable {
        private StringBuilder cache = new StringBuilder(10 << 20);
        private final Writer os;

        public FastOutput append(CharSequence csq) {
            cache.append(csq);
            return this;
        }

        public FastOutput append(CharSequence csq, int start, int end) {
            cache.append(csq, start, end);
            return this;
        }

        public FastOutput(Writer os) {
            this.os = os;
        }

        public FastOutput(OutputStream os) {
            this(new OutputStreamWriter(os));
        }

        public FastOutput append(char c) {
            cache.append(c);
            return this;
        }

        public FastOutput append(long c) {
            cache.append(c);
            return this;
        }

        public FastOutput println(long c) {
            return append(c).println();
        }

        public FastOutput println() {
            cache.append(System.lineSeparator());
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
}

