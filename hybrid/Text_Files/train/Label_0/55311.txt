import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Random;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.TreeSet;

@SuppressWarnings("unused")
public class Solution{
	
	static int N = 3100, S = 0, T = 3050;
	static final int inf = (int)1e9;
	static ArrayList<int[]>[] g;
	static int[] a;
	static int num = 1;
	
	
	public static void main(String[] args) throws IOException {
		FastScanner fs = new FastScanner();
    	PrintWriter out = new PrintWriter(System.out);
    	
    	int tt = 1;
    	outer:
    	while(tt-->0) {
    		
    		int n = fs.nextInt(), m = fs.nextInt();
    		a = new int[n+1];
    		for(int i=1;i<=n;i++) a[i] = fs.nextInt();
    		int[][] p = new int[m][2];
    		
    		for(int i=0;i<m;i++) {
    			p[i][0] = fs.nextInt(); p[i][1] = fs.nextInt();
    			if(p[i][0]%2!=0) {
    				int temp = p[i][0]; p[i][0] = p[i][1]; p[i][1] = temp;
    			}
    		}
    		
    		g = new ArrayList[n+1];
    		for(int i=0;i<=n;i++) g[i] = new ArrayList<int[]>();
    		
    		for(int i=1;i<=n;i++) {
    			factorize(i);
    		}
    		
    		
    		Dinic d = new Dinic(N, S, T);
    		boolean[] left = new boolean[4000], right = new boolean[4000];
    		
    		for(int i=0;i<m;i++) {
    			int fr = p[i][0], sec = p[i][1];
    			for(int[] ar1: g[fr]) {
    				for(int[] ar2: g[sec]) {
    					if(ar1[1]==ar2[1]) {
    						d.addEdge(ar1[0], ar2[0], 1);
    						if(!left[ar1[0]]) { d.addEdge(S, ar1[0], 1); left[ar1[0]] = true; }
    						if(!right[ar2[0]]) { d.addEdge(ar2[0], T, 1); right[ar2[0]] = true; }
    					}
    				}
    			}
    		}
    		
    		
    		out.print(d.maxFlow());
    		
    		
    	}
    	
    	out.close();
    }
	
	
	static void factorize(int idx) {
		int x = a[idx];
		for(int i=2;i*i<=x;i++) {
			while(x%i==0) {
				x /= i;
				g[idx].add(new int[] {num++, i});
			}
		}
		if(x>1) g[idx].add(new int[] {num++, x});
	}
	
	
	static class Edge{
		int u, v;
		long cap, flow = 0;
		Edge(int u, int v, long cap){
			this.u = u; this.v = v; this.cap = cap;
		}
	}
	
	static class Dinic{
		ArrayList<Edge> edges;
		ArrayList<Integer>[] g;
		int n, s, t, m = 0;
		ArrayDeque<Integer> q;
		int[] level, ptr;
		
		Dinic(int n, int s, int t){
			this.n = n; this.s = s; this.t = t;
			edges = new ArrayList<>();
			g = new ArrayList[n];
			for(int i=0;i<n;i++) g[i] = new ArrayList<>();
			q = new ArrayDeque<>();
			level = new int[n]; ptr = new int[n];
		}
		
		void addEdge(int u, int v, long cap) {
			edges.add(new Edge(u, v, cap));
			edges.add(new Edge(v, u, 0));
			g[u].add(m);
			g[v].add(m+1);
			m += 2;
		}
		
		boolean bfs() {
			q.add(s);
			while(!q.isEmpty()) {
				int u = q.poll();
				for(int id: g[u]) {
					int next = edges.get(id).v;
					if(level[next]!=-1 || edges.get(id).cap-edges.get(id).flow==0) continue;
					level[next] = 1 + level[u];
					q.add(next);
				}
			}
			return level[t] != -1;
		}
		
		
		long dfs(int u, long pushed) {
			if(u==t) return pushed;
			for(;ptr[u]<g[u].size();ptr[u]++) {
				int id = g[u].get(ptr[u]);
				int next = edges.get(id).v;
				if(level[next] != level[u] + 1 || edges.get(id).cap-edges.get(id).flow==0) continue;
				long num = dfs(next, Math.min(pushed, edges.get(id).cap-edges.get(id).flow));
				if(num==0) continue;
				edges.get(id).flow += num;
				edges.get(id^1).flow -= num;
				return num;
			}
			return 0;
		}
		
		
		long maxFlow() {
			long flow = 0;
			while(true) {
				Arrays.fill(level, -1);
				level[s] = 0;
				if(!bfs()) {
					break;
				}
				Arrays.fill(ptr, 0);
				while(true) {
					long x = dfs(s, (long)1e18);
					if(x==0) break;
					flow += x;
				}
			}
			return flow;
		}
		
		
	}
	
	
	
	

	
    static final Random random=new Random();
    
    static <T> void shuffle(T[] arr) {
    	int n = arr.length;
    	for(int i=0;i<n;i++	) {
    		int k = random.nextInt(n);
    		T temp = arr[k]; arr[k] = arr[i]; arr[i] = temp;
    	}
    }
    
    	
    static void ruffleSort(int[] a) {
    	int n=a.length;//shuffle, then sort 
    	for (int i=0; i<n; i++) {
    		int oi=random.nextInt(n); int temp=a[oi];
    		a[oi]=a[i]; a[i]=temp;
    	}
    	Arrays.sort(a);
    }
    
    static void ruffleSort(long[] a) {
    	int n=a.length;//shuffle, then sort 
    	for (int i=0; i<n; i++) {
    		int oi=random.nextInt(n); long temp=a[oi];
    		a[oi]=a[i]; a[i]=temp;
    	}
    	Arrays.sort(a);
    }
   
  
    
    static void reverse(int[] arr, int l, int r) {
    	for(int i=l;i<l+(r-l)/2;i++){
    		int temp = arr[i]; arr[i] = arr[r-i+l-1]; arr[r-i+l-1] = temp;
    	}
    }
    
    static void reverse(long[] arr, int l, int r) {
    	for(int i=l;i<l+(r-l)/2;i++){
    		long temp = arr[i]; arr[i] = arr[r-i+l-1]; arr[r-i+l-1] = temp;
    	}
    }
    
    
    static <T> void reverse(T[] arr, int l, int r) {
    	for(int i=l;i<l+(r-l)/2;i++) {
    		T temp = arr[i]; arr[i] = arr[r-i+l-1]; arr[r-i+l-1] = temp;
    	}
    }
    	
    	
    static class FastScanner{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer("");
     
    	public String next(){
    		while(!st.hasMoreElements()){
    			try{
    				st = new StringTokenizer(br.readLine());
    			} catch(IOException e){
    				e.printStackTrace();
    			}
    		}
    		return st.nextToken();
    	}
    		
    	public String nextLine() throws IOException {
    		return br.readLine();
    	}
    		
    	public int nextInt(){
    		return Integer.parseInt(next());
    	}
     
    	public int[] readArray(int n){
    		int[] a = new int[n];
    		for(int i=0;i<n;i++)
    			a[i] = nextInt();
    		return a;
    	}
    		
    	public long nextLong() {
    		return Long.parseLong(next());
    	}
    		
    	public char nextChar() {
    		return next().toCharArray()[0];
    	}
    }


   	
}
