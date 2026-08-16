import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	public static final int[][] move_dir = new int[][]{{1,0}, {-1,0}, {0, 1}, {0, -1}};
	
	public static boolean is_ok(int x, int y, int W, int H){
		if(x < 0 || y < 0 || x >= W || y >= H){
			return false;
		}else{
			return true;
		}
	}
	
	public static class Walk implements Comparable<Walk>{
		int x;
		int y;
		int cost;
		
		public Walk(int x, int y, int cost) {
			super();
			this.x = x;
			this.y = y;
			this.cost = cost;
		}

		@Override
		public int compareTo(Walk o) {
			return this.cost - o.cost;
		}
	}
	
	public static void Dijstra(int[][] cost, int[][] dist, int s_x, int s_y, final int W, final int H){
		PriorityQueue<Walk> queue = new PriorityQueue<Main.Walk>();
		queue.add(new Walk(s_x, s_y, 0));
		
		while(!queue.isEmpty()){
			final Walk walk = queue.poll();
			
			if(cost[walk.y][walk.x] != Integer.MAX_VALUE){
				continue;
			}else{
				cost[walk.y][walk.x] = walk.cost;
			}
			
			for(int[] move : move_dir){
				final int nx = walk.x + move[0];
				final int ny = walk.y + move[1];
				
				if(!is_ok(nx, ny, W, H)){
					continue;
				}else if(dist[ny][nx] == 0){
					continue;
				}else if(cost[ny][nx] != Integer.MAX_VALUE){
					continue;
				}
				
				final int add_cost = dist[walk.y][walk.x] == 1 ? 3 :
									 dist[walk.y][walk.x] == 2 ? 2 : 1;
				
				queue.add(new Walk(nx, ny, walk.cost + add_cost));
			}
		}
	}
	
	public static int dfs(int deep, boolean[] visited, int[][] adj, int cur_pos, int makimono_count){
		if(deep == makimono_count){
			return adj[cur_pos][makimono_count + 1];
		}else{
			int min = Integer.MAX_VALUE;
			
			visited[cur_pos] = true;
			
			for(int next = 0; next <= makimono_count; next++){
				if(visited[next]){
					continue;
				}
				
				min = Math.min(min, adj[cur_pos][next] + dfs(deep + 1, visited, adj, next, makimono_count));
			}
			
			visited[cur_pos] = false;
			
			return min;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		final int W = sc.nextInt();
		final int H = sc.nextInt();
		
		int[][] blank_dist = new int[H][W];
		for(int i = 0; i < H; i++){
			for(int j = 0; j < W; j++){
				blank_dist[i][j] = Integer.MAX_VALUE / 2;
			}
		}
		
		int makimono_count = 0;
		int[] makimono_x = new int[5];
		int[] makimono_y = new int[5];
		
		int s_x = -1, s_y = -1;
		int g_x = -1, g_y = -1;
		for(int i = 0; i < H; i++){
			char[] input = sc.next().toCharArray();
			
			for(int j = 0; j < W; j++){
				if(input[j] == '#'){
					blank_dist[i][j] = 0;
				}else if(input[j] == 'S'){
					s_x = j;
					s_y = i;
				}else if(input[j] == 'G'){
					g_x = j;
					g_y = i;
				}else if(input[j] == 'M'){
					makimono_x[makimono_count] = j;
					makimono_y[makimono_count] = i;
					makimono_count++;
				}
			}
		}
		int[] pur_x = new int[makimono_count + 2];
		int[] pur_y = new int[makimono_count + 2];
		pur_x[0] = s_x; pur_y[0] = s_y;
		for(int i = 1; i <= makimono_count; i++){
			pur_x[i] = makimono_x[i - 1];
			pur_y[i] = makimono_y[i - 1];
		}
		pur_x[makimono_count + 1] = g_x;
		pur_y[makimono_count + 1] = g_y;
		
		
		for(int y = 0; y < H; y++){
			for(int x = 0; x < W; x++){
				if(y != 0){
					blank_dist[y][x] = Math.min(blank_dist[y][x], blank_dist[y-1][x] + 1);
				}
				
				if(x != 0){
					blank_dist[y][x] = Math.min(blank_dist[y][x], blank_dist[y][x-1] + 1);
				}
				
				if(x != 0 && y != 0){
					blank_dist[y][x] = Math.min(blank_dist[y][x], blank_dist[y-1][x-1] + 1);
				}
				
				if(x != W - 1 && y != 0){
					blank_dist[y][x] = Math.min(blank_dist[y][x], blank_dist[y-1][x+1] + 1);
				}
			}
		}
		for(int y = H - 1; y >= 0; y--){
			for(int x = W - 1; x >= 0; x--){
				if(y != H - 1){
					blank_dist[y][x] = Math.min(blank_dist[y][x], blank_dist[y+1][x] + 1);
				}
				
				if(x != W - 1){
					blank_dist[y][x] = Math.min(blank_dist[y][x], blank_dist[y][x+1] + 1);
				}
				
				if(y != H - 1 && x != W - 1){
					blank_dist[y][x] = Math.min(blank_dist[y][x], blank_dist[y+1][x+1] + 1);
				}
				
				if(y != H - 1 && x != 0){
					blank_dist[y][x] = Math.min(blank_dist[y][x], blank_dist[y+1][x-1] + 1);
				}
			}
		}
		
		/*
		for(int i = 0; i < H; i++){
			for(int j = 0; j < W; j++){
				System.out.print(blank_dist[i][j]);
			}
			System.out.println();
		}
		*/
		
		int[][] adj = new int[makimono_count + 2][makimono_count + 2];
		int[][] map = new int[H][W];
		for(int i = 0; i < makimono_count + 2; i++){
			for(int j = 0; j < H; j++){
				for(int k = 0; k < W; k++){
					map[j][k] = Integer.MAX_VALUE;
				}
			}
			
			Dijstra(map, blank_dist, pur_x[i], pur_y[i], W, H);
			
			for(int j = 0; j < makimono_count + 2; j++){
				adj[i][j] = map[pur_y[j]][pur_x[j]];
			}
		}
		
		/*
		for(int i = 0; i < makimono_count + 2; i++){
			for(int j = 0; j < makimono_count + 2; j++){
				System.out.printf("%02d ", adj[i][j]);
			}
			System.out.println();
		}
		*/
		
		boolean[] visited = new boolean[makimono_count + 2];
		
		System.out.println(dfs(0, visited, adj, 0, makimono_count));
		
	}
}