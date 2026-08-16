import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Arrays;
import java.util.function.IntUnaryOperator;
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
            EConcatenationWithIntersection solver = new EConcatenationWithIntersection();
            solver.solve(1, in, out);
            out.close();
        }
    }

    static class EConcatenationWithIntersection {
        public void solve(int testNumber, FastInput in, FastOutput out) {
            int n = in.readInt();
            int m = in.readInt();
            char[] a = in.readString().toCharArray();
            char[] b = in.readString().toCharArray();
            char[] s = in.readString().toCharArray();

            int[] pre = new int[n];
            int[] suf = new int[n];

            ZAlgorithm pZ = new ZAlgorithm(m + n + 1, i -> {
                if (i < m) {
                    return s[i];
                }
                if (i == m) {
                    return '#';
                }
                return a[i - m - 1];
            });
            for (int i = 0; i < n; i++) {
                pre[i] = pZ.applyAsInt(i + m + 1);
            }

            ZAlgorithm sZ = new ZAlgorithm(m + n + 1, i -> {
                if (i < m) {
                    return s[m - 1 - i];
                }
                if (i == m) {
                    return '#';
                }
                return b[n - (i - m)];
            });
            for (int i = 0; i < n; i++) {
                suf[i] = sZ.applyAsInt((n - 1 - i) + m + 1);
            }

            Segment segtree = new Segment(0, m);
            int l = 0;
            int r = -1;
            long sum = 0;
            for (int i = 0; i < n; i++) {
                //limit - i + 1 < m => limit < m + i - 1
                int limit = Math.min(n - 1, m + i - 2);
                while (r < limit) {
                    r++;
                    segtree.update(m - suf[r], m - 1, 0, m, 1);
                }
                while (l < i) {
                    segtree.update(m - suf[l], m - 1, 0, m, -1);
                    l++;
                }
                if (pre[i] == 0) {
                    continue;
                }
                sum += segtree.query(1, pre[i], 0, m);
            }
            out.println(sum);
        }

    }

    static class Segment implements Cloneable {
        private Segment left;
        private Segment right;
        private long sum;
        private long dirty;
        private int size;

        public void pushUp() {
            size = left.size + right.size;
            sum = left.sum + right.sum;
        }

        private void modify(long x) {
            sum += x * size;
            dirty += x;
        }

        public void pushDown() {
            if (dirty != 0) {
                left.modify(dirty);
                right.modify(dirty);
                dirty = 0;
            }
        }

        public Segment(int l, int r) {
            if (l < r) {
                int m = (l + r) >> 1;
                left = new Segment(l, m);
                right = new Segment(m + 1, r);
                pushUp();
            } else {
                size = 1;
            }
        }

        private boolean covered(int ll, int rr, int l, int r) {
            return ll <= l && rr >= r;
        }

        private boolean noIntersection(int ll, int rr, int l, int r) {
            return ll > r || rr < l;
        }

        public void update(int ll, int rr, int l, int r, long x) {
            if (noIntersection(ll, rr, l, r)) {
                return;
            }
            if (covered(ll, rr, l, r)) {
                modify(x);
                return;
            }
            pushDown();
            int m = (l + r) >> 1;
            left.update(ll, rr, l, m, x);
            right.update(ll, rr, m + 1, r, x);
            pushUp();
        }

        public long query(int ll, int rr, int l, int r) {
            if (noIntersection(ll, rr, l, r)) {
                return 0;
            }
            if (covered(ll, rr, l, r)) {
                return sum;
            }
            pushDown();
            int m = (l + r) >> 1;
            return left.query(ll, rr, l, m) +
                    right.query(ll, rr, m + 1, r);
        }

        private Segment deepClone() {
            Segment seg = clone();
            if (seg.left != null) {
                seg.left = seg.left.deepClone();
            }
            if (seg.right != null) {
                seg.right = seg.right.deepClone();
            }
            return seg;
        }

        protected Segment clone() {
            try {
                return (Segment) super.clone();
            } catch (CloneNotSupportedException e) {
                throw new RuntimeException(e);
            }
        }

        private void toString(StringBuilder builder) {
            if (left == null && right == null) {
                builder.append("val").append(",");
                return;
            }
            pushDown();
            left.toString(builder);
            right.toString(builder);
        }

        public String toString() {
            StringBuilder builder = new StringBuilder();
            deepClone().toString(builder);
            if (builder.length() > 0) {
                builder.setLength(builder.length() - 1);
            }
            return builder.toString();
        }

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

        public FastOutput println(long c) {
            cache.append(c);
            println();
            return this;
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

    static class ZAlgorithm implements IntUnaryOperator {
        public int[] z;

        public ZAlgorithm(int n, IntUnaryOperator s) {
            if (n == 0) {
                return;
            }

            int l = 0;
            int r = -1;
            z = new int[n];
            z[0] = n;
            for (int i = 1; i < n; i++) {
                if (r < i) {
                    l = r = i;
                } else {
                    int t = i - l;
                    int k = r - i + 1;
                    if (z[t] < k) {
                        z[i] = z[t];
                        continue;
                    }
                    l = i;
                    r++;
                }
                while (r < n && s.applyAsInt(r - l) == s.applyAsInt(r)) {
                    r++;
                }
                r--;
                z[i] = r - l + 1;
            }
        }

        public int applyAsInt(int operand) {
            return z[operand];
        }

        public String toString() {
            return Arrays.toString(z);
        }

    }

    static class FastInput {
        private final InputStream is;
        private StringBuilder defaultStringBuf = new StringBuilder(1 << 13);
        private byte[] buf = new byte[1 << 20];
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

        public String readString(StringBuilder builder) {
            skipBlank();

            while (next > 32) {
                builder.append((char) next);
                next = read();
            }

            return builder.toString();
        }

        public String readString() {
            defaultStringBuf.setLength(0);
            return readString(defaultStringBuf);
        }

    }
}

