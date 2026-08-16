import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

public class Main {

	static int ans[];
	static int count = 0;

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {

			String str[] = br.readLine().split(" ");

			int n = Integer.parseInt(str[0]);
			int m = Integer.parseInt(str[1]);

			if (n == 0 && m == 0)
				break;

			ans = new int[n];
			Arrays.fill(ans, 0);
			count = 0;

			ArrayList<ArrayList<Edge>> edge = new ArrayList<>();

			for (int i = 0; i < n; i++) {
				edge.add(new ArrayList<>());
			}

			for (int i = 0; i < m; i++) {
				str = br.readLine().split(" ");

				int s = Integer.parseInt(str[0]) - 1;
				int t = Integer.parseInt(str[1]) - 1;
				int c = Integer.parseInt(str[2]);

				edge.get(s).add(new Edge(t, c));
				edge.get(t).add(new Edge(s, c));
			}

			prime(edge, n);
			Arrays.sort(ans);

			System.out.println(ans[n / 2]);
		}
	}

	static void prime(ArrayList<ArrayList<Edge>> edges, int n) {
		boolean[] done = new boolean[n];

		Queue<Edge> q = new PriorityQueue<Edge>();
		q.add(new Edge(0, 0)); // 0から(ダミー)

		double totalCost = 0;
		while (!q.isEmpty()) {
			Edge e = q.poll(); // 最小コストの辺を取り出す
			if (done[e.to]) {
				continue;
			}

			done[e.to] = true; // 訪問済にする
			ans[count++] = e.cost;
			q.addAll(edges.get(e.to)); // 隣接しているすべての辺を追加
		}
	}
}

class Edge implements Comparable<Edge> {
	int to;
	int cost;

	public Edge(int to, int cost) {
		this.to = to;
		this.cost = cost;

	}

	@Override
	public int compareTo(Edge e) {
		return this.cost - e.cost;
	}
}

