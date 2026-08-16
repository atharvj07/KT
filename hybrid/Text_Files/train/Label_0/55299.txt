import java.util.*;
import java.io.*;

public class Kay_and_Snowflake {

	public static int n;

	public static ArrayList<ArrayList<Integer>> adj;

	public static int[] ans, id;

	public static TreeSet<Pair> dfs(int x) {

		id[x] = x;

		int size = 1;
		int max = 0;
		TreeSet<Pair> set = new TreeSet<Pair>();

		/* DFS Through Points and Generate Data */
		for (int i : adj.get(x)) {

			TreeSet<Pair> tmp = dfs(i);

			size += tmp.size();
			max = Math.max(max, tmp.size());
			set = union(set, tmp);

		}

		set.add(new Pair(x, size));

		/* Get Answer */
		if (max < (size + 1) / 2) {
			ans[x] = x;
		} else {
			ans[x] = set.ceiling(new Pair(0, (size + 1) / 2)).n;
		}

		return set;

	}

	public static TreeSet<Pair> union(TreeSet<Pair> a, TreeSet<Pair> b) {
		
		if (a.size() > b.size()) {
			a.addAll(b);
			return a;
		} else {
			b.addAll(a);
			return b;
		}
		
	}

	public static void main(String[] args) throws IOException {

		/* Read in Input */
		BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(f.readLine());

		n = Integer.parseInt(st.nextToken());
		int q = Integer.parseInt(st.nextToken());

		adj = new ArrayList<ArrayList<Integer>>();

		for (int i = 0; i <= n; i++) {
			ArrayList<Integer> tl = new ArrayList<Integer>();
			adj.add(tl);
		}

		st = new StringTokenizer(f.readLine());

		for (int i = 2; i <= n; i++) {

			int p = Integer.parseInt(st.nextToken());

			adj.get(p).add(i);

		}

		/* DFS Through Nodes to Find Centroids */
		ans = new int[n + 1];
		id = new int[n + 1];

		dfs(1);

		/* Answer Queries */
		for (int i = 0; i < q; i++) {

			st = new StringTokenizer(f.readLine());

			int v = Integer.parseInt(st.nextToken());

			System.out.println(ans[v]);

		}

		f.close();

	}

	public static class Pair implements Comparable<Pair> {

		/* Class for Storing Data */
		public int n, v;

		public Pair(int n, int v) {
			this.n = n;
			this.v = v;
		}

		/* Make Compare Operator for TreeSet Sorting */
		public int compareTo(Pair o) {
			if (v == o.v) {
				if (n == o.n) {
					return 0;
				} else {
					return n < o.n ? -1 : 1;
				}
			} else {
				return v < o.v ? -1 : 1;
			}
		}

	}

}
