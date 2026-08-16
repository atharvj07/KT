import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.FilterInputStream;
import java.io.BufferedInputStream;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Jenish
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        ScanReader in = new ScanReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        EJeremyBearimy solver = new EJeremyBearimy();
        solver.solve(1, in, out);
        out.close();
    }

    static class EJeremyBearimy {
        int[] size;
        int[][] g;

        void dfs(int node, int par) {
            for (int k : g[node]) {
                if (k != par) {
                    dfs(k, node);
                    size[node] += size[k];
                }
            }
            size[node]++;
        }

        public void solve(int testNumber, ScanReader in, PrintWriter out) {
            int t = in.scanInt();
            while (t-- > 0) {
                int n = in.scanInt() * 2;
                size = new int[n + 1];
                int edges[][] = new int[n - 1][3];
                int from[] = new int[n - 1];
                int to[] = new int[n - 1];
                int val[] = new int[n - 1];
                for (int i = 0; i < n - 1; i++) {
                    edges[i] = new int[]{in.scanInt(), in.scanInt(), in.scanInt()};
                    from[i] = edges[i][0];
                    to[i] = edges[i][1];
                    val[i] = edges[i][2];
                }
                g = CodeX.packGraph(from, to, n);
                dfs(1, -1);

                long min = 0;
                long max = 0;
                for (int i = 0; i < n - 1; i++) {
                    int m = Math.min(size[edges[i][0]], size[edges[i][1]]);
                    max += (1l * edges[i][2] * Math.min(m, n - m));
                    min += 1l * edges[i][2] * (m % 2);
                }


                out.println(min + " " + max);

            }
        }

    }

    static class CodeX {
        public static int[][] packGraph(int[] from, int[] to, int n) {
            int[][] g = new int[n + 1][];
            int p[] = new int[n + 1];
            for (int i : from) p[i]++;
            for (int i : to) p[i]++;
            for (int i = 0; i <= n; i++) g[i] = new int[p[i]];
            for (int i = 0; i < from.length; i++) {
                g[from[i]][--p[from[i]]] = to[i];
                g[to[i]][--p[to[i]]] = from[i];
            }
            return g;
        }

    }

    static class ScanReader {
        private byte[] buf = new byte[4 * 1024];
        private int INDEX;
        private BufferedInputStream in;
        private int TOTAL;

        public ScanReader(InputStream inputStream) {
            in = new BufferedInputStream(inputStream);
        }

        private int scan() {
            if (INDEX >= TOTAL) {
                INDEX = 0;
                try {
                    TOTAL = in.read(buf);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                if (TOTAL <= 0) return -1;
            }
            return buf[INDEX++];
        }

        public int scanInt() {
            int I = 0;
            int n = scan();
            while (isWhiteSpace(n)) n = scan();
            int neg = 1;
            if (n == '-') {
                neg = -1;
                n = scan();
            }
            while (!isWhiteSpace(n)) {
                if (n >= '0' && n <= '9') {
                    I *= 10;
                    I += n - '0';
                    n = scan();
                }
            }
            return neg * I;
        }

        private boolean isWhiteSpace(int n) {
            if (n == ' ' || n == '\n' || n == '\r' || n == '\t' || n == -1) return true;
            else return false;
        }

    }
}

