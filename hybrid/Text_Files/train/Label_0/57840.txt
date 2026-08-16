import java.util.Scanner;

/**
 * Contest: Codeforces Round #518
 *
 * @author Arturs Licis
 */
public class ProblemB {
	public static long gcd(long a, long b) {
		if (b == 0) return a;
		return gcd(b, a % b);
	}

	public static long lcm(long a, long b) {
		return a * (b / gcd(a, b));
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long b = sc.nextLong();

		// long b = 13003;
		int cnt = 0;
		for (long i = 1; i <= Math.sqrt(b); i++) {
			if (b % i == 0) {
				cnt++;
				if (b / i != i) cnt++;
			}
		}


		System.out.println(cnt);
	}
}