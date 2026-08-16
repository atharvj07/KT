import java.util.*;

public class Main {

	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = 0;
		while (true) {
			++num;
			int n = sc.nextInt();
			int t = sc.nextInt();
			int k = sc.nextInt();
			if (n == 0 && k == 0 && t == 0)
				break;
			ArrayList<Edge>[] g = new ArrayList[n];
			for (int i = 0; i < n; ++i)
				g[i] = new ArrayList<>();
			PriorityQueue<Edge> pq = new PriorityQueue<>();
			for (int i = 0; i < n - 1; ++i) {
				int a = sc.nextInt() - 1;
				int b = sc.nextInt() - 1;
				int c = sc.nextInt();
				g[a].add(new Edge(a, b, c));
				g[b].add(new Edge(b, a, c));
			}

			boolean[] base = new boolean[n];
			for (int i = 0; i < t; ++i) {
				int a = sc.nextInt() - 1;
				pq.addAll(g[a]);
				base[a] = true;
			}

			DJSet ds = new DJSet(n);

			ArrayList<Edge> pending = new ArrayList<>();
			while (!pq.isEmpty()) {
				Edge e = pq.poll();
				if (ds.equiv(e.dst, e.src))
					continue;
				if (base[e.dst] || ds.size(e.dst) > 1)
					pending.add(e);
				else {
					if (ds.setUnion(e.src, e.dst)) {
						pq.addAll(g[e.dst]);
					}

				}
			}

			Collections.sort(pending);

			long ans = 0;
			int len = pending.size();
			for (int i = 0, j = 0; j < k; ++i) {
				Edge e = pending.get(len - 1 - i);
				if (ds.equiv(e.src, e.dst))
					continue;
				ans += e.cost;
				ds.setUnion(e.src, e.dst);
				++j;
			}
			System.out.println("Case " + num + ": " + ans);
		}
	}

	static class Edge implements Comparable<Edge> {
		int src;
		int dst;
		int cost;

		public Edge(int src, int dst, int cost) {
			this.src = src;
			this.dst = dst;
			this.cost = cost;
		}

		@Override
		public int compareTo(Edge o) {
			return -Integer.compare(this.cost, o.cost);
		}

	}

	static class DJSet {
		int n;
		int[] upper;

		public DJSet(int n) {
			this.n = n;
			upper = new int[n];
			Arrays.fill(upper, -1);
		}

		int root(int x) {
			return upper[x] < 0 ? x : (upper[x] = root(upper[x]));
		}

		boolean setUnion(int x, int y) {
			x = root(x);
			y = root(y);
			if (x != y) {
				if (upper[x] < upper[y]) {
					int d = x;
					x = y;
					y = d;
				}
				upper[y] += upper[x];
				upper[x] = y;
			}
			return x != y;
		}

		boolean equiv(int x, int y) {
			return root(x) == root(y);
		}

		int size(int x) {
			return -upper[root(x)];
		}

	}
}