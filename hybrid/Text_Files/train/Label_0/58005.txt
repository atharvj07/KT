import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskE solver = new TaskE();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskE {
        private int n;
        private String[] g;
        long[][][][] cache;

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            n = in.nextInt();
            g = new String[2 * n];
            for (int i = 0; i < 2 * n; ++i) {
                g[i] = in.next();
            }
            cache = new long[2 * n][2 * n][2 * n][2 * n];
            for (long[][][] a : cache) for (long[][] b : a) for (long[] c : b) Arrays.fill(c, -1);
            long res = 0;
            n *= 2;
            for (int i = 1; i < n; ++i)
                if (g[0].charAt(i) == '1') {
                    res += rec(1, i - 1, i + 1, n - i - 1);
                }
            out.println(res);
        }

        private long rec(int s1, int n1, int s2, int n2) {
            if (n1 == 0 && n2 == 0) {
                return 1;
            }
            if (n1 == 0 || n2 == 0) {
                return 0;
            }
            long cached = cache[s1][n1][s2][n2];
            if (cached >= 0) return cached;
            long res = 0;
            for (int f1 = s1, i1 = 0; i1 < n1; ++i1, ++f1) {
                if (f1 >= n) f1 = 0;
                int nf1 = f1 + 1;
                if (nf1 >= n) nf1 = 0;
                for (int f2 = s2, i2 = 0; i2 < n2; ++i2, ++f2) {
                    if (f2 >= n) f2 = 0;
                    int nf2 = f2 + 1;
                    if (nf2 >= n) nf2 = 0;
                    if (g[f1].charAt(f2) == '1') {
                        for (int q1 = f1, j1 = i1; j1 < n1; ++q1, ++j1) {
                            if (q1 >= n) q1 = 0;
                            int nq1 = q1 + 1;
                            if (nq1 >= n) nq1 = 0;
                            for (int q2 = s2, j2 = 0; j2 <= i2; ++q2, ++j2) {
                                if (q2 >= n) q2 = 0;
                                res += rec(s1, i1, nf1, j1 - i1) * rec(q2, i2 - j2, nf2, n2 - 1 - i2) * rec(nq1, n1 - 1 - j1, s2, j2);
                            }
                        }
                    }
                }
            }
            cache[s1][n1][s2][n2] = res;
            return res;
        }

    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

