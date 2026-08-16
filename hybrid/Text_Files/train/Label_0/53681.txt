import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		new Main().run();
	}

	void run() {
		Scanner sc = new Scanner(System.in);
		while (true) {
			char[] s = sc.next().toCharArray();
			if (s.length == 1 && s[0] == '#')
				break;
			solve(s);
		}
	}

	void solve(char[] s) {
		int[] v = new int[s.length];
		for (int i = 0; i < s.length; ++i) {
			v[i] = s[i] - 'A';
		}
		boolean[] valid = new boolean['z' - 'A' + 1];
		for (int i = 0; i < v.length; ++i) {
			valid[v[i]] = true;
		}
		@SuppressWarnings("unchecked")
		ArrayList<Integer>[] g = new ArrayList['z' - 'A' + 1];
		for (int i = 0; i < g.length; ++i) {
			g[i] = new ArrayList<>();
		}
		int e_sz = 0;
		for (int i = 0; i + 1 < v.length; ++i) {
			if (!g[v[i]].contains(v[i + 1])) {
				g[v[i]].add(v[i + 1]);
				++e_sz;
			}
		}

		if (v.length <= 2) {
			System.out.println("No Results");
			return;
		}
		int[] indegree = new int[g.length];
		int[] outdegree = new int[g.length];
		for (int i = 0; i < g.length; ++i) {
			if (!valid[i])
				continue;
			outdegree[i] = g[i].size();
			for (int dst : g[i]) {
				++indegree[dst];
			}
		}

		int d = 0;
		for (int i = 0; i < g.length; ++i) {
			if (!valid[i])
				continue;
			if (indegree[i] - outdegree[i] > 0)
				d += indegree[i] - outdegree[i];
		}

		if (d == 0) {
			System.out.println(e_sz + 1);
			return;
		}

		if (d == 1) {
			System.out.println(semi_Eulerian(g, v, valid, indegree, outdegree, e_sz));
			return;
		}

		if (d >= 2) {
			System.out.println(e_sz + d);
			return;
		}

	}

	int semi_Eulerian(ArrayList<Integer>[] g, int[] v, boolean[] valid, int[] indegree, int[] outdegree, int e_sz) {
		if (e_sz + 1 < v.length) {
			return e_sz + 1;
		}
		if (e_sz + 1 != v.length) {
			throw new AssertionError();
		}
		int src = -1;
		int dst = -1;
		for (int i = 0; i < g.length; ++i) {
			if (!valid[i])
				continue;
			if (indegree[i] - outdegree[i] > 0)
				dst = i;
			else if (indegree[i] - outdegree[i] < 0)
				src = i;
		}
		if (src == v[0] && dst == v[v.length - 1]) {
			if (dfs(g, new boolean[g.length][g.length], src, 0, e_sz) > 1)
				return v.length;
			return v.length + 1;
		} else {
			return v.length;
		}
	}

	int dfs(ArrayList<Integer>[] g, boolean[][] vis, int cur, int num, int e_sz) {
		if (e_sz == num)
			return 1;
		int sum = 0;
		for (int dst : g[cur]) {
			if (vis[cur][dst])
				continue;
			vis[cur][dst] = true;
			sum += dfs(g, vis, dst, num + 1, e_sz);
			if (sum >= 2)
				return sum;
			vis[cur][dst] = false;
		}
		return sum;
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}