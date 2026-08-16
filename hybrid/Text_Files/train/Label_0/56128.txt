import java.util.*;

public class Main {
    static final int MOD = 1000000007;
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int kk = sc.nextInt();
        int[] arr = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            arr[i] = sc.nextInt();
        }
        long[][][] dp = new long[n + 1][n + 1][256];
        dp[0][0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= i - 1; j++) {
                for (int k = 0; k < 256; k++) {
                    dp[i][j][k] += dp[i - 1][j][k];
                    dp[i][j][k] %= MOD;
                    dp[i][j + 1][k ^ arr[i]] += dp[i - 1][j][k];
                    dp[i][j + 1][k ^ arr[i]] %= MOD;
                }
            }
        }
        long total = 0;
        for (int i = 0; i <= n; i++) {
            if (dp[n][i][kk] != 0) {
                total += dp[n][i][kk] * kaijo(i) % MOD;
                total %= MOD;
            }
       }
        System.out.println(total);
    }
    
    static long kaijo(long x) {
        if (x == 0) {
            return 1;
        } else {
            return x * kaijo(x - 1) % MOD;
        }
    }
}

