import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Arrays;
import java.util.function.LongBinaryOperator;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UncheckedIOException;
import java.nio.charset.Charset;
import java.util.StringTokenizer;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author mikit
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        LightScanner in = new LightScanner(inputStream);
        LightWriter out = new LightWriter(outputStream);
        FCapture solver = new FCapture();
        solver.solve(1, in, out);
        out.close();
    }

    static class FCapture {
        public void solve(int testNumber, LightScanner in, LightWriter out) {
            // out.setBoolLabel(LightWriter.BoolLabel.YES_NO_FIRST_UP);
            int n = in.ints();
            long[] x = new long[n], s = new long[n];
            for (int i = 0; i < n; i++) {
                x[i] = in.longs();
                s[i] = in.longs();
            }
            IntLazySegmentTree st = new IntLazySegmentTree(new long[n], Long::max, 0, Long::sum, Long::sum, 0);
            long ans = 0, last = x[0];
            for (int i = 0; i < n; i++) {
                st.update(0, i + 1, s[i]);
                st.update(0, i, last - x[i]);
                last = x[i];
                ans = Math.max(ans, st.query(0, i + 1));
            }
            out.ans(ans).ln();
        }

    }

    static class IntLazySegmentTree {
        private final int n;
        private final int m;
        private final long[] tree;
        private final long[] lazy;
        private final LongBinaryOperator op;
        private final long zero;
        private final LongBinaryOperator up;
        private final LongBinaryOperator merge;
        private final long nop;
        private final LongIntToLongFunction mul;

        public IntLazySegmentTree(long[] array, LongBinaryOperator op, long zero, LongBinaryOperator up,
                                  LongBinaryOperator merge, long nop,
                                  LongIntToLongFunction mul) {
            this.n = array.length;
            int msb = BitMath.extractMsb(n);
            this.m = n == msb ? msb : (msb << 1);
            this.op = op;
            this.zero = zero;
            this.up = up;
            this.merge = merge;
            this.nop = nop;
            this.mul = mul;
            this.tree = new long[m * 2 - 1];
            Arrays.fill(tree, zero);
            System.arraycopy(array, 0, this.tree, m - 1, array.length);
            this.lazy = new long[m * 2 - 1];
            Arrays.fill(lazy, nop);
            for (int i = m - 2; i >= 0; i--) {
                tree[i] = op.applyAsLong(tree[2 * i + 1], tree[2 * i + 2]);
            }
        }

        public IntLazySegmentTree(long[] array, LongBinaryOperator op, long zero, LongBinaryOperator up,
                                  LongBinaryOperator merge, long nop) {
            this(array, op, zero, up, merge, nop, (q, n) -> q);
        }

        private void eval(int len, int k) {
            if (lazy[k] == nop) {
                return;
            } else if (k * 2 + 1 < m * 2 - 1) {
                lazy[k * 2 + 1] = merge.applyAsLong(lazy[k * 2 + 1], lazy[k]);
                lazy[k * 2 + 2] = merge.applyAsLong(lazy[k * 2 + 2], lazy[k]);
            }
            tree[k] = up.applyAsLong(tree[k], mul.applyAsLong(lazy[k], len));
            lazy[k] = nop;
        }

        private long update(int l, int r, long q, int k, int sl, int sr) {
            if (r <= sl || sr <= l) {
                eval(sr - sl, k);
                return tree[k];
            }
            if (l <= sl && sr <= r) {
                lazy[k] = merge.applyAsLong(lazy[k], q);
                eval(sr - sl, k);
                return tree[k];
            } else {
                eval(sr - sl, k);
                return tree[k] = op.applyAsLong(
                        update(l, r, q, k * 2 + 1, sl, (sl + sr) / 2),
                        update(l, r, q, k * 2 + 2, (sl + sr) / 2, sr)
                );
            }
        }

        public void update(int l, int r, long q) {
            update(l, r, q, 0, 0, m);
        }

        private long query(int l, int r, int k, int sl, int sr) {
            if (r <= sl || sr <= l) {
                return zero;
            }
            eval(sr - sl, k);
            if (l <= sl && sr <= r) {
                return tree[k];
            } else {
                long left = query(l, r, 2 * k + 1, sl, (sl + sr) / 2);
                long right = query(l, r, 2 * k + 2, (sl + sr) / 2, sr);
                return op.applyAsLong(left, right);
            }
        }

        public long query(int l, int r) {
            return query(l, r, 0, 0, m);
        }

    }

    static class LightScanner {
        private BufferedReader reader = null;
        private StringTokenizer tokenizer = null;

        public LightScanner(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
        }

        public String string() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new UncheckedIOException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int ints() {
            return Integer.parseInt(string());
        }

        public long longs() {
            return Long.parseLong(string());
        }

    }

    static class LightWriter implements AutoCloseable {
        private final Writer out;
        private boolean autoflush = false;
        private boolean breaked = true;

        public LightWriter(Writer out) {
            this.out = out;
        }

        public LightWriter(OutputStream out) {
            this(new BufferedWriter(new OutputStreamWriter(out, Charset.defaultCharset())));
        }

        public LightWriter print(char c) {
            try {
                out.write(c);
                breaked = false;
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
            return this;
        }

        public LightWriter print(String s) {
            try {
                out.write(s, 0, s.length());
                breaked = false;
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
            return this;
        }

        public LightWriter ans(String s) {
            if (!breaked) {
                print(' ');
            }
            return print(s);
        }

        public LightWriter ans(long l) {
            return ans(Long.toString(l));
        }

        public LightWriter ln() {
            print(System.lineSeparator());
            breaked = true;
            if (autoflush) {
                try {
                    out.flush();
                } catch (IOException ex) {
                    throw new UncheckedIOException(ex);
                }
            }
            return this;
        }

        public void close() {
            try {
                out.close();
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
        }

    }

    static interface LongIntToLongFunction<T, R> {
        long applyAsLong(long x, int y);

    }

    static final class BitMath {
        private BitMath() {
        }

        public static int extractMsb(int v) {
            v = (v & 0xFFFF0000) > 0 ? v & 0xFFFF0000 : v;
            v = (v & 0xFF00FF00) > 0 ? v & 0xFF00FF00 : v;
            v = (v & 0xF0F0F0F0) > 0 ? v & 0xF0F0F0F0 : v;
            v = (v & 0xCCCCCCCC) > 0 ? v & 0xCCCCCCCC : v;
            v = (v & 0xAAAAAAAA) > 0 ? v & 0xAAAAAAAA : v;
            return v;
        }

    }
}

