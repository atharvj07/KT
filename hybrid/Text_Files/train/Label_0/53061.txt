
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		new Main().run();
	}

	@SuppressWarnings("unchecked")
	private void run() {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			n = scanner.nextInt();
			if (n == 0)
				break;
			lists = new ArrayList[n];
			for (int i = 0; i < n; i++)
				lists[i] = new ArrayList<Edge>();
			for (int i = 0; i < n - 1; i++) {
				int from = scanner.nextInt() - 1;
				int to = scanner.nextInt() - 1;
				int cost = scanner.nextInt();
				lists[from].add(new Edge(to, cost));
				lists[to].add(new Edge(from, cost));
			}
			for (int i = 0; i < n; i++) {
				if (lists[i].size() == 1 && i != 0) {
					lists[i].get(0).cost = INF;
				} else
					for (Edge edge : lists[i]) {
						if (lists[edge.to].size() == 1 && edge.to != 0)
							edge.cost = INF;
					}
			}
			int sum = 0;
			for (List<Edge> list : lists)
				for (Edge edge : list)
					if (edge.cost != INF)
						sum += edge.cost;
			PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
			pq.offer(new Edge(0, 0));
			int[] costs = new int[n];
			Arrays.fill(costs, 1 << 24);
			costs[0] = 0;
			while (!pq.isEmpty()) {
				Edge edge = pq.poll();
				for (Edge e : lists[edge.to]) {
					if (costs[e.to] > e.cost + edge.cost) {
						costs[e.to] = e.cost + edge.cost;
						pq.offer(new Edge(e.to, costs[e.to]));
					}
				}
			}
			int max = 0;
			for (int ans : costs) {
				if (ans == INF)
					continue;
				max = Math.max(max, ans);
			}
			System.out.println(sum - max);
		}
	}

	int n;
	List<Edge>[] lists;
	int INF = 1 << 24;

	class Edge implements Comparable<Edge> {
		int to, cost;

		Edge() {
		}

		public Edge(int to, int cost) {
			super();
			this.to = to;
			this.cost = cost;
		}

		@Override
		public String toString() {
			return "Edge [to=" + to + ", cost=" + cost + "]";
		}

		@Override
		public int compareTo(Edge o) {
			return this.cost - o.cost;
		}

	}
}