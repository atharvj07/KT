import java.io.*;
import java.util.*;

public class Main {

	void submit() {
		int n = nextInt();
		int[] a = new int[n];
		int[] b = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = nextInt() - 1;
		}
		for (int i = 0; i < n; i++) {
			b[i] = nextInt() - 1;
		}

		if (a[0] == b[0]) {
			out.println(0);
			return;
		}

		int[][] union = new int[n + 1][n + 1];

		for (int i = 0; i <= n; i++) {
			boolean[] have = new boolean[n];
			for (int j = 0; j < i; j++) {
				have[a[j]] = true;
			}
			int cnt = i;
			for (int j = 0; j <= n; j++) {
				if (j > 0) {
					if (!have[b[j - 1]]) {
						have[b[j - 1]] = true;
						cnt++;
					}
				}
				union[i][j] = cnt;
			}
		}

		int[][] dp = new int[n][n];
		for (int i = 0; i < n; i++) {
			Arrays.fill(dp[i], 1);
		}

		int[] posInB = new int[n];
		int[] posInA = new int[n];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (a[i] == b[j]) {
					posInB[i] = j;
					posInA[j] = i;
				}
			}
		}

		for (int t = 2; t <= n / 3; t++) {
			int[][] nxt = new int[n][n];
			for (int i = 1; i < n; i++) {
				for (int j = 1; j < n; j++) {
					do {
						int ways = 3 * t - union[i + 1][j + 1];
						if (ways <= 0) {
							break;
						}
						if (posInB[i] <= j || posInA[j] <= i) {
							break;
						}
						nxt[i][j] = (int) ((long) dp[i - 1][j - 1] * ways % P);
					} while (false);
					nxt[i][j] += nxt[i - 1][j];
					if (nxt[i][j] >= P) {
						nxt[i][j] -= P;
					}
					nxt[i][j] += nxt[i][j - 1] - nxt[i - 1][j - 1];
					if (nxt[i][j] >= P) {
						nxt[i][j] -= P;
					}
					if (nxt[i][j] < 0) {
						nxt[i][j] += P;
					}
				}
			}
			dp = nxt;
		}

		out.println((long) dp[n - 1][n - 1] * go(n / 3) % P);
	}

	int go(int n) {
		int[] dp = new int[2 * n + 1];
		dp[0] = 1;
		for (int i = 0; i < 3 * n; i++) {
			int[] nxt = new int[2 * n + 1];
			for (int j = 0; j <= 2 * n; j++) {
				if (j + 2 <= 2 * n) {
					nxt[j + 2] += dp[j];
					if (nxt[j + 2] >= P) {
						nxt[j + 2] -= P;
					}
				}
				if (j > 0) {
					nxt[j - 1] += (int)((long)dp[j] * j % P);
					if (nxt[j - 1] >= P) {
						nxt[j - 1] -= P;
					}
				}
			}
			dp = nxt;
		}
		return dp[0];
	}

	static final int P = 1_000_000_007;

	void preCalc() {

	}

	void stress() {

	}

	void test() {

	}

	Main() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		preCalc();
		submit();
		// stress();
		// test();
		out.close();
	}

	static final Random rng = new Random();

	static int rand(int l, int r) {
		return l + rng.nextInt(r - l + 1);
	}

	public static void main(String[] args) throws IOException {
		new Main();
	}

	BufferedReader br;
	PrintWriter out;
	StringTokenizer st;

	String nextToken() {
		while (st == null || !st.hasMoreTokens()) {
			try {
				st = new StringTokenizer(br.readLine());
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
		return st.nextToken();
	}

	String nextString() {
		try {
			return br.readLine();
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}

	int nextInt() {
		return Integer.parseInt(nextToken());
	}

	long nextLong() {
		return Long.parseLong(nextToken());
	}

	double nextDouble() {
		return Double.parseDouble(nextToken());
	}
}
