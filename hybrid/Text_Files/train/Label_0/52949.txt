import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.io.BufferedInputStream;
import java.util.concurrent.Callable;
import java.util.HashMap;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		BufferedInputStream in = new BufferedInputStream(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskD solver = new TaskD();
		solver.solve(1, in, out);
		out.close();
	}

	static class TaskD {
		public void solve(int testNumber, BufferedInputStream _in, PrintWriter out) {
			InputReader in = new InputReader(_in);
			long startTime = System.currentTimeMillis();
			int nt = 1;
			Task t = new Task(1);
			t.readInput(in);
			t.call();
			t.writeOutput(out);
			in.close();
			System.err.println("Time: " + (System.currentTimeMillis() - startTime) + " miliseconds");
		}

	}

	static class Task implements Callable<Task> {
		long[] X = null;
		long[] Y = null;
		long[] Z = null;
		long RE = 0;
		int testNumber;

		public void readInput(InputReader in) {
	/* read input here */


			int n = in.nextInt();
			X = new long[n];
			Y = new long[n];
			Z = new long[n];
			int cnt = 0;
			for (int i = 0; i < n; ++i) {
				long a = in.nextInt();
				long b = in.nextInt();
				long c = in.nextInt();
				long ab = a * a + b * b;

				X[i] = (a * c);
				Y[i] = (b * c);
				Z[i] = (ab);

				if (X[(i)] == 0 && Y[(i)] == 0) {
					cnt++;
				}

			}
			if (cnt == 2) RE = n - 2;


		}

		long count(long n) {
			if (n < 3) return 0l;
			return n * (n - 1) * (n - 2) / 6l;
		}

		public Task call() {

			if (X.length < 3) return this;


			HashMap<PP, Long> mm = new HashMap<>();

			for (int i = 0; i < Y.length; ++i)
				if (X[i] != 0 || Y[i] != 0) {

					PP pa = new PP(Y[i], Z[i]);
					Long f = mm.get(pa);
					if (f == null) {
						mm.put(pa, 1l);
					} else mm.put(pa, 1l + f);
				}

			for (Long v : mm.values()) {
				RE += count(v);
			}


			mm.clear();
			for (int i = 0; i < X.length; ++i)
				if (X[i] != 0 || Y[i] != 0) {
					for (int j = i + 1; j < X.length; ++j)
						if (X[j] != 0 || Y[j] != 0) {
							long yi = Y[i];
							long zi = Z[i];
							long xi = X[i];

							long yj = Y[j];
							long zj = Z[j];
							long xj = X[j];
							long dy = yi * zj - zi * yj;
							if (dy != 0) {
								long dx = xi * zj - zi * xj;

								PP pa = new PP(dx, dy);
								Long f = mm.get(pa);
								if (f == null) {
									mm.put(pa, 1l);
								} else {
									mm.put(pa, f + 1);
								}
							}
						}

					for (Long v : mm.values()) {
						if (v >= 2) {
							RE += (v - 1) * v / 2;
						}
					}

					mm.clear();
				}


			System.err.println("Test case: " + testNumber + " done!");/**/


			return this;
		}

		public void writeOutput(PrintWriter out) {
			out.println(RE);
		}

		Task(int testNumber) {
			this.testNumber = testNumber;
		}

	}

	static class InputReader {
		public BufferedReader reader;
		public StringTokenizer tokenizer;

		public InputReader(BufferedInputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream), 32768);
			tokenizer = null;
		}

		public String next() {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(reader.readLine());
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return tokenizer.nextToken();
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}

		public void close() {
			try {
				if (reader != null)
					reader.close();
			} catch (Exception ex) {
				throw new RuntimeException(ex);
			}
		}

	}

	static class PP implements Comparable<PP> {
		Long first;
		Long second;

		long gcd(long a, long b) {
			return b == 0 ? a : gcd(b, a % b);
		}

		public PP(Long first, Long second) {

			long g = gcd(Math.abs(first), Math.abs(second));
			if (second < 0) g = -g;


			this.first = first / g;
			this.second = second / g;
		}


		public int compareTo(PP o) {
			int t = first.compareTo(o.first);
			if (t != 0) return t;
			else
				return second.compareTo(o.second);
		}

		public boolean equals(Object obj) {
			if (obj instanceof PP) {
				return compareTo((PP) obj) == 0;
			}
			return false;
		}


		public int hashCode() {
			return first.hashCode() ^ second.hashCode();
		}

	}
}

