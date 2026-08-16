import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		new Main().solver();
	}

	int[] dx = { 1, -1, 0, 0 };
	int[] dy = { 0, 0, 1, -1 };
	char[][] table;
	long INF = 1L << 50;

	int h, w;

	void solver() {
		Scanner sc = new Scanner(System.in);
		w = sc.nextInt();
		h = sc.nextInt();
		int sx = -1, sy = -1, gx = -1, gy = -1;
		double n = 0;
		table = new char[h][w];
		long[][] distance_from_goal = new long[h][w];
		long[][] distance_from_spring = new long[h][w];

		ArrayDeque<Pair> que1 = new ArrayDeque<>();
		ArrayDeque<Pair> que2 = new ArrayDeque<>();

		for (int i = 0; i < h; i++) {
			table[i] = sc.next().toCharArray();
			Arrays.fill(distance_from_goal[i], INF);
			Arrays.fill(distance_from_spring[i], INF);

			for (int j = 0; j < w; j++) {
				if (table[i][j] == 's') {
					sx = j;
					sy = i;
					n++;
				} else if (table[i][j] == 'g') {
					gx = j;
					gy = i;
					distance_from_goal[gy][gx] = 0;
				} else if (table[i][j] == '.')
					n++;
				else if (table[i][j] == '*') {
					distance_from_spring[i][j] = 0;
					que2.add(new Pair(j, i));
				}
			}
		}

		que1.add(new Pair(gx, gy));
		while (!que1.isEmpty()) {
			Pair p = que1.poll();
			for (int i = 0; i < 4; i++) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				if (on_filed(nx, ny) && distance_from_goal[ny][nx] > distance_from_goal[p.y][p.x] + 1) {
					distance_from_goal[ny][nx] = distance_from_goal[p.y][p.x] + 1;
					if (table[ny][nx] == '.' || table[ny][nx] == 's')
						que1.add(new Pair(nx, ny));
				}
			}
		}

		while (!que2.isEmpty()) {
			Pair p = que2.poll();
			for (int i = 0; i < 4; i++) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				if (on_filed(nx, ny) && distance_from_spring[ny][nx] > distance_from_spring[p.y][p.x] + 1) {
					distance_from_spring[ny][nx] = distance_from_spring[p.y][p.x] + 1;
					if (table[ny][nx] == '.' || table[ny][nx] == 's')
						que2.add(new Pair(nx, ny));
				}
			}
		}

		double a = 0, b = 0;
		ArrayList<P> list = new ArrayList<>();
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (table[i][j] == '.' || table[i][j] == 's') {
					if (distance_from_goal[i][j] >= INF) {
						a += distance_from_spring[i][j];
						b++;
						continue;
					} else {
						a += distance_from_goal[i][j];
						if (distance_from_spring[i][j] >= (1 << 30)
								|| distance_from_goal[i][j] <= distance_from_spring[i][j]) {
							continue;
						} else
							list.add(new P(distance_from_goal[i][j], distance_from_spring[i][j]));
					}
				}
			}
		}
		list.sort(null);

		// E=a+bE
		double e = a / (n - b);
		for (int i = 0; i < list.size(); i++) {
			a -= list.get(i).d_goal;
			a += list.get(i).d_spring;
			b++;
			if (i + 1 < list.size() && list.get(i).diff == list.get(i + 1).diff)
				continue;

			e = Math.min(e, (a / (n - b)));
		}

		System.out.println(Math.min(distance_from_goal[sy][sx], e + distance_from_spring[sy][sx]));
	}

	boolean on_filed(int x, int y) {
		if (0 <= x && x < w && 0 <= y && y < h && table[y][x] != '#')
			return true;
		else
			return false;
	}

	class Pair {
		int x;
		int y;

		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	class P implements Comparable<P> {
		long d_goal;
		long d_spring;
		long diff;

		public P(long d_goal, long d_spring) {
			this.d_goal = d_goal;
			this.d_spring = d_spring;
			diff = d_goal - d_spring;
		}

		@Override
		public int compareTo(P o) {
			return -Long.compare(this.diff, o.diff);
		}
	}

	void tr(Object... o) {
		System.out.println(Arrays.deepToString(o));
	}
}