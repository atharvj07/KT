import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class D {

	final int MOD = 1000000007;
	final double eps = 1e-12;

	public D () throws IOException {
		char [] S = sc.nextChars();
		char [] T = sc.nextChars();
		
		start();
		
		int [] C = new int [200];
		for (char s : S)
			++C[s];

		
		int N = Math.min(S.length, T.length);
		out: for (int n = N; n >= 0; --n) {
			int [] Q = Arrays.copyOf(C, 200);
			char [] D = new char [S.length];
			for (int i = 0; i < n; ++i) {
				char z = T[i];
				if (Q[z] > 0) {
					--Q[z];
					D[i] = z;
				} else
					continue out;
			}
			
			boolean good = false;
			if (n == T.length) {
				if (S.length > n) good = true;
				else continue out;
			}

			if (n < T.length) {
				int y = T[n];
				for (int x = (y+1); x < 200; ++x)
					if (Q[x] > 0) {
						--Q[x];
						D[n] = (char)x;
						good = true;
						break;
					}
				if (!good) continue out;
				++n;
			}
			
			for (int i = n, j = 0; i < S.length; ++i) {
				while (Q[j] == 0) ++j;
				D[i] = (char)j; --Q[j];
			}
			
			exit(new String(D));
				
		}
		exit(-1);
	}

	////////////////////////////////////////////////////////////////////////////////////
	
	static MyScanner sc;
	
	static void print (Object... a) {
		StringBuffer b = new StringBuffer();
		for (Object o : a)
			b.append(" ").append(o);
		System.out.println(b.toString().trim());
	}

	static void exit (Object... a) {
		print(a);
		System.out.flush();
		exit();
	}

	static void exit () {
		System.err.println("------------------");
		System.err.println("Time: " + (millis() - t) / 1000.0);
		System.exit(0);
	}
	
	static class MyScanner {
		String next() throws IOException {
			newLine();
			return line[index++];
		}
		
		char [] nextChars() throws IOException {
			return next().toCharArray();
		}
		
		double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}
		
		int nextInt() throws IOException {
			return Integer.parseInt(next());
		}
		
		long nextLong() throws IOException {
			return Long.parseLong(next());
		}
		
		String nextLine() throws IOException {
			line = null;
			return r.readLine();
		}
		
		String [] nextStrings() throws IOException {
			line = null;
			return r.readLine().split(" ");
		}
		
		int [] nextInts() throws IOException {
			String [] L = nextStrings();
			int [] res = new int [L.length];
			for (int i = 0; i < L.length; ++i)
				res[i] = Integer.parseInt(L[i]);
			return res;
		}
		
		long [] nextLongs() throws IOException {
			String [] L = nextStrings();
			long [] res = new long [L.length];
			for (int i = 0; i < L.length; ++i)
				res[i] = Long.parseLong(L[i]);
			return res;
		}

		boolean eol() {
			return index == line.length;
		}

		//////////////////////////////////////////////
		
		private final BufferedReader r;

		MyScanner () throws IOException {
			this(new BufferedReader(new InputStreamReader(System.in)));
		}
		
		MyScanner(BufferedReader r) throws IOException { 
			this.r = r;
		}
		
		private String [] line;
		private int index;

		private void newLine() throws IOException {
			if (line == null || eol()) {
				line = r.readLine().split(" ");
				index = 0;
			}
		}		
	}
	
	////////////////////////////////////////////////////////////////////////////////////
	
	public static void main(String[] args) throws IOException {
		run();
		exit();
	}

	static void start() {
		t = millis();
	}

	static void run () throws IOException {
		sc = new MyScanner ();
		new D();
	}

	static long t;
	
	static long millis() {
		return System.currentTimeMillis();
	}	
}
