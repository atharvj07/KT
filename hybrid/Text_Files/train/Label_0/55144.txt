import java.io.*;
import java.util.*;

public class A implements Runnable{
	public static void main (String[] args) {new Thread(null, new A(), "_cf", 1 << 28).start();}

	int ptr, append[];
	
	public void run() {
		FastScanner fs = new FastScanner();
		PrintWriter out = new PrintWriter(System.out);
		System.err.println("Go!");

		append = new int[1000]; ptr = 0;
		int n = fs.nextInt();
		int m = fs.nextInt();
		MaxFlowDinic mfd = new MaxFlowDinic();
		ST st = new ST(m);
		int nodes = 2 + n + st.n;
		ArrayList<Edge>[] graph = mfd.createGraph(nodes);
		int src = n + st.n, snk = src+1;
		
		int[][] data = new int[n][];
		for(int i = 0; i < n; i++) {
			int type = fs.nextInt();
			if(type == 0) { //list of k people they can hit
				int k = fs.nextInt();
				data[i] = new int[k+1];
				data[i][0] = type;
				for(int j = 1; j < data[i].length; j++) {
					data[i][j] = fs.nextInt()-1;
					mfd.addEdge(graph, i, n + st.loc[data[i][j]], 1);
				}
				mfd.addEdge(graph, src, i, 1);
				
			}
			else if(type == 1) { //range of [l, r] people they can hit
				data[i] = new int[3];
				data[i][0] = type;
				data[i][1] = fs.nextInt()-1;
				data[i][2] = fs.nextInt()-1;
				
				mfd.addEdge(graph, src, i, 1);
				
				ptr = 0;
				st.find(1, data[i][1], data[i][2]);
				for(int j = 0; j < ptr; j++) {
					mfd.addEdge(graph, i, n + append[j], 1);
				}
			}
			else { //can hit exactly 0/2 people.
				data[i] = new int[4];
				data[i][0] = type;
				for(int j = 1; j < 4; j++) {
					data[i][j] = fs.nextInt()-1;
					mfd.addEdge(graph, i, n + st.loc[data[i][j]], 1);
				}
				mfd.addEdge(graph, src, i, 2);
			}
		}
		
		int oo = (int)1e4;
		for(int i = 1; i < st.n; i++) {
			if(st.left[i] == -1) continue;
			if(st.left[i] == st.right[i]) {
				mfd.addEdge(graph, n + i, snk, 1);
			}
			else {
				mfd.addEdge(graph, n+i, n+st.left(i), oo);
				mfd.addEdge(graph, n+i, n+st.right(i), oo);
			}
		}
		
		int flow = mfd.maxFlow(graph, src, snk);
		out.println(flow);
		boolean[] hit = new boolean[m];
		for(int i = 1; i < st.n; i++) {
			if(st.left[i] == st.right[i] && st.left[i] != -1) {
				for(Edge e : graph[n + i]) if(e.t == snk && e.f > 0) {
					hit[ st.left[i] ] = true;
					break;
				}
			}
		}
		int[] id = new int[m]; Arrays.fill(id, -1);
		int[] gets = new int[3];
		for(int i = 0; i < n; i++) if(data[i][0] == 2) {
			int got = 0;
			ptr = 0; gets[0] = gets[1] = gets[2] = -1;
			for(Edge e : graph[i]) if(e.t != src) {
				if(e.f > 0) {
					got++;
					int it = e.t - n;
					id[st.left[it]] = i+1;
				}
				else if(hit[st.left[e.t-n]]) {
					gets[ptr++] = e.t;
				}
			}
			if(got == 1) {
				id[ st.left[gets[0] - n] ] = i+1;
			}
		}
		for(int i = 0; i < n; i++) if(data[i][0] == 0) {
			for(Edge e : graph[i]) if(e.t != src && e.f>0) {
				if(id[st.left[e.t-n]] == -1)
					id[st.left[e.t-n]] = i+1;
				break;
			}
		}
		for(int i = 0; i < n; i++) if(data[i][0] == 1) {
			int at = i;
			while(true) {
				int someone = -1;
				for(Edge e : graph[at]) if(e.f>0) {
					e.f--;
					at = e.t;
					someone = at;
					break;
				}
				if(someone == -1) break;
				if(at >= n && st.left[at-n] == st.right[at-n]) {
					if(id[st.left[at-n]] == -1) {
						id[st.left[at-n]] = i+1;
					}
					break;
				}
			}
		}
		for(int i = 0; i < m; i++) if(id[i] != -1) {
			out.printf("%d %d\n", id[i], i+1);
		}
		out.close();
	}
	
