import static java.lang.Math.*;
import static java.math.BigInteger.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

import java.io.*;
import java.lang.reflect.*;
//import java.util.*;

public class B {

	final int INF = (int) 1e5;
	
	//@SuppressWarnings("unused")
	public B () {
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		if (M == 3) {
			if (N >= 5)
				exit(-1);
			
			int [][] res = { { 0, 0 }, { 3, 0 }, { 0, 3 }, { 1, 1 } };
			//for (int i : rep(N))
			for (int i = 0; i < N; ++i)
				print(res[i]);
			exit();
		}
		
		int A = ceil(M-4, 2), D = floor(M-4, 2);
		int B = floor(N-M, 2), C = ceil(N-M, 2);
		
		int [][] P = { { 0, 0 }, { 0, INF }, { INF, INF }, { INF, 0 } };
		for (int [] p : P)
			print(p);

		int t, x, y;
		
		t = A+4; x = 1; y = INF;
		for (int i = 0; i < A; ++i) {
		//for (int i : rep(A)) {
			y += t;
			print(x, y);
			x += 4; --t;
		}
			
		t = B+4; x = 2; y = INF;
		for (int i = 0; i < B; ++i) {
		//for (int i : rep(B)) {
			y -= t;
			if (i == B-1)
				while (x + y <= INF) 
					x += 4;
			print(x, y);
			x += 4; --t;
		}
		
		t = C+4; x = 3; y = 0;
		for (int i = 0; i < C; ++i) {
		//for (int i : rep(C)) {
			y += t;
			if (i == C-1)
				while (x <= y) 
					x += 4;
			print(x, y);
			x += 4; --t;
		}
		
		t = D+4; x = 4; y = 0;
		for (int i = 0; i < D; ++i) {
		//for (int i : rep(D)) {
			y -= t;
			print(x, y);
			x += 4; --t;
		}
	}

	int floor (int p, int q) {
		return p / q;
	}
	
	int ceil (int p, int q) {
		return (p + q - 1) / q;
	}
	
	////////////////////////////////////////////////////////////////////////////////////

//	static Iterable<Integer> rep(final int S, final int T) {
//		return new Iterable<Integer>() {
//			public Iterator<Integer> iterator() { 
//				return new Iterator<Integer>() {
//					int i = S;
//					public void remove() { throw new UnsupportedOperationException(); }
//					public Integer next() { return i++; } 
//					public boolean hasNext() { return i < T; }
//				};
//			}
//		};
//	}
//	
//	static Iterable<Integer> rep(int N) { return rep(0, N); }
//	static Iterable<Integer> req(int S, int T) { return rep(S, T+1); }	
	
	////////////////////////////////////////////////////////////////////////////////////

	/* Dear hacker, don't bother reading below this line, unless you want to help me debug my I/O routines :-) */
	
	static MyScanner sc = new MyScanner();
	
	static class MyScanner {
		public String next() {
			newLine();
			return line[index++];
		}
		
		public char nextChar() {
			return next().charAt(0);
		}
				
		public int nextInt() {
			return Integer.parseInt(next());
		}
		
		public long nextLong() {
			return Long.parseLong(next());
		}
		
		public double nextDouble() {
			return Double.parseDouble(next());
		}
		
		public String nextLine() {
			line = null;
			return readLine();
		}
		
		public String [] nextStrings() {
			line = null;
			return readLine().split(" ");
		}
		
		public char [] nextChars() {
			return next().toCharArray();
		}

		public Integer [] nextInts() {
			String [] L = nextStrings();
			Integer [] res = new Integer [L.length];
			for (int i = 0; i < L.length; ++i)
				res[i] = Integer.parseInt(L[i]);
			return res;
		}	
		
		public Long [] nextLongs() {
			String [] L = nextStrings();
			Long [] res = new Long [L.length];
			for (int i = 0; i < L.length; ++i)
				res[i] = Long.parseLong(L[i]);
			return res;
		}

