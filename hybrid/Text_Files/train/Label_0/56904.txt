import java.util.Arrays;
import java.util.Scanner;

public class Main {
	void run() {
		Scanner sc = new Scanner(System.in);
		final int INF = 1 << 28;
		while (true) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			int p = sc.nextInt();
			int a = sc.nextInt();
			int b = sc.nextInt();
			if ((n | m | p | a | b) == 0)
				break;
			int t[] = new int[n];
			for (int i = 0; i < n; i++) {
				t[i] = sc.nextInt();
			}
			int dis[][] = new int[m][m];
			for (int i = 0; i < m; i++) {
				Arrays.fill(dis[i], -1);
				dis[i][i] = 0;
			}
			for (int i = 0; i < p; i++) {
				int x = sc.nextInt()-1;
				int y = sc.nextInt()-1;
				int z = sc.nextInt();
				dis[x][y] = dis[y][x] = z;
			}
			double dp[][] = new double[1 << n][m];
			for (int i = 0; i < 1 << n; i++) {
				Arrays.fill(dp[i], Double.POSITIVE_INFINITY);
			}
			dp[(1 << n) - 1][a - 1] = 0;
			double res = Double.POSITIVE_INFINITY;
			for (int S = (1 << n) - 1; S >= 0; S--) {
				res = Math.min(res, dp[S][b - 1]);
				for (int v = 0; v < m; v++) {
					for (int i = 0; i < n; i++) {
						if((S>>i & 1) == 1)
						for (int u = 0; u < m; u++) {
							if (dis[v][u] < 0)
								continue;
							dp[S & ~(1 << i)][u] = Math.min(
									dp[S & ~(1 << i)][u], dp[S][v] + 1.0
											* dis[v][u] / t[i]);
						}
					}
				}
			}
			if (res == Double.POSITIVE_INFINITY) {
				System.out.println("Impossible");
			} else {
				System.out.printf("%.7f\n",res);
			}
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}