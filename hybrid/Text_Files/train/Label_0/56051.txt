import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public final class Main {
	
	static boolean flag = false;
	
	static int[] vis;
	static List<List<Integer>> adj;
	
	static void dfs(int vertice, int pai){
		vis[vertice] = 1;
		for (Integer vizinho : adj.get(vertice)) {
			if (vis[vizinho] != 1){
				dfs(vizinho, vertice);
			} else if (pai != vizinho){
				flag = true;
			}
				
		}
	}

	public static void main(String[] args) {
		int N;
	  	int M;
	  	int u;
	  	int v;
	  	int cont = 0;
	  	
	    Scanner scanner = new Scanner(System.in);  
	    N = scanner.nextInt();
	    M = scanner.nextInt();
	    
	    vis = new int[N+1];
	    adj = new ArrayList<List<Integer>>(N+1);
	    for (int i = 0; i < N+1; i++) {
			adj.add(new ArrayList<Integer>());
		}
	    
	    
	    for (int i = 0; i < M; i++) {
			u = scanner.nextInt();
			v = scanner.nextInt();
			adj.get(u).add(v);
			adj.get(v).add(u);
			
		}
	    
	    
	    for (int i = 1; i < N+1; i++) {
			if (vis[i] != 1){
				dfs(i, -1);
				if (flag == false) cont++;
				else flag = false;
			}
				
		}
	    
	    System.out.println(cont);

	}

}
