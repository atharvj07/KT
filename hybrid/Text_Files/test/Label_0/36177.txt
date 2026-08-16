import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Vector;


public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		
		int v = sc.nextInt();
		int e = sc.nextInt();
		
		ArrayList<Edge> path = new ArrayList<Edge>();
		for(int i = 0; i < e; i++){
			
			path.add(new Edge(sc.nextInt(), sc.nextInt(), sc.nextInt(), 0));
		}
		
		System.out.println(solve(v, path));

	}
	
	static int solve(int V, ArrayList<Edge> path){
		//グラフの隣接リスト表現
		@SuppressWarnings("unchecked")
		Vector<Edge> G[] = new Vector[V];
		for(int i = 0; i < G.length; i++){
			G[i] = new Vector<Edge>();
		}
				
		//頂点間を結ぶ
		Iterator<Edge> it = path.iterator();
		while(it.hasNext()){
			Edge tmpEdge = it.next();
			addEdge(G, tmpEdge.from, tmpEdge.to, tmpEdge.cap);
		}
		
		return maxFlow(G, 0, V - 1);
	}
	
	static void addEdge(Vector<Edge>[] graph, int from, int to, int cap){
		graph[from].add(new Edge(-1, to, cap, graph[to].size()));
		graph[to].add(new Edge(-1, from, 0, graph[from].size() - 1));
	}
	
	static int maxFlow(Vector<Edge>[] graph, int s, int t){
		int flow = 0;
		
		boolean used[] = new boolean[graph.length];
		
		while(true){
			Arrays.fill(used, false);
			int f = dfs(graph, used, s, t, Integer.MAX_VALUE);
			if(f == 0){
				return flow;
			}
			flow += f;
			
		}
	}
	
	static int dfs(Vector<Edge>[] graph, boolean[] used, int v, int t, int f){
		if(v == t){
			return f;
		}
		
		used[v] = true;
		
		for(int i = 0; i < graph[v].size() ; i++){
			Edge e = graph[v].get(i);

			if(!used[e.to] && e.cap > 0){
				int d = dfs(graph, used, e.to, t, Math.min(f, e.cap));
				if(d > 0){
					e.cap -= d;
					graph[e.to].get(e.rev).cap += d;
					return d;
				}
			}
		}

		return 0;
	}	
}

class Edge {
	int from;
	int to;//行き先
	int cap;//容量
	int rev;//逆辺
	private int originalCap;
	
	Edge(int from, int to, int cap, int rev){
		this.from = from;
		this.to = to;
		this.cap = cap;
		this.rev = rev;
		this.originalCap = cap;
	}
	
	void recovery(){
		cap = originalCap;
	}
}
