import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
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
            int q = in.readInt();
            int a = in.readInt();
            int b = in.readInt();
            int[] xs = new int[q + 1];
            for (int i = 1; i <= q; i++) {
                xs[i] = in.readInt();
            }
            xs[0] = a;
            Segment seg = new Segment(1, n);
            seg.update(b, b, 1, n, -seg.query(b, b, 1, n));

            for (int i = 1; i <= q; i++) {
                long left = seg.queryMinMinusIndex(1, xs[i], 1, n) + xs[i];
                long right = seg.queryMinPlusIndex(xs[i], n, 1, n) - xs[i];
                seg.update(1, n, 1, n, Math.abs(xs[i - 1] - xs[i]));

                long now = seg.query(xs[i - 1], xs[i - 1], 1, n);
                if (Math.min(left, right) < now) {
                    seg.update(xs[i - 1], xs[i - 1], 1, n,
                            Math.min(left, right) - now);
                }
            }

            long ans = Long.MAX_VALUE;
            for (int i = 1; i <= n; i++) {
                ans = Math.min(ans, seg.query(i, i, 1, n));
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

    static class Segment implements Cloneable {
        private Segment left;
        private Segment right;
        private long mod;
        private long val;
        private int index;
        private long minMinusIndex;
        private long minPlusIndex;

        public void mod(long m) {
            mod += m;
            val += m;
            minPlusIndex += m;
            minMinusIndex += m;
        }

        public void pushUp() {
            minMinusIndex = Math.min(left.minMinusIndex, right.minMinusIndex);
            minPlusIndex = Math.min(left.minPlusIndex, right.minPlusIndex);
            val = Math.min(left.val, right.val);
        }

        public void pushDown() {
            if (mod != 0) {
                left.mod(mod);
                right.mod(mod);
                mod = 0;
            }
        }

        public Segment(int l, int r) {
            if (l < r) {
                int m = (l + r) >> 1;
                left = new Segment(l, m);
                right = new Segment(m + 1, r);
                pushUp();
            } else {
                index = l;
                val = (long) 1e18;
                minMinusIndex = val - index;
                minPlusIndex = val + index;
            }
        }

        private boolean covered(int ll, int rr, int l, int r) {
            return ll <= l && rr >= r;
        }

        private boolean noIntersection(int ll, int rr, int l, int r) {
            return ll > r || rr < l;
        }

        public void update(int ll, int rr, int l, int r, long mod) {
            if (noIntersection(ll, rr, l, r)) {
                return;
            }
            if (covered(ll, rr, l, r)) {
                mod(mod);
                return;
            }
            pushDown();
            int m = (l + r) >> 1;
            left.update(ll, rr, l, m, mod);
            right.update(ll, rr, m + 1, r, mod);
            pushUp();
        }

        public long queryMinMinusIndex(int ll, int rr, int l, int r) {
            if (noIntersection(ll, rr, l, r)) {
                return Long.MAX_VALUE;
            }
            if (covered(ll, rr, l, r)) {
                return minMinusIndex;
            }
            pushDown();
            int m = (l + r) >> 1;
            return Math.min(left.queryMinMinusIndex(ll, rr, l, m),
                    right.queryMinMinusIndex(ll, rr, m + 1, r));
        }

        public long queryMinPlusIndex(int ll, int rr, int l, int r) {
            if (noIntersection(ll, rr, l, r)) {
                return Long.MAX_VALUE;
            }
            if (covered(ll, rr, l, r)) {
                return minPlusIndex;
            }
            pushDown();
            int m = (l + r) >> 1;
            return Math.min(left.queryMinPlusIndex(ll, rr, l, m),
                    right.queryMinPlusIndex(ll, rr, m + 1, r));
        }

        public long query(int ll, int rr, int l, int r) {
            if (noIntersection(ll, rr, l, r)) {
                return Long.MAX_VALUE;
            }
            if (covered(ll, rr, l, r)) {
                return val;
            }
            pushDown();
            int m = (l + r) >> 1;
            return Math.min(left.query(ll, rr, l, m),
                    right.query(ll, rr, m + 1, r));
        }

    }
}

