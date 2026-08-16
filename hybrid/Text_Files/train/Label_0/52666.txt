import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

//Rock Man
public class Main{

	int n, COUNT, INF = 1<<29, res;
	
	List<E>[] edge, rev;
	Map<String, Integer> ref;
	int get(String s){
		if(ref.containsKey(s))return ref.get(s);
		ref.put(s, COUNT);
		return COUNT++;
	}
	
	class E{
		int t, c;
		public E(int t, int c) {
			this.t = t;
			this.c = c;
		}
	}
	
	boolean[] visited;
	List<Integer> list;
	void dfs(int k){
		if(visited[k])return;
		visited[k] = true;
		for(E e:edge[k])dfs(e.t);
		list.add(k);
	}
	int[] scc;
	void rdfs(int k, int ID){
		if(visited[k])return;
		visited[k] = true;
		scc[k] = ID;
		for(E e:rev[k])rdfs(e.t, ID);
	}
	
	int cycle(int k, int start, boolean f){
		if(k==start&&f||rev[k].isEmpty())return 0;
		E e = rev[k].get(0);
		return e.c+cycle(e.t, start, true);
	}
	void make(int k){
		for(E e:edge[k]){
			if(visited[e.t])continue;
			res += e.c; visited[e.t] = true; make(e.t);
		}
	}
	
	@SuppressWarnings("unchecked")
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			n = sc.nextInt();
			if(n==0)break;
			edge = new List[n]; rev = new List[n];
			ref = new HashMap<String, Integer>();
			COUNT = 0;
			for(int i=0;i<n;i++){
				edge[i] = new ArrayList<E>();
				rev[i] = new ArrayList<E>();
			}
			int[] cost = new int[n];
			for(int i=0;i<n;i++){
				int x = get(sc.next());
				cost[x] = sc.nextInt();
				int y = get(sc.next()), c = sc.nextInt();
				if(x==y)continue;
				edge[y].add(new E(x, c)); rev[x].add(new E(y, c));
			}
			visited = new boolean[n];
			list = new ArrayList<Integer>();
			for(int i=0;i<n;i++)if(!visited[i])dfs(i);
			int ID = 0;
			scc = new int[n];
			visited = new boolean[n];
			for(int i=list.size()-1;i>=0;i--){
				int v = list.get(i);
				if(visited[v])continue;
				rdfs(v, ID); ID++;
			}
			int[] deg = new int[ID];
			for(int i=0;i<n;i++)for(E e:edge[i]){
				if(scc[i]!=scc[e.t])deg[scc[e.t]]++;
			}
			res = 0;
			visited = new boolean[n];
			for(int i=0;i<n;i++){
				if(deg[scc[i]]>0||visited[i])continue;
				int p = -1;
				if(rev[i].isEmpty()){
					p = i;
				}
				else{
					int c = cycle(i, i, false);
					p = i;
					int min = c-rev[i].get(0).c+cost[i];
					for(int j=0;j<n;j++){
						if(scc[i]!=scc[j])continue;
						int v = c-rev[j].get(0).c+cost[j];
						if(v<min){
							min = v; p = j;
						}
					}
				}
				visited[p] = true; res+=cost[p];
				make(p);
			}
			System.out.println(res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}