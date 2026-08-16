
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.stream.Stream;

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

		@SuppressWarnings("unchecked")
		public void solve(int testNumber, InputReader in, PrintWriter out) {

			int n = in.nextInt();
			List<P>[] g = new ArrayList[n];
			g = Stream.generate(ArrayList::new).limit(n).toArray(List[]::new);

			for (int i = 0; i < n-1; i++) {
				int s = in.nextInt();
				int t = in.nextInt();
				long w = in.nextLong();
				g[s].add(new P(t, w));
				g[t].add(new P(s, w));
			}

			int s = 0;
			for (int i = 0; i < n-1; i++) {
				if (g[i].size() >= 2) {
					s = i;
					break;
				}
			}

			Queue<Integer> q = new ArrayDeque<>();
			long[] cost = new long[n];
			boolean[] used = new boolean[n];

			q.add(s);
			used[s] = true;
			while (!q.isEmpty()) {

				int from = q.remove();

				for (P pt : g[from]) {
					int to = pt.to;
					long w = pt.weight;

					if (!used[to]) {
						cost[to] = cost[from] + w;
						used[to] = true;
						q.add(to);
					}
				}
			}

			long max = -INF;
			for (int i = 0; i < n; i++) {
				if (max < cost[i]) {
					max = cost[i];
					s = i;
				}
			}

			cost = new long[n];
			used = new boolean[n];

			q.add(s);
			used[s] = true;
			while (!q.isEmpty()) {

				int from = q.remove();

				for (P pt : g[from]) {
					int to = pt.to;
					long w = pt.weight;

					if (!used[to]) {
						cost[to] = cost[from] + w;
						used[to] = true;
						q.add(to);
					}
				}
			}

			for (int i = 0; i < n; i++) {
				if (max < cost[i]) {
					max = cost[i];
					s = i;
				}
			}

			out.println(max);

		}

		class P {
			int to;
			long weight;

			public P(int to, long weight) {
				super();
				this.to = to;
				this.weight = weight;
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

		public long[] nextLongArray(int n) {
			long[] res = new long[n];
			for (int i = 0; i < n; i++) {
				res[i] = nextLong();
			}
			return res;
		}

		public InputReader(InputStream inputStream) {
			in = new BufferedReader(new InputStreamReader(inputStream));
			tok = new StringTokenizer("");
		}
	}

}

