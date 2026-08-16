import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.Math.min;
import static java.lang.System.exit;
import static java.util.Arrays.fill;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

	static void solve() throws Exception {
		int n = scanInt();
		boolean have[][] = new boolean[n + 2][n + 2];
		int dist[][] = new int[n + 2][n + 2];
		for (int i = 1; i <= n; i++) {
			fill(have[i], 1, n + 1, true);
			for (int j = 1; j <= n; j++) {
				dist[i][j] = min(min(i, n + 1 - i), min(j, n + 1 - j));
			}
		}
		int queue[] = new int[4 * n * n];
		int ans = 0;
		for (int it = 0; it < n * n; it++) {
			int cur = scanInt() - 1;
			int si = cur / n + 1, sj = cur % n + 1;
			have[si][sj] = false;
			ans += --dist[si][sj];
			int queueHead = 2 * n * n, queueTail = queueHead + 2;
			queue[queueHead] = si;
			queue[queueHead + 1] = sj;
			do {
				int i = queue[queueHead++], j = queue[queueHead++], d = dist[i][j];
				if (have[i - 1][j]) {
					if (dist[i - 1][j] > d + 1) {
						dist[i - 1][j] = d + 1;
						queue[queueTail++] = i - 1;
						queue[queueTail++] = j;
					}
				} else {
					if (dist[i - 1][j] > d) {
						dist[i - 1][j] = d;
						queue[--queueHead] = j;
						queue[--queueHead] = i - 1;
					}
				}
				if (have[i + 1][j]) {
					if (dist[i + 1][j] > d + 1) {
						dist[i + 1][j] = d + 1;
						queue[queueTail++] = i + 1;
						queue[queueTail++] = j;
					}
				} else {
					if (dist[i + 1][j] > d) {
						dist[i + 1][j] = d;
						queue[--queueHead] = j;
						queue[--queueHead] = i + 1;
					}
				}
				if (have[i][j - 1]) {
					if (dist[i][j - 1] > d + 1) {
						dist[i][j - 1] = d + 1;
						queue[queueTail++] = i;
						queue[queueTail++] = j - 1;
					}
				} else {
					if (dist[i][j - 1] > d) {
						dist[i][j - 1] = d;
						queue[--queueHead] = j - 1;
						queue[--queueHead] = i;
					}
				}
				if (have[i][j + 1]) {
					if (dist[i][j + 1] > d + 1) {
						dist[i][j + 1] = d + 1;
						queue[queueTail++] = i;
						queue[queueTail++] = j + 1;
					}
				} else {
					if (dist[i][j + 1] > d) {
						dist[i][j + 1] = d;
						queue[--queueHead] = j + 1;
						queue[--queueHead] = i;
					}
				}
			} while (queueHead < queueTail);
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