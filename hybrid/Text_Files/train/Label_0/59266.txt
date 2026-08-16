import java.io.*;
import java.util.*;

public class Mainn {

	public static class InputReader {
		public BufferedReader reader;
		public StringTokenizer tokenizer;

		public InputReader() {
			reader = new BufferedReader(new InputStreamReader(System.in), 32768);
			tokenizer = null;
		}

		public InputReader(InputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream), 32768);
			tokenizer = null;
		}

		public String next() {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(reader.readLine());
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return tokenizer.nextToken();
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

		public int[] nextIntArr(int n) {
			int[] arr = new int[n];
			for (int i = 0; i < n; i++) {
				arr[i] = this.nextInt();
			}
			return arr;
		}

		public int[][] next2DIntArr(int n, int m) {
			int[][] arr = new int[n][m];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					arr[i][j] = this.nextInt();
				}
			}
			return arr;
		}

		public int[] nextSortedIntArr(int n) {
			int[] arr = new int[n];
			for (int i = 0; i < n; i++) {
				arr[i] = this.nextInt();
			}
			Arrays.sort(arr);
			return arr;
		}

		public long[] nextLongArr(int n) {
			long[] arr = new long[n];
			for (int i = 0; i < n; i++) {
				arr[i] = this.nextLong();
			}
			return arr;
		}

		public char[] nextCharArr(int n) {
			char[] arr = new char[n];
			for (int i = 0; i < n; i++) {
				arr[i] = this.nextChar();
			}
			return arr;
		}
	}

	public static InputReader scn = new InputReader();
	public static PrintWriter out = new PrintWriter(System.out);

	public static int[] stair, lift;

	public static void main(String[] args) {
		// InputStream inputStream = System.in; // Useful when taking input other than
		// console eg file handling // check ctor of inputReader
		// To print in file use this:- out = new PrintWriter("destination of file
		// including extension");

		int n = scn.nextInt(), m = scn.nextInt(), s = scn.nextInt(), l = scn.nextInt(), v = scn.nextInt();
		stair = scn.nextIntArr(s);
		lift = scn.nextIntArr(l);

		int z = 0;
		if (s == 0) {
			z = -1;
		} else if (l == 0) {
			z = 1;
		}

		int q = scn.nextInt();
		while (q-- > 0) {
			int a = scn.nextInt(), b = scn.nextInt(), x = scn.nextInt(), y = scn.nextInt();
			if(a == x) {
				out.println(Math.abs(b - y));
				continue;
			}
			long u1, u2;
			if (z == 0) {
				u1 = calc(a, b, x, y, n, m, v);
				u2 = calc(x, y, a, b, n, m, v);
			} else if(z == -1) {
				u1 = calcL(a, b, x, y, n, m, v);
				u2 = calcL(x, y, a, b, n, m, v);
			} else {
				u1 = calcS(a, b, x, y, n, m, v);
				u2 = calcS(x, y, a, b, n, m, v);
			}
			out.println(Math.min(u1, u2));
		}
		out.close();
	}

	public static long calcS(int a, int b, int x, int y, int n, int m, int v) {
		int s = -Arrays.binarySearch(stair, b);

		if (s == stair.length + 1) {
			s--;
		}

		long ss = 100000000;
		
		if (s - 2 >= 0) {
			long s1 = cs(a, b, x, y, n, m, v, s - 1);
			long s2 = cs(a, b, x, y, n, m, v, s - 2);
			ss = Math.min(s1, s2);
		} else {
			ss = cs(a, b, x, y, n, m, v, s - 1);
		}

		return ss;
	}

	public static long calcL(int a, int b, int x, int y, int n, int m, int v) {
		int l = -Arrays.binarySearch(lift, b);

		if (l == lift.length + 1) {
			l--;
		}

		long ll = 100000000;
		
		if (l - 2 >= 0) {
			long l1 = cl(a, b, x, y, n, m, v, l - 1);
			long l2 = cl(a, b, x, y, n, m, v, l - 2);
			ll = Math.min(l1, l2);
		} else {
			ll = cl(a, b, x, y, n, m, v, l - 1);
		}
		
		return ll;
	}

	public static long calc(int a, int b, int x, int y, int n, int m, int v) {
		int s = -Arrays.binarySearch(stair, b);
		int l = -Arrays.binarySearch(lift, b);

		if (s == stair.length + 1) {
			s--;
		}

		if (l == lift.length + 1) {
			l--;
		}
		
		long ss = 100000000, ll = 100000000;
		
		if (s - 2 >= 0) {
			long s1 = cs(a, b, x, y, n, m, v, s - 1);
			long s2 = cs(a, b, x, y, n, m, v, s - 2);
			ss = Math.min(s1, s2);
		} else {
			ss = cs(a, b, x, y, n, m, v, s - 1);
		}

		if (l - 2 >= 0) {
			long l1 = cl(a, b, x, y, n, m, v, l - 1);
			long l2 = cl(a, b, x, y, n, m, v, l - 2);
			ll = Math.min(l1, l2);
		} else {
			ll = cl(a, b, x, y, n, m, v, l - 1);
		}

		return Math.min(ss, ll);
	}
	
	public static long cs(int a, int b, int x, int y, int n, int m, int v, int s) {
		return Math.abs(b - stair[s]) + Math.abs(y - stair[s]) + Math.abs(a - x);
	}
	
	public static long cl(int a, int b, int x, int y, int n, int m, int v, int l) {
		return Math.abs(b - lift[l]) + Math.abs(y - lift[l]) + f(Math.abs(a - x), v);
	}

	public static int f(int a, int b) {
		if (a % b == 0) {
			return a / b;
		} else {
			return a / b + 1;
		}
	}
}