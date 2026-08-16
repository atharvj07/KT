import java.util.*;

public class Main {
	static class Tree {
		public class Edge {
			int to, rev, cost;

			public Edge(int to, int rev, int cost) {
				this.to = to;
				this.rev = rev;
				this.cost = cost;
			}
		}
		
		int V;
		ArrayList<ArrayList<Edge>> G;
		int root;
		int[] p;
		
		public Tree(int[] a, int[] b, int[] cost) {
			this.V = a.length+1;
			p = new int[V];
			
			G = new ArrayList<ArrayList<Edge>>();
			for(int i=0; i<V; i++) {
				G.add(new ArrayList<Edge>());
			}
			
			for(int i=0; i<V-1; i++) {
				G.get(a[i]).add(new Edge(b[i], G.get(b[i]).size(), cost[i]));
				G.get(b[i]).add(new Edge(a[i], G.get(a[i]).size()-1, cost[i]));
			}
			setRoot(0);
		}
		
		public void setRoot(int root) {
			this.root = root;
			
			LinkedList<Integer> q1 = new LinkedList<Integer>();
			LinkedList<Integer> q2 = new LinkedList<Integer>();
			q1.add(root);
			q2.add(-1);
			while(q1.size()>0) {
				int cur = q1.poll();
				int parent = q2.poll();
				p[cur]=-1;
				for(int i=0; i<G.get(cur).size(); i++) {
					if(G.get(cur).get(i).to==parent) {
						p[cur] = i;
					} else {
						q1.add(G.get(cur).get(i).to);
						q2.add(cur);
					}
				}
			}
		}
		
		public int getMaxWin(int idx) {
			ArrayList<Integer> childWin = new ArrayList<>();
			for(int i=0; i<G.get(idx).size(); i++) {
				if(i != p[idx]) {
					childWin.add(getMaxWin(G.get(idx).get(i).to));
				}
			}
			Collections.sort(childWin);
			int max = childWin.size();
			for(int i=0; i<childWin.size(); i++)
				max = Math.max(max, childWin.get(i)+childWin.size()-i);
			
			return max;
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] a = new int[N-1];
		int[] b = new int[N-1];
		int[] c = new int[N-1];
		for(int i=0; i<N-1; i++) {
			a[i] = sc.nextInt()-1;
			b[i] = i+1;
		}
		
		Tree tree = new Tree(a, b, c);
		
		System.out.println(tree.getMaxWin(0));
		
		sc.close();
	}
}
