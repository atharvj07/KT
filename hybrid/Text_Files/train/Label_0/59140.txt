
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			int n = scanner.nextInt();
			int m = scanner.nextInt();
			if ((n | m) == 0)
				break;
			int[][] map = new int[n][n];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					map[i][j] = scanner.nextInt();
				}
			}
			int[][][] p = new int[4][m][m];
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < m; j++) {
					p[0][i][j] = scanner.nextInt();
				}
			}
			for (int k = 1; k < 4; k++) {
				for (int i = 0; i < m; i++) {
					for (int j = 0; j < m; j++) {
						p[k][i][j] = p[k - 1][j][m - i - 1];
					}
				}
			}
			int ay = -1;
			int ax = -1;
			boolean flag = false;
			loop: for (int i = 0; i <= n - m; i++) {
				for (int j = 0; j <= n - m; j++) {
					boolean ff = false;
					a: for (int k = 0; k < 4; k++) {
						ff = true;
						boolean f = false;
						for (int y = 0; y < m; y++) {
							for (int x = 0; x < m; x++) {
								if (p[k][y][x] == -1)
									continue;
								else if (!f) {
									f = true;
									ay = i + y + 1;
									ax = j + x + 1;
								}
								if (p[k][y][x] != map[i + y][j + x]) {
									ff = false;
									continue a;
								}
							}
						}
						if (ff) {
							flag = true;
							break loop;
						}
					}

				}
			}
			System.out.println(flag ? ax + " " + ay : "NA");

		}
	}
}