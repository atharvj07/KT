import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

//Quest of Merchant
public class Main{

	int N, M, W, T, INF = 1<<23;
	
	int[] w, p, x, y;
	int[][] item, adj;
	
	int[][] dist;
	int[] bestTime;
	int[][] sell;
	int[] bestSell;
	
	void run(){
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt(); M = sc.nextInt(); W = sc.nextInt(); T = sc.nextInt();
		Map<String, Integer> ref = new HashMap<String, Integer>();
		w = new int[M];
		p = new int[M];
		for(int i=0;i<M;i++){
			ref.put(sc.next(), i);
			w[i] = sc.nextInt();
			p[i] = sc.nextInt();
		}
		x = new int[N+1];
		y = new int[N+1];
		item = new int[N+1][M];
		for(int i=0;i<N;i++){
			Arrays.fill(item[i], INF);
			int L = sc.nextInt();
			x[i] = sc.nextInt(); y[i] = sc.nextInt();
			while(L--!=0){
				int id = ref.get(sc.next());
				item[i][id] = sc.nextInt();
			}
		}
		adj = new int[N+1][N+1];
		for(int i=0;i<=N;i++)for(int j=i+1;j<=N;j++)adj[i][j] = adj[j][i] = Math.abs(x[i]-x[j])+Math.abs(y[i]-y[j]);
		dist = new int[1<<N][N];
		for(int S=1;S<1<<N;S++)for(int last=0;last<N;last++)if(((S>>last)&1)>0){
			int ns = S-(1<<last);
			if(ns==0)dist[S][last] = adj[last][N];
			else{
				int min = INF;
				for(int j=0;j<N;j++)if(((ns>>j)&1)>0)min = Math.min(min, dist[ns][j]+adj[j][last]);
				dist[S][last] = min;
			}
		}
		bestTime = new int[1<<N];
		for(int S=1;S<1<<N;S++){
			int min = INF;
			for(int i=0;i<N;i++)if(((S>>i)&1)>0)min = Math.min(min, dist[S][i]+adj[i][N]);
			bestTime[S] = min;
		}
		bestSell = new int[1<<N];
		int[] c = new int[M];
		int[] ws = new int[W+1];
		for(int V=1;V<1<<N;V++){
			Arrays.fill(c, INF);
			Arrays.fill(ws, 0);
			for(int i=0;i<N;i++)if(((V>>i)&1)>0)for(int j=0;j<M;j++)c[j]=Math.min(c[j], item[i][j]);
			for(int j=0;j<M;j++)c[j] = Math.max(0, p[j]-c[j]);
			for(int k=1;k<=W;k++)for(int j=0;j<M;j++)if(w[j]<=k)ws[k] = Math.max(ws[k], ws[k-w[j]]+c[j]);
			bestSell[V] = ws[W];
		}
		long[] dp = new long[T+1];
		for(int t=1;t<=T;t++){
			dp[t] = dp[t-1];
			for(int V=1;V<1<<N;V++){
				if(bestTime[V]<=t)dp[t] = Math.max(dp[t], dp[t-bestTime[V]] + bestSell[V]);
			}
		}
		System.out.println(dp[T]);
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}