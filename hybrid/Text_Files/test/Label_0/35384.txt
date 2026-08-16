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
 * @author cplayer
 */
public class Main {
    public static void main (String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        DNekoAndAkisPrank solver = new DNekoAndAkisPrank();
        solver.solve(1, in, out);
        out.close();
    }

    static class DNekoAndAkisPrank {
        private int mod = 1000000000 + 7;

        public void solve (int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            int[][] dp = new int[2 * n + 5][2 * n + 5];
            dp[0][0] = 1;
            for (int i = 0; i < 2 * n; ++i) {
                for (int j = 0; j < 2 * n; ++j) {
                    dp[i + 1][j + 1] += dp[i][j];
                    dp[i + 1][j + 1] %= mod;
                    if (j > 0) {
                        dp[i + 1][j - 1] += dp[i][j];
                        dp[i + 1][j - 1] %= mod;
                    }
                }
            }
            long ans = 0;
            for (int i = 1; i < 2 * n; i += 2) {
                for (int j = 0; j <= 2 * n; ++j) {
                    if (i + j <= 2 * n) {
                        ans += dp[i][j];
                        ans %= mod;
                    }
                }
            }
            out.println(ans);
        }

    }

    static class InputReader {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        public InputReader (InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
            tokenizer = null;
        }

        public String next () {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt () {
            return Integer.parseInt(next());
        }

    }
}

