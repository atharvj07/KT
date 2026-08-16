import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class e {
	public static int SUB = 0;
	// public static int ADD = 1;
	public static int QUER = 2;
	public static int UPDATE = 1;
	public static boolean DEBUG = false;

	public static void main(String[] Args) throws Exception {
		FastScanner sc = new FastScanner(System.in);
		PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
		int n = sc.nextInt();
		int e = sc.nextInt();
		LowLink tj = new LowLink(n + 1);
		boolean[] hasEdge = new boolean[n];
		for (int i = 0; i < e; i++) {
			int a = sc.nextInt() - 1;
			int b = sc.nextInt() - 1;
			hasEdge[a] = true;
			hasEdge[b] = true;

			tj.add(a, b);
		}
		for (int i = 0; i < n; i++)
			if (!hasEdge[i])
				tj.add(i, n);
		tj.run();
		int[] min = new int[n + 2];
		Arrays.fill(min, -1);
		int[] max = new int[n + 2];
		for (int i = 0; i < n; i++) {
			if (min[tj.low[i]] == -1)
				min[tj.low[i]] = i;
			max[tj.low[i]] = i;
		}
		ArrayList<Pair> al = new ArrayList<Pair>();
		for (int i = 0; i <= n + 1; i++) {
			if (min[i] != max[i] && min[i] != -1) {
				al.add(new Pair(max[i] + 1, min[i] + 1, SUB, -1));
				if (DEBUG)
					System.out.println(max[i] + " " + min[i]);
			}
		}
		int q = sc.nextInt();
		for (int i = 0; i < q; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			al.add(new Pair(b, a, QUER, i));
		}
		for (int i = 0; i < n; i++) {
			al.add(new Pair(i + 1, i + 1, UPDATE, -1));
		}
		Collections.sort(al);
		long[] ans = new long[q];
		long[] rs = new long[n + 2];
		IntervalTree it = new IntervalTree(n + 2);
		long up = 0;
		int curP = 0;
		int last = 0;

		for (Pair p : al) {
			if (p.type == SUB) {
				if (p.e > last) {
					last = p.e;
				}
			}
			if (p.type == UPDATE) {
				it.inc(0, last, 1l);
			}
			if (p.type == QUER) {
				if (DEBUG)
					System.out.println(c2(p.b - p.e + 2));
				ans[p.ind] = c2(p.b - p.e + 2) - it.query(p.e, p.b);
				if (DEBUG) {
					System.out.println(" " + it.query(p.e, p.b));
					for (int i = 0; i < n; i++)
						System.out.print(" " + it.query(i, i));
					System.out.println();
				}
			}
		}
		if (DEBUG) {
			for (int i = 0; i < n; i++)
				System.out.print(" " + it.query(i, i));
			System.out.println();
		}
		for (Long i : ans)
			out.println(i);
		out.close();
	}

	public static long c2(int x) {
		return ((x) * 1l * (x - 1)) / 2;
	}

	public static class IntervalTree {
		static final int NULL_VALUE = 0; // change this
		int[] lo, hi;
		long[] carry, val;

		public IntervalTree(int N) {
			lo = new int[4 * (N + 1)];
			hi = new int[4 * (N + 1)];
			carry = new long[4 * (N + 1)];
			val = new long[4 * (N + 1)];
			init(1, 0, N - 1);
		}

		public void inc(int l, int h, long v) {
			inc(1, l, h, v);
		}

		public long query(int l, int h) {
			return query(1, l, h);
		}

		private long aggregate(long x, long y) {
			return x + y;
		} // change this

		private void init(int i, int l, int h) {
			lo[i] = l;
			hi[i] = h;
			if (l == h)
				return;
			int m = (l + h) / 2;
			init(2 * i, l, m);
			init(2 * i + 1, m + 1, h);
		}

		private void inc(int i, int l, int h, long v) {
			if (l <= lo[i] && hi[i] <= h) { // incorporation
				carry[i] += v;
				val[i] += v * (hi[i] - lo[i] + 1); // change this
			} else if (l <= hi[i] && lo[i] <= h) {
				push(i);
				inc(2 * i, l, h, v);
				inc(2 * i + 1, l, h, v);
				val[i] = aggregate(val[2 * i], val[2 * i + 1]);
			}
		}

		private long query(int i, int l, int h) {
			if (h < lo[i] || hi[i] < l)
				return NULL_VALUE;
			if (l <= lo[i] && hi[i] <= h)
				return val[i];
			push(i);
			return aggregate(query(2 * i, l, h), query(2 * i + 1, l, h));
		}

		private void push(int i) {
			if (carry[i] == 0)
				return;
			inc(2 * i, lo[2 * i], hi[2 * i], carry[i]);
			inc(2 * i + 1, lo[2 * i + 1], hi[2 * i + 1], carry[i]);
			carry[i] = 0;
		}
	}

	public static class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		FastScanner(InputStream is) throws Exception {
			br = new BufferedReader(new InputStreamReader(is));
			st = new StringTokenizer(br.readLine());
		}

		String next() throws Exception {
			if (!st.hasMoreTokens()) {
				st = new StringTokenizer(br.readLine());
				return next();
			}
			return st.nextToken();
		}

		int nextInt() throws Exception {
			return Integer.parseInt(next());
		}
	}

	public static class LowLink {
		int N, M, bccInd, sPtr, index;
		int[] low, pre, cnt, bccIn, bStk; // bccIn over edges
		boolean[] art, isBridge;
		ArrayList<Edge> E;
		ArrayList<Edge>[] g;

		public LowLink(int N) {
			g = new ArrayList[this.N = N];
			for (int i = 0; i < N; i++)
				g[i] = new ArrayList<Edge>();
			E = new ArrayList<Edge>();
			low = new int[N];
			cnt = new int[N];
			art = new boolean[N];
			Arrays.fill(pre = new int[N], -1);
		}

		void add(int u, int v) {
			g[u].add(new Edge(u, v, M));
			g[v].add(new Edge(v, u, M));
			E.add(new Edge(u, v, M++));
		}

		void run() {
			bStk = new int[M]; // PAY ATTENTION: M NOT N
			Arrays.fill(bccIn = new int[M], -1);
			isBridge = new boolean[M];
			for (int i = 0; i < N; i++)
				if (pre[i] == -1)
					dfs(i);
		}

		void buildBCC(int defEdge, int curEdge) {
			isBridge[defEdge] = bStk[sPtr - 1] == defEdge;
			while (curEdge != defEdge)
				bccIn[curEdge = bStk[--sPtr]] = bccInd;
			bccInd++;
		}

		void dfs(int rNode) {
			ArrayDeque<IState> stk = new ArrayDeque<IState>();
			stk.push(new IState(rNode, -1, -1));
			boolean flag = true; // firstRootChild
			while (!stk.isEmpty()) {
				IState at = stk.peek();
				if (at.c == 0)
					low[at.at] = pre[at.at] = index++;
				if (at.c == g[at.at].size()) {
					if (at.p == rNode)
						art[at.p] |= flag ? (flag = false) : true;
					if (at.at != rNode) {
						if (pre[at.p] <= low[at.at]) {
							art[at.p] |= at.p != rNode;
							buildBCC(at.eUsed, -1);
						}
						low[at.p] = Math.min(low[at.p], low[at.at]);
					}
					stk.pop();
				} else {
					Edge e = g[at.at].get(at.c++);
					if (pre[e.e] == -1) {
						bStk[sPtr++] = e.id;
						stk.push(new IState(e.e, at.at, e.id));
					} else if (e.id != at.eUsed && pre[e.e] < pre[at.at]) {
						bStk[sPtr++] = e.id;
						low[at.at] = Math.min(low[at.at], pre[e.e]);
					}
				}
			}
		}

		static class IState {
			int at, p, eUsed, c; // at, parent, edge to get here, child index

			public IState(int node, int parent, int e) {
				at = node;
				eUsed = e;
				p = parent;
			}
		}

		static class Edge {
			int s, e, id; // ends of the edge, index of the edge

			public Edge(int src, int end, int edgeId) {
				s = src;
				e = end;
				id = edgeId;
			}
		}
	}

	public static class Pair implements Comparable<Pair> {
		int b, e;
		int type;
		int ind;

		Pair(int bb, int ee, int tt, int ii) {
			b = bb;
			e = ee;
			type = tt;
			ind = ii;
		}

		public int compareTo(Pair o) {
			if (b == o.b)
				return type - o.type;
			return b - o.b;
		}
	}
}
