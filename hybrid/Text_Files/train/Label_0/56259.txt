import java.util.Arrays;
import java.util.Scanner;

public class TaskE {

	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);

		int n = s.nextInt();
		long W = s.nextInt();
		long B = s.nextInt();
		long X = s.nextInt();

		int[] c = new int[n];
		int sumC = 0;
		for (int i = 0; i < n; i++) {
			c[i] = s.nextInt();
			sumC += c[i];
		}

		long[] cost = new long[n];
		for (int i = 0; i < n; i++) {
			cost[i] = s.nextInt();
		}

		// Idea: We use a DP table of size n * max possible birds (sumC), DP[i][j] is
		// the max amount of mana left for summoning j birds for the first i trees.

		long[][] DP = new long[n][sumC + 1];

		// init -1
		for (long[] a : DP) {
			Arrays.fill(a, -1);
		}

		// init for the first tree
		for (int j = 0; j < sumC + 1; j++) {
			DP[0][j] = (W - cost[0] * j >= 0 && j <= c[0]) ? (W - cost[0] * j) : -1;
			if (DP[0][j] > W + j * B) {
				DP[0][j] = W + j * B;
			}
		}

		// init for 0 birds summoned
		for (int i = 0; i < n; i++) {
			DP[i][0] = W;
		}

		//System.out.println(Arrays.toString(DP[0]));
		for (int i = 1; i < n; i++) {
			for (int j = 1; j < sumC + 1; j++) {
				for (int k = 0; k <= c[i]; k++) {
					if (j - k < 0) {
						break;
					}
					if (DP[i - 1][j - k] >= 0) {
						DP[i][j] = Math.max(DP[i][j], Math.min(DP[i - 1][j - k] + X, W + (j - k) * B) - k * cost[i]);
					}
				}
			}

			//System.out.println(Arrays.toString(DP[i]));
		}

		// printout result
		int i = sumC;
		while (DP[n - 1][i] < 0) {
			i--;
		}
		System.out.println(i);

	}

}
