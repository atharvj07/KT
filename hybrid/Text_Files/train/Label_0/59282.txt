import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		new Main().solver();
	}

	final long MOD = 1_000_000_007L;

	void solver() {
		Scanner sc = new Scanner(System.in);
		int d = sc.nextInt();
		int[] l = new int[d];
		for (int i = 0; i < d; i++) {
			l[i] = sc.nextInt();
		}
		Arrays.sort(l);
		int s = sc.nextInt();
		long[] dp = new long[90010];
		dp[s] = 1;

		for (int i = 0; i < d; i++) {
			for (int j = 0; j <= s; j++) {
				if (j - l[i] > 0)
					dp[j - l[i]] += MOD - dp[j];
				dp[j] %= MOD;
			}
		}
		long cut = 0;
		for (int i = 1; i <= s; i++) {
			long tmp = dp[i];
			for (int j = 0; j < d; j++) {
				tmp = (tmp * i) % MOD;
			}
			cut = (cut + tmp) % MOD;
		}
		System.out.println(cut);
	}
}