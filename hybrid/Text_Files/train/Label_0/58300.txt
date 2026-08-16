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
		TaskF solver = new TaskF();
		solver.solve(1, in, out);
		out.close();
	}

	static class TaskF {
		final int MOD = (int) (1e9 + 7);

		public void solve(int testNumber, FastScanner in, PrintWriter out) {
			int n = in.nextInt();
			int D = in.nextInt();
			int[] p = new int[n];
			int[] firstChild = new int[n];
			int[] nextSibling = new int[n];
			Arrays.fill(firstChild, -1);
			for (int i = 1; i < n; i++) {
				p[i] = in.nextInt() - 1;
				nextSibling[i] = firstChild[p[i]];
				firstChild[p[i]] = i;
			}
			final int k = n + 1;
			// Exactly.
			int[][] f = new int[n][k];
			// Up to. (prefix sums of f)
			int[][] g = new int[n][k];
			for (int i = n - 1; i >= 0; i--) {
				for (int j = 0; j < k; j++) {
					long cur = 1;
					for (int c = firstChild[i]; c >= 0; c = nextSibling[c]) {
						cur = cur * g[c][j] % MOD;
					}
					f[i][j] = (int) cur;
				}
				for (int j = 0; j < k; j++) {
					g[i][j] = f[i][j];
					if (j > 0) {
						g[i][j] += g[i][j - 1];
						if (g[i][j] >= MOD) {
							g[i][j] -= MOD;
						}
					}
				}
			}

			int[] x = new int[k];
			int[] y = new int[k];
			for (int i = 0; i < k; i++) {
				x[i] = i;
				y[i] = g[0][i];
			}
			TaskF.Interpolation.Polynom poly = new TaskF.Interpolation().interpolationNewton(x, y);
			out.println(poly.eval(D - 1));
		}

		static class Interpolation {
			final int N = 5000;
			final int[] inv = new int[N];
			final int MOD = (int) (1e9 + 7);

			Interpolation() {
				inv[1] = 1;
				for (int i = 2; i < N; i++) {
					inv[i] = (int) ((MOD - (MOD / i) * (long) inv[MOD % i] % MOD) % MOD);
				}
			}

			private Polynom interpolationNewton(int[] x, int[] y) {
				int n = x.length - 1;
				Polynom[] newt = new Polynom[x.length];
				newt[0] = new Polynom(n);
				newt[0].coef[0] = 1;
				for (int i = 1; i < x.length; i++) {
					Polynom p = new Polynom(n);
					p.coef[0] = -x[i - 1];
					if (p.coef[0] < 0) {
						p.coef[0] += MOD;
					}
					p.coef[1] = 1;
					newt[i] = newt[i - 1].multiply(p, 1 /* deg */);
				}
				// Divided differences.
				int[][] ys = new int[x.length][x.length];
				for (int len = 1; len <= x.length; len++) {
					for (int start = 0; start + len <= x.length; start++) {
						int l = start;
						int r = start + len - 1;
						if (len == 1) {
							ys[l][r] = y[l];
							continue;
						}
						int dys = (ys[l + 1][r] - ys[l][r - 1]) % MOD;
						if (dys < 0) {
							dys += MOD;
						}
						int dx = (x[r] - x[l]) % MOD;
						if (dx < 0) {
							dx += MOD;
						}
						ys[l][r] = (int) (dys * (long) inv(dx) % MOD);
					}
				}
				Polynom res = new Polynom(n);
				for (int i = 0; i < x.length; i++) {
					// res = res.add(newt[i].multiply(ys[0][i]));
					addTo(res, newt[i], ys[0][i]);
				}
				return res;
			}

			private void addTo(Polynom a, Polynom b, long coef) {
				if (a.coef.length != b.coef.length) {
					throw new AssertionError();
				}
				for (int i = 0; i < a.coef.length; i++) {
					a.coef[i] = (int) ((a.coef[i] + coef * b.coef[i]) % MOD);
				}
			}

			private int inv(int x) {
				if (x < N) {
					return inv[x];
				}
				return pow(x, MOD - 2);
			}

			private int pow(long a, long n) {
				long r = 1;
				while (n > 0) {
					if (n % 2 == 1) {
						r = r * a % MOD;
					}
					a = a * a % MOD;
					n /= 2;
				}
				return (int) r;
			}

			class Polynom {
				int[] coef;

				public Polynom(int deg) {
					coef = new int[deg + 1];
				}

				public int eval(int x) {
					long res = 0;
					long p = 1;
					for (int i = 0; i < coef.length; i++) {
						res = (res + coef[i] * p) % MOD;
						p = p * x % MOD;
					}
					return (int) res;
				}

				public Polynom multiply(Polynom p, int deg) {
					if (coef.length != p.coef.length) {
						throw new AssertionError();
					}
					Polynom res = new Polynom(coef.length - 1);
					for (int i = 0; i < coef.length; i++) {
						for (int j = 0; i + j < coef.length && j <= deg; j++) {
							res.coef[i + j] = (int) ((res.coef[i + j] + coef[i] * (long) p.coef[j]) % MOD);
						}
					}
					return res;
				}

			}

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

		public int nextInt() {
			return Integer.parseInt(next());
		}

	}
}

