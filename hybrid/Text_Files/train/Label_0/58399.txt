import static java.lang.Math.*;

import java.util.*;
import java.util.stream.*;

public class A2 {

	int N, M = 2000; int [][][] G;
	int [] H, L;
	HashMap<Long, Integer> res = new HashMap<>();

	public Object solve () {
		N = sc.nextInt();
		int [][] E = dec(sc.nextInts(N-1), 2);

		G = wgraph(N, E);
		for (int i : rep(N))
			if (G[0][i].length == 2)
				return "NO";

		H = new int [N]; L = new int [N];
		for (int i : rep(N))
			if (G[0][i].length == 1) {
				dfs(i, -1, 0);
				break;
			}

		print("YES");
		print(res.size());
		for (long key : res.keySet()) {
			long x = key / M, y = key % M;
			print(x+1, y+1, res.get(key));
		}
		return null;
	}

	void dfs (int s, int p, int v) {
		int W = 0;
		for (int m : rep(G[0][s].length)) {
			int j = G[0][s][m], w = G[1][s][m];
			if (j != p) {
				dfs(j, s, w);
				L[s] = L[j];
				W += w;
			}
		}

		if (p == -1) {
			H[s] = G[1][s][0];
			for (int i : rep(N))
				if (i != s)
					addEdge(s, i, H[i]);
			for (int i : rep(N))
				assert H[i] == 0;
			return;

		}

		if (G[0][s].length == 1) {
			H[s] = v; L[s] = s;
			return;
		}

		if (W != v) {
			int n = 0;
			while (G[0][s][n] == p) ++n;
			int j = G[0][s][n++];
			while (G[0][s][n] == p) ++n;
			int k = G[0][s][n++];
			addEdge(L[j], L[k], (W - v) / 2);
		}
	}

	void addEdge(int j, int k, int v) {
		if (v == 0)
			return;
		int x = min(j, k), y = max(j, k);
		long key = M * x + y;
		int w = res.getOrDefault(key, 0) + v;
		res.remove(key);
		if (w != 0)
			res.put(key, w);
		H[j] -= v; H[k] -= v;
	}

	private static final int CONTEST_TYPE = 1;

	private static void init () {
	}

