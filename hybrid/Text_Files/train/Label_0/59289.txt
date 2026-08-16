import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.TreeMap;
 
 
public class Main{
	
	public static class Walk implements Comparable<Walk> {
		int pos;
		int money;
		int danger;
		
		public Walk(int pos, int money, int danger) {
			super();
			this.pos = pos;
			this.money = money;
			this.danger = danger;
		}

		@Override
		public int compareTo(Walk arg0) {
			return this.danger == arg0.danger ? arg0.money - this.money : this.danger - arg0.danger;
		}
		
	}
	
    public static void main(String[] args) throws IOException {
    	Scanner sc = new Scanner(System.in);
    	
    	while(true){
    		final int N = sc.nextInt();
    		final int M = sc.nextInt();
    		final int L = sc.nextInt();
    		
    		if(N == 0 && M == 0 && L == 0){
    			break;
    		}
    		
    		int[][] adj = new int[N][N];
    		int[][] warn = new int[N][N];
    		
    		for(int i = 0; i < N; i++){
    			for(int j = 0; j < N; j++){
    				adj[i][j] = -1;
    				warn[i][j] = -1;
    			}
    		}
    		
    		for(int i = 0; i < M; i++){
    			final int A = sc.nextInt() - 1;
    			final int B = sc.nextInt() - 1;
    			final int D = sc.nextInt();
    			final int E = sc.nextInt();
    			
    			adj[A][B] = adj[B][A] = D;
    			warn[A][B] = warn[B][A] = E;
    		}
    		
    		boolean[][] is_visited = new boolean[N][L + 1];
    		
    		PriorityQueue<Walk> queue = new PriorityQueue<Walk>();
    		queue.add(new Walk(0, L, 0));
    		
    		while(!queue.isEmpty()){
    			Walk walk = queue.poll();
    			
    			if(is_visited[walk.pos][walk.money]){
    				continue;
    			}else{
    				is_visited[walk.pos][walk.money] = true;
    			}
    			
    			if(walk.pos == N - 1){
    				System.out.println(walk.danger);
    				break;
    			}
    			
    			for(int to = 0; to < N; to++){
    				if(adj[walk.pos][to] < 0){
    					continue;
    				}
    				
    				if(walk.money >= adj[walk.pos][to]){
    					final int new_money = walk.money - adj[walk.pos][to];
    					final int new_pos   = to;
    					
    					if(!is_visited[new_pos][new_money]){
    						queue.add(new Walk(new_pos, new_money, walk.danger));
    					}
    				}
    				
    				if(!is_visited[to][walk.money]){
    					queue.add(new Walk(to, walk.money, walk.danger + warn[walk.pos][to]));
    				}
    			}
    		}
    		
    	}
    	
    	
    	
    }
     
}