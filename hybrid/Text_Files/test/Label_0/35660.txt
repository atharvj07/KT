import java.util.*;
import java.io.*;

public class Main {

	BufferedReader in;
	StringTokenizer str = null;
	PrintWriter out;
	
	private String next() throws Exception{
		while (str == null || !str.hasMoreElements())
			str = new StringTokenizer(in.readLine());
		return str.nextToken();
	}
	
	private int nextInt() throws Exception{
		return Integer.parseInt(next());
	}
	
	private long nextLong() throws Exception{
		return Long.parseLong(next());
	}
	
	private double nextDouble() throws Exception{
		return Double.parseDouble(next());
	}
	
	public void run() throws Exception{
		in =  new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		
		int n = nextInt(), m = nextInt();
		int []a = new int[n];
		for(int i=0;i<n;i++) a[i] = nextInt();

		PriorityQueue<Edge> pq = new PriorityQueue<Edge>();

		for(int i=0;i<m;i++){
			int x = nextInt()-1;
			int y = nextInt()-1;
			Edge e = new Edge(x, y, Math.min(a[x], a[y]));
			pq.add(e);
		}

		p = new int[n];
		size = new int[n];
		for(int i=0;i<n;i++) {
			p[i] = i;	
			size[i] = 1;
		} 

		double ret = 0;
		while(pq.size() > 0) {
			Edge c = pq.poll();
			int u = c.u, v = c.v;
			u = find(u);
			v = find(v);

			if (u != v) {
				int size1 = size[u];
				int size2 = size[v];
				union(u, v);
				ret+=1L * c.cost * size1 * size2;
			}
		}
		
		out.println(2.*ret/n/(n-1));
		out.close();
	}

	int []p, size;

	private int find(int x){
		if (x != p[x])
			return p[x] = find(p[x]);
		return x;
	}

	private void union(int x, int y) {
		x = find(x);
		y = find(y);
		p[y] = x;
		size[x]+=size[y];
	}

	static class Edge implements Comparable<Edge> {
		int v, u, cost;

		public Edge(int v, int u, int cost) {
			this.v = v;
			this.u = u;
			this.cost = cost;
		}

		public int compareTo(Edge e) {
			if (cost > e.cost) return -1;
			if (cost < e.cost) return 1;
			return 0;
		}
	}
		
	public static void main(String[] args) throws Exception{
		new Main().run();
	}
}