	private static int [][] dec (int [][] E, int N) { for (int [] e : E) for (int i = 0; i < e.length && i < N; ++i) --e[i]; return E; }
	private static int [][] dup (int [][] E) {
		int [][] res = new int [2*E.length][];
		for (int i = 0; i < E.length; ++i) {
			res[2*i] = E[i].clone();
			res[2*i+1] = E[i].clone();
			res[2*i+1][0] = E[i][1]; res[2*i+1][1] = E[i][0];
		}
		return res;
	}
	private static int [][][] dwgraph (int N, int [][] E) {
		int [] D = new int [N];
		for (int [] e : E)
			++D[e[0]];
		int [][][] res = new int [2][N][];
		for (int i = 0; i < 2; ++i)
			for (int j = 0; j < N; ++j)
				res[i][j] = new int [D[j]];
		D = new int [N];
		for (int [] e : E) {
			int x = e[0], y = e[1], z = e.length > 2 ? e[2] : 1;
			res[0][x][D[x]] = y;
			res[1][x][D[x]] = z;
			++D[x];
		}
		return res;
	}
	private static int [] rep (int N) { return rep(0, N); }
	private static int [] rep (int S, int T) { if (S >= T) return new int [0]; int [] res = new int [T-S]; for (int i = S; i < T; ++i) res[i-S] = i; return res; }
	private static int [][][] wgraph (int N, int [][] E) { return dwgraph(N, dup(E)); }
	//////////////////////////////////////////////////////////////////////////////////// OFF
	private static IOUtils.MyScanner sc = new IOUtils.MyScanner();
	private static Object print (Object o, Object ... A) { IOUtils.print(o, A); return null; }
	private static class IOUtils {
		public static class MyScanner {
			public String next () { newLine(); return line[index++]; }
			public int nextInt () { return Integer.parseInt(next()); }
			public String nextLine () { line = null; return readLine(); }
			public String [] nextStrings () { return split(nextLine()); }
			public int[] nextInts () { return nextStream().mapToInt(Integer::parseInt).toArray(); }
			public int[][] nextInts (int N) { return IntStream.range(0, N).mapToObj(i -> nextInts()).toArray(int[][]::new); }
			//////////////////////////////////////////////
			private boolean eol () { return index == line.length; }
			private String readLine () {
				try {
					return r.readLine();
				} catch (Exception e) {
					throw new Error (e);
				}
			}
			private final java.io.BufferedReader r;
			private MyScanner () { this(new java.io.BufferedReader(new java.io.InputStreamReader(System.in))); }
			private MyScanner (java.io.BufferedReader r) {
				try {
					this.r = r;
					while (!r.ready())
						Thread.sleep(1);
					start();
				} catch (Exception e) {
					throw new Error(e);
				}
			}
			private String [] line;
			private int index;
			private void newLine () {
				if (line == null || eol()) {
					line = split(readLine());
					index = 0;
				}
			}
			private java.util.stream.Stream<String> nextStream () { return java.util.Arrays.stream(nextStrings()); }
			private String [] split (String s) { return s.length() > 0 ? s.split(" ") : new String [0]; }
		}
		private static String build (Object o, Object ... A) { return buildDelim(" ", o, A); }
		private static String buildDelim (String delim, Object o, Object ... A) {
			StringBuilder b = new StringBuilder();
			append(b, o, delim);
			for (Object p : A)
				append(b, p, delim);
			return b.substring(delim.length());
		}
		//////////////////////////////////////////////////////////////////////////////////
		private static final java.text.DecimalFormat formatter = new java.text.DecimalFormat("#.#########");
		private static void start () { if (t == 0) t = millis(); }
		private static void append (java.util.function.Consumer<Object> f, java.util.function.Consumer<Object> g, final Object o) {
			if (o.getClass().isArray()) {
				int len = java.lang.reflect.Array.getLength(o);
				for (int i = 0; i < len; ++i)
					f.accept(java.lang.reflect.Array.get(o, i));
			}
			else if (o instanceof Iterable<?>)
				((Iterable<?>)o).forEach(f::accept);
			else
				g.accept(o instanceof Double ? formatter.format(o) : o);
		}
		private static void append (final StringBuilder b, Object o, final String delim) {
			append(x -> { append(b, x, delim); }, x -> b.append(delim).append(x), o);
		}
		private static java.io.PrintWriter pw = new java.io.PrintWriter(System.out);
		private static void print (Object o, Object ... A) {
			String res = build(o, A);
			if (DEBUG == 2)
				err(res, '(', time(), ')');
			pw.println(res);
			if (DEBUG == 1) {
				pw.flush();
				System.out.flush();
			}
		}
		private static void err (Object o, Object ... A) { System.err.println(build(o, A)); }
		private static int DEBUG;
		private static void exit () {
			String end = "------------------" + System.lineSeparator() + time();
			switch(DEBUG) {
			case 1: print(end); break;
			case 2: err(end); break;
			}
			IOUtils.pw.close();
			System.out.flush();
			System.exit(0);
		}
		private static long t;
		private static long millis () { return System.currentTimeMillis(); }
		private static String time () { return "Time: " + (millis() - t) / 1000.0; }
		private static void run (int N) {
			try { DEBUG = Integer.parseInt(System.getProperties().get("DEBUG").toString()); }
			catch (Throwable t) {}

			for (int n = 1; n <= N; ++n) {
				Object res = new A2().solve();
				if (res != null) {
					@SuppressWarnings("all")
					Object o = CONTEST_TYPE == 0 ? "Case #" + n + ": " + build(res) : res;
					print(o);
				}
			}
			exit();
		}
	}
	////////////////////////////////////////////////////////////////////////////////////
	public static void main (String[] args) {
		init();
		@SuppressWarnings("all")
		int N = CONTEST_TYPE == 1 ? 1 : sc.nextInt();
		IOUtils.run(N);
	}
}
