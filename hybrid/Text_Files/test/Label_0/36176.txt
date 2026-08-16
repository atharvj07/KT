import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int[] DR = { 1, 1, 1, 0, -1, -1, -1, 0 };
	static int[] DC = { -1, 0, 1, 1, 1, 0, -1, -1 };
	static char[][] f;

	public static void main(String[] args) {
		int N = sc.nextInt();
		String[] dic = new String[N];
		int[] v = new int[N];
		for (int i = 0; i < N; ++i) {
			dic[i] = sc.next();
			v[i] = sc.nextInt();
		}
		f = new char[4][];
		for (int i = 0; i < 4; ++i) {
			f[i] = sc.next().toCharArray();
		}
		int[][] count = new int[9][101];
		boolean[][] visited = new boolean[4][4];
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < 4; ++j) {
				for (int k = 0; k < 4; ++k) {
					if (f[j][k] == dic[i].charAt(0)) {
						count[dic[i].length()][v[i]] += find(dic[i], 0, j, k, visited);
					}
				}
			}
		}

		int T = sc.nextInt();
		int[] dp = new int[T + 1];
		Arrays.fill(dp, -1);
		dp[T] = 0;
		for (int i = 1; i <= 8; ++i) {
			for (int j = 1; j <= 100; ++j) {
				if (count[i][j] == 0) continue;
				for (int k = 0; k <= T; ++k) {
					if (dp[k] < 0) continue;
					int n = k - i;
					for (int l = 1; l <= count[i][j] && n >= 0; ++l, n -= i) {
						dp[n] = Math.max(dp[n], dp[k] + l * j);
					}
				}
			}
		}
		int ans = 0;
		for (int i = 0; i <= T; ++i) {
			ans = Math.max(ans, dp[i]);
		}
		System.out.println(ans);
	}

	static int find(String word, int p, int r, int c, boolean[][] visited) {
		if (p == word.length() - 1) return 1;
		visited[r][c] = true;
		int ret = 0;
		for (int i = 0; i < 8; ++i) {
			int nr = r + DR[i];
			int nc = c + DC[i];
			if (nr < 0 || 3 < nr || nc < 0 || 3 < nc) continue;
			if (visited[nr][nc]) continue;
			if (f[nr][nc] != word.charAt(p + 1)) continue;
			ret += find(word, p + 1, nr, nc, visited);
		}
		visited[r][c] = false;
		return ret;
	}
}