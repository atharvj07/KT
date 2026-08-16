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
 *
 * @author llamaoo7
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        FVasyaAndEndlessCredits solver = new FVasyaAndEndlessCredits();
        solver.solve(1, in, out);
        out.close();
    }

    static class FVasyaAndEndlessCredits {
        long INF = (long) 1e18;
        int MX = 507;
        long[][] a = new long[MX][MX];

        long hungarian(int n, int m) {
            long[] u = new long[n + 1];
            long[] v = new long[m + 1];
            int[] p = new int[m + 1];
            int[] way = new int[m + 1];
            for (int i = 1; i <= n; i++) {
                p[0] = i;
                int j0 = 0;
                long[] minv = new long[m + 1];
                Arrays.fill(minv, INF);
                boolean[] used = new boolean[m + 1];
                do {
                    used[j0] = true;
                    int i0 = p[j0];
                    int j1 = 0;
                    long d = INF;
                    for (int j = 1; j <= m; j++)
                        if (!used[j]) {
                            long cur = a[i0][j] - u[i0] - v[j];
                            if (cur < minv[j]) {
                                minv[j] = cur;
                                way[j] = j0;
                            }
                            if (minv[j] < d) {
                                d = minv[j];
                                j1 = j;
                            }
                        }
                    for (int j = 0; j <= m; j++)
                        if (used[j]) {
                            u[p[j]] += d;
                            v[j] -= d;
                        } else minv[j] -= d;
                    j0 = j1;
                } while (p[j0] != 0);
                do {
                    int j1 = way[j0];
                    p[j0] = p[j1];
                    j0 = j1;
                } while (j0 != 0);
            }

            int[] ans = new int[n + 1];
            for (int j = 1; j <= m; j++)
                ans[p[j]] = j;
            return -1 * v[0];
        }

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            for (int i = 1; i <= n; i++) {
                long x = in.nextInt();
                long y = in.nextInt();
                long k = in.nextInt();
                for (int j = 1; j <= n; j++) {
                    a[i][j] = -1 * Math.max(0, x);
                    if (j <= k) x -= y;
                }
            }
            out.println(-1 * hungarian(n, n));
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

