import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.Math.min;
import static java.lang.System.exit;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

	static final int MOD = 1000000007;

	static int add(int a, int b) {
		int res = a + b;
		return res >= MOD ? res - MOD : res;
	}

	static int sub(int a, int b) {
		int res = a - b;
		return res < 0 ? res + MOD : res;
	}

	static int mul(int a, int b) {
		int res = (int) ((long) a * b % MOD);
		return res < 0 ? res + MOD : res;
	}

	static int fib(int i) {
		int c0 = 0, c1 = 1;
		while (i-- > 0) {
			int c2 = add(c0, c1);
			c0 = c1;
			c1 = c2;
		}
		return c0;
	}

	static void solve() throws Exception {
		int n = scanInt(), m = scanInt();
		String s = scanString();
		char c1 = s.charAt(0);
		boolean diff = false;
		int cnt = 1, cntMin = Integer.MAX_VALUE;
		for (int i = 1; i < m; i++) {
			if (s.charAt(i) == c1) {
				++cnt;
			} else {
				if (cnt % 2 == 1 || !diff) {
					cntMin = min(cntMin, cnt);
				}
				diff = true;
				cnt = 0;
			}
		}
		int ans;
		if (diff) {
			if (n % 2 == 0) {
				n /= 2;
				ans = 0;
				int k = cntMin / 2;
//				System.err.println(n + " " + k);
				int dyn[] = new int[k + 1];
				dyn[0] = 1;
				int sum = 1;
				for (int i = 0; i < n; i++) {
//					System.err.println(i + " " + dyn[i % (k + 1)]);
					if (i + 1 + k >= n) {
						ans = add(ans, mul(dyn[i % (k + 1)], n - i));
					}
					int v = sum;
					sum = sub(sum, dyn[(i + 1) % (k + 1)]);
					dyn[(i + 1) % (k + 1)] = v;
					sum = add(sum, v);
				}
				ans = add(ans, ans);
			} else {
				ans = 0;
			}
		} else {
			ans = add(fib(n - 1), fib(n + 1));
		}
		out.print(ans);
	}

	static int scanInt() throws IOException {
		return parseInt(scanString());
	}

	static long scanLong() throws IOException {
		return parseLong(scanString());
	}

	static String scanString() throws IOException {
		while (tok == null || !tok.hasMoreTokens()) {
			tok = new StringTokenizer(in.readLine());
		}
		return tok.nextToken();
	}

	static BufferedReader in;
	static PrintWriter out;
	static StringTokenizer tok;

	public static void main(String[] args) {
		try {
			in = new BufferedReader(new InputStreamReader(System.in));
			out = new PrintWriter(System.out);
			solve();
			in.close();
			out.close();
		} catch (Throwable e) {
			e.printStackTrace();
			exit(1);
		}
	}
}