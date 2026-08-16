import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

//Reverse a Road
public class Main{

	class E{
		int id, t;
		public E(int id, int t) {
			this.id = id;
			this.t = t;
		}
	}
	
	@SuppressWarnings("unchecked")
	void run(){
		Scanner sc = new Scanner(System.in);
		int INF = 1<<29;
		int[] d = new int[1001];
		int[][] e = new int[10001][2];
		List<E>[] adj = new List[1001];
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			for(int i=1;i<=n;i++)adj[i]=new ArrayList<E>();
			int S = sc.nextInt(), T = sc.nextInt(), m = sc.nextInt();
			for(int i=1;i<=m;i++){
				int s = sc.nextInt(), t = sc.nextInt();
				adj[s].add(new E(i, t));
				e[i][0] = s; e[i][1] = t;
			}
			Arrays.fill(d, INF);
			d[S] = 0;
			Queue<Integer> q = new LinkedList<Integer>();
			q.add(S);
			while(!q.isEmpty()){
				int v = q.poll();
				for(E r:adj[v])if(d[r.t]==INF){
					d[r.t] = d[v]+1; q.add(r.t);
				}
			}
			int res = d[T], ID = 0;
			for(int i=1;i<=m;i++){
				Arrays.fill(d, INF);
				d[S] = 0;
				q = new LinkedList<Integer>();
				q.add(S);
				int rs = e[i][1], rt = e[i][0];
				while(!q.isEmpty()){
					int v = q.poll();
					if(res<=d[v])break;
					for(E r:adj[v])if(r.id!=i&&d[r.t]==INF){
						d[r.t] = d[v]+1; q.add(r.t);
					}
					if(v==rs&&d[rt]==INF){
						d[rt] = d[v]+1; q.add(rt);
					}
				}
				if(d[T]<res){
					res = d[T]; ID = i;
				}
			}
			System.out.println(res+" "+ID);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}