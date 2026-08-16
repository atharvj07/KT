import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class A implements Runnable {
	static String Y = "YES", N = "NO";
	static long inf = (long) 1e18;

	public static void main(String[] args) {
		new Thread(null, new A(), "Solver", 1L << 26).start();
	}

	private FastScanner scan;
	private PrintWriter out;

	public A() {
		scan = new FastScanner(System.in);
		out = new PrintWriter(System.out);
	}

	public void run() {
		try {
			solve();
			out.close();
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println(1 / 0);
		}
	}

	static long ceilDiv(long n, long d) {
		if (n < 0 != d < 0) {
			return (n / d) - (n % d == 0 ? 0 : 1);
		}
		return (n / d) + (n % d == 0 ? 0 : 1);
	}

	void solve() throws IOException {
		int n = scan.nextInt(), k = scan.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++)
			arr[i] = scan.nextInt();
		int[] cs = new int[k];
		for (int i = 0; i < n; i++) {
			if (arr[i] == 1)
				cs[i % k]++;
		}
		int ans = 0;
		for(int i=0;i<k;i++) {
			ans += Math.min(cs[i], n/k-cs[i]);
		}
		out.println(ans);
	}

	void print(int[] arr) {
		for (int i = 0; i < arr.length; i++) {
			out.print(arr[i]);
			if (i == arr.length - 1)
				out.println();
			else
				out.print(" ");
		}

	}

	static class Pair implements Comparable<Pair> {
		long a, b;

		public Pair(long a, long b) {
			this.a = a;
			this.b = b;
		}

		@Override
		public int compareTo(Pair o) {
			if (a == o.a)
				return Long.compare(b, o.b);
			return Long.compare(a, o.a);
		}
	}

	static long max(long... ls) {
		long max = ls[0];
		for (long l : ls) {
			if (l > max)
				max = l;
		}
		return max;
	}

	static int max(int... ls) {
		int max = ls[0];
		for (int l : ls) {
			if (l > max)
				max = l;
		}
		return max;
	}

	static double max(double... ls) {
		double max = ls[0];
		for (double l : ls) {
			if (l > max)
				max = l;
		}
		return max;
	}

	static long min(long... ls) {
		long min = ls[0];
		for (long l : ls) {
			if (l < min)
				min = l;
		}
		return min;
	}

	static double min(double... ls) {
		double min = ls[0];
		for (double l : ls) {
			if (l < min)
				min = l;
		}
		return min;
	}

	static int min(int... ls) {
		int min = ls[0];
		for (int l : ls) {
			if (l < min)
				min = l;
		}
		return min;
	}

	static void yes(boolean a) {
		System.out.println(a ? Y : N);
	}

	static long gcd(long a, long b) {
		if (b == 0)
			return a;
		return gcd(b, a % b);
	}

	static class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		public FastScanner(InputStream in) {
			br = new BufferedReader(new InputStreamReader(in));
			st = new StringTokenizer("");
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public String next() throws IOException {
			while (!st.hasMoreTokens()) {
				st = new StringTokenizer(br.readLine());
			}
			return st.nextToken();
		}
	}

	class BPM {
		private Dinics d;
		private int leftCount;
		private int rightCount;

		public BPM(int leftCount, int rightCount) {
			this.leftCount = leftCount;
			this.rightCount = rightCount;
			this.d = new Dinics(leftCount + rightCount + 2, 0, leftCount + rightCount + 1);
			for (int i = 1; i <= leftCount; i++) {
				d.addEdge(d.s, i, 1);
			}
			for (int i = leftCount + 1; i <= leftCount + rightCount; i++) {
				d.addEdge(i, d.t, 1);
			}
		}

		public void addMatching(int left, int right) {
			d.addEdge(1 + left, 1 + leftCount + right, 1);
		}

		public int[] getMatchings() {
			this.d.calculateFlow();
			int[] answer = new int[leftCount];
			Arrays.fill(answer, -1);
			for (edge e : this.d.e) {
				if (e.a == d.s || e.b == d.t)
					continue;
				if (e.flow != 1)
					continue;
				answer[e.a - 1] = e.b - (leftCount + 1);
			}
			return answer;
		}
	}

	class Dinics {
		public static final int INF = 1000000000;

		public Dinics(int n, int s, int t) {
			this.n = n;
			this.g = new ArrayList[n];
			this.s = s;
			this.t = t;
			this.q = new int[n];
			this.d = new int[n];
			this.ptr = new int[n];
			this.intd = new int[n];
			for (int i = 0; i < n; i++)
				g[i] = new ArrayList<Integer>();
		}

		int n, s, t;
		int[] intd;
		int[] ptr;
		int[] d;
		int[] q;
		ArrayList<edge> e = new ArrayList<edge>();
		ArrayList<Integer>[] g;

		void addEdge(int a, int b, int cap) {
			edge e1 = new edge(a, b, cap, 0);
			edge e2 = new edge(b, a, 0, 0);
			g[a].add((int) e.size());
			e.add(e1);
			g[b].add((int) e.size());
			e.add(e2);
		}

		boolean bfs() {
			int qh = 0, qt = 0;
			q[qt++] = s;
			Arrays.fill(d, -1);
			d[s] = 0;
			while (qh < qt && d[t] == -1) {
				int v = q[qh++];
				for (int i = 0; i < g[v].size(); ++i) {
					int id = g[v].get(i), to = e.get(id).b;
					if (d[to] == -1 && e.get(id).flow < e.get(id).cap) {
						q[qt++] = to;
						d[to] = d[v] + 1;
					}
				}
			}
			return d[t] != -1;
		}

		int dfs(int v, int flow) {
			if (flow == 0)
				return 0;
			if (v == t)
				return flow;
			for (; ptr[v] < (int) g[v].size(); ++ptr[v]) {
				int id = g[v].get(ptr[v]), to = e.get(id).b;
				if (d[to] != d[v] + 1)
					continue;
				int pushed = dfs(to, Math.min(flow, e.get(id).cap - e.get(id).flow));
				if (pushed != 0) {
					e.get(id).flow += pushed;
					e.get(id ^ 1).flow -= pushed;
					return pushed;
				}
			}
			return 0;
		}

		public int calculateFlow() {
			int flow = 0;
			for (;;) {
				if (!bfs())
					break;
				Arrays.fill(ptr, 0);
				int pushed;
				while ((pushed = dfs(s, INF)) != 0)
					flow += pushed;
			}
			return flow;
		}

	}

	static class edge {
		int a, b, cap, flow;

		public edge(int a, int b, int cap, int flow) {
			this.a = a;
			this.b = b;
			this.cap = cap;
			this.flow = flow;
		}
	}
}