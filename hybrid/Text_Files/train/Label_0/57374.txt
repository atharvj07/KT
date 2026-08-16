import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] g = { 2, 3, 5, 10, 12, 15 };
        int[] a = { 380, 550, 850, 1520, 1870, 2244 };
        int[] dp = new int[51];
        Arrays.fill(dp, 10000);
        dp[0] = 0;
        for (int i = 0; i < dp.length - 1; i++) {
            for (int j = 0; j < g.length; j++) {
                if (i + g[j] > dp.length - 1) continue;
                dp[i + g[j]] = Math.min(dp[i + g[j]], dp[i] + a[j]);
            }
        }
        while (true) {
            int n = sc.nextInt();
            if (n == 0) {
                break;
            }
            System.out.println(dp[n / 100]);
        }
        sc.close();
    }
}
