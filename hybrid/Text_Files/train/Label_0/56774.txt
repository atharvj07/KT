import java.util.Scanner;

public class Main {

	public static int[][] move_dir = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
	
	public static boolean ok(int x, int y, int w, int h){
		if(x < 0 || x >= w || y < 0 || y >= h){
			return false;
		}
		return true;
	}
	
	public static boolean check_dir(int x, int y, int dx, int dy, int w, int h, int n, int[][] board, boolean[][] removable){
		if(!ok(x, y, w, h) || board[y][x] == 0){
			return false;
		}
		int start_color = board[y][x];
		int len = 1;
		
		int sx = x;
		int sy = y;
		while(true){
			sx += dx;
			sy += dy;
			
			if(!ok(sx, sy, w, h)){
				break;
			}else if(board[sy][sx] != start_color){
				break;
			}
			
			len++;
		}
		
		if(len >= n){
			for(int i = 0; i < len; i++){
				removable[y][x] = true;
				x += dx;
				y += dy;
			}
			return true;
		}else{
			return false;
		}
	}
	
	public static void down(int w, int h, int[][] board){
		//System.out.println("--------------down--------------");
		for(int x = 0; x < w; x++){
			boolean updated = false;
			
			for(int y = 0; y < h - 1; y++){
				if(board[y][x] != 0 && board[y+1][x] == 0){
					board[y+1][x] = board[y][x];
					board[y][x] = 0;
					updated = true;
				}
			}
			
			//disp(w, h, board);
			
			if(updated){
				x--;
			}
		}
	}
	
	public static void copy_board(int w, int h, int[][] src, int[][] dest){
		for(int y = 0; y < h; y++){
			for(int x = 0; x < w; x++){
				dest[y][x] = src[y][x];
			}
		}
	}
	
	public static void disp(int w, int h, int[][] board){
		for(int y = 0; y < h; y++){
			for(int x = 0; x < w; x++){
				System.out.printf("%2d ", board[y][x]);
			}
			System.out.println();
		}
		System.out.println("------------------");
	}
	
	public static void disp_r(int w, int h, boolean[][] board){
		for(int y = 0; y < h; y++){
			for(int x = 0; x < w; x++){
				System.out.printf("%2d ", board[y][x] ? 1 : 0);
			}
			System.out.println();
		}
		System.out.println("------------------");
	}
	
	public static int[][] check(int w, int h, int n, int[][] board){
		boolean[][] remove = new boolean[h][w];
		
		down(w, h, board);
		//System.out.println("--------------start--------------");
		while(true){
			boolean updated = false;
			for(int y = 0; y < h; y++){
				for(int x = 0; x < w; x++){
					remove[y][x] = false;
				}
			}
			
			for(int y = 0; y < h; y++){
				for(int x = 0; x < w; x++){
					if(board[y][x] == 0){
						continue;
					}
				
					for(int[] move : move_dir){
						final int dx = move[0];
						final int dy = move[1];
						
						//System.out.println(x + " " + y + " " + dx + " " + dy + " " + updated);
						
						if(check_dir(x, y, dx, dy, w, h, n, board, remove)){
							updated = true;
						}
					}
				}
			}
			//disp(w, h, board);
			//disp_r(w, h, remove);
			if(!updated){
				break;
			}
			
			for(int y = 0; y < h; y++){
				for(int x = 0; x < w; x++){
					if(remove[y][x] && board[y][x] != 0){
						board[y][x] = 0;
					}
				}
			}
			
			down(w, h, board);
		}
		
		return board;
	}
	
	public static boolean all_white(int w, int h, int[][] board){
		for(int y = 0; y < h; y++){
			for(int x = 0; x < w; x++){
				if(board[y][x] != 0){
					return false;
				}
			}
		}
		
		return true;
	}
	
	public static boolean choose(int w, int h, int n, int[][] board){
		int[][] copy = new int[h][w];
		
		for(int y = 0; y < h; y++){
			for(int x = 0; x < w; x++){
				if(y == h - 1 && x == w - 1){
					continue;
				}else if(y == h - 1){
					if(board[y][x] != board[y][x+1]){
						copy_board(w, h, board, copy);
						int tmp = copy[y][x];
						copy[y][x] = copy[y][x+1];
						copy[y][x+1] = tmp;
					
						check(w, h, n, copy);
						if(all_white(w, h, copy)){
							return true;
						}
					}
				}else if(x == w - 1){
					/*
					if(board[y][x] != board[y+1][x] && board[y][x] != 0 && board[y+1][x] != 0){
						copy_board(w, h, board, copy);
						int tmp = copy[y][x];
						copy[y][x] = copy[y+1][x];
						copy[y+1][x] = tmp;
					
						check(w, h, n, copy);
						if(all_white(w, h, copy)){
							return true;
						}
					}
					*/
				}else{
					if((board[y][x] != board[y][x+1])){
						copy_board(w, h, board, copy);
						int tmp = copy[y][x];
						copy[y][x] = copy[y][x+1];
						copy[y][x+1] = tmp;
					
						check(w, h, n, copy);
						if(all_white(w, h, copy)){
							return true;
						}
					}
					/*
					if(board[y][x] != board[y+1][x] && board[y][x] != 0 && board[y+1][x] != 0){
						copy_board(w, h, board, copy);
						int tmp = copy[y][x];
						copy[y][x] = copy[y+1][x];
						copy[y+1][x] = tmp;
					
						check(w, h, n, copy);
						if(all_white(w, h, copy)){
							return true;
						}
					}
					*/
				}
			}
		}
		
		return false;
	}
	
	public static void main(String[] args) {
		final Scanner sc = new Scanner(System.in);

		final int h = sc.nextInt();
		final int w = sc.nextInt();
		final int n = sc.nextInt();
		
		int[][] map = new int[h][w];
		for(int i = 0; i < h; i++){
			char[] input = sc.next().toCharArray();
			
			for(int j = 0; j < w; j++){
				if(input[j] == '.'){
					map[i][j] = 0;
				}else{
					map[i][j] = input[j] - 'A' + 1;
				}
			}
		}
		
		System.out.println(choose(w, h, n, map) ? "YES" : "NO");
		
	}

}