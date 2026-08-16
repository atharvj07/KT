import java.io.*;
import java.util.*;

public class A {
	public static void main (String[] args) { new A(); }

	public A() {
		FastScanner fs = new FastScanner();
		PrintWriter out = new PrintWriter(System.out);
		System.err.println("");

		int n = fs.nextInt();
		int m = fs.nextInt();
		
		if(n == 1 && m == 1) {
			System.out.println(1);
			return;
		}
		
		char[][] g = new char[n][m];
		int sumNodes = 0;
		
		for(int i = 0; i < n; i++) {
			g[i] = fs.next().toCharArray();
			for(char ch : g[i]) if(ch == '#') sumNodes++;
		}
		
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		
		int[][][] nodeID = new int[4][n][m];
		for(int[][] x : nodeID)
			for(int[] y : x)
				Arrays.fill(y, -1);
		
		int curNode = 0;
		boolean[] leftSide = new boolean[4 * n * m];
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(g[i][j] != '#') continue;
				
				for(int k = 0; k < 4; k++) {
					int nx = dx[k]+i, ny = dy[k]+j;
					if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
					if(g[nx][ny] != '#') continue;
					
					if(nodeID[k][i][j] != -1) continue;
					
					nodeID[k][i][j] = curNode;
					nodeID[k ^ 1][nx][ny] = curNode;
					
					if(k < 2) leftSide[curNode] = true;
					else leftSide[curNode] = false;
					
					curNode++;
				}
				
			}
		}
		
		Dinic dinic = new Dinic(curNode);
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(g[i][j] != '#') continue;
				
				for(int k1 = 0; k1 < 2; k1++) {
					if(nodeID[k1][i][j] == -1) continue;
					int u = nodeID[k1][i][j];
					
					for(int k2 = 2; k2 < 4; k2++) {
						if(nodeID[k2][i][j] == -1) continue;
						
						int v = nodeID[k2][i][j];
						
						dinic.add(u, v, 1, 0);
						
					}
				}
				
			}
		}

		for(int i = 0; i < curNode; i++) {
			if(leftSide[i]) dinic.add(dinic.s, i, 1, 0);
			else dinic.add(i, dinic.t, 1, 0);
		}
		
		dinic.flow();
		
		ArrayList<MyEdge>[] adj = new ArrayList[curNode];
		for(int i = 0; i < curNode; i++) adj[i] = new ArrayList<>();
		
		boolean[] isMatched = new boolean[curNode];
		
		for(int i = 0; i < curNode; i++) {
			if(!leftSide[i]) continue;
			
			for(Edge e : dinic.adj[i]) {
				if(e.v2 < curNode && !leftSide[e.v2] && e.cap > 0) {
					
					boolean isMatch = e.flow > 0;

					if(isMatch) {
						isMatched[e.v1] = isMatched[e.v2] = true;
						adj[e.v2].add(new MyEdge(e.v2, e.v1, isMatch));
					}
					else {
						adj[e.v1].add(new MyEdge(e.v1, e.v2, isMatch));
					}
					
				}
			}
		}
		
		int[] state = new int[curNode];
		Arrays.fill(state, -1);
		//0 = visited on left side
		//1 = unvisited on left side
		//2 = visited on right side
		//3 = unvisited on right side
		
		ArrayDeque<Integer> dq = new ArrayDeque<>();

		for(int i = 0; i < curNode; i++) {
			if(!leftSide[i]) continue;
			if(isMatched[i] || state[i] == 0) continue;
			
			state[i] = 0;
			dq.add(i);
			
			while(!dq.isEmpty()) {
				int u = dq.pollFirst();

				for(MyEdge e : adj[u]) {
					if(state[e.v] != -1) continue;
					if(leftSide[u]) state[e.v] = 2;
					else state[e.v] = 0;
					
					dq.add(e.v);
				}
				
			}
			
		}
		
		int maxIndSet = 0;
		for(int i = 0; i < curNode; i++) {
			if(leftSide[i]) {
				if(state[i] == 0) maxIndSet++;
			}
			else {
				if(state[i] == -1) maxIndSet++;
			}
		}
		
		out.println(sumNodes - maxIndSet);
		
		out.close();
	}
	
	class MyEdge {
		int u, v;
		boolean matchingEdge;
		MyEdge(int a, int b, boolean c) {
			u = a;
			v = b;
			matchingEdge = c;
		}
	}
	
	static class Edge {  int v1, v2, cap, flow; Edge rev;
	Edge(int V1, int V2, int Cap, int Flow) { v1 = V1; v2 = V2; cap = Cap; flow = Flow; }
	}
	static class Dinic {

		ArrayDeque<Integer> q;  ArrayList<Edge>[] adj;
		int n, s, t, mS, mT, oo = (int)1E9;
		boolean[] blocked;  int[] dist;
		public Dinic (int N) {
			n = N; s = n++; t = n++; mS = n++; mT = n++; blocked = new boolean[n];
			dist = new int[n];  q = new ArrayDeque<Integer>();
			adj = new ArrayList[n];  for(int i = 0; i < n; ++i)  adj[i] = new ArrayList<Edge>();
		}
		// Specifying flow can represent minimum flow for circulation.
		Edge add(int v1, int v2, int cap, int flow) {
			Edge e = new Edge(v1, v2, cap, flow);  Edge rev = new Edge(v2, v1, 0, 0);
			adj[v1].add(rev.rev = e);  adj[v2].add(e.rev = rev);
			return e;
		}

		boolean bfs() {
			q.clear();  Arrays.fill(dist, -1);  dist[t] = 0;  q.add(t);

			while(!q.isEmpty()) {
				int node = q.poll();
				if(node == s)   return true;
				for(Edge e : adj[node]) {
					if(e.rev.cap > e.rev.flow && dist[e.v2] == -1) {
						dist[e.v2] = dist[node] + 1;  q.add(e.v2);
					}
				}
			}
			return dist[s] != -1;
		}

		int dfs(int pos, int min) {
			if(pos == t)  return min;
			int flow = 0;
			for(Edge e : adj[pos]) {
				int cur = 0;
				if(!blocked[e.v2] && dist[e.v2] == dist[pos]-1 && e.cap - e.flow > 0) {
					cur = dfs(e.v2, Math.min(min-flow, e.cap - e.flow));
					e.flow += cur;  e.rev.flow = -e.flow;  flow += cur;
				}
				if(flow == min)  return flow;
			}
			blocked[pos] = flow != min;
			return flow;
		}
		int flow() {
			int ret = 0;
			while(bfs()) {  Arrays.fill(blocked, false);  ret += dfs(s, oo);  }
			return ret;
		}
	}

	class FastScanner {
		public int BS = 1<<16;
		public char NC = (char)0;
		byte[] buf = new byte[BS];
		int bId = 0, size = 0;
		char c = NC;
		double num = 1;
		BufferedInputStream in;

		public FastScanner() {
			in = new BufferedInputStream(System.in, BS);
		}

		public FastScanner(String s) {
			try {
				in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
			}
			catch (Exception e) {
				in = new BufferedInputStream(System.in, BS);
			}
		}

		public char nextChar(){
			while(bId==size) {
				try {
					size = in.read(buf);
				}catch(Exception e) {
					return NC;
				}                
				if(size==-1)return NC;
				bId=0;
			}
			return (char)buf[bId++];
		}

		public int nextInt() {
			return (int)nextLong();
		}

		public long nextLong() {
			num=1;
			boolean neg = false;
			if(c==NC)c=nextChar();
			for(;(c<'0' || c>'9'); c = nextChar()) {
				if(c=='-')neg=true;
			}
			long res = 0;
			for(; c>='0' && c <='9'; c=nextChar()) {
				res = (res<<3)+(res<<1)+c-'0';
				num*=10;
			}
			return neg?-res:res;
		}

		public double nextDouble() {
			double cur = nextLong();
			return c!='.' ? cur:cur+nextLong()/num;
		}

		public String next() {
			StringBuilder res = new StringBuilder();
			while(c<=32)c=nextChar();
			while(c>32) {
				res.append(c);
				c=nextChar();
			}
			return res.toString();
		}

		public String nextLine() {
			StringBuilder res = new StringBuilder();
			while(c<=32)c=nextChar();
			while(c!='\n') {
				res.append(c);
				c=nextChar();
			}
			return res.toString();
		}

		public boolean hasNext() {
			if(c>32)return true;
			while(true) {
				c=nextChar();
				if(c==NC)return false;
				else if(c>32)return true;
			}
		}
		
		public int[] nextIntArray(int n) {
			int[] res = new int[n];
			for(int i = 0; i < n; i++) res[i] = nextInt();
			return res;
		}
		
	}

}