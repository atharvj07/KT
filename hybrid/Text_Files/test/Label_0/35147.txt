import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int N, M;
	static int[][] g;
	static int ans;
	static int[] min = new int[20];

	public static void main(String[] arg) {
		N = sc.nextInt();
		M = sc.nextInt();
		g = new int[N][N];
		for (int i = 0; i < M; ++i) {
			int u = sc.nextInt() - 1;
			int v = sc.nextInt() - 1;
			int f = sc.nextInt();
			g[u][v] = g[v][u] = f;
		}
		int[] r = new int[20];
		dfs(0, r, 0);
		System.out.println(ans);
	}

	static void dfs(int c, int[] r, int d) {
		if (d >= 2) {
			for (int i = 0; i < d; ++i) {
				min[i] = 1 << 30;
			}
			for (int i = 0; i < d; ++i) {
				for (int j = 0; j < i; ++j) {
					min[i] = Math.min(min[i], g[r[i]][r[j]]);
					min[j] = Math.min(min[j], g[r[i]][r[j]]);
				}
			}
			int sum = 0;
			for (int i = 0; i < d; ++i) {
				sum += min[i];
			}
			ans = Math.max(ans, sum);
		}
		for (int i = c; i < N; ++i) {
			boolean ok = true;
			for (int j = 0; j < d; ++j) {
				if (g[i][r[j]] == 0) {
					ok = false;
					break;
				}
			}
			if (!ok) continue;
			r[d] = i;
			dfs(i + 1, r, d + 1);
		}
	}
}