	class ST {
		int[] left, right;
		int[] loc;
		int n, nn;
		ST(int a) {
			nn = a;
			n = 4*a+100;
			left = new int[n];
			right = new int[n];
			Arrays.fill(left, -1); Arrays.fill(right, -1);
			loc = new int[nn];
			init(1, 0, a-1);
		}
		int left(int p) { return p << 1; }
		int right(int p) { return (p << 1)+1; }
		void init(int p, int ll, int rr) {
			left[p] = ll; right[p] = rr;
			if(ll == rr) {
				loc[ll] = p;
				return;
			}
			int mid = (ll + rr) / 2;
			init(left(p), ll, mid);
			init(right(p), mid+1, rr);
		}
		void find(int p, int ll, int rr) {
			if(rr < left[p] || ll > right[p]) return;
//			System.out.printf("Finding on %d [%d, %d] Looking for (%d, %d)\n", p, left[p], right[p], ll, rr);
			if(ll <= left[p] && right[p] <= rr) {
//				System.out.println(" Back");
				append[ptr++] = p;
				return;
			}
			if(left[p] == right[p]) return;
			find(left(p), ll, rr);
			find(right(p), ll, rr);
		}
	}
	
	class Edge {
		int t, rev, cap, f;
		public Edge(int t, int rev, int cap) {
			this.t = t;
			this.rev = rev;
			this.cap = cap;
		}
	}

	class MaxFlowDinic {
		ArrayList<Edge>[] createGraph(int nodes) {
			ArrayList<Edge>[] graph = new ArrayList[nodes];
			for (int i = 0; i < nodes; i++)
				graph[i] = new ArrayList<>();
			return graph;
		}

		void addEdge(List<Edge>[] graph, int s, int t, int cap) {
			graph[s].add(new Edge(t, graph[t].size(), cap));
			graph[t].add(new Edge(s, graph[s].size() - 1, 0));
		}

		boolean dinicBfs(List<Edge>[] graph, int src, int dest, int[] dist) {
			Arrays.fill(dist, -1);
			dist[src] = 0;
			int[] Q = new int[graph.length];
			int sizeQ = 0;
			Q[sizeQ++] = src;
			for (int i = 0; i < sizeQ; i++) {
				int u = Q[i];
				for (Edge e : graph[u]) {
					if (dist[e.t] < 0 && e.f < e.cap) {
						dist[e.t] = dist[u] + 1;
						Q[sizeQ++] = e.t;
					}
				}
			}
			return dist[dest] >= 0;
		}

		int dinicDfs(List<Edge>[] graph, int[] ptr, int[] dist, int dest, int u, int f) {
			if (u == dest)
				return f;
			for (; ptr[u] < graph[u].size(); ++ptr[u]) {
				Edge e = graph[u].get(ptr[u]);
				if (dist[e.t] == dist[u] + 1 && e.f < e.cap) {
					int df = dinicDfs(graph, ptr, dist, dest, e.t, Math.min(f, e.cap - e.f));
					if (df > 0) {
						e.f += df;
						graph[e.t].get(e.rev).f -= df;
						return df;
					}
				}
			}
			return 0;
		}

		int maxFlow(List<Edge>[] graph, int src, int dest) {
			int flow = 0;
			int[] dist = new int[graph.length];
			while (dinicBfs(graph, src, dest, dist)) {
				int[] ptr = new int[graph.length];
				while (true) {
					int df = dinicDfs(graph, ptr, dist, dest, src, Integer.MAX_VALUE);
					if (df == 0)
						break;
					flow += df;
				}
			}
			return flow;
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

		public FastScanner(String s) throws FileNotFoundException {
			in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
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