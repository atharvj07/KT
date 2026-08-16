import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int N = sc.nextInt();
		int M = sc.nextInt();
		int R = sc.nextInt();
		int[] D = new int[N];
		for (int i = 0; i < N; ++i) {
			D[i] = sc.nextInt();
		}
		ArrayList<ArrayList<Edge>> g = new ArrayList<>();
		for (int i = 0; i < N; ++i) {
			g.add(new ArrayList<>());
		}
		for (int i = 0; i < M; ++i) {
			int A = sc.nextInt() - 1;
			int B = sc.nextInt() - 1;
			int C = sc.nextInt();
			g.get(A).add(new Edge(B, C));
			g.get(B).add(new Edge(A, C));
		}
		int[][][] dp = new int[R + 1][2 * N][2 * N];
		for (int[][] a : dp) {
			for (int[] aa : a) {
				Arrays.fill(aa, -1);
			}
		}
		dp[0][0][0] = 0;
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < 2 * N; ++j) {
				int prev = j % N;
				for (int k = 0; k < 2 * N; ++k) {
					if (dp[i][j][k] == -1) continue;
					int pos = k % N;
					for (Edge e : g.get(pos)) {
						if (i + e.cost > R) continue;
						if (e.to != prev) {
							dp[i + e.cost][k][e.to] = Math.max(dp[i + e.cost][k][e.to], dp[i][j][k] + D[e.to]);
						} else {
							if (e.cost * 2 < 15) {
								if (j >= N) {
									dp[i + e.cost][k][e.to] = Math.max(dp[i + e.cost][k][e.to], dp[i][j][k] + D[e.to]);
								}
								dp[i + e.cost][k][e.to + N] = Math.max(dp[i + e.cost][k][e.to + N], dp[i][j][k]);
								if (i - e.cost + 15 <= R) {
									dp[i - e.cost + 15][pos + N][e.to] = Math.max(dp[i - e.cost + 15][pos + N][e.to], dp[i][j][k] + D[e.to]);
								}
							} else {
								dp[i + e.cost][k][e.to] = Math.max(dp[i + e.cost][k][e.to], dp[i][j][k] + D[e.to]);
							}
						}
					}
					if (i + 15 <= R) dp[i + 15][pos][pos] = Math.max(dp[i + 15][pos][pos], dp[i][j][k] + D[pos]);
					dp[i + 1][j][k] = Math.max(dp[i + 1][j][k], dp[i][j][k]);
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < 2 * N; ++i) {
			ans = Math.max(ans, dp[R][i][N - 1]);
			ans = Math.max(ans, dp[R][i][N + N - 1]);
		}
		System.out.println(ans);
	}

	static class Edge {
		int to, cost;

		public Edge(int to, int cost) {
			this.to = to;
			this.cost = cost;
		}

	}

}