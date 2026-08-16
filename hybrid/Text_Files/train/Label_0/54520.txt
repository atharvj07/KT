import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

/**
 * @author Don Li
 */
public class BacterialMelee {
    
    int MOD = (int) (1e9 + 7);
    
    void solve() {
        int n = in.nextInt();
        char[] s = in.nextToken().toCharArray();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = s[i] - 'a';
        
        int[][] dp = new int[n + 1][26];
        int[] sum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            sum[1] = (sum[1] - dp[1][a[i]] + MOD) % MOD;
            dp[1][a[i]] = 1;
            sum[1] = (sum[1] + dp[1][a[i]]) % MOD;
            for (int j = 2; j <= n; j++) {
                sum[j] = (sum[j] - dp[j][a[i]] + MOD) % MOD;
                dp[j][a[i]] = (sum[j - 1] - dp[j - 1][a[i]] + MOD) % MOD;
                sum[j] = (sum[j] + dp[j][a[i]]) % MOD;
            }
        }
        
        int[][] c = new int[n][n];
        for (int i = 0; i < n; i++) {
            c[i][0] = 1;
            for (int j = 1; j <= i; j++) c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD;
        }
        
        long ans = 0;
        for (int i = 1; i <= n; i++) {
            ans = (ans + (long) sum[i] * c[n - 1][i - 1] % MOD) % MOD;
        }
        out.println(ans);
    }
    
    public static void main(String[] args) {
        in = new FastScanner(new BufferedReader(new InputStreamReader(System.in)));
        out = new PrintWriter(System.out);
        new BacterialMelee().solve();
        out.close();
    }
    
    static FastScanner in;
    static PrintWriter out;
    
    static class FastScanner {
        BufferedReader in;
        StringTokenizer st;
        
        public FastScanner(BufferedReader in) {
            this.in = in;
        }
        
        public String nextToken() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        public int nextInt() {
            return Integer.parseInt(nextToken());
        }
        
        public long nextLong() {
            return Long.parseLong(nextToken());
        }
        
        public double nextDouble() {
            return Double.parseDouble(nextToken());
        }
    }
}
