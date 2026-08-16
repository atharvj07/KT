
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {

		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			n = scanner.nextInt();
			if (n == 0)
				break;
			map = new int[n][n];
			v = new boolean[n][n];
			m = 0;
			p = new int[2][n * n];
			int sum = 0;
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++) {
					map[i][j] = scanner.nextInt();
					sum += map[i][j];
					if (map[i][j] < 0) {
						p[0][m] = i;
						p[1][m++] = j;
						v[i][j] = true;
					}

				}
			if (sum != 0) {
				System.out.println("NO");
				continue;
			}
			System.out
					.println(slove(p[0][0], p[1][0], 0, map[p[0][0]][p[1][0]]) ? "YES"
							: "NO");

		}
	}

	private boolean slove(int y, int x, int k, int sum) {
		if (sum > 0)
			return false;
		if (sum == 0) {
			if (++k == m)
				return true;
			return slove(p[0][k], p[1][k], k, map[p[0][k]][p[1][k]]);
		}
		for (int[] mo : move) {
			int ny = y + mo[0];
			int nx = x + mo[1];
			if (!isOK(ny, nx))
				continue;
			if (v[ny][nx])
				continue;
			v[ny][nx] = true;
			if (slove(ny, nx, k, sum + map[ny][nx]))
				return true;
			v[ny][nx] = false;
		}

		return false;
	}

	private boolean isOK(int ny, int nx) {
		return 0 <= ny && ny < n && 0 <= nx && nx < n;
	}

	int n, m;
	int[][] map;
	int[][] p;
	boolean[][] v;
	int[][] move = { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };
}