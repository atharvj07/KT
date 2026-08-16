import java.io.*;
import java.util.StringTokenizer;

public class Round574BasketballExercise_1195C {
    static PrintWriter pr = new PrintWriter(System.out);
    public static class InputReader {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

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

        public long nextLong() {
            return Long.parseLong(next());
        }
    }
    public static void main(String[] args) {

        InputReader in = new InputReader(System.in);
        int n = in.nextInt();
        long[] a = new long[n];
        long[] b = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = in.nextLong();
        }

        for (int i = 0; i < n; i++) {
            b[i] = in.nextLong();
        }

        pr.print(sol(a,b,n));
        pr.flush();
    }

    public static long sol(long[] a, long[] b, int n){

        long[][] dp = new long[2][n];
        dp[0][0] = a[0];
        dp[1][0] = b[0];


        for (int i = 1; i < n; i++) {
            dp[0][i] = Math.max(dp[1][i-1] + a[i], dp[0][i-1]);
            dp[1][i] = Math.max(dp[0][i-1] + b[i], dp[1][i-1]);
        }

        return Math.max(dp[0][n-1],dp[1][n-1]);

    }

}
