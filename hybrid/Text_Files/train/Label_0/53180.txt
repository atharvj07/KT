import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

	public static final int MAX = 7;

	public static boolean is_ok(int x, int y, int w, int h){
		if(x < 0 || x >= w || y < 0 || y >= h){
			return false;
		}else{
			return true;
		}
	}
	
	public static final int[][] move_dir = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
	
	public static void main(String[] args) {
		final Scanner sc = new Scanner(System.in);

		boolean[][] can_enter = new boolean[MAX][MAX];
		boolean[][][][] is_visited = new boolean[MAX][MAX][MAX][MAX];
		
		while (true) {
			final int w = sc.nextInt();
			final int h = sc.nextInt();
			
			if(w == 0 && h == 0){
				break;
			}
			
			int s_x = -1, s_y = -1, g_x = -1, g_y = -1;
			int c_s_x = -1, c_s_y = -1;
			
			for(int i = 0; i < h; i++){
				for(int j = 0; j < w; j++){
					final int in = sc.nextInt();
					
					can_enter[i][j] = in != 1;
					
					if(in == 2){
						c_s_x = j;
						c_s_y = i;
					}
					
					if(in == 3){
						g_x = j;
						g_y = i;
					}
					
					if(in == 4){
						s_x = j;
						s_y = i;
					}
				}
			}
			
			for(int i = 0; i < h; i++){
				for(int j = 0; j < w; j++){
					for(int k = 0; k < h; k++){
						for(int l = 0; l < w; l++){
							is_visited[i][j][k][l] = false;
						}
					}
				}
			}
			
			LinkedList<Integer> p_x_queue = new LinkedList<Integer>();
			LinkedList<Integer> p_y_queue = new LinkedList<Integer>();
			LinkedList<Integer> c_x_queue = new LinkedList<Integer>();
			LinkedList<Integer> c_y_queue = new LinkedList<Integer>();
			LinkedList<Integer> time_queue = new LinkedList<Integer>();
			
			p_x_queue.add(s_x);
			p_y_queue.add(s_y);
			c_x_queue.add(c_s_x);
			c_y_queue.add(c_s_y);
			time_queue.add(0);
			
			is_visited[s_y][s_x][c_s_y][c_s_x] = true;
			
			boolean flag = false;
			while(!time_queue.isEmpty()){
				final int p_x  = p_x_queue.poll();
				final int p_y  = p_y_queue.poll();
				final int c_x  = c_x_queue.poll();
				final int c_y  = c_y_queue.poll();
				final int time = time_queue.poll();
				
				//System.out.println(p_x + " " + p_y + " " + c_x + " " + c_y + " " + time);
				
				if(c_x == g_x && c_y == g_y){
					flag = true;
					System.out.println(time);
					break;
				}
				
				for(int[] move : move_dir){
					final int n_p_x = p_x + move[0];
					final int n_p_y = p_y + move[1];
					final int n_c_x = c_x + ((c_x == n_p_x && c_y == n_p_y) ? move[0] : 0);
					final int n_c_y = c_y + ((c_x == n_p_x && c_y == n_p_y) ? move[1] : 0);
					
					boolean moved = n_c_x != c_x || n_c_y != c_y;
					
					if(!is_ok(n_p_x, n_p_y, w, h) || !is_ok(n_c_x, n_c_y, w, h)){
						continue;
					}else if(!can_enter[n_p_y][n_p_x] || !can_enter[n_c_y][n_c_x]){
						continue;
					}else if(is_visited[n_p_y][n_p_x][n_c_y][n_c_x]){
						continue;
					}
					
					is_visited[n_p_y][n_p_x][n_c_y][n_c_x] = true;
					if(moved){
						p_x_queue.add(n_p_x);
						p_y_queue.add(n_p_y);
						c_x_queue.add(n_c_x);
						c_y_queue.add(n_c_y);
						time_queue.add(time + 1);
					}else{
						p_x_queue.addFirst(n_p_x);
						p_y_queue.addFirst(n_p_y);
						c_x_queue.addFirst(n_c_x);
						c_y_queue.addFirst(n_c_y);
						time_queue.addFirst(time);
					}
				}
			}
			
			if(!flag){
				System.out.println(-1);
			}
		}
	}

}