		public Double [] nextDoubles() {
			String [] L = nextStrings();
			Double [] res = new Double [L.length];
			for (int i = 0; i < L.length; ++i)
				res[i] = Double.parseDouble(L[i]);
			return res;
		}

		public String [] next (int N) {
			String [] res = new String [N];
			for (int i = 0; i < N; ++i)
				res[i] = sc.next();
			return res;
		}
		
		public Integer [] nextInt (int N) {
			Integer [] res = new Integer [N];
			for (int i = 0; i < N; ++i)
				res[i] = sc.nextInt();
			return res;
		}		
		
		public Long [] nextLong (int N) {
			Long [] res = new Long [N];
			for (int i = 0; i < N; ++i)
				res[i] = sc.nextLong();
			return res;
		}		
		
		public Double [] nextDouble (int N) {
			Double [] res = new Double [N];
			for (int i = 0; i < N; ++i)
				res[i] = sc.nextDouble();
			return res;
		}		
		
		public String [][] nextStrings (int N) {
			String [][] res = new String [N][];
			for (int i = 0; i < N; ++i)
				res[i] = sc.nextStrings();
			return res;
		}
		
		public Integer [][] nextInts (int N) {
			Integer [][] res = new Integer [N][];
			for (int i = 0; i < N; ++i)
				res[i] = sc.nextInts();
			return res;
		}
		
		public Long [][] nextLongs (int N) {
			Long [][] res = new Long [N][];
			for (int i = 0; i < N; ++i)
				res[i] = sc.nextLongs();
			return res;
		}
		
		public Double [][] nextDoubles (int N) {
			Double [][] res = new Double [N][];
			for (int i = 0; i < N; ++i)
				res[i] = sc.nextDoubles();
			return res;
		}
		
		//////////////////////////////////////////////
		
		private boolean eol() {
			return index == line.length;
		}

		private String readLine() {
			try {
				return r.readLine();
			} catch (Exception e) {
				throw new Error(e);
			}
		}
		private final BufferedReader r;

		MyScanner () {
			this(new BufferedReader(new InputStreamReader(System.in)));
		}
		
		MyScanner(BufferedReader r) {
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
	
	static void print(Object o, Object... a) {
		printDelim(" ", o, a);
	}
	
	static void cprint(Object o, Object... a) {
		printDelim("", o, a);
	}
	
	static void printDelim (String delim, Object o, Object... a) {
		pw.println(build(delim, o, a));
	}

	static void exit (Object o, Object... a) {
		print(o, a);
		exit();
	}

	static void exit () {
		pw.close();
		System.out.flush();
		System.err.println("------------------");
		System.err.println("Time: " + ((millis() - t) / 1000.0));
		System.exit(0);
	}
	
	void NO() {
		throw new Error("NO!");
	}
	
	////////////////////////////////////////////////////////////////////////////////////
	
	static String build(String delim, Object o, Object... a) {
		StringBuilder b = new StringBuilder();
		append(b, o, delim);
		for (Object p : a)
			append(b, p, delim);
		return b.toString().trim();		
	}
	
	static void append(StringBuilder b, Object o, String delim) {
		if (o.getClass().isArray()) {
			int L = Array.getLength(o);
			for (int i = 0; i < L; ++i)
				append(b, Array.get(o, i), delim);
		} else if (o instanceof Iterable<?>) {
			for (Object p : (Iterable<?>)o)
				append(b, p, delim);
		} else
			b.append(delim).append(o);		
	}

	////////////////////////////////////////////////////////////////////////////////////
	
	static void statics() {
		abs(0);
		valueOf(0);
		sort((int[])null);
		reverseOrder();
	}
	
	public static void main(String[] args) {
		new B();
		exit();
	}

	static void start() {
		t = millis();
	}

	static PrintWriter pw = new PrintWriter(System.out);
	
	static long t;
	
	static long millis() {
		return System.currentTimeMillis();
	}	
}
