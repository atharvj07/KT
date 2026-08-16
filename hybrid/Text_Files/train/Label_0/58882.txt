import java.io.*;
import java.util.*;

public class CF1497D extends PrintWriter {
	CF1497D() { super(System.out); }
	Scanner sc = new Scanner(System.in);
	public static void main(String[] $) {
		CF1497D o = new CF1497D(); o.main(); o.flush();
	}

	void main() {
		int t = sc.nextInt();
		while (t-- > 0) {
			int n = sc.nextInt();
			int[] aa = new int[n];
			for (int i = 0; i < n; i++)
				aa[i] = sc.nextInt();
			int[] ss = new int[n];
			for (int i = 0; i < n; i++)
				ss[i] = sc.nextInt();
			long[] dp = new long[n];
			for (int j = 0; j < n; j++)
				for (int i = j - 1; i >= 0; i--)
					if (aa[i] != aa[j]) {
						int s = Math.abs(ss[i] - ss[j]);
						long x = dp[i], y = dp[j];
						dp[j] = Math.max(dp[j], x + s);
						dp[i] = Math.max(dp[i], y + s);
					}
			long ans = 0;
			for (int i = 0; i < n; i++)
				ans = Math.max(ans, dp[i]);
			println(ans);
		}
	}
}
