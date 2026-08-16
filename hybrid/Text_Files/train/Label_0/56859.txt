import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] a = new int[N];
        for (int i = 0; i < N; i++) {
            a[i] = sc.nextInt();
        }

        long[][] dp = new long[N][N];


        long res = backtrack(dp, 0, N - 1, a);
        System.out.println(res);
    }

    public static long backtrack(long[][] dp, int start, int end, int[] a) {
        if (start == end) return 0;
        //if (start > end) return 0;

        if (dp[start][end] != 0) return dp[start][end];
        long sum = 0;
        for (int i = start; i <= end; i++) sum += a[i];

        long min = Long.MAX_VALUE;
        for (int i = start; i < end; i++) {
            min = Math.min(min, sum + backtrack(dp, start, i, a) + backtrack(dp, i + 1, end, a));
        }
        dp[start][end] = min;
        return dp[start][end];
    }
}
