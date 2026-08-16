import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.System.exit;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

	static final int MOD = 998244353;

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

	static int pow(int a, int e) {
		if (e == 0) {
			return 1;
		}
		int r = a;
		for (int i = 30 - Integer.numberOfLeadingZeros(e); i >= 0; i--) {
			r = mul(r, r);
			if ((e & (1 << i)) != 0) {
				r = mul(r, a);
			}
		}
		return r;
	}

	static int inv(int a) {
		return pow(a, MOD - 2);
	}

	static void solve() throws Exception {
		int n = scanInt();
		int m = 1 << n;
		int a[] = new int[m];
		int s = 0;
		for (int i = 0; i < m; i++) {
			s = add(s, a[i] = scanInt());
		}
		for (int i = 0; i < n; i++) {
			int mask = m - 1 - (1 << i);
			for (int j = mask;; j = (j - 1) & mask) {
				int x = a[j], y = a[j + (1 << i)];
				a[j] = add(x, y);
				a[j + (1 << i)] = sub(x, y);
				if (j == 0) {
					break;
				}
			}
		}
		for (int i = 1; i < m; i++) {
			a[i] = mul(mul(m, s), inv(sub(a[i], s)));
		}
		for (int i = 0; i < n; i++) {
			int mask = m - 1 - (1 << i);
			for (int j = mask;; j = (j - 1) & mask) {
				int x = a[j], y = a[j + (1 << i)];
				a[j] = add(x, y);
				a[j + (1 << i)] = sub(x, y);
				if (j == 0) {
					break;
				}
			}
		}
		int norm = inv(m);
		int sub = mul(a[0], norm);
		for (int i = 0; i < m; i++) {
			out.println(sub(mul(a[i], norm), sub));
		}
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