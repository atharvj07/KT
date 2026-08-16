import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int Q = sc.nextInt();
		int[] A = new int[Q];
		int[] B = new int[Q];
		long[] C = new long[Q];
		long[] min_cost = new long[N];
		Arrays.fill(min_cost, Long.MAX_VALUE/ 10);
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		for (int i = 0; i < Q; ++i) {
			A[i] = sc.nextInt();
			B[i] = sc.nextInt();
			C[i] = sc.nextInt();
			pq.add(new Edge(A[i], B[i], C[i]));
			min_cost[A[i]] = Math.min(min_cost[A[i]], C[i] + 1);
			min_cost[B[i]] = Math.min(min_cost[B[i]], C[i] + 2);
		}
		for (int i = 0; i < 2 * N; ++i) {
			min_cost[(i + 1) % N] = Math.min(min_cost[(i + 1) % N], min_cost[i % N] + 2);
		}
		for (int i = 0; i < N; ++i) {
			pq.add(new Edge(i, (i + 1) % N, min_cost[i]));
		}
		DJSet ds = new DJSet(N);
		long ret = 0;
		while (!pq.isEmpty()) {
			Edge edge = pq.poll();
			if (ds.equiv(edge.a, edge.b))
				continue;
			ret += edge.cost;
			ds.setUnion(edge.a, edge.b);
			pq.add(new Edge(edge.b, (edge.a + 1) % N, edge.cost + 1));
		}
		System.out.println(ret);

	}

	static class DJSet {
		int n = 1;
		int[] upper;

		public DJSet(int n) {
			this.n = n;
			upper = new int[n];
			Arrays.fill(upper, -1);
		}

		int root(int x) {
			return upper[x] < 0 ? x : (upper[x] = root(upper[x]));
		}

		boolean equiv(int x, int y) {
			return root(x) == root(y);
		}

		void setUnion(int x, int y) {
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
		}
	}

	static class Edge implements Comparable<Edge> {
		int a;
		int b;
		long cost;

		public Edge(int a, int b, long cost) {
			this.a = a;
			this.b = b;
			this.cost = cost;
		}

		@Override
		public int compareTo(Edge o) {
			return Long.compare(this.cost, o.cost);
		}
	}
}
