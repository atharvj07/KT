import java.io.*;

import java.awt.geom.Point2D;
import java.text.*;
import java.math.*;
import java.util.*;

public class Main implements Runnable {

	final String filename = "";

	public void solve() throws Exception {
		int n = iread(), m = iread();
		Edge[] edges = new Edge[2 * m];
		for (int i = 0; i < m; i++) {
			int x = iread(), y = iread();
			x--;
			y--;
			edges[i * 2] = new Edge(x, y);
			edges[i * 2 + 1] = new Edge(y, x);
		}
		first = new Edge[n];
		for (int i = 0; i < 2 * m; i++)
			edges[i].add();
		num = new int[n];
		rev_num = new int[n];
		parent = new int[n];
		curnum = 0;
		Arrays.fill(num, -1);
		for (int i = 0; i < n; i++)
			if (num[i] == -1)
				dfs(i, -1);
		fup = new int[n];
		for (int i = 0; i < n; i++)
			fup[i] = i;
		for (int i = n - 1; i >= 0; i--) {
			int x = rev_num[i];
			for (Edge e = first[x]; e != null; e = e.next) {
				int y = e.to;
				if (y == parent[x])
					continue;
				if (num[fup[x]] > num[fup[y]])
					fup[x] = fup[y];
			}
		}

		for (int i = 0; i < n; i++)
			parent[i] = i;
		rank = new int[n];
		for (int i = 0; i < n; i++)
			join(i, fup[i]);
		first = new Edge[n];
		HashSet<Edge> h = new HashSet<Edge>();
		for (int i = 0; i < 2 * m; i++) {
			edges[i].from = getParent(edges[i].from);
			edges[i].to = getParent(edges[i].to);
			if (edges[i].from != edges[i].to && !h.contains(edges[i])) {
				edges[i].add();
				h.add(edges[i]);
			}
		}
		h.clear();
		Arrays.fill(num, -1);
		curnum = 0;

		is_leaf = new boolean[n];
		int ans = 0;
		boolean flag = false;
		for (int i = 0; i < n; i++) {
			if (parent[i] != i)
				continue;
			if (num[i] != -1)
				continue;
			if (first[i] == null) {
				if (!flag) {
					ans++;
					flag = true;
				}
				continue;
			}
			int p = -1, x = i;
			if (first[i].next == null) {
				p = i;
				x = first[i].to;
			}
			leafs = 0;
			dfs1(x, p);
			if (p != -1)
				leafs++;
			int[] res = dfs2(x, p);
			ans += leafs + Math.max(res[0], res[1]);
			if (flag)
				ans--;
			else
				flag = true;
		}
		ans = n - ans;
		out.write(ans + "\n");
	}

	Edge[] first;
	int[] num, rev_num, parent, fup, rank;
	int leafs;
	boolean[] is_leaf;
	int curnum;

	void dfs(int x, int par) {
		if (num[x] != -1)
			return;
		parent[x] = par;
		num[x] = curnum;
		rev_num[curnum] = x;
		curnum++;
		for (Edge e = first[x]; e != null; e = e.next)
			dfs(e.to, x);
	}

	void dfs1(int x, int par) {
		if (num[x] != -1)
			return;
		num[x] = curnum++;
		is_leaf[x] = true;
		for (Edge e = first[x]; e != null; e = e.next) {
			int y = e.to;
			if (y != par) {
				dfs1(y, x);
				is_leaf[x] = false;
			}
		}
		if (is_leaf[x])
			leafs++;
	}

	int[] dfs2(int x, int par) {
		if (is_leaf[x])
			return new int[] { 0, 0 };
		int[] ans = new int[2];
		int best1 = 0, best2 = 0;
		int v = 0;
		for (Edge e = first[x]; e != null; e = e.next) {
			int y = e.to;
			if (y == par)
				continue;
			int[] res = dfs2(y, x);
			ans[1] = Math.max(ans[1], res[1]);
			if (res[0] > best1) {
				best2 = best1;
				best1 = res[0];
			} else if (res[0] > best2)
				best2 = res[0];
			v++;
		}
		ans[0] = best1 + 1;
		ans[1] = Math.max(ans[1], best1 + best2 + 1);
		return ans;
	}

	int getParent(int x) {
		int y = x;
		while (x != parent[x])
			x = parent[x];
		while (y != x) {
			int z = parent[y];
			parent[y] = x;
			y = z;
		}
		return x;
	}

	void join(int x, int y) {
		x = getParent(x);
		y = getParent(y);
		if (x == y)
			return;
		if (rank[x] < rank[y])
			parent[x] = y;
		else {
			parent[y] = x;
			if (rank[x] == rank[y])
				rank[x]++;
		}
	}

	class Edge {
		int from, to;
		Edge next;

		public Edge(int from, int to) {
			this.from = from;
			this.to = to;
		}

		void add() {
			next = first[from];
			first[from] = this;
		}

		public boolean equals(Object o) {
			Edge e = (Edge) o;
			if (e == null)
				return false;
			return from == e.from && to == e.to;
		}

		public int hashCode() {
			return from * 239 + to;
		}
	}

	public void run() {
		try {
			in = new BufferedReader(new InputStreamReader(System.in));
			out = new BufferedWriter(new OutputStreamWriter(System.out));
			// in = new BufferedReader(new FileReader(filename+".in"));
			// out = new BufferedWriter(new FileWriter(filename+".out"));
			solve();
			out.flush();
		} catch (Exception e) {
			e.printStackTrace();
			System.exit(1);
		}
	}

	public int iread() throws Exception {
		return Integer.parseInt(readword());
	}

	public double dread() throws Exception {
		return Double.parseDouble(readword());
	}

	public long lread() throws Exception {
		return Long.parseLong(readword());
	}

	BufferedReader in;

	BufferedWriter out;

	public String readword() throws IOException {
		StringBuilder b = new StringBuilder();
		int c;
		c = in.read();
		while (c >= 0 && c <= ' ')
			c = in.read();
		if (c < 0)
			return "";
		while (c > ' ') {
			b.append((char) c);
			c = in.read();
		}
		return b.toString();
	}

	public static void main(String[] args) {
		try {
			Locale.setDefault(Locale.US);
		} catch (Exception e) {

		}
		// new Thread(new Main()).start();
		new Thread(null, new Main(), "1", 1 << 25).start();
	}
}