import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;



public class Main {

	public static void main(String[] args) {
		IO io = new IO();
		int n = io.nextInt();
		int m = io.nextInt();
		int s = io.nextInt() - 1;
		int t = io.nextInt() - 1;
		int[] d = new int[n];
		for(int i=0;i<n;i++) {
			d[i] = io.nextInt();
		}
		Graph g = new Graph(n);
		for(int i=0;i<n-1;i++) {
			g.addEdge(i+1, i, 0);
		}
		for(int i=0;i<m;i++) {
			int a = io.nextInt() - 1;
			int b = io.nextInt() - 1;
			g.addEdge(a, b, d[b]);
		}
		System.out.println(g.minDistDijkstra(s)[t]);
	}

}
class Graph {
	public static final int INF = 1000000000;
	int n;
	ArrayList<Edge>[] graph;

	@SuppressWarnings("unchecked")
	public Graph(int n) {
		this.n = n;
		this.graph = new ArrayList[n];
		for(int i=0;i<n;i++) {
			graph[i] = new ArrayList<>();
		}
	}

	public void addBidirectionalEdge(int from, int to, int cost) {
		addEdge(from, to, cost);
		addEdge(to, from, cost);
	}
	public void addEdge(int from, int to, int cost) {
		graph[from].add(new Edge(to,cost));
	}

	public int[] minDistDijkstra(int s) {
		int[] dist = new int[n];
		Arrays.fill(dist, INF);
		dist[s] = 0;
		PriorityQueue<Node> q = new PriorityQueue<>();
		q.offer(new Node(0,s));
		while(!q.isEmpty()) {
			Node node = q.poll();
			int v = node.id;
			if (dist[v] < node.dist) {
				continue;
			}
			for(Edge e: graph[v]) {
				if (dist[e.to] > dist[v] + e.cost) {
					dist[e.to] = dist[v] + e.cost;
					q.add(new Node(dist[e.to], e.to));
				}
			}
		}
		return dist;
	}
	class Edge {
		int to,cost;
		public Edge(int to, int cost) {
			this.to = to;
			this.cost = cost;
		}
	}

	class Node implements Comparable<Node> {
		int dist,id;
		public Node(int dist, int i) {
			this.dist = dist;
			this.id = i;
		}
		public int compareTo(Node o) {
			return Integer.compare(dist, o.dist);
		}
	}
}
class IO extends PrintWriter {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = null;
	public IO() { super (System.out); };
	public String next() {
		while( st== null || !st.hasMoreTokens()) {
			String s;
			try {
				s = br.readLine();
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
			if (s == null) return null;
			st = new StringTokenizer(s);
		}
		return st.nextToken();
	}
	public int nextInt() {
		return Integer.parseInt(next());
	}
}
