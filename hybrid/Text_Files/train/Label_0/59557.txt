import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static String line;
	static final int MOD = 100000007;

	static long solve(int len, int loop) {
		long ret = 0;
		long[] dp = new long[len + 1];
		dp[0] = 1;
		for (int i = 1; i <= len; ++i) {
			for (int j = 1; j <= Math.min(loop, i); ++j) {
				dp[i] += dp[i - j];
			}
			dp[i] %= MOD;
			if ((len - i) % loop == 0) {
				ret += dp[i];
				ret %= MOD;
			}
		}
		return ret;
	}

	static int solve() {
		long ans = 1;
		int prev = 0;
		for (int i = 1; i < line.length(); ++i) {
			if (line.charAt(i) != line.charAt(i - 1)) {
				ans *= solve(i - prev, loop(line.charAt(prev)));
				ans %= MOD;
				prev = i;
			}
		}
		ans *= solve(line.length() - prev, loop(line.charAt(prev)));
		ans %= MOD;
		return (int) ans;
	}

	static int loop(char c) {
		return c == '8' || c == '0' ? 3 : 5;
	}

	public static void main(String[] args) throws Exception {
		while (true) {
			line = sc.next();
			if (line.equals("#")) break;
			System.out.println(solve());
		}
	}
}