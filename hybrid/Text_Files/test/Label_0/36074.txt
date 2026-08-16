import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		new Main().solver();
	}

	void solver() {
		Scanner sc = new Scanner(System.in);
		while (true) {
			long a = sc.nextLong();
			long b = sc.nextLong();
			long p = sc.nextLong();
			if (a == 0 && b == 0 && p == 0)
				break;
			long[] dp = new long[111111];
			dp[0] = 1;
			long ans = 0;
			for (long i = a; i <= b; i++) {
				if (i > a) {
					dp[(int) (i - a)] += dp[(int) (i - a - 1)];
				}
				ans += dp[(int) (i - a)];
				ans %= p;
				for (long j = i; j <= b; j *= 10) {
					long t = 1;
					while (t <= j)
						t *= 10;
					long l = Math.max(i - a + 1, j - a), r = Math.min(b - a + 1, t - a);
					dp[(int) l] += dp[(int) (i - a)];
					dp[(int) r] -= dp[(int) (i - a)];
					dp[(int) l] %= p;
					dp[(int) r] %= p;
				}
			}
			System.out.println(ans);
		}
	}
}