//https://github.com/EgorKulikov/yaal/tree/master/lib/main/net/egork
        
import java.util.*;
import java.io.*;
public class F{
    static PrintWriter out;
    static InputReader in;
    public static void main(String args[]){
        out = new PrintWriter(System.out);
        in = new InputReader();
        new F();
        out.flush(); out.close();
    }   
    F(){
        solve();
    }

	  class Edge {
	    int t, rev, cap, f;
	    public Edge(int t, int rev, int cap) {
	      this.t = t;
	      this.rev = rev;
	      this.cap = cap;
	    }
	  }
	  class tuple{
	  	int P, C, L;
	  	tuple(int a, int b, int c){
	  		P = a; C = b; L = c;
	  	}
	  }
	  final int max = Integer.MAX_VALUE / 100 - 100;
	  int maxv = 200010;
	  boolean comp[] = new boolean[maxv];

	  List<Edge>[] createGraph(int nodes) {
	    List<Edge>[] graph = new List[nodes];
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

    void solve(){
    	for(int i = 2; i < maxv; i++){
    		if(comp[i])continue;
    		for(int j = 2 * i; j < maxv; j += i){
    			comp[j] = true;
    		}
    	}

    	int n = in.nextInt(), k = in.nextInt();
    	int tot = 1 + n + n + 1, mincut = 0;
    	List<Edge> graph[] = createGraph(tot);
    	ArrayList<tuple> al = new ArrayList<>();
    	for(int i = 0; i < n; i++){
    		al.add(new tuple(in.nextInt(), in.nextInt(), in.nextInt()));
    	}
    	Collections.sort(al, (A, B) -> A.L - B.L);
    	int sum = 0;
    	for(int i = 0; i < al.size();){
    		tuple N = al.get(i);
    		int j = i; 
    		while(j < al.size() && al.get(j).L == N.L){
    			tuple T = al.get(j); sum += T.P;
    			int pid = j + 1;
    			addEdge(graph, 0, pid, T.P);
    			for(int x = 0; x < j; x++){
    				tuple T1 = al.get(x);
    				int nid = n + x + 1;
    				if(!comp[T.C + T1.C]){
    				    addEdge(graph, pid, nid, max);
    				    addEdge(graph, nid - n, pid + n, max);
    				}
    			}
    			int nid = n + j + 1;
    			addEdge(graph, nid, tot - 1, T.P);
    			j++;
    		}
    		mincut += maxFlow(graph, 0, tot - 1);
    		// System.out.println(N.L + " " + mincut + " " + sum);
    		if(2 * sum - mincut >= 2 * k){
    			out.println(N.L); return;
    		}
    		i = j;
    	}
    	out.println(-1);
    }
    public static class InputReader{
        BufferedReader br;
        StringTokenizer st;
        InputReader(){
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        public int nextInt(){
            return Integer.parseInt(next());
        }
        public long nextLong(){
            return Long.parseLong(next());
        }
        public double nextDouble(){
            return Double.parseDouble(next());
        }
        public String next(){
            while(st == null || !st.hasMoreTokens()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch(IOException e){}
            }
            return st.nextToken();
        }
    }
}
	