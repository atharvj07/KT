import static java.util.Arrays.deepToString;

import java.io.*;
import java.math.*;
import java.util.*;

import static java.lang.Math.max;

public class B {

	static double[] fact;

	static void solve() {
		int n = nextInt();
		int[] a = new int[n];
		int sum_a = 0;
		for (int i = 0; i < n; i++) {
			a[i] = nextInt();
			sum_a += a[i];
		}
		int p = nextInt();
		if (sum_a <= p) {
			writer.println(n);
			return;
		}
		fact = new double[n + 1];
		fact[0] = 1;
		for (int i = 1; i < fact.length; i++) {
			fact[i] = i * fact[i - 1];
		}
		double total = 0;
		for (int last = 0; last < n; last++) {
			int[] _a = new int[n - 1];
			for (int i = 0, cnt = 0; i < n; i++) {
				if (i != last) {
					_a[cnt++] = a[i];
				}
			}
			// debug(p, _a, a[last], get(p, _a, a[last]));
			total += get(p, _a, a[last]);
		}
		writer.println(total / fact[n]);
	}

	private static double get(int p, int[] a, int size) {
		int n = a.length;
		double[][][] d = new double[n + 1][n + 1][p + 1];
		d[0][0][0] = 1;
		for (int i = 0; i < n; i++) {
			for (int used = 0; used <= i; used++) {
				for (int filled = 0; filled <= p; filled++) {
					d[i + 1][used][filled] += d[i][used][filled];
					if (filled + a[i] <= p) {
						d[i + 1][used + 1][filled + a[i]] += d[i][used][filled];
					}
				}
			}
		}
		double ret = 0;
		for (int filled = max(0, p - size + 1); filled <= p; filled++) {
			for (int used = 0; used <= n; used++) {
				ret += d[n][used][filled] * used * fact[used] * fact[n - used];
				// if (d[n][used][filled] != 0) {
				// debug(n, used, filled, d[n][used][filled]);
				// }
			}
		}
		return ret;
	}

	public static void main(String[] args) throws Exception {
		reader = new BufferedReader(new InputStreamReader(System.in));
		writer = new PrintWriter(System.out);
		Locale.setDefault(Locale.US);

		setTime();
		solve();
		printTime();
		printMemory();

		writer.close();
	}

	static BufferedReader reader;
	static PrintWriter writer;
	static StringTokenizer tok = new StringTokenizer("");
	static long systemTime;

	static void debug(Object... o) {
		System.err.println(deepToString(o));
	}

	static void setTime() {
		systemTime = System.currentTimeMillis();
	}

	static void printTime() {
		System.err.println("Time consumed: " + (System.currentTimeMillis() - systemTime));
	}

	static void printMemory() {
		System.err.println("Memory consumed: "
				+ (Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory()) / 1000 + "kb");
	}

	static String next() {
		while (!tok.hasMoreTokens()) {
			String w = null;
			try {
				w = reader.readLine();
			} catch (Exception e) {
				e.printStackTrace();
			}
			if (w == null)
				return null;
			tok = new StringTokenizer(w);
		}
		return tok.nextToken();
	}

	static int nextInt() {
		return Integer.parseInt(next());
	}

	static long nextLong() {
		return Long.parseLong(next());
	}

	static double nextDouble() {
		return Double.parseDouble(next());
	}

	static BigInteger nextBigInteger() {
		return new BigInteger(next());
	}
}