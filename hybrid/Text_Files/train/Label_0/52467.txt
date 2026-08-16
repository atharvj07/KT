import java.util.*;

public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		while(true){
			int n = sc.nextInt();
			int m = sc.nextInt();
			if(n == 0 && m == 0) break;

			ArrayList<ArrayList<Edge>> map = new ArrayList<ArrayList<Edge>>();
			for(int i=0;i<n;i++){
				map.add(new ArrayList<Edge>());
			}

			for(int i=0;i<m;i++){
				int a = sc.nextInt();
				int b = sc.nextInt();
				int cost = sc.nextInt();

				map.get(a).add(new Edge(a,b,cost));
				map.get(b).add(new Edge(b,a,cost));
			}

			System.out.println(kruskal(map));
		}
	}

	static int kruskal(ArrayList<ArrayList<Edge>> g){
		int n = g.size();
		UnionFind uf = new UnionFind(n);
		PriorityQueue<Edge> open = new PriorityQueue<Edge>();
		for(int i=0;i<n;i++){
			for(Edge e : g.get(i)) if(i < e.to) open.add(e);
		}

		int cost = 0;
		HashSet<Edge> closed = new HashSet<Edge>();
		while(closed.size() < n - 1 && !open.isEmpty()){
			Edge e = open.poll();
			if(uf.unionSet(e.from,e.to)){
				closed.add(e);
				cost += e.cost;
			}
		}
		return cost;
	}
}

class UnionFind{
	int[] data;

	UnionFind(int n){
		data = new int[n];
		Arrays.fill(data,-1);
	}

	boolean unionSet(int x,int y){
		x = root(x);
		y = root(y);
		if(x != y){
			if(data[y] < data[x]){
				x ^= y;
				y ^= x;
				x ^= y;
			}
			data[x] += data[y];
			data[y] = x;
		}
		return x!=y;
	}

	boolean findSet(int x,int y){
		return root(x) == root(y);
	}

	int root(int x){
		return data[x] < 0 ? x : (data[x] = root(data[x]));
	}

	int size(int x){
		return -data[root(x)];
	}
}

class Edge implements Comparable<Edge>{
	int from,to,cost;

	Edge(int from,int to,int cost){
		this.from = from;
		this.to = to;
		this.cost = cost;
	}

	public int compareTo(Edge e){
		return this.cost - e.cost;
	}
}