
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {

		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			int h = scanner.nextInt();
			int w = scanner.nextInt();
			int n = scanner.nextInt();
			if ((h | w | n) == 0)
				break;
			int[][] map = new int[h + 1][w + 1];
			map[0][0] = --n;
			boolean[][] b = new boolean[h][w];
			for (int i = 0; i < h; i++)
				for (int j = 0; j < w; j++) {
					int m = scanner.nextInt();
					map[i][j + 1] += (map[i][j] + (m & 1)) / 2;
					map[i + 1][j] += (map[i][j] + (m ^ 1)) / 2;
					b[i][j] = (map[i][j] + m) % 2 == 1;
				}
			int px = 0;
			int py = 0;
			while (px < w && py < h) {
				if (b[py][px])
					px++;
				else
					py++;
			}
			System.out.println((py + 1) + " " + (px + 1));
		}
	}
}