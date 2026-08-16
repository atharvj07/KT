
import java.io.*;
import java.util.*;

public class Main {
	
	int W, H, N;
	int[][] field = new int[16][16];

	int[] dx = {0, 1, 0, -1, 0};
	int[] dy = {1, 0, -1, 0, 0};

	short[][][] bfs = new short[16*16][16*16][16*16];
	int[][] graph = new int[16*16][6];
	Queue<int[]> Q = new ArrayDeque<>();
	public void solve() {
		Scanner sc = new Scanner(System.in);
		while(true){
			W = sc.nextInt();
			H = sc.nextInt();
			N = sc.nextInt();
			if(W == 0) break;
			int[] begin = new int[3];
			int[] end = new int[3];
			int idx = 1;
			sc.nextLine();
			for(int i = 0; i < H; i++){
				String str = sc.nextLine();
				for(int j = 0; j < W; j++){
					char c = str.charAt(j);
					if(c == '#') field[i][j] = 0;
					else{
						field[i][j] = idx++;
						if('A' <= c && c <= 'C') end[c - 'A'] = field[i][j];
						else if('a' <= c && c <= 'c') begin[c - 'a'] = field[i][j];
					}
				}
			}
			graph[0][0] = 0;
			graph[0][1] = -1;
			for(int i = 0; i < H; i++){
				for(int j = 0; j < W; j++){
					if(field[i][j] > 0){
						int cnt = 0;
						for(int k = 0; k < 5; k++){
							if(field[i + dy[k]][j + dx[k]] > 0){
								graph[field[i][j]][cnt++] = field[i + dy[k]][j + dx[k]];
							}
						}
						graph[field[i][j]][cnt] = -1;
					}
				}
			}
			
			for(int i = 0; i < idx; i++){
				for(int j = 0; j < idx; j++){
					for(int k = 0; k < idx; k++){
						bfs[i][j][k] = -1;
					}
				}
			}
			
			Q.clear();
			Q.add(begin);
			bfs[begin[0]][begin[1]][begin[2]] = 0;
			LOOP:
			while(!Q.isEmpty()){
				int[] t = Q.poll();
				for(int i = 0; graph[t[0]][i] != -1; i++){
					for(int j = 0; graph[t[1]][j] != -1; j++){
						for(int k = 0; graph[t[2]][k] != -1; k++){
							int n0 = graph[t[0]][i];
							int n1 = graph[t[1]][j];
							int n2 = graph[t[2]][k];
							if(
								bfs[n0][n1][n2] != -1 ||
								N >= 2 && t[0] == n1 && t[1] == n0 ||
								N >= 3 && t[0] == n2 && t[2] == n0 ||
								N >= 3 && t[1] == n2 && t[2] == n1 ||
								N >= 2 && n0 == n1 ||
								N >= 3 && n0 == n2 ||
								N >= 3 && n1 == n2
							){
								continue;
							}
							bfs[n0][n1][n2] = (short)(bfs[t[0]][t[1]][t[2]] + 1);
							if(n0 == end[0] && n1 == end[1] && n2 == end[2]) break LOOP;
							Q.add(new int[]{n0,n1,n2});
						}
					}
				}
			}
			System.out.println(bfs[end[0]][end[1]][end[2]]);
			
		}
	}
	private static PrintWriter out;

	public static void main(String[] args) {
		new Main().solve();
	}
}