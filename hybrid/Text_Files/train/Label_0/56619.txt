import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.BitSet;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author lewin
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        GNewRoadNetwork solver = new GNewRoadNetwork();
        solver.solve(1, in, out);
        out.close();
    }

    static class GNewRoadNetwork {
        int[] tree;
        int[] dist;
        int[] vis;
        int ctr;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int t = in.nextInt();
            int maxn = 2001;
            char[][] s = new char[maxn][maxn];
            BitSet[] bs = new BitSet[maxn];
            for (int i = 0; i < maxn; i++) bs[i] = new BitSet();
            int[][] counts = new int[maxn][maxn];
            tree = new int[maxn];
            dist = new int[maxn];
            ctr = 0;
            vis = new int[maxn];
            int[] r = new int[maxn];
            int[] want = new int[maxn];

            outer:
            while (t-- > 0) {
                int n = in.nextInt(), m = in.nextInt();
                for (int i = 0; i < n; i++) {
                    bs[i].clear();
                }
                Arrays.fill(want, 0);
                Arrays.fill(r, 0);
                for (int i = 0; i < m; i++) {
                    char[] rr = in.next().toCharArray();
                    for (int j = 0; j < n; j++) {
                        s[i][j] = rr[j];
                        if (s[i][j] == '1') {
                            bs[j].set(i);
                            want[i]++;
                        }
                    }
                    want[i]--;
                }
                for (int i = 0; i < n; i++) {
                    for (int j = i + 1; j < n; j++) {
                        BitSet a = (BitSet) bs[i].clone();
                        a.and(bs[j]);
                        counts[i][j] = counts[j][i] = a.cardinality();
                    }
                }
                ctr++;
                mstPrim(counts, n);
                for (int i = 1; i < n; i++) {
                    for (int k = 0; k < m; k++) {
                        if (s[k][i] == '1' && s[k][tree[i]] == '1') {
                            r[k]++;
                        }
                    }
                }
                for (int k = 0; k < m; k++) {
                    if (r[k] != want[k]) {
                        out.println("NO");
                        continue outer;
                    }
                }
                out.println("YES");
                for (int i = 1; i < n; i++) {
                    out.println((i + 1) + " " + (tree[i] + 1));
                }
            }

        }

        public void mstPrim(int[][] d, int n) {
            Arrays.fill(dist, Integer.MIN_VALUE);
            dist[0] = 0;
            for (int i = 0; i < n; i++) {
                int u = -1;
                for (int j = 0; j < n; j++) {
                    if (vis[j] != ctr && (u == -1 || dist[u] < dist[j]))
                        u = j;
                }
                vis[u] = ctr;
                for (int j = 0; j < n; j++) {
                    if (vis[j] != ctr && dist[j] < d[u][j]) {
                        dist[j] = d[u][j];
                        tree[j] = u;
                    }
                }
            }
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

        public void println(Object... objects) {
            print(objects);
            writer.println();
        }

        public void close() {
            writer.close();
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1 << 16];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            if (this.numChars == -1) {
                throw new InputMismatchException();
            } else {
                if (this.curChar >= this.numChars) {
                    this.curChar = 0;

                    try {
                        this.numChars = this.stream.read(this.buf);
                    } catch (IOException var2) {
                        throw new InputMismatchException();
                    }

                    if (this.numChars <= 0) {
                        return -1;
                    }
                }

                return this.buf[this.curChar++];
            }
        }

        public int nextInt() {
            int c;
            for (c = this.read(); isSpaceChar(c); c = this.read()) {
                ;
            }

            byte sgn = 1;
            if (c == 45) {
                sgn = -1;
                c = this.read();
            }

            int res = 0;

            while (c >= 48 && c <= 57) {
                res *= 10;
                res += c - 48;
                c = this.read();
                if (isSpaceChar(c)) {
                    return res * sgn;
                }
            }

            throw new InputMismatchException();
        }

        public String next() {
            int c;
            while (isSpaceChar(c = this.read())) {
                ;
            }

            StringBuilder result = new StringBuilder();
            result.appendCodePoint(c);

            while (!isSpaceChar(c = this.read())) {
                result.appendCodePoint(c);
            }

            return result.toString();
        }

        public static boolean isSpaceChar(int c) {
            return c == 32 || c == 10 || c == 13 || c == 9 || c == -1;
        }

    }
}

