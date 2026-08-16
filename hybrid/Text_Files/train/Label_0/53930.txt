import java.util.Arrays;
import java.util.Scanner;

public class Main {
	final int INF = 1 << 28;

	void run() {
		Scanner sc = new Scanner(System.in);
		final int MAX = 1000 * 1000 + 1;
		boolean isPrime[] = new boolean[MAX];
		Arrays.fill(isPrime, true);
		int[] primes = new int[MAX];
		int idx = 0;
		for (int i = 2; i < MAX; i++) {
			if (isPrime[i]) {
				primes[idx++] = i;
				for (int j = i + i; j < MAX; j += i) {
					isPrime[j] = false;
				}
			}
		}
		while (true) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			if ((a | b) == 0)
				break;
			int i = 0;
			int sum = 0;
			int last = 0;
			int a_key = 0;
			while (true) {
				if (primes[i] > a || primes[i] == 0) {
					a_key = last - sum;
					break;
				}
				if (a % primes[i] == 0) {
					sum += last;
					last = primes[i];
				}
				i++;
			}
			sum = 0;
			last = 0;
			i = 0;
			int b_key = 0;
			while (true) {
				if (primes[i] > b || primes[i] == 0) {
					b_key = last - sum;
					break;
				}
				if (b % primes[i] == 0) {
					sum += last;
					last = primes[i];
				}
				i++;
			}
			System.out.println(a_key > b_key ? "a" : "b");
		}
	}

	public static void main(String[] args) throws Exception {
		new Main().run();
	}
}