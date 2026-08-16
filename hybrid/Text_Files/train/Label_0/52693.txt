import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		FastScanner in = new FastScanner(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskD solver = new TaskD();
		solver.solve(1, in, out);
		out.close();
	}

	static class TaskD {
		FastScanner in;
		PrintWriter out;

		public void solve(int testNumber, FastScanner in, PrintWriter out) {
			this.in = in;
			this.out = out;
			long k = in.nextLong();
			solve(k);
//		for (int i = 1; i < 10000; i++) {
//			solve(i);
//		}
		}

		private void solve(long k) {
			long[] a = construct(k);
			if (!check(a.clone(), k)) {
				throw new AssertionError("" + k);
			}
			out.println(a.length);
			for (int i = 0; i < a.length; i++) {
				if (i > 0) {
					out.print(" ");
				}
				out.print(a[i]);
			}
			out.println();
		}

		private long[] construct(long k) {
			int n = 50;
			long[] a = new long[n];
			for (int i = 0; i < n; i++) {
				a[i] += k / n + i;
				if (i >= k % n) {
					continue;
				}
				a[i] += n;
				for (int j = 0; j < n; j++) {
					if (j != i) {
						a[j] -= 1;
					}
				}
			}
			return a;
		}

		boolean check(long[] a, long k) {
			int n = a.length;
			long ans = 0;
			while (true) {
				boolean changed = false;
				for (int i = 0; i < n; i++) {
					if (a[i] < n) {
						continue;
					}
					changed = true;
					long x = a[i] / n;
					a[i] -= n * x;
					ans += x;
					for (int j = 0; j < n; j++) {
						if (j != i) {
							a[j] += x;
						}
					}
				}
				if (!changed) {
					break;
				}
			}
			return ans == k;
		}

	}

	static class FastScanner {
		private BufferedReader in;
		private StringTokenizer st;

		public FastScanner(InputStream stream) {
			in = new BufferedReader(new InputStreamReader(stream));
		}

		public String next() {
			while (st == null || !st.hasMoreTokens()) {
				try {
					String rl = in.readLine();
					if (rl == null) {
						return null;
					}
					st = new StringTokenizer(rl);
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return st.nextToken();
		}

		public long nextLong() {
			return Long.parseLong(next());
		}

	}
}

