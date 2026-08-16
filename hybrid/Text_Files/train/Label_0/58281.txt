
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

	public static void main(String[] args) throws IOException {

		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			int h = scanner.nextInt();
			int w = scanner.nextInt();
			if ((h | w) == 0)
				break;
			StringBuilder b = new StringBuilder();
			for (int i = 0; i < h; i++)
				b.append(scanner.next());
			Deque<Point> deque = new ArrayDeque<Main.Point>();
			int k = b.indexOf("@");
			deque.push(new Point(k / w, k % w, b.toString(), 1));
			int ans = -1;
			Set<String> set = new HashSet<String>();
			loop: while (!deque.isEmpty()) {
				Point p = deque.poll();
				String g = p.g;
				int d = p.d;
				int y = p.y;
				int x = p.x;
				int a = y * w + x;
				if (set.contains(g))
					continue;
				set.add(g);
				for (int i = 0; i < 4; i++) {
					int sy = y + dy[i];
					int sx = x + dx[i];
					int aa = sy * w + sx;
					char c = g.charAt(aa);
					if (c == '#' || c == 'w')
						continue;
					if (c == 'E') {
						ans = d;
						break loop;
					}
					if (c == '.') {
						char[] tmp = g.toCharArray();
						tmp[a] = '.';
						tmp[aa] = '@';
						deque.offer(new Point(sy, sx, String.valueOf(tmp),
								d + 1));
					}
					if (c == 'c') {
						char[] tmp = g.toCharArray();
						tmp[aa] = '.';
						while (true) {
							int ny = sy + dy[i];
							int nx = sx + dx[i];
							char nc = tmp[ny * w + nx];
							if (nc == '#' || nc == 'c') {
								tmp[sy * w + sx] = 'c';
								break;
							}
							if (nc == 'w') {
								tmp[ny * w + nx] = '.';
								break;
							}
							sy = ny;
							sx = nx;
						}
						deque.offer(new Point(y, x, String.valueOf(tmp), d));
					}
				}

			}
			System.out.println(ans);
		}
	}

	int[] dy = { -1, 0, 0, 1 };
	int[] dx = { 0, -1, 1, 0 };

	class Point {
		int y, x;
		String g;
		int d;

		public Point(int y, int x, String g, int d) {
			super();
			this.y = y;
			this.x = x;
			this.g = g;
			this.d = d;
		}

		@Override
		public String toString() {
			return "Point [y=" + y + ", x=" + x + ", g=" + g + ", d=" + d + "]";
		}

	}
}