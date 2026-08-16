import java.io.*;
import java.util.StringTokenizer;

/**
 * _607B
 * θ(n^3) time
 * θ(n^2) space
 *
 * @author artyom
 */
public class _607B implements Runnable {
    private BufferedReader in;
    private PrintStream out;
    private StringTokenizer tok;

    private void solve() throws IOException {
        int n = nextInt();
        int[] c = readIntArray(n);
        int[][] dp = new int[n + 1][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        for (int i = n - 2; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                dp[i][j] = 1 + dp[i + 1][j];
                if (c[i] == c[i + 1]) {
                    dp[i][j] = Math.min(dp[i][j], 1 + dp[i + 2][j]);
                }
                for (int k = i + 2; k <= j; k++) {
                    if (c[i] == c[k] && dp[i + 1][k - 1] + dp[k + 1][j] < dp[i][j]) {
                        dp[i][j] = dp[i + 1][k - 1] + dp[k + 1][j];
                    }
                }
            }
        }
        out.print(dp[0][n - 1]);
    }

    //--------------------------------------------------------------
    public static void main(String[] args) {
        new _607B().run();
    }

    @Override
    public void run() {
        try {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = System.out;
            tok = null;
            solve();
            in.close();
        } catch (IOException e) {
            System.exit(0);
        }
    }

    private String nextToken() throws IOException {
        while (tok == null || !tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine());
        }
        return tok.nextToken();
    }

    private int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    private int[] readIntArray(int n) throws IOException {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextInt();
        }
        return arr;
    }
}