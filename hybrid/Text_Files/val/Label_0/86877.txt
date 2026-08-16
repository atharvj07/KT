import java.io.IOException;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

class Main {
	public static void main(String[] args) throws IOException {
		new Main().run();
	}

	long INF = (long) (1e19);

	void run() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		long k = sc.nextLong();
		INF = k + 1;
		long[] f = new long[m + 1];
		f[0] = 1;
		char[][] s = new char[n][];
		for (int i = 0; i < n; ++i) {
			s[i] = sc.next().toCharArray();
		}
		for (int j = 0; j < m; ++j) {
			for (int i = 0; i < n; ++i) {
				if (j + s[i].length > m)
					continue;
				f[j + s[i].length] = add(f[j + s[i].length], f[j]);
			}
		}
		if (f[m] < k) {
			System.out.println("-");
			return;
		}
		boolean[][] cap = new boolean[n][m + 1];
		for (int i = 0; i < n; ++i) {
			cap[i][0] = true;
		}
		String ans = "";
		long[] g = new long[m + 1];
		g[0] = 1;
		boolean[][] h = new boolean[n][];
		for (int i = 0; i < n; ++i) {
			h[i] = new boolean[s[i].length + 1];
			if (s[i].length <= m) {
				h[i][0] = true;
			}
		}
		for (int T = 0; T < m; ++T) {
			char c = '*';
			long sum = 0;
			boolean flag = false;
			for (int i = 0; i < 26; ++i) {
				c = (char) ('a' + i);
				long tmp = 0;
				for (int u = 0; u < n; ++u) {
					for (int v = 1; v <= Math.min(s[u].length, T + 1); ++v) {
						if (h[u][v - 1] && s[u][v - 1] == c) {
							tmp = add(tmp, mul(g[T + 1 - v], f[m - (T + 1) - (s[u].length - v)]));
						}
					}
				}
				if (add(tmp, sum) >= k) {
					k -= sum;
					flag = true;
					break;
				}
				sum = add(sum, tmp);
			}
			if (!flag)
				throw new AssertionError();
			ans += c;
			if (k == 0)
				break;
			for (int i = 0; i < n; ++i) {
				for (int j = h[i].length - 1; j >= 1; --j) {
					h[i][j] = s[i][j - 1] == c && h[i][j - 1];
				}
			}
			for (int i = 0; i < n; ++i) {
				h[i][0] = T + s[i].length + 1 <= m;
			}
			for (int i = 0; i < n; ++i) {
				if (h[i][s[i].length]) {
					g[T + 1] = add(g[T + 1], g[T + 1 - s[i].length]);
				}
			}
		}
		System.out.println(ans);
	}

	long add(long a, long b) {
		if (a + b < 0 || a + b >= INF) {
			return INF;
		} else {
			return a + b;
		}
	}

	long mul(long a, long b) {
		if (a * b < 0 || a * b >= INF) {
			return INF;
		} else {
			return a * b;
		}
	}

	void solve(ArrayList<Integer>[] g, int h, int w) {
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}