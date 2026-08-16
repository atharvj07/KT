import java.awt.Point;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
	
	public static final int MAX_N = 1000;
	public static final int MAX_SIZE = MAX_N * 2;
	
	public static final int[][] move_dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
	
	public static boolean is_ok(int x, int y, int w, int h){
		if(x < 0 || x >= w || y < 0 || y >= h){
			return false;
		}else{
			return true;
		}
	}
	
	public static void bfs(int x, int y, final int w, final int h, short[][] masked, boolean[][] visited){
		LinkedList<Integer> x_queue = new LinkedList<Integer>();
		LinkedList<Integer> y_queue = new LinkedList<Integer>();
		
		visited[y][x] = true;
		x_queue.add(x);
		y_queue.add(y);
		
		while(!x_queue.isEmpty()){
			final int c_x = x_queue.poll();
			final int c_y = y_queue.poll();
			
			for(int[] move : move_dir){
				final int nx = c_x + move[0];
				final int ny = c_y + move[1];
			
				if(!is_ok(nx, ny, w, h)){
					continue;
				}else if(masked[ny][nx] > 0){
					continue;
				}else if(visited[ny][nx]){
					continue;
				}
			
				visited[ny][nx] = true;
				x_queue.add(nx);
				y_queue.add(ny);
				//bfs(nx, ny, w, h, masked, visited);
			}
		}
	}
	
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		short[][] masked = new short[MAX_SIZE + 1][MAX_SIZE + 1];
		boolean[][] visited = new boolean[MAX_SIZE + 1][MAX_SIZE + 1];
		
		TreeSet<Integer> x_set = new TreeSet<Integer>();
		TreeSet<Integer> y_set = new TreeSet<Integer>();
		ArrayList<Integer> x_list = new ArrayList<Integer>();
		ArrayList<Integer> y_list = new ArrayList<Integer>();
		
		int[][] data = new int[MAX_N][4];
		
		while (true) {
			final int w = sc.nextInt();
			final int h = sc.nextInt();
			
			if(w == 0 && h == 0){
				break;
			}
			
			final int n = sc.nextInt();
			
			x_set.clear();
			y_set.clear();
			x_list.clear();
			y_list.clear();
			
			x_set.add(0);
			x_set.add(w - 1);
			y_set.add(0);
			y_set.add(h - 1);
			
			for(int i = 0; i < n; i++){
				final int x1 = sc.nextInt();
				final int y1 = sc.nextInt();
				final int x2 = sc.nextInt() - 1;
				final int y2 = sc.nextInt() - 1;
				
				data[i][0] = x1;
				data[i][1] = y1;
				data[i][2] = x2;
				data[i][3] = y2;
				
				if(x1 > 0){
					x_set.add(x1 - 1);
				}
				x_set.add(x1);
				x_set.add(x2);
				if(x2 < w - 1){
					x_set.add(x2 + 1);
				}
				
				if(y1 > 0){
					y_set.add(y1 - 1);
				}
				y_set.add(y1);
				y_set.add(y2);
				if(y2 < h - 1){
					y_set.add(y2 + 1);
				}
			}
			
			x_list.addAll(x_set);
			y_list.addAll(y_set);
			
			final int w_c = x_list.size();
			final int h_c = y_list.size();
			
			for(int i = 0; i <= h_c; i++){
				for(int j = 0; j <= w_c; j++){
					masked[i][j] = 0;
				}
			}
			
			for(int i = 0; i < n; i++){
				final int x1 = Collections.binarySearch(x_list, data[i][0]);
				final int y1 = Collections.binarySearch(y_list, data[i][1]);
				final int x2 = Collections.binarySearch(x_list, data[i][2]);
				final int y2 = Collections.binarySearch(y_list, data[i][3]);
				
				//System.out.println(x1 + " " + y1 + " , " + x2 + " " + y2);
				
				masked[y1][x1]++;
				masked[y1][x2 + 1]--;
				masked[y2 + 1][x1]--;
				masked[y2 + 1][x2 + 1]++;
			}
			
			/*
			{
				//int x_zero_pos = Collections.binarySearch(x_list, 0);
				//int x_max_pos  = Collections.binarySearch(x_list, w - 1);
				int y_zero_pos = Collections.binarySearch(y_list, 0);
				int y_max_pos  = Collections.binarySearch(y_list, h - 1);
				
				if(y_zero_pos < 0){
					y_zero_pos = -(y_zero_pos - 2);
				}else{
					y_zero_pos--;
				}
				
				if(y_max_pos < 0){
					y_max_pos  = -(y_max_pos  - 1);
				}else{
					y_max_pos++;
				}
				
				//System.out.println(x_zero_pos + " " + 0);
				//System.out.println(x_max_pos + " " + w_c);
				
				//System.out.println(y_zero_pos + " " + 0);
				//System.out.println(y_max_pos + " " + h_c);
				
				if(y_zero_pos >= 0){
					masked[0][0]++;
					masked[y_zero_pos + 1][0]--;
					masked[0][w_c + 1]--;
					masked[y_zero_pos + 1][w_c + 1]++;
				}
				
				if(y_max_pos < h_c){
					masked[y_max_pos][0]++;
					masked[h_c + 1][0]--;
					masked[y_max_pos][w_c + 1]--;
					masked[h_c + 1][w_c + 1]++;
				}
				
			}
			*/
			
			/*
			System.out.println(x_list);
			for(int i = h_c - 1; i >= 0; i--){
				for(int j = 0; j < w_c; j++){
					System.out.print(masked[i][j] + " ");
				}
				System.out.println();
			}
			System.out.println(y_list);
			*/
			
			for(int i = 0; i < h_c; i++){
				for(int j = 1; j < w_c; j++){
					masked[i][j] += masked[i][j-1];
				}
			}
			
			for(int j = 0; j < w_c; j++){
				for(int i = 1; i < h_c; i++){
					masked[i][j] += masked[i-1][j];
				}
			}
			
			/*
			for(int i = 0; i < w_c; i++){
				
				
				masked[h_c - 1][i] = 1;
				masked[0][i] = 1;
			}
			
			for(int i = 0; i < h_c; i++){
				masked[i][w_c-1] = 1;
				masked[i][0] = 1;
			}
			*/
			
			/*
			System.out.println(x_list);
			for(int i = h_c - 1; i >= 0; i--){
				for(int j = 0; j < w_c; j++){
					System.out.print(masked[i][j] + " ");
				}
				System.out.println();
			}
			System.out.println(y_list);
			*/
			
			for(int i = 0; i < h_c; i++){
				for(int j = 0; j < w_c; j++){
					visited[i][j] = false;
				}
			}
			
			int count = 0;
			for(int i = 0; i < h_c; i++){
				for(int j = 0; j < w_c; j++){
					if(masked[i][j] > 0){
						continue;
					}else if(visited[i][j]){
						continue;
					}
					
					bfs(j, i, w_c, h_c, masked, visited);
					count++;
				}
			}
			
			System.out.println(count);
		}
	}
}