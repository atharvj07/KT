import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.ArrayList;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author ilyakor
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        static final long SENTINEL = (long) (-1E17);
        public static final long inf = (long) (1E16);
        long[] d1;
        long[] d2;
        ArrayList<Pair<Integer, Long>>[] g1;
        ArrayList<Pair<Integer, Long>>[] g2;
        int i0;
        int j0;
        long c0;
        long lower;
        long upper;
        long len;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.nextInt();
            int m = in.nextInt();
            d1 = new long[n];
            d2 = new long[m];
            Arrays.fill(d1, SENTINEL);
            Arrays.fill(d2, SENTINEL);

            g1 = new ArrayList[n];
            for (int i = 0; i < n; ++i)
                g1[i] = new ArrayList<>();
            g2 = new ArrayList[m];
            for (int i = 0; i < m; ++i)
                g2[i] = new ArrayList<>();

            int k = in.nextInt();
            i0 = -1;
            j0 = -1;
            c0 = -1;
            for (int i = 0; i < k; ++i) {
                int x = in.nextInt() - 1;
                int y = in.nextInt() - 1;
                long c = in.nextLong();
                if (i0 == -1) {
                    i0 = x;
                    j0 = y;
                    c0 = c;
                    d1[x] = c;
                    d2[y] = c;
                } else if (x == i0) {
                    d2[y] = c;
                } else if (y == j0) {
                    d1[x] = c;
                } else {
                    g1[x].add(new Pair<>(y, c + c0));
                    g2[y].add(new Pair<>(x, c + c0));
                }
            }

            for (int i = 0; i < n; ++i)
                if (d1[i] != SENTINEL)
                    if (!dfs1(0, i)) {
                        out.printLine("No");
                        return;
                    }
            for (int i = 0; i < m; ++i)
                if (d2[i] != SENTINEL)
                    if (!dfs1(1, i)) {
                        out.printLine("No");
                        return;
                    }

            len = c0;
            long U = inf + 1, D = inf + 1;
            for (int i = 0; i < n; ++i)
                if (d1[i] != SENTINEL)
                    U = Math.min(U, d1[i]);
            for (int i = 0; i < m; ++i)
                if (d2[i] != SENTINEL)
                    D = Math.min(D, d2[i]);
            len = Math.max(len, 2 * c0 - U - D);

            if (U + D < c0) {
                out.printLine("No");
                return;
            }

            for (int i = 0; i < n; ++i) {
                if (d1[i] != SENTINEL) continue;
                lower = 0;
                upper = inf + 1;
                dfs2(0, i, 0);
                if (lower + len > upper) {
                    out.printLine("No");
                    return;
                }
                long val = Math.max(0L, c0 - D);
                val = upper - lower - val;
                U = Math.min(U, val);
            }

            for (int i = 0; i < m; ++i) {
                if (d2[i] != SENTINEL) continue;
                lower = -inf - 1;
                upper = 0;
                dfs2(1, i, 0);
                if (lower + len > upper) {
                    out.printLine("No");
                    return;
                }
                long val = Math.max(0L, c0 - D);
                val = upper - lower - val;
                U = Math.min(U, val);
            }
//        if (U + D < c0) {
//            out.printLine("No");
//            return;
//        }
            out.printLine("Yes");
        }

        private void dfs2(int ind, int x, long c) {
            if (ind == 0) {
                d1[x] = c;
                // 0 <= c + x
                // x >= -c
                if (lower < -c)
                    lower = -c;
            } else {
                d2[x] = c;
                // c - x >= 0
                // x <= c
                if (upper > c)
                    upper = c;
            }
            if (lower + len > upper) return;
            int oind = 1 - ind;
            ArrayList<Pair<Integer, Long>> adj = ind == 0 ? g1[x] : g2[x];
            for (Pair<Integer, Long> edge : adj) {
                int y = edge.first;
                long oc = edge.second - c;
                long oval = oind == 0 ? d1[y] : d2[y];
                if (oval == SENTINEL) {
                    dfs2(oind, y, oc);
                } else {
                    if (oval != oc) {
                        lower = 1;
                        upper = -1;
                        return;
                    }
                }
                if (lower + len > upper) return;
            }
        }

        private boolean dfs1(int ind, int x) {
            int oind = 1 - ind;
            ArrayList<Pair<Integer, Long>> adj = ind == 0 ? g1[x] : g2[x];
            long val = ind == 0 ? d1[x] : d2[x];
            for (Pair<Integer, Long> edge : adj) {
                int y = edge.first;
                long c = edge.second - val;
                if (c < 0)
                    return false;
                long oval = oind == 0 ? d1[y] : d2[y];
                if (oval == SENTINEL) {
                    if (oind == 0)
                        d1[y] = c;
                    else
                        d2[y] = c;
                    if (!dfs1(oind, y))
                        return false;
                } else {
                    if (oval != c)
                        return false;
                }
            }
            return true;
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buffer = new byte[10000];
        private int cur;
        private int count;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public static boolean isSpace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public int read() {
            if (count == -1) {
                throw new InputMismatchException();
            }
            try {
                if (cur >= count) {
                    cur = 0;
                    count = stream.read(buffer);
                    if (count <= 0)
                        return -1;
                }
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            return buffer[cur++];
        }

        public int readSkipSpace() {
            int c;
            do {
                c = read();
            } while (isSpace(c));
            return c;
        }

        public int nextInt() {
            int sgn = 1;
            int c = readSkipSpace();
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res = res * 10 + c - '0';
                c = read();
            } while (!isSpace(c));
            res *= sgn;
            return res;
        }

        public long nextLong() {
            long sgn = 1;
            int c = readSkipSpace();
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            long res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res = res * 10L + (long) (c - '0');
                c = read();
            } while (!isSpace(c));
            res *= sgn;
            return res;
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

        public void print(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                if (i != 0) {
                    writer.print(' ');
                }
                writer.print(objects[i]);
            }
        }

        public void printLine(Object... objects) {
            print(objects);
            writer.println();
        }

        public void close() {
            writer.close();
        }

    }

    static class Pair<P, Q> {
        public P first;
        public Q second;

        public Pair() {
        }

        public Pair(P first, Q second) {
            this.first = first;
            this.second = second;
        }


        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Pair pair = (Pair) o;

            if (first != null ? !first.equals(pair.first) : pair.first != null) return false;
            if (second != null ? !second.equals(pair.second) : pair.second != null) return false;

            return true;
        }


        public int hashCode() {
            int result = first != null ? first.hashCode() : 0;
            result = 31 * result + (second != null ? second.hashCode() : 0);
            return result;
        }

    }
}

