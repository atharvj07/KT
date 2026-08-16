import java.util.*;

public class Main {

	int[] dy = {0,0,1,-1,0};
	int[] dx = {1,-1,0,0,0};

	void run(){
		Scanner in = new Scanner(System.in);
		for(int n=in.nextInt(); n-- > 0; ){
			boolean[][] board = new boolean[10][10];
			for(int i=0; i<10; i++){
				for(int j=0; j<10; j++){
					int x = in.nextInt();
					board[i][j] = x == 1;
				}
			}
			boolean[][] ans = solve(board);
			for(int i=0; i<10; i++){
				for(int j=0; j<10; j++){
					System.out.printf("%d%c",ans[i][j]?1:0, j==9?'\n':' ');
				}
			}
		}
	}

	boolean[][] check(boolean[][] board, int bit){
		boolean[][] tmp = new boolean[10][];
		boolean[][] ans = new boolean[10][10];
		for(int i=0; i<10; i++){
			tmp[i] = board[i].clone();
		}
		for(int j=0; j<10; j++)if(((bit>>j)&1) == 1){
			ans[0][j] = true;
			for(int k=0; k<5; k++){
				int ny = 0 + dy[k], nx = j + dx[k];
				if(0<=ny && ny<10 && 0<=nx && nx<10){
					tmp[ny][nx] = !tmp[ny][nx];
				}
			}
		}
		for(int i=1; i<10; i++){
			for(int j=0; j<10; j++)if(tmp[i-1][j]){
				ans[i][j] = true;
				for(int k=0; k<5; k++){
					int ny = i + dy[k], nx = j + dx[k];
					if(0<=ny && ny<10 && 0<=nx && nx<10){
						tmp[ny][nx] = !tmp[ny][nx];
					}
				}
			}
		}
		for(int j=0; j<10; j++)if(tmp[9][j]) return null;
		return ans;
	}

	boolean[][] solve(boolean[][] board){
		for(int bit=0; bit<1<<10; bit++){
			boolean[][] ans = check(board, bit);
			if(ans != null) return ans;
		}
		return null;
	}

	public static void main(String args[]){
		new Main().run();
	}
}