import static java.lang.Math.*;
import static java.util.Arrays.*;
import java.util.*;
import java.io.*;

public class Main {

	void tr(Object... os) {
		System.err.println(deepToString(os));
	}
	public static void main(String[] args) {
		try {
			System.setIn(new FileInputStream("src/aoj2106/input.txt"));
			//System.setOut(new PrintStream(new FileOutputStream("src/aoj2106/result.txt")));
		} catch (FileNotFoundException e) {
		}
		new Main().run();
	}


	Scanner sc;
	void run() {
		sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (;t-->0;) {
			solve();
		}
	}

	void solve()
	{
		int n = sc.nextInt();
		int[] e = new int[n];
		for (int i = 0; i < n; i++) e[i] = sc.nextInt();

		int[][] dp = new int[n+1][401]; // dp[i][k] := i-1番目が k のとき i番目のエネルギーの最大値
		for (int i = 0; i < dp.length; i++) {
			fill(dp[i], -1);
		}
		dp[0][0] = e[0];

		for (int i = 0; i < n - 1; i++) {
			for (int k = 0; k <= 400; k++) if (dp[i][k] >= 0) {
				int cur = dp[i][k];

				// not excitation
				dp[i+1][cur] = max(dp[i+1][cur], e[i+1]);

				// excition
				if (i > 0 && cur > 0) {
					dp[i+1][cur - 1] = max(dp[i+1][cur-1], e[i+1] + k);
				}
			}
		}
		int ans = 0;
		for (int i = 0; i <= 400; i++) {
			ans = max(ans, dp[n-1][i]);
		}
		System.out.println(ans);
	}


}