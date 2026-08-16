import static java.lang.Math.*;

import java.io.*;
import java.lang.reflect.*;
import java.util.*;

public class E {

	final int MOD = (int)1e9 + 7;
	final double eps = 1e-12;
	final int INF = (int)1e9;
	
	public E () {
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		char [][] G = new char [N][];
		for (int i = 0; i < N; ++i)
			G[i] = sc.nextChars();
		
		long res = 0;
		int x = 0, y = 0, j = 1;
		
		while (x < N-1) {
			int [] D = { -1, 1 }, E = { 0, M-1 }, T = { -1, M };
			boolean ok = false;
			
			for (int i = 0, z; i < 2; ++i) {
				for (z = y; z != T[i] && G[x][z] != '#'; z += D[i]); E[i] = z - D[i];
				for (z = y; z != T[i] && G[x+1][z] != '.'; z += D[i]); T[i] = z;
				ok = ok || (D[i] * (E[i] - T[i]) >= 0);
				T[i] = D[i] * min(D[i]*T[i], D[i]*E[i]);
			}
			
			if (!ok)
				exit("Never");
			
			List<Integer> LB = new LinkedList<Integer>();
			for (int z = T[0]; z <= T[1]; ++z)
				if (G[x][z] == '+')
					LB.add(z);
			
			int [] U = new int [2], Z = { -1, LB.size() };
			Integer [] B = LB.toArray(new Integer [Z[1]]);
			for (U[0] = -1; U[0] < Z[1] - 1 && B[U[0]+1] < y; ++U[0]); U[1] = U[0]+1;
			
			for (int w = x; w == x; j = 1-j) {
				if (U[j] == Z[j]) {
					res += D[j] * (T[j] - y) + 1; y = T[j];
					if (G[x+1][y] == '.') { ++x; j = 1-j; }
				}
				else { res += D[j] * (B[U[j]] - y); y = B[U[j]] - D[j]; U[j] += D[j]; }
			}
		}
		
		exit(res);
	}
	
	////////////////////////////////////////////////////////////////////////////////////
	
	static MyScanner sc;
	
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
	
	static void print (Object... a) {
		pw.println(build(a));
	}

	static void exit (Object... a) {
		print(a);
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
	
	static String build(Object... a) {
		StringBuilder b = new StringBuilder();
		for (Object o : a)
			append(b, o);
		return b.toString().trim();		
	}
	
	static void append(StringBuilder b, Object o) {
		if (o.getClass().isArray()) {
			int L = Array.getLength(o);
			for (int i = 0; i < L; ++i)
				append(b, Array.get(o, i));
		} else if (o instanceof Iterable<?>) {
			for (Object p : (Iterable<?>)o)
				append(b, p);
		} else
			b.append(" ").append(o);		
	}
	
	////////////////////////////////////////////////////////////////////////////////////
	
	public static void main(String[] args) {
		sc = new MyScanner ();
		new E();
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
