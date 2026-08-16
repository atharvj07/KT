import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static final int MOD = 1000000007;

	public static void main(String[] args) {
		int N = sc.nextInt();
		long[][][] dp = new long[N + 1][N + 1][N + 1];
		dp[0][0][0] = 1;
		int idx = 0;
		for (int i = 0; i < N; ++i) {
			char v = sc.next().charAt(0);
			if (v == '-') continue;
			++idx;
			if (v == 'D') {
				for (int j = 0; j < idx; ++j) {
					for (int k = 1; k < idx; ++k) {
						dp[idx][j][k] += dp[idx - 1][j][k] * j % MOD;
						if (j > 0) dp[idx][j - 1][k - 1] += dp[idx - 1][j][k] * j * k % MOD;
					}
				}
			} else {
				for (int j = 0; j < idx; ++j) {
					for (int k = 0; k < idx; ++k) {
						dp[idx][j + 1][k + 1] += dp[idx - 1][j][k];
						dp[idx][j][k] += dp[idx - 1][j][k] * j % MOD;
					}
				}
			}
		}
		System.out.println(dp[idx][0][0] % MOD);
	}
}