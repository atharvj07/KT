import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Rustam Musin (t.me/musin_acm)
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        C2HaidiITestTyuringaSrednyaya solver = new C2HaidiITestTyuringaSrednyaya();
        solver.solve(1, in, out);
        out.close();
    }

    static class C2HaidiITestTyuringaSrednyaya {
        int maxx = (int) 1e6;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
//        maxx = 3;
            int n = in.readInt();
            int r = in.readInt();
            int offset = 2 * maxx;
            Tree tree = new Tree(2 * offset + 1);
            int[] changesSize = new int[2 * offset + 2];
            int[][] nxs = new int[n][3];
            for (int i = 0; i < n; i++) {
                int x = in.readInt();
                int y = in.readInt();
                int nx = x + y;
                int ny = x - y + offset;
                int nx1 = Math.max(-offset, nx - r) + offset;
                int nx2 = Math.min(+offset + 1, nx + r + 1) + offset;
                changesSize[nx1]++;
                changesSize[nx2]++;
                nxs[i][0] = nx1;
                nxs[i][1] = nx2;
                nxs[i][2] = ny;
            }
            Pair<IntIntPair, Integer>[][] changes = new Pair[changesSize.length][];
            for (int i = 0; i < changes.length; i++) {
                changes[i] = new Pair[changesSize[i]];
            }
            for (int i = 0; i < n; i++) {
                int nx1 = nxs[i][0];
                int nx2 = nxs[i][1];
                int ny = nxs[i][2];
                changes[nx1][--changesSize[nx1]] = Pair.makePair(IntIntPair.makePair(ny - r, ny + r), +1);
                changes[nx2][--changesSize[nx2]] = Pair.makePair(IntIntPair.makePair(ny - r, ny + r), -1);
            }
            int ans = 0;
            for (int x = -offset; x <= offset; x++) {
                for (Pair<IntIntPair, Integer> p : changes[x + offset]) {
                    tree.add(p.first.first, p.first.second, p.second);
                }
                ans = Math.max(ans, tree.fullMax());
            }
            out.print(ans);
        }

        class Tree {
            int n;
            int[] tree;
            int[] push;
            int[] max;

            Tree(int size) {
                int log = 0;
                while (1 << log < size) {
                    log++;
                }
                n = 1 << log;
                tree = new int[2 * n];
                push = new int[2 * n];
                max = new int[2 * n];
            }

            int fullMax() {
                return max[1];
            }

            void add(int l, int r, int x) {
                add(1, 0, n - 1, l, r, x);
            }

            void add(int v, int tl, int tr, int l, int r, int x) {
                push(v);
                if (r < tl || l > tr) {
                    return;
                }
                if (l <= tl && tr <= r) {
                    push[v] += x;
                    push(v);
                    return;
                }
                int tm = tl + tr >> 1;
                add(v << 1, tl, tm, l, r, x);
                add(v << 1 | 1, tm + 1, tr, l, r, x);
                update(v);
            }

            void push(int v) {
                if (v < n) {
                    push[v << 1] += push[v];
                    push[v << 1 | 1] += push[v];
                }
                tree[v] += push[v];
                max[v] += push[v];
                push[v] = 0;
            }

            void update(int v) {
                if (v < n) {
                    max[v] = join(max[v << 1], max[v << 1 | 1]);
                } else {
                    max[v] = tree[v];
                }
            }

            int join(int a, int b) {
                return Math.max(a, b);
            }

        }

    }

    static class IntIntPair implements Comparable<IntIntPair> {
        public final int first;
        public final int second;

        public static IntIntPair makePair(int first, int second) {
            return new IntIntPair(first, second);
        }

        public IntIntPair(int first, int second) {
            this.first = first;
            this.second = second;
        }

        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }

            IntIntPair pair = (IntIntPair) o;

            return first == pair.first && second == pair.second;
        }

        public int hashCode() {
            int result = first;
            result = 31 * result + second;
            return result;
        }

        public String toString() {
            return "(" + first + "," + second + ")";
        }

        public int compareTo(IntIntPair o) {
            int value = Integer.compare(first, o.first);
            if (value != 0) {
                return value;
            }
            return Integer.compare(second, o.second);
        }

    }

    static class OutputWriter {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void close() {
            writer.close();
        }

        public void print(int i) {
            writer.print(i);
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private InputReader.SpaceCharFilter filter;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            if (numChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }

        public int readInt() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public boolean isSpaceChar(int c) {
            if (filter != null) {
                return filter.isSpaceChar(c);
            }
            return isWhitespace(c);
        }

        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);

        }

    }

    static class Pair<U, V> implements Comparable<Pair<U, V>> {
        public final U first;
        public final V second;

        public static <U, V> Pair<U, V> makePair(U first, V second) {
            return new Pair<U, V>(first, second);
        }

        private Pair(U first, V second) {
            this.first = first;
            this.second = second;
        }

        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }

            Pair pair = (Pair) o;

            return !(first != null ? !first.equals(pair.first) : pair.first != null) &&
              !(second != null ? !second.equals(pair.second) : pair.second != null);
        }

        public int hashCode() {
            int result = first != null ? first.hashCode() : 0;
            result = 31 * result + (second != null ? second.hashCode() : 0);
            return result;
        }

        public String toString() {
            return "(" + first + "," + second + ")";
        }

        public int compareTo(Pair<U, V> o) {
            int value = ((Comparable<U>) first).compareTo(o.first);
            if (value != 0) {
                return value;
            }
            return ((Comparable<V>) second).compareTo(o.second);
        }

    }
}

