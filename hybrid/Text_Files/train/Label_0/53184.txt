
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {

		new Main().run();
	}

	@SuppressWarnings("unchecked")
	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			int n = scanner.nextInt();
			int m = scanner.nextInt();
			if ((n | m) == 0)
				break;
			List<Point>[] lists = new ArrayList[n + 1];
			for (int i = 0; i <= n; i++)
				lists[i] = new ArrayList<Point>();
			for (int i = 1; i <= n; i++) {
				int k = scanner.nextInt();
				for (int j = 0; j < k; j++) {
					int x = scanner.nextInt();
					int cost = scanner.nextInt();
					lists[i - 1].add(new Point(1, x, cost));
					if (i != 1)
						lists[i - 2].add(new Point(2, x, cost));
					if (i == n - 1)
						lists[i].add(new Point(2, x, 0));
					if (i == n)
						lists[i].add(new Point(1, x, 0));

				}
			}
			PriorityQueue<Point> pq = new PriorityQueue<Main.Point>();
			pq.offer(new Point(0, 0, 0, 0, m));
			int[][][] dp = new int[m + 1][n + 1][1001];
			for (int[][] d : dp)
				for (int[] dd : d)
					Arrays.fill(dd, Integer.MAX_VALUE);
			dp[m][0][0] = 0;
			while (!pq.isEmpty()) {
				Point point = pq.poll();
				int y = point.y;
				int x = point.x;
				int cost = point.cost;
				int total = point.total;
				int mm = point.m;

				if (y >= n) {
					System.out.println(total);
					break;
				}
				if (dp[mm][y][x] < total)
					continue;
				for (Point p : lists[y]) {
					int nc = (cost + p.cost) * Math.abs(x - p.x) + total;
					int ny = Math.min(n, y + p.y);
					if (p.y == 2) {
						if (mm >= 1) {
							if (dp[mm - 1][ny][p.x] > nc) {
								dp[mm - 1][ny][p.x] = nc;
								pq.offer(new Point(ny, p.x, p.cost,
										y == 0 ? 0 : nc, mm - 1));
							}
						}
					} else {
						if (dp[mm][ny][p.x] > nc) {
							dp[mm][ny][p.x] = nc;
							pq.offer(new Point(ny, p.x, p.cost, y == 0 ? 0
									: nc, mm));
						}
					}
				}
			}

		}
	}

	class Point implements Comparable<Point> {
		int y, x, cost, total, m;

		public Point(int y, int x, int cost, int total, int m) {
			super();
			this.y = y;
			this.x = x;
			this.cost = cost;
			this.total = total;
			this.m = m;
		}

		public Point(int y, int x, int cost) {
			super();
			this.y = y;
			this.x = x;
			this.cost = cost;

		}

		@Override
		public String toString() {
			return "Point [y=" + y + ", x=" + x + ", cost=" + cost + ", total="
					+ total + ", m=" + m + "]";
		}

		@Override
		public int compareTo(Point o) {
			if (this.total == o.total)
				return o.y - this.y;
			return this.total - o.total;
		}
	}
}