import static java.lang.Math.*;
import static java.util.Arrays.*;

public class E {

	public Object solve () {
		int N = sc.nextInt(), M = sc.nextInt();
		int [] A = dec(sc.nextInts()); B = dec(sc.nextInts());

		int [] J = invert(A);
		B = pri(permute(obj(J), B));
		C = invert(B);

		Q = 1 + (int)Math.round(sqrt(N));
		S = new Fenwick2(Q, Q);
		for (int i : rep(N))
			S.add(1, i/Q, B[i]/Q);

		for (@SuppressWarnings("unused") int i : rep(M))
			switch(sc.nextInt()) {
			case 1:
				int la = sc.nextInt() - 1, ra = sc.nextInt();
				int lb = sc.nextInt() - 1, rb = sc.nextInt();
				long res = calc(rb, ra) - calc(lb, ra) - calc(rb, la) + calc(lb, la);
				print(res);
				break;
			case 2:
				int p = sc.nextInt() - 1, q = sc.nextInt() - 1;
				int v = B[p], w = B[q];
				B[p] = w; B[q] = v;
				C[w] = p; C[v] = q;
				S.add(-1, p/Q, v/Q); S.add(1, p/Q, w/Q);
				S.add(1, q/Q, v/Q); S.add(-1, q/Q, w/Q);
				break;
			}
		return null;
	}

	long calc(int x, int y) {
		long res = S.get(x/Q, y/Q);
		int rx = Q*(x/Q), ry = Q*(y/Q);
		for (int i : rep(rx, x))
			if (B[i] < y)
				++res;
		for (int i : rep(ry, y))
			if (C[i] < rx)
				++res;
		return res;
	}

	Fenwick2 S;
	int Q;
	int [] B, C;

	private static final boolean ONE_TEST_CASE = true;

	private static void init () {
	}

	private static int [] dec(int ... A) { for (int i = 0; i < A.length; ++i) --A[i]; return A; }
	private static int [] invert (int [] J) {
		int N = J.length;
		int [] res = new int [N];
		for (int i = 0; i < N; ++i)
			res[J[i]] = i;
		return res;
	}
	private static Integer [] obj (int ... A) { return stream(A).mapToObj(x -> x).toArray(Integer[]::new); }
	private static <T> T [] permute(T [] A, int [] J) {
		T [] res = A.clone();
		for (int i = 0; i < J.length; ++i)
			res[i] = A[J[i]];
		return res;
	}
	private static int [] pri(Integer [] A) { return stream(A).mapToInt(x -> x).toArray(); }
	private static int [] rep (int N) { return rep(0, N); }
	private static int [] rep (int S, int T) { if (S >= T) return new int [0]; int [] res = new int [T-S]; for (int i = S; i < T; ++i) res[i-S] = i; return res; }
	private static class Fenwick2 {
		private final long [][] X;
		private long mod;
		public Fenwick2 (int N, int M) { this(N, M, 0); }
		public Fenwick2 (int N, int M, int mod) { X = new long [N][M]; this.mod = mod; }
		public void add(long x, int i, int j) {
			++i; ++j; assert i <= X.length && j <= X[0].length;
			while (i <= X.length) {
				int k = j;
				while (k <= X[i-1].length) {
					X[i-1][k-1] += x;
					if (mod > 0)
						X[i-1][k-1] = ((X[i-1][k-1] % mod) + mod) % mod;
					k += (k & (-k));
				}
				i += (i & (-i));
			}
		}
		public long get(int i, int j) {
			assert i <= X.length && j <= X[0].length;
			long res = 0;
			for (; i > 0; i -= (i & (-i)))
				for (int k = j; k > 0; k -= (k & (-k))) {
					res += X[i-1][k-1];
					if (mod > 0)
						res = ((res % mod) + mod) % mod;
				}
			return res;
		}
	}
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
			pw.println(build(o, A));
			if (DEBUG)
				pw.flush();
		}
		private static void err (Object o, Object ... A) { System.err.println(build(o, A)); }
		private static boolean DEBUG;
		private static void write (Object o) {
			err(o, '(', time(), ')');
			if (!DEBUG)
				pw.println(o);
		}
		private static void exit () {
			IOUtils.pw.close();
			System.out.flush();
			err("------------------");
			err(time());
			System.exit(0);
		}
		private static long t;
		private static long millis () { return System.currentTimeMillis(); }
		private static String time () { return "Time: " + (millis() - t) / 1000.0; }
		private static void run (int N) {
			try { DEBUG = System.getProperties().containsKey("DEBUG"); }
			catch (Throwable t) {}

			for (int n = 1; n <= N; ++n) {
				Object res = new E().solve();
				if (res != null)
					write("Case #" + n + ": " + build(res));
			}
			exit();
		}
	}
	////////////////////////////////////////////////////////////////////////////////////
	public static void main (String[] args) {
		init();
		int N = ONE_TEST_CASE ? 1 : sc.nextInt();
		IOUtils.run(N);
	}
}
