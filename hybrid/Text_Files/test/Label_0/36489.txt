import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Main implements Runnable {
	public static void main(String[] args) {
		new Thread(null, new Main(), "", Runtime.getRuntime().maxMemory()).start();
	}

	public void run() {
		Scanner sc = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(System.out);
		int n = sc.nextInt();
		int q = sc.nextInt();
		int[] w = new int[n];
		for (int i = 0; i < n; ++i) {
			w[i] = sc.nextInt();
		}
		HLDecomposition hl = new HLDecomposition(n);
		for (int i = 0; i < n - 1; ++i) {
			int s = sc.nextInt() - 1;
			int e = sc.nextInt() - 1;
			hl.ae(s, e);
		}
		hl.pre();
		SegmentTree st = new SegmentTree(n);
		for (int i = 0; i < n; ++i) {
			st.v[hl.id[i] + st.n - 1] = new E(w[i], 1);
		}
		for (int i = st.n - 2; i >= 0; --i) {
			st.v[i] = merge(st.v[2 * i + 1], st.v[2 * i + 2]);
		}
		while (q-- > 0) {
			int t = sc.nextInt();
			int a = sc.nextInt() - 1;
			int b = sc.nextInt() - 1;
			int c = sc.nextInt();
			if (t == 1) {// modification query
				modification(a, b, c, hl, st);
			} else {// output query
				pw.println(output(a, b, hl, st));
			}
		}
		pw.close();
	}

	long output(int a, int b, HLDecomposition hl, SegmentTree st) {
		E ea = new E(-(Long.MAX_VALUE >> 8), 1);
		E eb = new E(-(Long.MAX_VALUE >> 8), 1);

		while (hl.head[a] != hl.head[b]) {
			if (hl.depth[hl.head[a]] < hl.depth[hl.head[b]]) {
				int tmp = a;
				a = b;
				b = tmp;
				E tmp_e = ea;
				ea = eb;
				eb = tmp_e;
			}
			// a???head???????????±???
			ea = merge(st.query(hl.id[hl.head[a]], hl.id[a] + 1), ea);
			a = hl.parent[hl.head[a]];
		}
		if (hl.depth[a] < hl.depth[b]) {
			int tmp = a;
			a = b;
			b = tmp;
			E tmp_e = ea;
			ea = eb;
			eb = tmp_e;
		}
		// a???????????±???
		return merge(eb.reverse(), merge(st.query(hl.id[b], hl.id[a] + 1), ea)).max;
	}

	void modification(int a, int b, int c, HLDecomposition hl, SegmentTree st) {
		while (hl.head[a] != hl.head[b]) {
			if (hl.depth[hl.head[a]] < hl.depth[hl.head[b]]) {
				int tmp = a;
				a = b;
				b = tmp;
			}
			// a???head???????????±???
			st.modification(hl.id[hl.head[a]], hl.id[a] + 1, c);
			a = hl.parent[hl.head[a]];
		}
		if (hl.depth[a] < hl.depth[b]) {
			int tmp = a;
			a = b;
			b = tmp;
		}
		// a???????????±???
		if (hl.id[b] > hl.id[a]) {
			throw new AssertionError();
		}
		st.modification(hl.id[b], hl.id[a] + 1, c);
	}

	class E {
		long top;
		long bottom;
		long max;
		long sum;

		public E(long top, long bottom, long max, long sum) {
			this.top = top;
			this.bottom = bottom;
			this.max = max;
			this.sum = sum;
		}

		public E(long v, int width) {
			this.top = Math.max(v, v * width);
			this.bottom = Math.max(v, v * width);
			this.max = Math.max(v, v * width);
			this.sum = width * v;
		}

		public E() {
			this.top = -(Long.MAX_VALUE >> 8);
			this.bottom = -(Long.MAX_VALUE >> 8);
			this.max = -(Long.MAX_VALUE >> 8);
			this.sum = 0;
		}

		E reverse() {
			E e = new E();
			e.top = this.bottom;
			e.bottom = this.top;
			e.sum = this.sum;
			e.max = this.max;
			return e;
		}

		void tr() {
			System.out.println("top" + top);
			System.out.println("bottom" + bottom);
			System.out.println("max" + max);
			System.out.println("sum" + sum);
		}
	}

	E merge(E top, E bottom) {
		E e = new E();
		e.top = Math.max(top.top, top.sum + bottom.top);
		e.bottom = Math.max(bottom.bottom, top.bottom + bottom.sum);
		e.max = Math.max(Math.max(top.max, bottom.max), top.bottom + bottom.top);
		e.sum = top.sum + bottom.sum;
		return e;
	}

	class SegmentTree {
		int n;
		E[] v;
		long[] lazy;
		long nil = Long.MAX_VALUE >> 3;

		public SegmentTree(int n) {
			this.n = 1;
			while (this.n < n) {
				this.n *= 2;
			}
			v = new E[2 * this.n - 1];
			lazy = new long[2 * this.n - 1];
			Arrays.fill(lazy, nil);
			Arrays.fill(v, new E());
		}

		void push(int k, int l, int r) {
			if (lazy[k] == nil) {
				return;
			}
			v[k] = new E(lazy[k], r - l);
			if (r - l > 1) {
				lazy[2 * k + 1] = lazy[k];
				lazy[2 * k + 2] = lazy[k];
			}
			lazy[k] = nil;
		}

		void modification(int a, int b, int c) {
			modification(a, b, c, 0, n, 0);
		}

		// [a,b),[l,r)
		void modification(int a, int b, int c, int l, int r, int k) {
			push(k, l, r);
			if (b <= l || r <= a) {
				return;
			}
			if (a <= l && r <= b) {
				lazy[k] = c;
				push(k, l, r);
			} else {
				modification(a, b, c, l, (l + r) / 2, 2 * k + 1);
				modification(a, b, c, (l + r) / 2, r, 2 * k + 2);
				v[k] = merge(v[2 * k + 1], v[2 * k + 2]);
			}
		}

		E query(int a, int b) {
			return query(a, b, 0, n, 0);
		}

		E query(int a, int b, int l, int r, int k) {
			if (b <= l || r <= a) {
				return new E();
			}
			push(k, l, r);
			if (a <= l && r <= b) {
				return v[k];
			} else {
				E vl = query(a, b, l, (l + r) / 2, 2 * k + 1);
				E vr = query(a, b, (l + r) / 2, r, 2 * k + 2);
				return merge(vl, vr);
			}
		}
	}

	class HLDecomposition {
		int n;
		int[] depth;
		int[] head;
		int[] heavy;
		int[] parent;
		int[] sz;
		ArrayList<Integer>[] g;
		int[] id;

		@SuppressWarnings("unchecked")
		public HLDecomposition(int n) {
			this.n = n;
			depth = new int[n];
			head = new int[n];
			heavy = new int[n];
			parent = new int[n];
			id = new int[n];
			sz = new int[n];
			g = new ArrayList[n];
			for (int i = 0; i < n; ++i) {
				g[i] = new ArrayList<>();
			}
			Arrays.fill(head, -1);
			Arrays.fill(id, -1);
			Arrays.fill(parent, -1);
		}

		void ae(int a, int b) {
			g[a].add(b);
			g[b].add(a);
		}

		void pre() {
			dfs(0, -1);
			bfs();
		}

		void bfs() {
			ArrayDeque<Integer> pend = new ArrayDeque<>();
			int gen = 0;
			pend.add(0);
			while (!pend.isEmpty()) {
				int v = pend.pollFirst();
				int top = v;
				for (; v != -1; v = heavy[v]) {
					id[v] = gen++;
					head[v] = top;
					for (int d : g[v]) {
						if (d == parent[v] || d == heavy[v]) {
							continue;
						}
						pend.add(d);
					}
				}
			}
		}

		int lca(int u, int v) {
			if (head[u] != head[v]) {
				if (depth[head[u]] < depth[head[v]]) {
					int tmp = u;
					u = v;
					v = tmp;
				}
				return lca(parent[head[u]], v);
			} else {
				if (depth[u] > depth[v]) {
					int tmp = u;
					u = v;
					v = tmp;
				}
				return u;
			}
		}

		int dfs(int c, int p) {
			parent[c] = p;
			int s = 1;
			int to = -1;
			for (int d : g[c]) {
				if (d == p)
					continue;
				depth[d] = depth[c] + 1;
				s += dfs(d, c);
				if (to == -1 || sz[d] > sz[to]) {
					to = d;
				}
			}
			sz[c] = s;
			heavy[c] = to;
			return s;
		}

	}

	static void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}

}