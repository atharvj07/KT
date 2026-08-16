
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			int w = scanner.nextInt();
			int h = scanner.nextInt();
			if ((w | h) == 0)
				break;
			PriorityQueue<Player> pq = new PriorityQueue<Player>();
			char[][] map = new char[h][w];
			for (int i = 0; i < h; i++) {
				map[i] = scanner.next().toCharArray();
				for (int j = 0; j < w; j++) {
					if (map[i][j] != '#' && map[i][j] != '.'
							&& map[i][j] != 'X') {
						char c = map[i][j];
						int dir = c == 'W' ? 0 : c == 'S' ? 1 : c == 'E' ? 2
								: 3;
						map[i][j] = 'P';
						pq.add(new Player(i, j, dir));
					}
				}
			}
			String ans = "NA";
			int step = 1;
			while (step <= 180) {
				PriorityQueue<Player> next = new PriorityQueue<Player>();
				pl: while (!pq.isEmpty()) {
					Player player = pq.poll();
					for (int k = 3; k < 7; k++) {
						int y = player.y;
						int x = player.x;
						int dir = player.dir;
						int ny = y + move[(k + dir) % 4][0];
						int nx = x + move[(k + dir) % 4][1];
						if (map[ny][nx] == '.' || map[ny][nx] == 'X') {
							player.dir = (k + dir) % 4;
							player.ny = ny;
							player.nx = nx;
							next.add(player);
							continue pl;
						}
					}
					player.b = false;
					next.add(player);
				}
				pq = next;
				next = new PriorityQueue<Player>();
				while (!pq.isEmpty()) {
					Player player = pq.poll();
					if (!player.b) {
						player.b = true;
						next.add(player);
					} else {
						int y = player.y;
						int x = player.x;
						int ny = player.ny;
						int nx = player.nx;
						map[y][x] = '.';
						if (map[ny][nx] == 'X') {
							map[ny][nx] = 'x';
							continue;
						}
						if (map[ny][nx] == '.') {
							map[ny][nx] = 'P';
							player.y = ny;
							player.x = nx;
							next.add(player);
						} else {
							map[y][x] = 'P';
							next.add(player);
						}

					}

				}
				if (next.isEmpty()) {
					ans = String.valueOf(step);
					break;
				}
				pq.addAll(next);
				for (int i = 0; i < h; i++)
					for (int j = 0; j < w; j++)
						if (map[i][j] == 'x')
							map[i][j] = 'X';
				step++;
			}
			System.out.println(ans);

		}
	}

	int[][] move = { { 0, -1 }, { 1, 0 }, { 0, 1 }, { -1, 0 } };

	class Player implements Comparable<Player> {
		int y;
		int x;
		int dir;
		int ny;
		int nx;
		boolean b = true;

		public Player(int y, int x, int dir) {
			super();
			this.y = y;
			this.x = x;
			this.dir = dir;
		}

		@Override
		public int compareTo(Player o) {
			return this.dir - o.dir;
		}

	}
}