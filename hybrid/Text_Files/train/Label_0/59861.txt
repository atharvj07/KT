
import java.util.ArrayList;
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
			int n = scanner.nextInt();
			int m = scanner.nextInt();
			if ((n | m) == 0)
				break;
			List<Edge>[] lists = new ArrayList[n];
			for (int i = 0; i < n; i++) {
				lists[i] = new ArrayList<Edge>();
			}
			for (int i = 0; i < m; i++) {
				int from = scanner.nextInt() - 1;
				int to = scanner.nextInt() - 1;
				int cost = scanner.nextInt();
				lists[from].add(new Edge(to, cost));
				lists[to].add(new Edge(from, cost));
			}
			int g = n - 1;
			PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
			pq.offer(new Edge(0, 0, 2));
			boolean[][] b = new boolean[3][n];
			b[0][0] = true;
			while (!pq.isEmpty()) {
				Edge edge = pq.poll();
				if (edge.to == g && edge.ticket != 1) {
					System.out.println(edge.cost);
					break;
				}
				if (b[edge.ticket][edge.to])
					continue;
				b[edge.ticket][edge.to] = true;

				for (Edge e : lists[edge.to]) {
					if (edge.ticket == 1) {
						pq.offer(new Edge(e.to, edge.cost, 0));
					} else {
						if (edge.ticket == 2) {
							pq.offer(new Edge(e.to, edge.cost, 1));
						}
						pq.offer(new Edge(e.to, edge.cost + e.cost, edge.ticket));
					}
				}
			}
		}
	}

	class Edge implements Comparable<Edge> {
		int to, cost, ticket;

		public Edge(int to, int cost, int ticket) {
			super();
			this.to = to;
			this.cost = cost;
			this.ticket = ticket;
		}

		public Edge(int to, int cost) {
			super();
			this.to = to;
			this.cost = cost;
		}

		@Override
		public String toString() {
			return "Edge [to=" + to + ", cost=" + cost + ", ticket=" + ticket
					+ "]";
		}

		@Override
		public int compareTo(Edge o) {
			if (this.cost == o.cost)
				return o.to - this.to;
			return this.cost - o.cost;
		}

	}
}