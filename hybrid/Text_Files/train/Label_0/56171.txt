import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int N = sc.nextInt();
		int[] P = new int[4];
		int[] T = new int[4];
		for (int i = 0; i < 4; i++) {
			P[i] = sc.nextInt();
		}
		for (int i = 0; i < 4; i++) {
			T[i] = sc.nextInt();
		}
		int[] dp = new int[201];
		Arrays.fill(dp, 200000);
		dp[0] = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j + T[i] < dp.length; j++) {
				dp[j + T[i]] = Math.min(dp[j + T[i]], dp[j] + P[i]);
			}
		}
		int ans = Integer.MAX_VALUE;
		for (int i = N; i < dp.length; i++) {
			ans = Math.min(ans, dp[i]);
		}
		System.out.println(ans);
	}

}

