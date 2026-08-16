import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.System.exit;
import static java.util.Arrays.fill;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

	static void solve() throws Exception {
		int n = scanInt(), m = scanInt(), t = scanInt();
		int x[] = new int[m], y[] = new int[m];
		for (int i = 0; i < m; i++) {
			x[i] = scanInt() - 1;
			y[i] = scanInt() - 1;
		}
		char ans[] = new char[m];
		fill(ans, '^');
		switch (t) {
		case 1:
		{
			int nn = (n + 63) >> 6;
			long sets[][] = new long[n][nn];
			for (int i = 0; i < n; i++) {
				sets[i][i >> 6] |= 1L << i;
			}
			for (int i = 0; i < m; i++) {
				long s1[] = sets[x[i]], s2[] = sets[y[i]];
				for (int j = 0; j < nn; j++) {
					s1[j] = s2[j] = s1[j] | s2[j];
				}
			}
			int o = -1;
			i: for (int i = 0; i < n; i++) {
				long s[] = sets[i];
				for (int j = 0; j < nn - 1; j++) {
					if (s[j] != -1) {
						continue i;
					}
				}
				if (s[nn - 1] != -1L >>> -n) {
					continue;
				}
				o = i;
				break;
			}
			if (o < 0) {
				out.print(-1);
				return;
			}
			boolean cur[] = new boolean[n];
			cur[o] = true;
			for (int i = m - 1; i >= 0; i--) {
				if (cur[x[i]] && !cur[y[i]]) {
					cur[y[i]] = true;
				} else if (cur[y[i]] && !cur[x[i]]) {
					cur[x[i]] = true;
					ans[i] = 'v';
				}
			}
		}
		break;
		case 2:
		{
			if (n == 2) {
				out.print(-1);
				return;
			}
			int next[] = new int[n], xNext[] = new int[m], yNext[] = new int[m];
			fill(next, -1);
			for (int i = m - 1; i >= 0; i--) {
				xNext[i] = next[x[i]];
				yNext[i] = next[y[i]];
				next[x[i]] = next[y[i]] = i;
			}
			int a = 0, b;
			for (b = 1; next[b] >= 0 && next[b] == next[a]; b++) { }
			int aNext = next[a], bNext = next[b];
			while (aNext >= 0 && bNext >= 0) {
				if (aNext < bNext) {
					if (xNext[aNext] == bNext) {
						ans[aNext] = 'v';
						aNext = yNext[aNext];
					} else {
						aNext = xNext[aNext];
					}
				} else {
					if (xNext[bNext] == aNext) {
						ans[bNext] = 'v';
						bNext = yNext[bNext];
					} else {
						bNext = xNext[bNext];
					}
				}
			}
		}
		break;
		default:
			throw new AssertionError();
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