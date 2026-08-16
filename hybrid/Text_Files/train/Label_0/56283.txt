import java.util.*;

public class Main {
	static ArrayList<Integer>[] g;

	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int m = sc.nextInt();
			int n = sc.nextInt();
			if (m == 0 && n == 0)
				break;
			int[] b = new int[m];
			int[] r = new int[n];
			for (int i = 0; i < m; ++i) {
				b[i] = sc.nextInt();
			}
			for (int i = 0; i < n; ++i) {
				r[i] = sc.nextInt();
			}

			g = new ArrayList[n + m];
			for (int i = 0; i < n + m; ++i) {
				g[i] = new ArrayList<>();
			}

			for (int i = 0; i < m; ++i) {
				for (int j = 0; j < n; ++j) {
					if (gcd(b[i], r[j]) > 1) {
						g[i].add(m + j);
						g[m + j].add(i);
					}
				}
			}
			vis = new boolean[n + m];
			matchTo = new int[n + m];
			Arrays.fill(matchTo, -1);
			int match = 0;
			for (int i = 0; i < m; ++i) {
				Arrays.fill(vis, false);
				if (dfs(i)) {
					++match;
				}
			}
			System.out.println(match);
		}
		sc.close();
	}

	static boolean[] vis;
	static int[] matchTo;

	static boolean dfs(int v) {
		if (v < 0)
			return true;
		for (int dst : g[v]) {
			if (vis[dst])
				continue;
			vis[dst] = true;
			if (dfs(matchTo[dst])) {
				matchTo[v] = dst;
				matchTo[dst] = v;
				return true;
			}
		}
		return false;
	}

	static int gcd(int a, int b) {
		if (a > b) {
			int d = a;
			a = b;
			b = d;
		}
		if (a == 0)
			return b;
		else
			return gcd(b % a, a);
	}

}