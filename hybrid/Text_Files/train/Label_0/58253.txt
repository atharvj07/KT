import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int C, D, W, X;
	static int[][] E, F;

	public static void main(String[] args) throws Exception {
		while (true) {
			C = sc.nextInt();
			D = sc.nextInt();
			W = sc.nextInt();
			X = sc.nextInt();
			if (C == 0) break;
			E = new int[C][D];
			F = new int[C][D];
			for (int i = 0; i < C; ++i) {
				for (int j = 0; j < D; ++j) {
					E[i][j] = sc.nextInt();
				}
			}
			for (int i = 0; i < C; ++i) {
				for (int j = 0; j < D; ++j) {
					F[i][j] = sc.nextInt();
				}
			}
			System.out.println(solve());
		}
	}

	static int solve() {
		int[][][] dp = new int[D + 1][W + 1][X + 1];
		for (int[][] a : dp) {
			for (int[] aa : a) {
				Arrays.fill(aa, -1);
			}
		}
		dp[0][0][0] = 0;
		for (int i = 0; i < D; ++i) {
			for (int j = 0; j <= W; ++j) {
				for (int k = 0; k <= X; ++k) {
					dp[i + 1][j][k] = dp[i][j][k];
				}
			}
			for (int j = 0; j < C; ++j) {
				int gain = 0;
				int tire = 0;
				for (int k = j; k < C; ++k) {
					if (E[k][i] == 0) break;
					gain += E[k][i];
					tire += F[k][i];
					if (k == j) {
						for (int l = W - tire; l >= 0; --l) {
							for (int m = X; m >= 0; --m) {
								if (dp[i][l][m] >= 0) dp[i + 1][l + tire][m] = Math.max(dp[i + 1][l + tire][m], dp[i][l][m] + gain);
							}
						}
					} else {
						for (int l = W - tire; l >= 0; --l) {
							for (int m = X - 1; m >= 0; --m) {
								if (dp[i][l][m] >= 0)
									dp[i + 1][l + tire][m + 1] = Math.max(dp[i + 1][l + tire][m + 1], dp[i][l][m] + gain);
							}
						}
					}
				}
			}
		}
		int max = 0;
		for (int i = 0; i <= D; ++i) {
			for (int j = 0; j <= W; ++j) {
				for (int k = 0; k <= X; ++k) {
					max = Math.max(max, dp[i][j][k]);
				}
			}
		}
		return max;
	}

}