import java.io.*;
import java.util.*;

public class CF231Task {
	FastScanner in;
	PrintWriter out;

	ArrayList<Integer>[] g;
	ArrayList<Integer>[] g2;
	long[] pow;
	int[] wasColor;
	boolean[] was2;
	int[] cycleId;
	boolean[] isNotCycle;
	int numCycles = 0;
	int[] numCyclesTo;
	int[] h;
	int[][] up;
	int[] treeId;
	int numTrees;

	int go(int v, int p) {
		wasColor[v] = 1;
		int r = -1;
		for (int to : g[v]) {
			if (to == p)
				continue;
			if (wasColor[to] == 2)
				continue;
			if (wasColor[to] == 1) {
				cycleId[to] = numCycles;
				cycleId[v] = numCycles;
				r = numCycles++;
			} else {
				int res = go(to, v);
				if (cycleId[v] == -1 && res != -1) {
					r = res;
					cycleId[v] = r;
				}
			}
		}

		if (cycleId[v] == -1) {
			cycleId[v] = numCycles;
			isNotCycle[numCycles++] = true;
		}
		wasColor[v] = 2;
		return r;
	}

	void go2(int v, int s, int h1, int parent, int tree) {
		treeId[v] = tree;
		if (parent != -1) {
			up[v][0] = parent;
			for (int i = 1; i < 20; i++)
				up[v][i] = up[up[v][i - 1]][i - 1];
		}
		was2[v] = true;
		if (!isNotCycle[v])
			s++;
		numCyclesTo[v] = s;
		h[v] = h1;
		for (int to : g2[v]) {
			if (to == parent)
				continue;
			go2(to, s, h1 + 1, v, tree);
		}
	}

	int lca(int v1, int v2) {
		if (treeId[v1] != treeId[v2])
			return -1;
		if (h[v1] < h[v2]) {
			int tmp = v1;
			v1 = v2;
			v2 = tmp;
		}
		for (int i = 19; i >= 0; i--)
			if (h[up[v1][i]] >= h[v2])
				v1 = up[v1][i];
		if (v1 == v2)
			return v1;
		for (int i = 19; i >= 0; i--)
			if (up[v1][i] != up[v2][i]) {
				v1 = up[v1][i];
				v2 = up[v2][i];
			}
		return up[v1][0];
	}

	long ans(int fr, int to) {
		int c1 = cycleId[fr];
		int c2 = cycleId[to];
		int lca = lca(c1, c2);
		if (lca == -1)
			return 0;
		int a = numCyclesTo[c1] - numCyclesTo[lca];
		int b = numCyclesTo[c2] - numCyclesTo[lca];
		int sum = a + b + (isNotCycle[lca] ? 0 : 1);
		return pow[sum];

	}

	void solve() {
		int n = in.nextInt();
		int m = in.nextInt();
		g = new ArrayList[n];
		for (int i = 0; i < n; i++)
			g[i] = new ArrayList<Integer>();
		for (int i = 0; i < m; i++) {
			int fr = in.nextInt() - 1;
			int to = in.nextInt() - 1;
			g[fr].add(to);
			g[to].add(fr);
		}
		wasColor = new int[n];
		isNotCycle = new boolean[n];
		cycleId = new int[n];
		Arrays.fill(cycleId, -1);
		for (int i = 0; i < n; i++)
			if (wasColor[i] == 0) {
				go(i, -1);
			}
		g2 = new ArrayList[numCycles];
		for (int i = 0; i < numCycles; i++)
			g2[i] = new ArrayList<Integer>();
		for (int i = 0; i < n; i++)
			for (int to : g[i]) {
				if (i > to)
					continue;
				int from = cycleId[i];
				int too = cycleId[to];
				if (from != too) {
					g2[from].add(too);
					g2[too].add(from);
				}
			}
		numCyclesTo = new int[numCycles];
		was2 = new boolean[numCycles];
		h = new int[numCycles];
		up = new int[numCycles][20];
		treeId = new int[n];
		for (int i = 0; i < numCycles; i++)
			if (!was2[i]) {
				for (int j = 0; j < 20; j++)
					up[i][j] = i;
				go2(i, 0, 0, -1, numTrees++);
			}
		int k = in.nextInt();
		pow = new long[n + 1];
		pow[0] = 1;
		long mod = (long) 1e9 + 7;
		for (int i = 1; i <= n; i++)
			pow[i] = (pow[i - 1] * 2) % mod;
		for (int i = 0; i < k; i++) {
			int fr = in.nextInt() - 1;
			int to = in.nextInt() - 1;
			out.println(ans(fr, to));
		}
	}

	void run() {
		try {
			in = new FastScanner(new File("input.txt"));
			out = new PrintWriter(new File("output.txt"));

			solve();

			out.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	void runIO() {

		in = new FastScanner(System.in);
		out = new PrintWriter(System.out);

		solve();

		out.close();
	}

	class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		public FastScanner(File f) {
			try {
				br = new BufferedReader(new FileReader(f));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}

		public FastScanner(InputStream f) {
			br = new BufferedReader(new InputStreamReader(f));
		}

		String next() {
			while (st == null || !st.hasMoreTokens()) {
				String s = null;
				try {
					s = br.readLine();
				} catch (IOException e) {
					e.printStackTrace();
				}
				if (s == null)
					return null;
				st = new StringTokenizer(s);
			}
			return st.nextToken();
		}

		boolean hasMoreTokens() {
			while (st == null || !st.hasMoreTokens()) {
				String s = null;
				try {
					s = br.readLine();
				} catch (IOException e) {
					e.printStackTrace();
				}
				if (s == null)
					return false;
				st = new StringTokenizer(s);
			}
			return true;
		}

		int nextInt() {
			return Integer.parseInt(next());
		}

		long nextLong() {
			return Long.parseLong(next());
		}
	}

	public static void main(String[] args) {
		new CF231Task().runIO();
	}
}