import java.util.Scanner;

public class Main {
	Scanner sc = new Scanner(System.in);

	void run() {
		int[] table = new int[17];
		for (int i = 1; i <= table.length; i++) table[i - 1] = i * i;
		int M = 300;
		int[] dp = new int[M];
		dp[0] = 1;
		for (int i = 0; i < table.length; i++) {
			for (int j = 0; j < M; j++) {
				if (j + table[i] < M) dp[j + table[i]] += dp[j];
			}
		}
		for (;;) {
			int n = sc.nextInt();
			if (n == 0) return;
			System.out.println(dp[n]);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}