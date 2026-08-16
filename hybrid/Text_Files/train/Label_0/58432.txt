import java.util.Arrays;
import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int maxW = sc.nextInt();
		
		int[] w = new int[n + 1];
		int[] v = new int[n + 1];
		int sumV = 0;
		for (int i = 1; i <= n; i++) {
			w[i] = sc.nextInt();
			v[i] = sc.nextInt();
			sumV += v[i];
		}
		
		long[][] dp = new long[n + 1][sumV + 1];
		for (int i = 1; i <= sumV; i++)
			dp[0][i] = Integer.MAX_VALUE;
		
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= sumV; j++) {
				dp[i][j] = dp[i - 1][j];
				if (j - v[i] >= 0)
					dp[i][j] = Math.min(dp[i][j], dp[i - 1][j - v[i]] + w[i]);
			}
		}
		
		long ans = 0;
		for (int i = sumV; i >= 0; i--) {
			if (dp[n][i] <= maxW) {
				ans = i;
				break;
			}
		}
		
		System.out.println(ans);
//		for (long[] arr : dp)
//			System.out.println(Arrays.toString(arr));
		
		sc.close();
	}
}

