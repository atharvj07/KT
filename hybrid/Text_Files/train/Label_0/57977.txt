import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.println(solve());
	}

	static long solve() {
		long M = sc.nextLong();
		int rd = sc.nextInt();
		int rr = sc.nextInt();
		long cd = sc.nextLong();
		long cr = sc.nextLong();
		long minD = (cd * 100 + rd - 1) / rd;
		long minR = (cr * 100 + rr - 1) / rr;
		if (M < minD + minR) return -1;
		long ans = 0;
		for (int i = 0; i < 100; ++i) {
			long yd = minD + i;
			long md = yd * rd / 100;
			for (int j = 0; j < 100; ++j) {
				long yr = minR + j;
				if (M < yd + yr) break;
				long mc = yr * rr / 100;
				long rem = M - yd - yr;
				rem += (md - cd) * 100 / rd;
				rem += (mc - cr) * 100 / rr;
				ans = Math.max(ans, rem);
			}
		}
		return ans;
	}

}