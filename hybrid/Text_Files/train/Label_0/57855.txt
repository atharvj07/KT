import java.io.*;
import java.util.*;

public class tr1 {
	static PrintWriter out;
	static StringBuilder sb;
	static int n, m, id, max;
	static long mod = 998244353;
	static Boolean[][] memo;
	static String s;
	static int[][] ad;
	static long inf = Long.MAX_VALUE;
	static int[] color;
	static ArrayList<Integer> o;
	static char[][] g;
	static boolean[] vis, vis1;
	static boolean f;
	static int[] ar, a;

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		out = new PrintWriter(System.out);
		n = sc.nextInt();
		ar = new int[6000];
		a = sc.nextArrInt(n);
		int ans = 0;
		ad = new int[n][];
		int[] deg = new int[n];
		int[] ed = new int[n - 1];
		int[] ed1 = new int[n - 1];
		for (int i = 0; i < n - 1; i++) {
			int a = sc.nextInt() - 1;
			int c = sc.nextInt() - 1;
			deg[a]++;
			deg[c]++;
			ed[i] = a;
			ed1[i] = c;
		}
		for (int i = 0; i < n; i++)
			ad[i] = new int[deg[i]];
		for (int i = 0; i < n - 1; i++) {
			ad[ed[i]][--deg[ed[i]]] = ed1[i];
			ad[ed1[i]][--deg[ed1[i]]] = ed[i];
		}
//		dfs(0, -1);
		for (int i = 0; i < n; i++) {
			id = 0;
			max = 0;
			dfs(i, -1);
			// System.out.println(max + " " + i);
			ans = Math.max(ans, max);
		}
		System.out.println(ans);
		out.flush();
	}

	static void dfs(int u, int p) {
	//	System.out.println(u+" "+p);
		//System.out.println(Arrays.toString(ar));
		if (id == 0) {
			ar[id++] = a[u];
			max = Math.max(1, max);
			for (int v : ad[u])
				if (v != p)
					dfs(v, u);
			id--;
		} else {
			int lo = 0;
			int hi = id - 1;
			int pl = -1;
			while (lo <= hi) {
				int mid = (lo + hi) >> 1;
				if (ar[mid] >= a[u]) {
					hi = mid - 1;
					pl = mid;
				} else {
					lo = mid + 1;
				}
			}
			if (pl == -1) {
				ar[id++] = a[u];
				max = Math.max(max, id);
				for (int v : ad[u])
					if (v != p)
						dfs(v, u);
				id--;
			} else {
				int val = ar[pl];
				ar[pl] = a[u];
				for (int v : ad[u])
					if (v != p)
						dfs(v, u);
				ar[pl] = val;
			}
		}
	}

	static class Scanner {
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream system) {
			br = new BufferedReader(new InputStreamReader(system));
		}

		public Scanner(String file) throws Exception {
			br = new BufferedReader(new FileReader(file));
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public String nextLine() throws IOException {
			return br.readLine();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		public char nextChar() throws IOException {
			return next().charAt(0);
		}

		public Long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public int[] nextArrInt(int n) throws IOException {
			int[] a = new int[n];
			for (int i = 0; i < n; i++)
				a[i] = nextInt();
			return a;
		}

		public long[] nextArrLong(int n) throws IOException {
			long[] a = new long[n];
			for (int i = 0; i < n; i++)
				a[i] = nextLong();
			return a;
		}

		public boolean ready() throws IOException {
			return br.ready();
		}

		public void waitForInput() throws InterruptedException {
			Thread.sleep(3000);
		}
	}
}