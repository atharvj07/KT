import java.io.BufferedReader;
import java.io.Closeable;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.SortedMap;
import java.util.StringTokenizer;
import java.util.TreeMap;
 
public class Main {
	
	public static boolean[][] mul(final int n, final boolean[][] mat1, final boolean[][] mat2){
		boolean[][] ret = new boolean[n][n];
		
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				for(int k = 0; k < n; k++){
					ret[i][j] |= mat1[i][k] && mat2[k][j];
				}
			}
		}
		
		return ret;
	}
	
	public static boolean[][] pow(final int n, final boolean[][] adj, final int a){
		if(a == 1){
			boolean[][] ret = new boolean[n][n];
			for(int i = 0; i < n; i++){
				for(int j = 0; j < n; j++){
					ret[i][j] = adj[i][j];
				}
			}
			return ret;
		}else if(a % 2 == 0){
			boolean[][] ret = pow(n, adj, a / 2);
			return mul(n, ret, ret);
		}else{
			return mul(n, adj, pow(n, adj, a - 1));
		}
	}
	
	public static int[][] warshallFroyd(final int n, int[][] adj){
		int[][] ret = new int[n][n];
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				ret[i][j] = adj[i][j];
			}
		}
		
		for(int k = 0; k < n; k++){
			for(int i = 0; i < n; i++){
				for(int j = 0; j < n; j++){
					ret[i][j] = Math.min(ret[i][j], Math.min(ret[i][k] + ret[k][j], INF));
				}
			}
		}
		
		return ret;
	}
	
	public static final int INF = Integer.MAX_VALUE / 2 - 1;
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		final int n = sc.nextInt();
		final int m = sc.nextInt();
		
		int[] hops = new int[3];
		for(int i = 0; i < 3; i++){
			hops[i] = sc.nextInt();
		}
		
		boolean[][] adj = new boolean[n][n];
		for(int i = 0; i < m; i++){
			final int u = sc.nextInt() - 1;
			final int v = sc.nextInt() - 1;
			
			adj[u][v] = true;
		}
		
		boolean[][][] hop_adjs = new boolean[3][n][n];
		for(int index = 0; index < 3; index++){
			hop_adjs[index] = pow(n, adj, hops[index]);
			//System.out.println(Arrays.deepToString(hop_adjs[index]));
		}
		
		int[] costs = new int[n];
		Arrays.fill(costs, INF);
		costs[n - 1] = 0;
		
		while(true){
			boolean updated = false;
			
			LOOP:
			for(int from = 0; from < n; from++){
				int max_cost = 0;
				
				for(int type = 0; type < 3; type++){
					boolean found = false;
					int min_cost = INF;
					
					for(int next = 0; next < n; next++){
						if(!hop_adjs[type][from][next]){ continue; }
						if(costs[next] >= INF){ continue; }
						
						min_cost = Math.min(min_cost, costs[next] + 1);
						found = true;
					}
					
					if(!found){ continue LOOP; }
					max_cost = Math.max(max_cost, min_cost);
				}
				
				//System.out.println(max_cost + " " + from);
				if(costs[from] > max_cost){
					costs[from] = max_cost;
					updated = true;
				}
			}
			
			//System.out.println(Arrays.toString(costs));
			if(!updated){
				break;
			}
		}
		
		System.out.println(costs[0] >= INF ? "IMPOSSIBLE" : costs[0]);
	}
}