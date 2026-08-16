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
 * @author HossamDoma
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        int[] t;
        int[] f;
        int[][][] dp;
        int n;
        int k;

        public void solve(int testNumber, InputReader in, PrintWriter out) {

            n = in.nextInt();
            k = in.nextInt();
            t = new int[n + 1];
            f = new int[n + 1];
            dp = new int[2][k + 1][n * 30];

            for (int i = 1; i <= n; ++i) {
                long x = in.nextLong();
                while (x % 2 == 0) {
                    x /= 2;
                    t[i]++;
                }
                while (x % 5 == 0) {
                    x /= 5;
                    f[i]++;
                }
            }

            for (int i = 0; i <= k; ++i) {
                Arrays.fill(dp[0][i], -30 * n);
                Arrays.fill(dp[1][i], -30 * n);
            }

            int e5 = 0;
            int cur = 0, nxt = 1;
            dp[cur][0][0] = 0;

            for (int i = 1; i <= n; ++i) {
                for (int kk = 0; kk <= Math.min(k, i); ++kk) {
                    for (int jj = 0; jj <= e5; ++jj) {
                        if (kk < k)
                            dp[nxt][kk + 1][jj + f[i]] = Math.max(dp[nxt][kk + 1][jj + f[i]], dp[cur][kk][jj] + t[i]);
                        dp[nxt][kk][jj] = Math.max(dp[nxt][kk][jj], dp[cur][kk][jj]);
                    }
                }

                e5 += f[i];

                for (int row = 0; row <= k; ++row)
                    dp[cur][row] = Arrays.copyOf(dp[nxt][row], dp[nxt][row].length);

                cur ^= 1;
                nxt ^= 1;

            }


            int ans = 0;
            for (int i = 0; i <= e5; ++i)
                ans = Math.max(ans, Math.min(i, dp[cur][k][i]));

            out.println(ans);
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

        public Long nextLong() {
            return Long.parseLong(next());
        }

    }
}

