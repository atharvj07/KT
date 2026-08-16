import java.io.*;
public class Main {

	static int n, m;
	static int[] dx = {0,0,-1,1}, dy = {-1,1,0,0};
	static boolean[][] map, check;

	public static int dfs (int y, int x) {
		int ret = 0;
		for (int i = 0; i < 4; i++) {
			int nextX = x + dx[i];
			int nextY = y + dy[i];
			if (0 <= nextX && nextX < m &&
				0 <= nextY && nextY < n &&
				map[nextY][nextX] &&
				!check[nextY][nextX]) {

				check[nextY][nextX] = true;
				ret = Math.max(dfs(nextY,nextX) + 1,ret);
				check[nextY][nextX] = false;
			}
		}
		return ret;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader s = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out = new PrintWriter(System.out);
		while (true) {
			m = Integer.valueOf(s.readLine());
			n = Integer.valueOf(s.readLine());
			if (m == 0 && n == 0) break;
			map = new boolean[n][m];
			for (int i = 0 ; i < n ; i++) {
				String[] data = s.readLine().split(" ");
				for (int j = 0 ; j < m ; j++)
					map[i][j] = Integer.valueOf(data[j]) == 1;
			}
			int max = 0;
			for (int i = 0 ; i < n ; i++) {
				for (int j = 0 ; j < m ; j++) {
					if (map[i][j]) {
						check = new boolean[n][m];
						max = Math.max(max, dfs(i, j));
					}
				}
			}
			out.println(max);
		}
		out.flush();
	}
}