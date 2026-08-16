
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main{
	static InputStream is;
	static PrintWriter out;
	static String INPUT = "";

	public static void main(String[] args) throws Exception {
		new Main().run();
	}

	@SuppressWarnings("unchecked")
	void solver() {
		while (true) {
			int N = ni();
			int M = ni();
			int[] s = new int[] { ni() - 1, ni() - 1 };
			int t = ni() - 1;
			if (N == 0 && M == 0 && s[0] == -1 && s[1] == -1 && t == -1)
				break;

			ArrayList<Edge>[] g = new ArrayList[N];
			for (int i = 0; i < N; i++)
				g[i] = new ArrayList<>();
			for (int i = 0; i < M; i++) {
				int a = ni() - 1;
				int b = ni() - 1;
				String c = ns();
				g[a].add(new Edge(a, b, c));
				g[b].add(new Edge(b, a, c));
			}

			long[][] dist = new long[101][N];
			for (int i = 0; i < dist.length; i++)
				for (int j = 0; j < dist[i].length; j++)
					dist[i][j] = 1L << 60;
			dist[0][t] = 0;
			PriorityQueue<P> pq = new PriorityQueue<>();
			pq.add(new P(t, 0, 0));
			while (!pq.isEmpty()) {
				P p = pq.poll();
				if (p.dist > 1_000_000_000L * 1_000L)
					continue;
				if (dist[p.magicalBridgeNum][p.cur] < p.dist)
					continue;
				else
					dist[p.magicalBridgeNum][p.cur] = p.dist;
				for (Edge e : g[p.cur]) {
					long nD = p.dist + e.dist;
					int nM = p.magicalBridgeNum + e.magicalBridgeNum;
					if (nM > 100)
						continue;
					if (nD < dist[nM][e.dst]) {
						dist[nM][e.dst] = nD;
						pq.add(new P(e.dst, nD, nM));
					}
				}
			}

			ArrayList<Long> pos = new ArrayList<>();
			for (int pos1 = 0; pos1 <= 1; pos1++) {
				for (int pos2 = pos1; pos2 <= 1; pos2++) {
					for (int i = 0; i <= 100; i++) {
						for (int j = 0; j <= 100; j++) {
							long bi = dist[i][s[pos1]];
							long bj = dist[j][s[pos2]];
							if (bi == (1L << 60) || bj == (1L << 60))
								continue;
							if (i == j)
								continue;
							long x = (bj - bi) / (i - j);
							if (x < 0)
								continue;
							pos.add(x);
							pos.add(x + 1);
						}
					}
				}
			}

			pos.add(0L);
			Collections.sort(pos);

			long mingap = 1L << 60;
			for (Long x : pos) {
				long[] mindis = new long[] { 1L << 60, 1L << 60 };
				for (int i = 0; i < 2; i++) {
					for (int magicalBridge = 0; magicalBridge <= 100; magicalBridge++) {
						if (dist[magicalBridge][s[i]] == 1L << 60)
							continue;
						mindis[i] = Math.min(mindis[i], dist[magicalBridge][s[i]] + magicalBridge * x);
					}
				}
				if (mindis[0] != 1L << 60 && mindis[1] != 1L << 60)
					mingap = Math.min(mingap, Math.abs(mindis[0] - mindis[1]));
			}
			out.println(mingap);
		}
	}

	class P implements Comparable<P> {
		int cur;
		long dist;
		int magicalBridgeNum;

		public P(int cur, long dist, int magicalBridgeNum) {
			this.cur = cur;
			this.dist = dist;
			this.magicalBridgeNum = magicalBridgeNum;
		}

		@Override
		public int compareTo(P o) {
			if (magicalBridgeNum != o.magicalBridgeNum) {
				return Integer.compare(magicalBridgeNum, o.magicalBridgeNum);
			} else {
				return Long.compare(dist, o.dist);
			}
		}
	}

	class Edge {
		int src;
		int dst;
		long dist = 0;
		int magicalBridgeNum = 0;

		Edge(int src, int dst, String s) {
			this.src = src;
			this.dst = dst;

			if (s.equals("x"))
				magicalBridgeNum = 1;
			else
				dist = Long.parseLong(s);

		}
	}

	void run() {
		is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
		out = new PrintWriter(System.out);
		solver();
		out.flush();

	}

	static long nl() {
		try {
			long num = 0;
			boolean minus = false;
			while ((num = is.read()) != -1 && !((num >= '0' && num <= '9') || num == '-'))
				;
			if (num == '-') {
				num = 0;
				minus = true;
			} else {
				num -= '0';
			}

			while (true) {
				int b = is.read();
				if (b >= '0' && b <= '9') {
					num = num * 10 + (b - '0');
				} else {
					return minus ? -num : num;
				}
			}
		} catch (IOException e) {
		}
		return -1;
	}

	static char nc() {
		try {
			int b = skip();
			if (b == -1)
				return 0;
			return (char) b;
		} catch (IOException e) {
		}
		return 0;
	}

	static double nd() {
		try {
			return Double.parseDouble(ns());
		} catch (Exception e) {
		}
		return 0;
	}

	static String ns() {
		try {
			int b = skip();
			StringBuilder sb = new StringBuilder();
			if (b == -1)
				return "";
			sb.append((char) b);
			while (true) {
				b = is.read();
				if (b == -1)
					return sb.toString();
				if (b <= ' ')
					return sb.toString();
				sb.append((char) b);
			}
		} catch (IOException e) {
		}
		return "";
	}

	public static char[] ns(int n) {
		char[] buf = new char[n];
		try {
			int b = skip(), p = 0;
			if (b == -1)
				return null;
			buf[p++] = (char) b;
			while (p < n) {
				b = is.read();
				if (b == -1 || b <= ' ')
					break;
				buf[p++] = (char) b;
			}
			return Arrays.copyOf(buf, p);
		} catch (IOException e) {
		}
		return null;
	}

	public static byte[] nse(int n) {
		byte[] buf = new byte[n];
		try {
			int b = skip();
			if (b == -1)
				return null;
			is.read(buf);
			return buf;
		} catch (IOException e) {
		}
		return null;
	}

	static int skip() throws IOException {
		int b;
		while ((b = is.read()) != -1 && !(b >= 33 && b <= 126))
			;
		return b;
	}

	static boolean eof() {
		try {
			is.mark(1000);
			int b = skip();
			is.reset();
			return b == -1;
		} catch (IOException e) {
			return true;
		}
	}

	static int ni() {
		try {
			int num = 0;
			boolean minus = false;
			while ((num = is.read()) != -1 && !((num >= '0' && num <= '9') || num == '-'))
				;
			if (num == '-') {
				num = 0;
				minus = true;
			} else {
				num -= '0';
			}

			while (true) {
				int b = is.read();
				if (b >= '0' && b <= '9') {
					num = num * 10 + (b - '0');
				} else {
					return minus ? -num : num;
				}
			}
		} catch (IOException e) {
		}
		return -1;
	}

	static void tr(Object... o) {
		System.out.println(Arrays.deepToString(o));
	}
}