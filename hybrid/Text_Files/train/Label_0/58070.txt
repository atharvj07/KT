import static java.lang.Math.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.InputMismatchException;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputReader in = new InputReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskX solver = new TaskX();
		solver.solve(1, in, out);
		out.close();
	}

	static int INF = 1 << 30;
	static long LINF = 1L << 55;
	static int MOD = 1000000007;
	static int[] mh4 = { 0, -1, 1, 0 };
	static int[] mw4 = { -1, 0, 0, 1 };
	static int[] mh8 = { -1, -1, -1, 0, 0, 1, 1, 1 };
	static int[] mw8 = { -1, 0, 1, -1, 1, -1, 0, 1 };

	static class TaskX {

		public void solve(int testNumber, InputReader in, PrintWriter out) {

			int n = in.nextInt();
			long[] x = new long[n], y = new long[n];
			for (int i = 0; i < n; i++) {
				x[i] = in.nextLong();
				y[i] = in.nextLong();
				if (abs(x[0] + y[0] - x[i] - y[i]) % 2 != 0) {
					out.println(-1);
					return;
				}
			}

			List<Long> list = new ArrayList<>();
			for (int i = 0; i <= 30; i++) list.add(1L << i);
			if (abs(x[0] + y[0]) % 2 == 0) list.add(1L);
			Collections.sort(list, Comparator.reverseOrder());

			out.println(list.size());
			for (int i = 0; i < list.size(); i++) {
				if (i > 0) out.print(" ");
				out.print(list.get(i));
			}
			out.print("\n");

			for (int i = 0; i < n; i++) {

				long u = x[i] + y[i];
				long v = x[i] - y[i];
				StringBuilder sb = new StringBuilder();

				for (int j = 0; j < list.size(); j++) {
					if (u >= 0 && v >= 0) {
						u -= list.get(j);
						v -= list.get(j);
						sb.append("R");
					} else if (u >= 0 && v < 0) {
						u -= list.get(j);
						v += list.get(j);
						sb.append("U");
					} else if (u < 0 && v >= 0) {
						u += list.get(j);
						v -= list.get(j);
						sb.append("D");
					} else if (u < 0 && v < 0) {
						u += list.get(j);
						v += list.get(j);
						sb.append("L");
					}
				}

				out.println(sb.toString());
			}
		}
	}

	static class InputReader {
		BufferedReader in;
		StringTokenizer tok;

		public String nextString() {
			while (!tok.hasMoreTokens()) {
				try {
					tok = new StringTokenizer(in.readLine(), " ");
				} catch (IOException e) {
					throw new InputMismatchException();
				}
			}
			return tok.nextToken();
		}

		public int nextInt() {
			return Integer.parseInt(nextString());
		}

		public long nextLong() {
			return Long.parseLong(nextString());
		}

		public double nextDouble() {
			return Double.parseDouble(nextString());
		}

		public int[] nextIntArray(int n) {
			int[] res = new int[n];
			for (int i = 0; i < n; i++) {
				res[i] = nextInt();
			}
			return res;
		}

		public int[] nextIntArrayDec(int n) {
			int[] res = new int[n];
			for (int i = 0; i < n; i++) {
				res[i] = nextInt() - 1;
			}
			return res;
		}

		public int[] nextIntArray1Index(int n) {
			int[] res = new int[n + 1];
			for (int i = 0; i < n; i++) {
				res[i + 1] = nextInt();
			}
			return res;
		}

		public long[] nextLongArray(int n) {
			long[] res = new long[n];
			for (int i = 0; i < n; i++) {
				res[i] = nextLong();
			}
			return res;
		}

		public long[] nextLongArrayDec(int n) {
			long[] res = new long[n];
			for (int i = 0; i < n; i++) {
				res[i] = nextLong() - 1;
			}
			return res;
		}

		public long[] nextLongArray1Index(int n) {
			long[] res = new long[n + 1];
			for (int i = 0; i < n; i++) {
				res[i + 1] = nextLong();
			}
			return res;
		}

		public double[] nextDoubleArray(int n) {
			double[] res = new double[n];
			for (int i = 0; i < n; i++) {
				res[i] = nextDouble();
			}
			return res;
		}

		public InputReader(InputStream inputStream) {
			in = new BufferedReader(new InputStreamReader(inputStream));
			tok = new StringTokenizer("");
		}
	}

}
