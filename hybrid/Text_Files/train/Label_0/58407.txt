import java.util.*;

public class B {

	private final static boolean autoflush = false;

	public B () {
		int N = sc.nextInt();

		Integer [] T = sc.nextInts();
		Integer [] S = sc.nextInts();
		for (int i = 0; i < N; ++i)
			--S[i];

		int [] cnt = new int [N];
		for (int i = 0; i < N; ++i)
			if (S[i] >= 0)
				++cnt[S[i]];

		for (int i = 0; i < N; ++i)
			if (S[i] >= 0 && cnt[S[i]] > 1)
				S[i] = -1;

		Deque<Integer> res = new LinkedList<Integer>();
		for (int i = 0; i < N; ++i)
			if (T[i] == 1) { // Hotel!
				Deque<Integer> x = new LinkedList<Integer>();
				int j = i;
				do {
					x.addFirst(j+1);
					j = S[j];
				} while (j != -1);
				if (x.size() > res.size())
					res = x;
			}

		print(res.size());
		exit(res);
	}

	////////////////////////////////////////////////////////////////////////////////////
	private final static MyScanner sc = new MyScanner();
	private static class MyScanner {
		public String next() { newLine(); return line[index++]; }
		public int nextInt() { return Integer.parseInt(next()); }
		public String nextLine() { line = null; return readLine(); }
		public String [] nextStrings() { return nextLine().split(" "); }
		public Integer [] nextInts() {
			String [] L = nextStrings();
			Integer [] res = new Integer [L.length];
			for (int i = 0; i < L.length; ++i)
				res[i] = Integer.parseInt(L[i]);
			return res;
		}
		//////////////////////////////////////////////
		private boolean eol() { return index == line.length; }
		private String readLine() {
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
		private void newLine() {
			if (line == null || eol()) {
				line = readLine().split(" ");
				index = 0;
			}
		}
	}
	private static void print (Object o, Object... a) { printDelim(" ", o, a); }
	private static void printDelim (String delim, Object o, Object... a) { pw.println(build(delim, o, a)); }
	private static void exit (Object o, Object... a) { print(o, a); exit(); }
	private static void exit() {
		pw.close();
		System.out.flush();
		System.err.println("------------------");
		System.err.println("Time: " + ((millis() - t) / 1000.0));
		System.exit(0);
	}
	////////////////////////////////////////////////////////////////////////////////////
	private static String build (String delim, Object o, Object... a) {
		StringBuilder b = new StringBuilder();
		append(b, o, delim);
		for (Object p : a)
			append(b, p, delim);
		return b.substring(delim.length());
	}
	private static void append(StringBuilder b, Object o, String delim) {
		if (o.getClass().isArray()) {
			int L = java.lang.reflect.Array.getLength(o);
			for (int i = 0; i < L; ++i)
				append(b, java.lang.reflect.Array.get(o, i), delim);
		} else if (o instanceof Iterable<?>)
			for (Object p : (Iterable<?>)o)
				append(b, p, delim);
		else
			b.append(delim).append(o);
	}
	////////////////////////////////////////////////////////////////////////////////////
	private static void start() { t = millis(); }
	private static java.io.PrintWriter pw = new java.io.PrintWriter(System.out, autoflush);
	private static long t;
	private static long millis() { return System.currentTimeMillis(); }
	public static void main (String[] args) { new B(); exit(); }
}
