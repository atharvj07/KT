
import java.io.*;
import java.util.*;

public class Main {
	FastScanner in = new FastScanner(System.in);
	PrintWriter out = new PrintWriter(System.out);

	class Ant {
		char d;
		int p;

		Ant(char d, int p) {
			this.d = d;
			this.p = p;
		}
	}
	
	public void run() {
		outer : 
		while (true) {
			int n = in.nextInt(), l = in.nextInt();
			if (n == 0) break;
			
			Ant[] ant = new Ant[n];
			for (int i = 0; i < n; i++) {
				ant[i] = new Ant(in.next().charAt(0), in.nextInt());
			}
			
			int cnt = 0;
			for (int t = 1; ; t++) {
				for (int i = 0; i < n; i++) {
					if (ant[i].p == 0 || ant[i].p == l) continue;
					
					if (ant[i].d == 'R') {
						ant[i].p++;
					} 
					
					if (ant[i].p == 0 || ant[i].p == l) {
						cnt++;
						if (cnt == n) {
							System.out.println(t + " " + (i+1));
							continue outer;
						}
					}
				}
				
				for (int i = 0; i < n; i++) {
					if (ant[i].p == 0 || ant[i].p == l) continue;
					
					if (ant[i].d == 'L') {
						ant[i].p--;
					} 
					
					if (ant[i].p == 0 || ant[i].p == l) {
						cnt++;
						if (cnt == n) {
							System.out.println(t + " " + (i+1));
							continue outer;
						}
					}
				}
				
				for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) {
					if (ant[i].p == ant[j].p) {
						char temp = ant[i].d;
						ant[i].d = ant[j].d;
						ant[j].d = temp;
					}
				}
			}
		}
		out.close();
	}

	public static void main(String[] args) {
		new Main().run();
	}

	public void mapDebug(int[][] a) {
		System.out.println("--------map display---------");

		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				System.out.printf("%3d ", a[i][j]);
			}
			System.out.println();
		}

		System.out.println("----------------------------");
		System.out.println();
	}

	public void debug(Object... obj) {
		System.out.println(Arrays.deepToString(obj));
	}

	class FastScanner {
		private InputStream stream;
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;

		public FastScanner(InputStream stream) {
			this.stream = stream;
			//stream = new FileInputStream(new File("dec.in"));

		}

		int read() {
			if (numChars == -1)
				throw new InputMismatchException();
			if (curChar >= numChars) {
				curChar = 0;
				try {
					numChars = stream.read(buf);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (numChars <= 0)
					return -1;
			}
			return buf[curChar++];
		}

		boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		boolean isEndline(int c) {
			return c == '\n' || c == '\r' || c == -1;
		}

		int nextInt() {
			return Integer.parseInt(next());
		}

		int[] nextIntArray(int n) {
			int[] array = new int[n];
			for (int i = 0; i < n; i++)
				array[i] = nextInt();

			return array;
		}

		long nextLong() {
			return Long.parseLong(next());
		}

		long[] nextLongArray(int n) {
			long[] array = new long[n];
			for (int i = 0; i < n; i++)
				array[i] = nextLong();

			return array;
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}

		double[] nextDoubleArray(int n) {
			double[] array = new double[n];
			for (int i = 0; i < n; i++)
				array[i] = nextDouble();

			return array;
		}

		String next() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isSpaceChar(c));
			return res.toString();
		}

		String[] nextStringArray(int n) {
			String[] array = new String[n];
			for (int i = 0; i < n; i++)
				array[i] = next();

			return array;
		}

		String nextLine() {
			int c = read();
			while (isEndline(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isEndline(c));
			return res.toString();
		}
	}
}