import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
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
		TaskC solver = new TaskC();
		int testCount = Integer.parseInt(in.next());
		for (int i = 1; i <= testCount; i++)
			solver.solve(i, in, out);
		out.close();
	}

	static class TaskC {
		public void solve(int testNumber, FastScanner in, PrintWriter out) {
			int k = in.nextInt();
			int[] s = readPermutation(in);
			int[] a = readPermutation(in);
			int[] b = readPermutation(in);
			int n = s.length;
			int[] p = new int[k];
			Arrays.fill(p, -1);
			boolean[] used = new boolean[k];
			if (!canExtend(s, p.clone(), used, a)) {
				out.println("NO");
				return;
			}
			int pos = 0;
			for (int step = 0; step < k; step++) {
				while (pos < n && p[s[pos]] >= 0) {
					++pos;
				}
				if (pos == n) {
					break;
				}
				for (int i = 0; i < k; i++) {
					if (used[i]) {
						continue;
					}
					p[s[pos]] = i;
					used[i] = true;
					if (canExtend(s, p.clone(), used, a)) {
						break;
					}
					p[s[pos]] = -1;
					used[i] = false;
				}
			}
			for (int i = 0; i < n; i++) {
				s[i] = p[s[i]];
			}
			if (compare(s, b) > 0) {
				out.println("NO");
				return;
			}
			char[] ans = new char[k];
			for (int i = 0; i < k; i++) {
				if (p[i] < 0) {
					for (int j = 0; j < k; j++) {
						if (!used[j]) {
							used[j] = true;
							p[i] = j;
							break;
						}
					}
				}
				ans[i] = (char) (p[i] + 'a');
			}
			out.println("YES");
			out.println(new String(ans));
		}

		private int compare(int[] a, int[] b) {
			for (int i = 0; i < a.length; i++) {
				if (a[i] != b[i]) {
					return a[i] < b[i] ? -1 : 1;
				}
			}
			return 0;
		}

		private boolean canExtend(int[] s, int[] p, boolean[] used, int[] a) {
			int n = s.length;
			int k = p.length;
			int last = k - 1;
			for (int i = 0; i < n; i++) {
				if (p[s[i]] >= 0) {
					continue;
				}
				while (used[last]) {
					--last;
				}
				p[s[i]] = last;
				--last;
			}

			int[] ns = new int[n];
			for (int i = 0; i < n; i++) {
				ns[i] = p[s[i]];
			}
			return compare(ns, a) >= 0;
		}

		private int[] readPermutation(FastScanner in) {
			String s = in.next();
			int[] p = new int[s.length()];
			for (int i = 0; i < s.length(); i++) {
				p[i] = (int) (s.charAt(i) - 'a');
			}
			return p;
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
					st = new StringTokenizer(in.readLine());
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return st.nextToken();
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}

	}
}

