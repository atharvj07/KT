
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {

		new Main().run();
	}

	@SuppressWarnings("unchecked")
	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		loop: while (true) {
			int n = scanner.nextInt();
			if (n == 0)
				break;
			Map<String, Integer>[] supers = new Map[n];
			for (int i = 0; i < n; i++)
				supers[i] = new HashMap<String, Integer>();
			Map<String, Integer> min = new HashMap<String, Integer>();
			for (int i = 0; i < n; i++) {
				int k = scanner.nextInt();
				for (int j = 0; j < k; j++) {
					String name = scanner.next();
					int value = scanner.nextInt();
					supers[i].put(name, value);
					if (!min.containsKey(name) || min.get(name) > value)
						min.put(name, value);
				}
			}
			int q = scanner.nextInt();
			String[] name = new String[q];
			for (int i = 0; i < q; i++)
				name[i] = scanner.next();
			int m = scanner.nextInt();
			List<Point>[] lists = new List[n + 1];
			for (int i = 0; i <= n; i++)
				lists[i] = new ArrayList<Main.Point>();

			while (m-- > 0) {
				int s = scanner.nextInt();
				int t = scanner.nextInt();
				int d = scanner.nextInt();
				lists[s].add(new Point(t, d));
				lists[t].add(new Point(s, d));
			}
			int sum = 0;
			for (int i = 0; i < q; i++) {
				if (!min.containsKey(name[i])) {
					System.out.println("impossible");
					continue loop;
				}
				sum += min.get(name[i]);
			}
			int[][] dp = new int[n + 1][1 << q];
			for (int[] dp1 : dp)
				Arrays.fill(dp1, 1 << 20);
			PriorityQueue<Point> pq = new PriorityQueue<Point>();
			pq.offer(new Point(0, 0, 0));
			int ans = 0;
			int[] bits = new int[n];
			for (int i = 0; i < n; i++) {
				int bit = 0;
				for (int j = 0; j < q; j++) {
					if (supers[i].containsKey(name[j])
							&& supers[i].get(name[j]).equals(min.get(name[j])))
						bit |= 1 << j;
				}
				bits[i] = bit;
			}
			while (!pq.isEmpty()) {
				Point p = pq.poll();
				int t = p.t;
				int cost = p.cost;
				int bit = p.bit;
				if (t == 0 && bit == (1 << q) - 1) {
					ans = cost;
					break;
				}
				if (dp[t][bit] < cost)
					continue;
				dp[t][bit] = cost;
				if (t > 0)
					bit |= bits[t - 1];
				for (Point point : lists[t])
					pq.offer(new Point(point.t, cost + point.cost, bit));

			}
			System.out.println(sum + " " + ans);
		}
	}

	class Point implements Comparable<Point> {
		int t, cost, bit;

		@Override
		public String toString() {
			return "Point [t=" + t + ", cost=" + cost + ", bit=" + bit + "]";
		}

		public Point(int t, int cost, int bit) {
			super();
			this.t = t;
			this.cost = cost;
			this.bit = bit;
		}

		public Point(int t, int cost) {
			super();
			this.t = t;
			this.cost = cost;
		}

		@Override
		public int compareTo(Point o) {
			if (cost == o.cost)
				return o.bit - bit;
			return cost - o.cost;
		}
	}
}