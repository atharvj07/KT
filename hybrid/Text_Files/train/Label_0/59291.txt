
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {

		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		int t = scanner.nextInt();
		int s = scanner.nextInt();
		int[] a = new int[n];
		int[] b = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = scanner.nextInt();
			b[i] = scanner.nextInt();
		}
		int[] dp = new int[t + 1];
		int ans = 0;
		for (int i = 0; i < n; i++)
			for (int j = t; j - b[i] >= 0; j--) {
				if (j - b[i] >= s || s >= j)
					dp[j] = Math.max(dp[j], dp[j - b[i]] + a[i]);
				ans = Math.max(ans, dp[j]);
			}
		System.out.println(ans);
	}
}