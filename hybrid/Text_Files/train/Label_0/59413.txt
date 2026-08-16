import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.Scanner;

class State{
	int h, w;
	public State(int _h, int _w) {
		h = _h; w = _w;
	}
}
public class Main{
	static int[] dx = {0, 0, -1, 1};
	static int[] dy = {-1, 1, 0, 0};
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int H = sc.nextInt(), W = sc.nextInt();
		int ans = 0;
		int[][] map = new int[H][W];
		Queue<State> que = new ArrayDeque<State>();
		for(int i = 0; i < H; i++) {
			Arrays.fill(map[i], Integer.MAX_VALUE);
			String str = sc.next();
			for(int j = 0; j < W; j++) {
				if(str.charAt(j) == '#') {
					map[i][j] = 0;
					que.add(new State(i, j));
				}
			}
		}
		while(!que.isEmpty()) {
			State now = que.poll();
			for(int k = 0; k < 4; k++) {
				if(now.h + dx[k] < 0 || now.h + dx[k] >= H || now.w + dy[k] < 0 || now.w + dy[k] >= W) continue;
				int nh = now.h + dx[k], nw = now.w + dy[k];
				if(map[nh][nw] == Integer.MAX_VALUE) {
					map[nh][nw] = map[now.h][now.w] + 1;
					que.add(new State(nh, nw));
				}
			}
		}
		for(int i = 0; i < H; i++) for(int j = 0; j < W; j++) ans = Math.max(ans, map[i][j]);
		System.out.println(ans);
	}
}
