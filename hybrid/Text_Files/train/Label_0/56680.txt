import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	public static class Walk implements Comparable<Walk> {
		int cost;
		int pos;
		int pass;
		
		public Walk(int cost, int pos, int pass) {
			super();
			this.cost = cost;
			this.pos = pos;
			this.pass = pass;
		}

		@Override
		public int compareTo(Walk o) {
			// TODO Auto-generated method stub
			return this.cost - o.cost;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			final int c = sc.nextInt();
			final int n = sc.nextInt();
			final int m = sc.nextInt();
			final int s = sc.nextInt() - 1;
			final int d = sc.nextInt() - 1;
			
			if(c == 0 && n == 0 && m == 0 && s == -1 && d == -1){
				break;
			}
			
			int[][] adj = new int[n][n];
			for(int i = 0; i < n; i++){
				for(int j = 0; j < n; j++){
					adj[i][j] = -1;
				}
			}
			for(int i = 0; i < m; i++){
				final int from = sc.nextInt() - 1;
				final int to = sc.nextInt() - 1;
				final int cost = sc.nextInt();
				
				adj[from][to] = adj[to][from] = cost;
			}
			
			PriorityQueue<Walk> queue = new PriorityQueue<Walk>();
			queue.add(new Walk(0,s,c));
			
			boolean[][] visited = new boolean[n][c+1];
			
			while(!queue.isEmpty()){
				Walk walk = queue.poll();
				
				//System.out.println(walk.cost + " " + walk.pos + " " + walk.pass);
				if(walk.pos == d){
					System.out.println(walk.cost);
					break;
				}
				
				if(visited[walk.pos][walk.pass]){
					continue;
				}
				visited[walk.pos][walk.pass] = true;
				
				for(int to = 0; to < n; to++){
					if(adj[walk.pos][to] != -1){
						if(walk.pass > 0 && !visited[to][walk.pass - 1]){
							queue.add(new Walk(walk.cost + adj[walk.pos][to]/2, to, walk.pass - 1));
						}
						
						if(!visited[to][walk.pass]){
							queue.add(new Walk(walk.cost + adj[walk.pos][to], to, walk.pass));
						}
					}
				}
			}
		}
	}
}