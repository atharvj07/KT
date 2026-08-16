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
 * Built using CHelper plug-in Actual solution is at the top
 * 
 * @author daltao
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Thread thread = new Thread(null, new TaskAdapter(), "daltao", 1 << 27);
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
            StringsofEternity solver = new StringsofEternity();
            solver.solve(1, in, out);
            out.close();
        }
    }
    static class StringsofEternity {
        boolean circle;

        public void solve(int testNumber, FastInput in, FastOutput out) {
            StringBuilder builder = new StringBuilder(1000000);
            in.readString(builder);
            int tLen = builder.length();

            char[] s = new char[500000];
            int sLen = in.readString(s, 0);

            builder.append(builder);
            while (s.length + tLen > builder.length()) {
                builder.append(builder);
            }
            char[] t = new char[builder.length()];
            builder.getChars(0, builder.length(), t, 0);


            Hash s31 = new Hash(sLen, 31);
            Hash s61 = new Hash(sLen, 61);
            Hash t31 = new Hash(t.length, 31);
            Hash t61 = new Hash(t.length, 61);

            s31.populate(s, sLen);
            s61.populate(s, sLen);
            t31.populate(t, t.length);
            t61.populate(t, t.length);

            Node[] nodes = new Node[tLen];
            for (int i = 0; i < tLen; i++) {
                if ((t31.partial(i, i + sLen - 1) == s31.partial(0, sLen - 1)
                                && t61.partial(i, i + sLen - 1) == s61.partial(0, sLen - 1))) {
                    nodes[i] = new Node();
                }

            }

            for (int i = 0; i < tLen; i++) {
                if (nodes[i] == null) {
                    continue;
                }
                nodes[i].next = nodes[(i + sLen) % tLen];
            }

            int ans = 0;
            for (int i = 0; i < tLen; i++) {
                if (nodes[i] != null) {
                    dfs(nodes[i]);
                    ans = Math.max(ans, nodes[i].dp);
                }
            }

            if (circle) {
                out.println(-1);
            } else {
                out.println(ans);
            }
        }

        public void dfs(Node root) {
            if (root.visited) {
                if (root.instk) {
                    circle = true;
                }
                return;
            }
            root.visited = true;
            root.instk = true;
            root.dp = 1;
            if (root.next != null) {
                dfs(root.next);
                root.dp += root.next.dp;
            }
            root.instk = false;
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

        public FastOutput println(int c) {
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
    static class NumberTheory {
        public static class Modular {
            int m;

            public Modular(int m) {
                this.m = m;
            }

            public Modular(long m) {
                this.m = (int) m;
                if (this.m != m) {
                    throw new IllegalArgumentException();
                }
            }

            public Modular(double m) {
                this.m = (int) m;
                if (this.m != m) {
                    throw new IllegalArgumentException();
                }
            }

            public int valueOf(int x) {
                x %= m;
                if (x < 0) {
                    x += m;
                }
                return x;
            }

            public int valueOf(long x) {
                x %= m;
                if (x < 0) {
                    x += m;
                }
                return (int) x;
            }

            public int mul(int x, int y) {
                return valueOf((long) x * y);
            }

            public int plus(int x, int y) {
                return valueOf(x + y);
            }

            public String toString() {
                return "mod " + m;
            }

        }

        public static class Power {
            final NumberTheory.Modular modular;

            public Power(NumberTheory.Modular modular) {
                this.modular = modular;
            }

            public int pow(int x, long n) {
                if (n == 0) {
                    return 1;
                }
                long r = pow(x, n >> 1);
                r = modular.valueOf(r * r);
                if ((n & 1) == 1) {
                    r = modular.valueOf(r * x);
                }
                return (int) r;
            }

            public int inverse(int x) {
                return pow(x, modular.m - 2);
            }

        }

    }
    static class Node {
        Node next;
        boolean visited;
        int dp;
        boolean instk;

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

        public String readString(StringBuilder builder) {
            skipBlank();

            while (next > 32) {
                builder.append((char) next);
                next = read();
            }

            return builder.toString();
        }

        public int readString(char[] data, int offset) {
            skipBlank();

            int originalOffset = offset;
            while (next > 32) {
                data[offset++] = (char) next;
                next = read();
            }

            return offset - originalOffset;
        }

    }
    static class Hash {
        private static final NumberTheory.Modular MOD = new NumberTheory.Modular((int) (1e9 + 7));
        private int[] inverse;
        private int[] xs;
        private int[] hash;
        private int n;

        public Hash(Hash model) {
            inverse = model.inverse;
            hash = new int[model.hash.length];
            n = model.n;
            xs = model.xs;
        }

        public Hash(int size, int x) {
            inverse = new int[size];
            hash = new int[size];
            xs = new int[size];
            int invX = new NumberTheory.Power(MOD).inverse(x);
            inverse[0] = 1;
            xs[0] = 1;
            for (int i = 1; i < size; i++) {
                this.inverse[i] = MOD.mul(this.inverse[i - 1], invX);
                xs[i] = MOD.mul(xs[i - 1], x);
            }
        }

        public void populate(char[] data, int n) {
            this.n = n;
            hash[0] = data[0];
            for (int i = 1; i < n; i++) {
                hash[i] = MOD.plus(hash[i - 1], MOD.mul(data[i], xs[i]));
            }
        }

        public int partial(int l, int r) {
            int h = hash[r];
            if (l > 0) {
                h = MOD.plus(h, -hash[l - 1]);
                h = MOD.mul(h, inverse[l]);
            }
            return h;
        }

    }
}

