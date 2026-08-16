
import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

public class Main {

	int INF = 1 << 28;
	//long INF = 1L << 62;
	double EPS = 1e-10;
	int[][] map;
	String rp = ".OPYBGR";
	int w = 6, h = 12;

	void run() {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(;t>0;t--) {
			map = new int[h+2][w+2];
			for(int i=1;i<=12;i++) {
				String s = sc.next();
				for(int j=0;j<rp.length();j++) s = s.replace(rp.charAt(j), (char)('0' + j));
				for(int j=1;j<=6;j++) map[i][j] = s.charAt(j-1) - '0';
			}
			boolean ch = true;
			int c = 0;
//			for(int[] a: map) debug(a);
			for(;;c++) {
				ch = false;
				for(int i=1;i<=w;i++) for(int j=1;j<=h;j++) if(map[j][i] > 1) {
					int cnt = dfs(i, j, map[j][i]);
					if(cnt >= 4) { del(i, j, map[j][i]); ch = true; }
//					for(int[] a: map) debug(a);
				}
				if(!ch) break;
				down();
//				for(int[] a: map) debug(a);

			}
			System.out.println(c);
		}
	}

	int dx[] = {-1,0,1,0}, dy[] = {0,-1,0,1};
	int dfs(int x, int y, int c) {
//		debug(x, y);
		map[y][x] = 0;
		int cnt = 1;
		for(int i=0;i<4;i++) if(map[y+dy[i]][x+dx[i]] == c) cnt += dfs(x+dx[i], y+dy[i], c);
		map[y][x] = c;
		return cnt;
	}

	void del(int x, int y, int c) {
		map[y][x] = 0;
		for(int i=0;i<4;i++) {
			if(map[y+dy[i]][x+dx[i]] == c) del(x+dx[i], y+dy[i], c);
			if(map[y+dy[i]][x+dx[i]] == 1) map[y+dy[i]][x+dx[i]] = 0;
		}
	}

	void down() {
		for(int j=1;j<=w;j++){
			for(int k=0;k<=h+2;k++) for(int i=0;i<=h-1;i++)
				if(map[i+1][j] == 0) { map[i+1][j] = map[i][j]; map[i][j] = 0;}
		}
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}