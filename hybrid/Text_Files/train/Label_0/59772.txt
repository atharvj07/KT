import java.io.*;

public class E14G {
    static int[][] choose;
    public static void main(String[] args) throws IOException {
        init_io();
        int N = nint(), M = nint();
        choose = new int[N+1][];
        long[] ways = new long[N+1];
        ways[0] = 1; ways[1] = 1;
        for (int i = 0; i <= N; i++) choose[i] = new int[i+1];
        for (int i = 0; i <= N; i++) {
            choose[i][0] = choose[i][i] = 1;
            for (int j = 1; j < i; j++) {
                choose[i][j] = (choose[i-1][j-1] + choose[i-1][j]) % M;
            }
        }
        for (int i = 2; i <= N; i++) {
            for (int j = 0; j < i; j++) {
                ways[i] = (ways[i] + choose[i-1][j]) % M;
            }
        }
        long[][] dp = new long[(N+1)/2+1][N+1];
        dp[0][0] = 1;
        for (int i = 1; i <= (N+1)/2; i++) {
            for (int j = 1; j <= N; j++) {
                for (int k = 1; k <= j; k++) {
                    dp[i][j] = (dp[i][j] + ways[k] * choose[j][k] % M * dp[i-1][j-k] % M) % M;
                }
            }
        }
        long ans = 0;
        for (int i = 1; i <= (N+1)/2; i++) {
            ans = (ans + dp[i][N-(i-1)]) % M;
        }
        out.println(ans);
        out.close();
    }

    static StreamTokenizer in;
    static PrintWriter out;
    static BufferedReader br;

    static int nint() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    static void init_io() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        in = new StreamTokenizer(br);
        out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    }
}