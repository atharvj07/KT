import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Queue;
import java.util.concurrent.ArrayBlockingQueue;

public class ProblemD {
	static final long MOD = 1000000007;
	
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out = new PrintWriter(System.out);
		
		String[] nm = in.readLine().split(" ");
		int n = Integer.valueOf(nm[0]);
		int m = Integer.valueOf(nm[1]);
		
		char[][] map = new char[n][m];
		int minx = 100000;
		int maxx = -1;
		int miny = 100000;
		int maxy = -1;
		for (int i = 0 ; i < n ; i++) {
			map[i] = in.readLine().toCharArray();
			for (int j = 0 ; j < m ; j++) {
				if (map[i][j] == 'w') {
					minx = Math.min(minx, j);
					maxx = Math.max(maxx, j);
					miny = Math.min(miny, i);
					maxy = Math.max(maxy, i);
				}
			}
		}
		
		for (int i = miny+1 ;  i <= maxy-1 ; i++) {
			for (int j = minx+1 ; j <= maxx-1; j++) {
				if (map[i][j] == 'w') {
					out.println(-1);
					out.flush();
					return;
				}
			}
		}
		
		
		int[][] yimos = new int[m][n+1];
		int[][] ximos = new int[n][m+1];
		for (int i = 0 ; i < m ; i++) {
			for (int j = 0 ; j < n ; j++) {
				yimos[i][j+1] = yimos[i][j] + ((map[j][i] == 'w') ? 1 : 0);
			}
		}
		for (int i = 0 ; i < n ; i++) {
			for (int j = 0 ; j < m ; j++) {
				ximos[i][j+1] = ximos[i][j] + ((map[i][j] == 'w') ? 1 : 0);
			}
		}
		

		
		int yl = maxy-miny+1;
		int xl = maxx-minx+1;
		if (xl == 1 && xl < yl && yimos[minx][maxy] - yimos[minx][miny+1] >= 1) {
			int need = yl - xl;
			int low = minx;
			int high = (m-1)-maxx;
			int gain = Math.min(need, Math.max(low, high));
			xl += gain;
			if (low < high) {
				maxx += gain;
			} else {
				minx -= gain;
			}
		} else if (yl == 1 && yl < xl && ximos[miny][maxx] - ximos[miny][minx+1] >= 1) {
			int need = xl - yl;
			int low = miny;
			int high = (n-1)-maxy;
			int gain = Math.min(need, Math.max(low, high));
			yl += gain;
			if (low < high) {
				maxy += gain;
			} else {
				miny -= gain;
			}
		} else {
			while (minx >= 1 && xl < yl && (yimos[minx][maxy] - yimos[minx][miny+1]) <= 0) {
				xl++;
				minx--;
			}
			while (maxx <= m-2 && xl < yl && (yimos[maxx][maxy] - yimos[maxx][miny+1]) <= 0) {
				xl++;
				maxx++;
			}
			while (miny >= 1 && yl < xl && (ximos[miny][maxx] - ximos[miny][minx+1]) <= 0) {
				yl++;
				miny--;
			}
			while (maxy <= n-2 && yl < xl && (ximos[maxy][maxx] - ximos[maxy][minx+1]) <= 0) {
				yl++;
				maxy++;
			}
		}
		
		if (xl != yl) {
			out.println(-1);
			out.flush();
			return;
		}
		
		for (int i = minx ; i <= maxx ; i++) {
			if (map[miny][i] == '.') {
				map[miny][i] = '+';
			}
			if (map[maxy][i] == '.') {
				map[maxy][i] = '+';
			}
		}
		for (int i = miny ; i <= maxy ; i++) {
			if (map[i][minx] == '.') {
				map[i][minx] = '+';
			}
			if (map[i][maxx] == '.') {
				map[i][maxx] = '+';
			}
		}
		
		
		for (int i = 0 ; i < n ; i++) {
			out.println(String.valueOf(map[i]));
		}
		
		out.flush();
	}
	
	
	static int needFrame(int size) {
		return Math.max(1, (size-1)*4);
	}
	
	public static void debug(Object... o) {
		System.err.println(Arrays.deepToString(o));
	}
	
}
