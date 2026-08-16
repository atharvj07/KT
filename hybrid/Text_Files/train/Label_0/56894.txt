import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	public static void main(String[] args) {
		new Main().run();
	}
	final static int MOD = (int)1e9 + 7;
	int addMod(int a, int b) {
		return a + b >= MOD ? a + b - MOD : a + b;
	}
	int mulMod(int a, int b) {
		return (int)((long)a * b % MOD);
	}
	int subMod(int a, int b) {
		return a < b ? a + MOD - b : a - b;
	}
	int sign(int x) {
		return x == 3 ? 2 : x > 0 ? 1 : 0;
	}
	void run() {
		InputReader in = new InputReader(System.in);
		PrintWriter out = new PrintWriter(System.out);

		int n = in.nextInt(), m = in.nextInt();
		int[][][] dp = new int[n + 1][n + 1][4];
		int[][] comb = new int[n + 1][n + 1];
		for (int i = 0; i <= n; ++i) {
			comb[i][0] = comb[i][i] = 1;
			for (int j = 1; j < i; ++j)
				comb[i][j] = addMod(comb[i - 1][j - 1], comb[i - 1][j]);
		}

		dp[1][0][0] = 1;
		for (int i = 1; i < n; ++i)
			for (int j = 0; j <= i; ++j)
				for (int k = 0; k < 4; ++k)
					if (dp[i][j][k] > 0)
						for (int l = 0; l < 4; ++l) {
							int x = j + sign(l);

							if (l == 0 || k == 0 || k == l && k != 3) {
								dp[i + 1][x][l] = addMod(dp[i + 1][x][l], dp[i][j][k]);
							}
						}
		int[] ways = new int[n + 1];
		int[] fact = new int[n + 1];
		fact[0] = 1;
		for (int i = 1; i <= n; ++i)
			fact[i] = mulMod(fact[i - 1], i);
		for (int i = 0; i <= n; ++i) {
			int val = 0;
			for (int j = 0; j < 4; ++j)
				val = addMod(val, dp[n][i][j]);
			ways[i] = mulMod(val, fact[n - i]);
		}

		for (int i = n; i >= 0; --i)
			for (int j = i + 1; j <= n; ++j)
				ways[i] = subMod(ways[i], mulMod(comb[j][i], ways[j]));

		out.println(ways[m]);

		out.close();
	}
}

class InputReader {
	BufferedReader buff;
	StringTokenizer tokenizer;

	InputReader(InputStream stream) {
		buff = new BufferedReader(new InputStreamReader(stream));
		tokenizer = null;
	}
	boolean hasNext() {
		while (tokenizer == null || !tokenizer.hasMoreTokens())
			try {
				tokenizer = new StringTokenizer(buff.readLine());
			}
			catch (Exception e) {
				return false;
			}
		return true;
	}
	String next() {
		if (!hasNext())
			throw new RuntimeException();
		return tokenizer.nextToken();
	}
	int nextInt() { return Integer.parseInt(next()); }
	long nextLong() { return Long.parseLong(next()); }
}

