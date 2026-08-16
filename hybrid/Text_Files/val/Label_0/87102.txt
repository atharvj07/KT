import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		new Main().solver();
	}

	@SuppressWarnings("unchecked")
	void solver() {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] A = new int[N];
		int[] B = new int[N];
		ArrayList<Integer> list = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			A[i] = sc.nextInt();
			B[i] = sc.nextInt();
			list.add(A[i]);
			list.add(B[i]);
		}
		list.sort(null);
		for (int i = 0; i < list.size(); i++) {
			while (i + 1 < list.size() && list.get(i) == list.get(i + 1))
				list.remove(i + 1);
		}
		ArrayList<Edge>[] g = new ArrayList[N + list.size() + 3];
		for (int i = 0; i < g.length; i++) {
			g[i] = new ArrayList<>();
		}
		for (int i = 0; i < N; i++) {
			g[i].add(new Edge(i, list.indexOf(A[i]) + N, 1, -B[i]));
			if (A[i] != B[i]) {
				g[i].add(new Edge(i, list.indexOf(B[i]) + N, 1, -A[i]));
			}
			g[list.size() + N].add(new Edge(list.size() + N, i, 1, 0));
		}
		for (int i = 0; i < list.size(); i++) {
			g[i + N].add(new Edge(i + N, list.size() + N + 1, 1, 0));
		}

		// g[N+list.size()]:source
		// g[N+1+list.size()]:sink
		// g[N+2+list.size()]:unused vertice collector
		for (int i = 0; i < N; i++) {
			g[i].add(new Edge(i, N + 2 + list.size(), 1, 0));
		}
		g[N + 2 + list.size()].add(new Edge(N + 2 + list.size(), N + 1 + list.size(), N, 0));

		System.out.println(-1 * min_cost_flow(N + list.size(), N + list.size() + 1, g));

	}

	// I don't validated if this method work correctly dealing a graph which has
	// reversed edges.
	int min_cost_flow(int s, int t, ArrayList<Edge>[] g) {
		class Vertice implements Comparable<Vertice> {
			int id;
			long dist;

			public Vertice(int id, long dist) {
				this.id = id;
				this.dist = dist;
			}

			public int compareTo(Vertice o) {
				return Long.compare(this.dist, o.dist);
			};
		}

		int n = g.length;

		int min_cost = 0;
		g[t].add(new Edge(t, s, (1 << 30), 0));

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < g[i].size(); j++) {
				Edge e = g[i].get(j);
				g[e.src].get(j).rev_id = g[e.dst].size();
				g[e.dst].add(new Edge(e.dst, e.src, 0, -e.cost));
				g[e.dst].get(g[e.dst].size() - 1).rev_id = j;
			}
		}

		long[] potential = new long[n];
		int[] excess = new int[n];
		for (int i = 0; i < n; i++) {
			for (Edge e : g[i]) {
				if (e.cost < 0) {
					e.add_flow(e.cap);
					excess[e.dst] += e.flow;
					excess[e.src] -= e.flow;
					g[e.dst].get(e.rev_id).add_flow(-e.cap);
					min_cost += e.cost * e.flow;
				}
			}
		}

		ArrayList<Integer> sink_v = new ArrayList<>();
		ArrayDeque<Integer> source_v = new ArrayDeque<>();

		for (int i = 0; i < n; i++) {
			if (excess[i] < 0)
				sink_v.add(i);
			else if (excess[i] > 0)
				source_v.add(i);
		}
		while (!source_v.isEmpty()) {

			PriorityQueue<Vertice> priority_queue = new PriorityQueue<>();
			int[] pre_v = new int[n];
			int[] pre_e = new int[n];
			long[] dist = new long[n];
			Arrays.fill(pre_v, -1);
			Arrays.fill(pre_e, -1);
			Arrays.fill(dist, 1L << 60);
			int source = source_v.poll();
			dist[source] = 0;
			pre_v[source] = -1;
			pre_e[source] = -1;
			boolean[] looked = new boolean[n];

			priority_queue.add(new Vertice(source, 0));

			while (!priority_queue.isEmpty()) {
				int v = priority_queue.poll().id;
				if (looked[v])
					continue;
				else
					looked[v] = true;
				for (int i = 0; i < g[v].size(); i++) {
					Edge e = g[v].get(i);
					if (e.residue > 0) {
						if (dist[e.dst] > dist[v] + e.cost - potential[v] + potential[e.dst]) {
							dist[e.dst] = dist[v] + e.cost - potential[v] + potential[e.dst];

							priority_queue.add(new Vertice(e.dst, dist[e.dst]));
							pre_v[e.dst] = v;
							pre_e[e.dst] = i;
							looked[e.dst] = false;
						}
					}
				}
			}
			int sink = -1;
			for (int i = 0; i < sink_v.size(); i++) {
				if (pre_v[sink_v.get(i)] != -1) {
					sink = sink_v.get(i);
					sink_v.remove(i);
					break;
				}
			}
			if (sink == -1) {
				source_v.add(source);
				continue;
			}

			for (int i = 0; i < n; i++) {
				if (dist[i] < (1L << 60))
					potential[i] -= dist[i];
				else
					potential[i] -= (1 << 30);
			}

			int delta = Math.min(Math.abs(excess[source]), Math.abs(excess[sink]));

			for (int i = sink; i != source; i = pre_v[i]) {
				delta = Math.min(delta, g[pre_v[i]].get(pre_e[i]).residue);
			}
			for (int i = sink; i != source; i = pre_v[i]) {
				Edge e = g[pre_v[i]].get(pre_e[i]);
				e.add_flow(delta);
				g[i].get(e.rev_id).add_flow(-delta);
				min_cost += delta * e.cost;
			}
			excess[sink] += delta;
			excess[source] -= delta;
			if (excess[sink] < 0)
				sink_v.add(sink);
			if (excess[source] > 0)
				source_v.add(source);

		}

		return min_cost;
	}

	void show_reduced_cost(ArrayList<Edge>[] g, long[] potential) {
		int n = g.length;
		for (int i = 0; i < n; i++) {
			for (Edge e : g[i]) {
				if (e.residue > 0)
					System.out.println("??°???´???????¨" + (e.cost - potential[e.src] + potential[e.dst]));
			}
		}
	}

	class Edge {
		int src;
		int dst;
		int cap;
		int cost;
		int residue;
		int flow = 0;
		int rev_id = -1;

		Edge(int src, int dst, int cap, int cost) {
			this.src = src;
			this.dst = dst;
			this.cap = cap;
			this.cost = cost;
			residue = this.cap - flow;
		}

		void add_flow(int flow) {
			this.flow += flow;
			residue = cap - this.flow;
		}

	}

	void tr(Object... o) {
		System.out.println(Arrays.deepToString(o));
	}
}