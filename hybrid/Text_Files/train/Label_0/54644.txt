import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.PriorityQueue;

public class Main {

	static PrintWriter out;
	static InputReader ir;

	static void solve() {
		int n = ir.nextInt();
		int m = ir.nextInt();
		int k = ir.nextInt();
		long[] P = ir.nextLongArray(n);
		int[] c = ir.nextIntArray(n);
		long[] J = ir.nextLongArray(n);
		Graph[] g = new Graph[n];
		Graph[] jam = new Graph[k];
		for (int i = 0; i < n; i++) {
			g[i] = new Graph();
		}
		for (int i = 0; i < k; i++) {
			jam[i] = new Graph();
		}
		for (int i = 0; i < n; i++) {
			jam[c[i] - 1].add(new long[] { i });
		}
		for (int i = 0; i < m; i++) {
			int u = ir.nextInt() - 1;
			int v = ir.nextInt() - 1;
			long t = ir.nextLong();
			g[u].add(new long[] { v, t });
			g[v].add(new long[] { u, t });
		}
		long[] d = dijkstra(0, g);
		long[] d2 = dijkstra2(P, g, d);
		// tr(d2);
		for (int i = 0; i < k; i++) {
			long ma = -(1L << 60);
			for (long[] j : jam[i]) {
				ma = Math.max(ma, J[(int) j[0]] - d[(int) j[0]] + d2[(int) j[0]]);
			}
			out.println(ma);
		}
	}

	public static long[] dijkstra(int s, Graph[] g) {
		long[] d = new long[g.length];
		PriorityQueue<long[]> pq = new PriorityQueue<long[]>(new Comparator<long[]>() {
			public int compare(long[] a, long[] b) {
				return Long.compare(a[1], b[1]);
			}
		});
		Arrays.fill(d, 1L << 60);
		d[s] = 0;
		pq.offer(new long[] { s, 0 });
		while (!pq.isEmpty()) {
			long[] p = pq.poll();
			int from = (int) p[0];
			if (d[from] != p[1])
				continue;
			for (int i = 0; i < g[from].size(); i++) {
				long[] e = g[from].get(i);
				int to = (int) e[0];
				if (d[to] > d[from] + e[1]) {
					d[to] = d[from] + e[1];
					pq.offer(new long[] { to, d[to] });
				}
			}
		}
		return d;
	}

	public static long[] dijkstra2(long[] P, Graph[] g, long[] dd) {
		int n = g.length;
		PriorityQueue<long[]> pq = new PriorityQueue<long[]>(new Comparator<long[]>() {
			public int compare(long[] a, long[] b) {
				return Long.compare(b[1], a[1]);
			}
		});
		long[] d = new long[n];
		for (int i = 0; i < n; i++) {
			d[i] = P[i] - dd[i];
			pq.offer(new long[] { i, P[i] - dd[i] });
		}
		while (!pq.isEmpty()) {
			long[] p = pq.poll();
			int from = (int) p[0];
			if (d[from] != p[1])
				continue;
			for (int i = 0; i < g[from].size(); i++) {
				long[] e = g[from].get(i);
				int to = (int) e[0];
				if (d[to] < d[from] - e[1]) {
					d[to] = d[from] - e[1];
					pq.offer(new long[] { to, d[to] });
				}
			}
		}
		return d;
	}

	static class Graph extends ArrayList<long[]> {
	}

	public static void main(String[] args) {
		ir = new InputReader(System.in);
		out = new PrintWriter(System.out);
		solve();
		out.flush();
	}

	static class InputReader {

		private InputStream in;
		private byte[] buffer = new byte[1024];
		private int curbuf;
		private int lenbuf;

		public InputReader(InputStream in) {
			this.in = in;
			this.curbuf = this.lenbuf = 0;
		}

		public boolean hasNextByte() {
			if (curbuf >= lenbuf) {
				curbuf = 0;
				try {
					lenbuf = in.read(buffer);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (lenbuf <= 0)
					return false;
			}
			return true;
		}

		private int readByte() {
			if (hasNextByte())
				return buffer[curbuf++];
			else
				return -1;
		}

		private boolean isSpaceChar(int c) {
			return !(c >= 33 && c <= 126);
		}

		private void skip() {
			while (hasNextByte() && isSpaceChar(buffer[curbuf]))
				curbuf++;
		}

		public boolean hasNext() {
			skip();
			return hasNextByte();
		}

		public String next() {
			if (!hasNext())
				throw new NoSuchElementException();
			StringBuilder sb = new StringBuilder();
			int b = readByte();
			while (!isSpaceChar(b)) {
				sb.appendCodePoint(b);
				b = readByte();
			}
			return sb.toString();
		}

		public int nextInt() {
			if (!hasNext())
				throw new NoSuchElementException();
			int c = readByte();
			while (isSpaceChar(c))
				c = readByte();
			boolean minus = false;
			if (c == '-') {
				minus = true;
				c = readByte();
			}
			int res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res = res * 10 + c - '0';
				c = readByte();
			} while (!isSpaceChar(c));
			return (minus) ? -res : res;
		}

		public long nextLong() {
			if (!hasNext())
				throw new NoSuchElementException();
			int c = readByte();
			while (isSpaceChar(c))
				c = readByte();
			boolean minus = false;
			if (c == '-') {
				minus = true;
				c = readByte();
			}
			long res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res = res * 10 + c - '0';
				c = readByte();
			} while (!isSpaceChar(c));
			return (minus) ? -res : res;
		}

		public double nextDouble() {
			return Double.parseDouble(next());
		}

		public int[] nextIntArray(int n) {
			int[] a = new int[n];
			for (int i = 0; i < n; i++)
				a[i] = nextInt();
			return a;
		}

		public long[] nextLongArray(int n) {
			long[] a = new long[n];
			for (int i = 0; i < n; i++)
				a[i] = nextLong();
			return a;
		}

		public char[][] nextCharMap(int n, int m) {
			char[][] map = new char[n][m];
			for (int i = 0; i < n; i++)
				map[i] = next().toCharArray();
			return map;
		}
	}

	static void tr(Object... o) {
		out.println(Arrays.deepToString(o));
	}
}
