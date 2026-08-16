import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author ATailouloute
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        QuickScanner in = new QuickScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        public void solve(int testNumber, QuickScanner in, PrintWriter out) {
            int n = in.nextInt();
            int k = in.nextInt();
            int a = in.nextInt();
            int b = in.nextInt();
            int q = in.nextInt();

            IntFenwickTree ftA = new IntFenwickTree();
            IntFenwickTree ftB = new IntFenwickTree();

            for (int i = 0; i < q; i++) {
                int op = in.nextInt();
                if (op == 1) {
                    int di = in.nextInt();
                    int ai = in.nextInt();
                    ftA.incr(di, ai);
                    ftB.incr(di, ai);
                    int x = ftA.read(di, di);
                    int y = ftB.read(di, di);
                    if (a < x) ftA.incr(di, a - x);
                    if (b < y) ftB.incr(di, b - y);
                } else {
                    int pi = in.nextInt();
                    int before = 0, after = 0;
                    if (pi > 1) before = ftB.read(1, pi - 1);
                    if (pi + k <= n) after = ftA.read(pi + k, n);
                    out.println(before + after);
                }
            }
        }

    }

    static class QuickScanner {
        BufferedReader br;
        StringTokenizer st;
        InputStream is;

        public QuickScanner(InputStream stream) {
            is = stream;
            br = new BufferedReader(new InputStreamReader(stream), 32768);
        }

        public String nextToken() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(nextToken());
        }

    }

    static class IntFenwickTree {
        final static int MAX = (int) 1e6;
        private int[] bit;

        public IntFenwickTree() {
            this(MAX);
        }

        public IntFenwickTree(int max) {
            bit = new int[max];
        }

        public int read(int idx) {
            int ret = 0;
            for (; idx > 0; idx -= (idx & -idx)) {
                ret += bit[idx];
            }
            return ret;
        }

        public int read(int from, int to) {
            return read(to) - (from > 0 ? read(from - 1) : 0);
        }

        public void incr(int idx, int by) {
            for (; idx < bit.length; idx += (idx & -idx)) {
                bit[idx] += by;
            }
        }

    }
}

