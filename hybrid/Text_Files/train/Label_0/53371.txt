import java.util.*;

public class Main {
    static final int MOD = 1000000007;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean[] isNotPrimes = new boolean[1000001];
        isNotPrimes[0] = true;
        isNotPrimes[1] = true;
        for (int i = 2; i < isNotPrimes.length; i++) {
            if (isNotPrimes[i]) {
                continue;
            }
            for (int j = 2; j * i < isNotPrimes.length; j++) {
                isNotPrimes[i * j] = true;
            }
        }
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int[][] dp = new int[n][2];
        if (!isNotPrimes[arr[0]]) {
            dp[0][0] = 1;
        }
        for (int i = 1; i < n; i++) {
            dp[i][1] += dp[i - 1][0];
            dp[i][1] %= MOD;
            if (!isNotPrimes[arr[i]]) {
                if (i >= 2 && arr[i - 2] < arr[i]) {
                    dp[i][0] += dp[i - 1][1];
                    dp[i][0] %= MOD;
                }
                if (arr[i - 1] < arr[i]) {
                    dp[i][0] += dp[i - 1][0];
                    dp[i][0] %= MOD;
                }
            }
        }
        System.out.println((dp[n - 1][0] + dp[n - 1][1]) % MOD);
    }
}

