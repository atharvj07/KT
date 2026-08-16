import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class A {

	public static void main(String[] args) throws NumberFormatException, IOException {
		Scanner sc = new Scanner();
		PrintWriter out = new PrintWriter(System.out);
		V = sc.nextInt(); int m = sc.nextInt();
		long [] a = new long[V];
		int minIdx = 0;
		for (int i = 0; i < a.length; ++i) {
			a[i] = sc.nextLong();
			if(a[i] < a[minIdx]){
				minIdx = i;
			}
		}
		PriorityQueue<Edge> rem = new PriorityQueue<Edge>();
		adjList = new ArrayList[V];
		for (int i = 0; i < adjList.length; ++i) {
			adjList[i] = new ArrayList<>();
			if(i != minIdx)
				rem.add(new Edge(i, a[i]));
		}
		for (int i = 0; i < m; ++i) {
			int u = sc.nextInt()-1, v = sc.nextInt()-1;
			long w = sc.nextLong();
			adjList[u].add(new Edge(v, w));
			adjList[v].add(new Edge(u, w));
		}
		long mst = 0;
		boolean [] visited = new boolean[V];
		PriorityQueue<Edge> weights = new PriorityQueue<Edge>();
		for(Edge e:adjList[minIdx])
			weights.add(e);
		long min = a[minIdx];
		visited[minIdx] = true;
		loop: while(!rem.isEmpty())
		{
			while(!rem.isEmpty() && visited[rem.peek().node]) rem.poll();
			while(!weights.isEmpty() && visited[weights.peek().node]) weights.poll();
			if(rem.isEmpty())
				break;
			long cost = rem.peek().cost + min;
			if(!weights.isEmpty() && weights.peek().cost <= cost){
				Edge cur = weights.remove();
				mst += cur.cost;
				visited[cur.node] = true;
				for(Edge e:adjList[cur.node])
					if(!visited[e.node])
						weights.add(e);
				min = Math.min(min, a[cur.node]);
			}
			else{
				int cand = rem.peek().node;
				mst += cost;
				visited[cand] = true;
				for(Edge e:adjList[cand])
					if(!visited[e.node])
						weights.add(e);
				min = Math.min(min, a[cand]);
			}
		}	
		out.println(mst);
		out.close();
	}
	static ArrayList<Edge>[] adjList;
	static int V;

	static class Edge implements Comparable<Edge>
	{
		int node; long cost;

		Edge(int a, long b) { node = a; cost = b; }

		public int compareTo(Edge e) { return Long.compare(cost, e.cost); }

		@Override
		public boolean equals(Object e){
			Edge ed = (Edge) e;
			return node == ed.node && cost == ed.cost;

		}
	}
	static class Scanner {
		BufferedReader br;
		StringTokenizer st;

		public Scanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens()) {
				st = new StringTokenizer(br.readLine());
			}
			return st.nextToken();
		}

		public int nextInt() throws NumberFormatException, IOException {
			return Integer.parseInt(next());
		}
		public long nextLong() throws NumberFormatException, IOException {
			return Long.parseLong(next());
		}
	}

}
