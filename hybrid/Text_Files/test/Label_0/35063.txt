import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	public static class Walk implements Comparable<Walk> {
		int s_x_pos;
		int s_y_pos;
		int g_x_pos;
		int g_y_pos;
		int time;
		
		public Walk(int s_x_pos, int s_y_pos, int g_x_pos, int g_y_pos, int time) {
			super();
			this.s_x_pos = s_x_pos;
			this.s_y_pos = s_y_pos;
			this.g_x_pos = g_x_pos;
			this.g_y_pos = g_y_pos;
			this.time = time;
		}

		@Override
		public int compareTo(Walk arg0) {
			return this.time - arg0.time;
		}
	}
	
	public static int[][] move_dir = new int[][]{{1,0}, {-1,0}, {0, 1}, {0, -1}, {0, 0}};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		boolean[][][][][] is_visited = new boolean[20][20][20][20][10];
		boolean[][] is_wall = new boolean[20][20];
		
		while(true){
			final int h = sc.nextInt();
			final int w = sc.nextInt();
			
			if(h == 0 && w == 0){
				break;
			}
			
			for(int i = 0; i < h; i++){
				for(int j = 0; j < w; j++){
					for(int k = 0; k < h; k++){
						for(int l = 0; l < w; l++){
							Arrays.fill(is_visited[i][j][k][l], false);
						}
					}
					
					is_wall[i][j] = false;
				}
			}
			
			int s_x = -1, s_y = -1, g_x = -1, g_y = -1;
			
			for(int i = 0; i < h; i++){
				char[] input = sc.next().toCharArray();
				
				for(int j = 0; j < w; j++){
					if(input[j] == 'A'){
						s_x = j;
						s_y = i;
					}else if(input[j] == 'B'){
						g_x = j;
						g_y = i;
					}
					
					if(input[j] == '#'){
						is_wall[i][j] = true;
					}else{
						is_wall[i][j] = false;
					}
				}
			}
			
			char[] pattern = sc.next().toCharArray();
			
			PriorityQueue<Walk> queue = new PriorityQueue<Main.Walk>();
			queue.add(new Walk(s_x, s_y, g_x, g_y, 0));
			
			boolean flag = false;
			while(!queue.isEmpty()){
				Walk walk = queue.poll();
				
				final int pat_time = walk.time % pattern.length;
				
				if(is_visited[walk.s_y_pos][walk.s_x_pos][walk.g_y_pos][walk.g_x_pos][pat_time]){
					continue;
				}else{
					is_visited[walk.s_y_pos][walk.s_x_pos][walk.g_y_pos][walk.g_x_pos][pat_time] = true;
				}
				
				if(walk.s_x_pos == walk.g_x_pos && walk.s_y_pos == walk.g_y_pos){
					flag = true;
					System.out.println(walk.time + " " + walk.s_y_pos + " " + walk.s_x_pos);
					break;
				}
				
				int n_g_x = walk.g_x_pos;
				int n_g_y = walk.g_y_pos;
				if(pattern[pat_time] == '8'){
					n_g_y--;
				}else if(pattern[pat_time] == '6'){
					n_g_x++;
				}else if(pattern[pat_time] == '4'){
					n_g_x--;
				}else if(pattern[pat_time] == '2'){
					n_g_y++;
				}
				
				if(n_g_y < 0 || n_g_y >= h){
					n_g_y = walk.g_y_pos;
				}
				if(n_g_x < 0 || n_g_x >= w){
					n_g_x = walk.g_x_pos;
				}
				
				final int next_pat_time = (pat_time + 1) % pattern.length;
				
				for(int[] move : move_dir){
					final int nx = walk.s_x_pos + move[0];
					final int ny = walk.s_y_pos + move[1];
					
					if(0 > ny || ny >= h ||0 > nx || nx >= w){
						continue;
					}else if(is_wall[ny][nx]){
						continue;
					}else if(is_visited[ny][nx][n_g_x][n_g_y][next_pat_time]){
						continue;
					}
					
					queue.add(new Walk(nx, ny, n_g_x, n_g_y, walk.time + 1));
				}
			}
			
			if(!flag){
				System.out.println("impossible");
			}
			
		}
	}

}