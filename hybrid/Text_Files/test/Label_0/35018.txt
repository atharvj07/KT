import java.util.*;

public class Main {

    long INF = Long.MAX_VALUE;
    long[] dp;
    int MAX_M = 100000;
    int MAX_N = 100000;

    public static void main(String[] args) {
        new Main().solve();
    }

    void solve() {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        dp = new long[N];
        for (int i = 0; i < N; i++) {
            dp[i] = sc.nextInt();
        }
        long x = 0;
        for (int i = 0; i < N; i++) {
            if (i % 2 == 1) {
                x -= dp[i];
            } else {
                x += dp[i];
            }
        }
        long[] ans = new long[N];
        ans[0] = x / 2;
        for (int i = 0; i < N-1; i++) {
            ans[i+1]  = dp[i] - ans[i];
        }
        
        for(int i = 0;i < N;i++){
            System.out.print(ans[i]*2+" ");
        }
        System.out.println();
    }
}