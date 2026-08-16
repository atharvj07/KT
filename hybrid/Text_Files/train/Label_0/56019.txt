
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {

		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		h = scanner.nextInt();
		w = scanner.nextInt();
		K = scanner.nextInt();
		mask = (1 << (4 * K)) - 1;
		map = new char[h][w];
		for (int i = 0; i < h; i++)
			map[i] = scanner.next().toCharArray();
		dp = new int[4][h][w][1 << (K * 4)];
		for (int[][][] dp1 : dp)
			for (int[][] dp2 : dp1)
				for (int[] dp3 : dp2)
					Arrays.fill(dp3, -1);
		v = new boolean[mask + 1];
		loop: for (int i = 0; i <= mask; i++) {
			int py = 0;
			int px = 0;
			int bit = i;
			for (int j = 0; j < K * 2; j++) {
				py -= dy[bit & 3];
				px -= dx[bit & 3];
				if (py == 0 && px == 0) {
					v[i] = true;
					continue loop;
				}
				bit >>= 2;
			}
		}

		System.out.println(slove(K, 0, 0, 0));
	}

	private int slove(int k, int y, int x, int bit) {
		if (dp[k][y][x][bit] != -1)
			return dp[k][y][x][bit];
		if (y == h - 1 && x == w - 1 && k == 0)
			return 0;
		int ret = 0;
		if (!v[bit] && map[y][x] != '.')
			ret += map[y][x] - '0';
		int val = -(1 << 20);
		for (int i = 0; i < 4; i++) {
			if (k == 0 && i >= 2)
				break;
			int ny = y + dy[i];
			int nx = x + dx[i];
			if (!isOK(ny, nx))
				continue;
			if (map[ny][nx] == '#')
				continue;
			val = Math
					.max(val,
							slove(k - (i >= 2 ? 1 : 0), ny, nx,
									((bit << 2) | i) & mask) + ret);
		}
		return dp[k][y][x][bit] = val;
	}

	private boolean isOK(int ny, int nx) {
		return (0 <= ny && ny < h && 0 <= nx && nx < w);
	}

	int h, w, K, mask;
	boolean[] v;
	int[] dy = { 0, 1, 0, -1 };
	int[] dx = { 1, 0, -1, 0 };
	int[][][][] dp;
	char[][] map;
}