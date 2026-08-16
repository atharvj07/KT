import java.util.Arrays;
import java.util.Scanner;


public class Main {
	final int INF = 1<<28;
	
	int solve(final int s, final int e, final int[][] map, final int n){
		boolean[] used = new boolean[n];
		int d[] = new int[n];
		Arrays.fill(d, INF);
		
		d[s] = 0;
		while(true){
			int u=-1;
			for(int v=0; v<n; ++v){
				if(!used[v] && (u==-1 || d[v] < d[u])){
					u=v;
				}
			}
			if(u==-1)break;
			used[u] = true;
			for(int v=0; v<n; ++v){
				if(d[v] > d[u] + map[u][v]){
					d[v] = d[u] + map[u][v];
				}
			}
		}
		
		return d[e];
	}
	
	void io(){
		Scanner sc = new Scanner(System.in);
		while(true){
			final int n = sc.nextInt();  final int m = sc.nextInt();
			if(n==0 && m==0)break;
			
			int[][] map_cost = new int[m][m];
			int[][] map_time = new int[m][m];
			
			for(int i=0; i<m; ++i){
				for(int j=0; j<m; ++j){
					map_cost[i][j] = map_time[i][j] = i==j ? 0 : INF;
				}
			}
			
			for(int i=0; i<n; ++i){
				final int a = sc.nextInt() -1;
				final int b = sc.nextInt() -1;
				final int cost = sc.nextInt();
				final int time = sc.nextInt();
				
				map_cost[a][b] = map_cost[b][a] = cost;
				map_time[a][b] = map_time[b][a] = time;
			}
			
			final int k = sc.nextInt();
			for(int i=0; i<k; ++i){
				final int p = sc.nextInt()-1; final int q = sc.nextInt()-1;
				final int r = sc.nextInt();
				
				System.out.println(solve(p, q, r==0 ? map_cost : map_time, m));
			}
		}
	}
	
	public static void main(String[] args) {
		new Main().io();
	}

}