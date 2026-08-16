import java.io.*;
import java.util.*;

public class CF_635_Div2 {

	static class Reader {

		private InputStream mIs;
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;

		public Reader() {
			this(System.in);
		}

		public Reader(InputStream is) {
			mIs = is;
		}

		public int read() {
			if (numChars == -1) {
				throw new InputMismatchException();

			}
			if (curChar >= numChars) {
				curChar = 0;
				try {
					numChars = mIs.read(buf);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (numChars <= 0) {
					return -1;
				}
			}
			return buf[curChar++];
		}

		public String nextLine() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isEndOfLine(c));
			return res.toString();
		}

		public String next() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isSpaceChar(c));
			return res.toString();
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}

		public long nextLong() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			long res = 0;
			do {
				if (c < '0' || c > '9') {
					throw new InputMismatchException();
				}
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public int nextInt() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			int res = 0;
			do {
				if (c < '0' || c > '9') {
					throw new InputMismatchException();
				}
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public int[] intArray(int n) {
			Reader r = new Reader();
			int arr[] = new int[n];
			for (int i = 0; i < n; i++) {
				arr[i] = r.nextInt();
			}
			return arr;
		}

		public long[] longArray(int n) {
			Reader r = new Reader();
			long arr[] = new long[n];
			for (int i = 0; i < n; i++) {
				arr[i] = r.nextInt();
			}
			return arr;
		}

		public void printArray(int arr[]) {
			PrintWriter out = new PrintWriter(System.out);
			for (int i = 0; i < arr.length; i++) {
				if (i == arr.length - 1)
					out.println(arr[i]);
				else
					out.print(arr[i] + " ");
			}
			out.close();
		}

		public boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		public boolean isEndOfLine(int c) {
			return c == '\n' || c == '\r' || c == -1;
		}
	}

	static Reader r = new Reader();

	private static void solve1() {

		int t = r.nextInt();
		StringBuilder res = new StringBuilder();

		while (t-- > 0) {

			int a = r.nextInt();
			int b = r.nextInt();
			int c = r.nextInt();
			int d = r.nextInt();

			String ans = "" + b + " " + c + " " + c;

			res.append(ans).append("\n");
		}

		System.out.print(res);

	}

	private static void solve2() {

		int t = r.nextInt();
		StringBuilder res = new StringBuilder();

		while (t-- > 0) {

			int x = r.nextInt();
			int n = r.nextInt();
			int m = r.nextInt();

			int first = n;
			int second = m;

			while ((first > 0 || second > 0)) {
				if (x > 20) {
					if (first > 0) {
						x = ((x / 2) + 10);
						first--;
					} else if (second > 0) {
						x -= 10;
						second--;
					}
				} else {
					if (second > 0) {
						x -= 10;
						second--;
					} else if (first > 0) {
						x = ((x / 2) + 10);
						first--;
					}
				}

				if (x <= 0) {
					break;
				}

			}

			res.append((x <= 0) ? "YES" : "NO").append("\n");
		}

		System.out.print(res);

	}

	static ArrayList<Integer> tree[] = new ArrayList[(int) 2e5 + 1];
	static int vis[] = new int[(int) 2e5 + 1];
	static ArrayList<Integer> happiness = new ArrayList<Integer>();

	private static int DFS(int start, int depth) {
		vis[start] = 1;
		int noOfChild = 0;
		for (Integer v : tree[start]) {
			if (vis[v] == 0)
				noOfChild += DFS(v, depth + 1);
		}
		happiness.add(depth - noOfChild);
		return noOfChild + 1;
	}

	@SuppressWarnings("unchecked")
	private static void solve3() {

		int n = r.nextInt();
		int k = r.nextInt();

		for (int i = 0; i <= n; i++) {
			tree[i] = new ArrayList<Integer>();
		}

		for (int i = 1; i < n; i++) {
			int u = r.nextInt();
			int v = r.nextInt();
			tree[u].add(v);
			tree[v].add(u);
		}

		DFS(1, 0);

		Collections.sort(happiness, Collections.reverseOrder());

		long happi = 0;
		for (int i = 0; i < k; i++)
			happi += happiness.get(i);

		System.out.println(happi);

	}

	private static void solve4() {

		int t = r.nextInt();
		StringBuilder res = new StringBuilder();

		while (t-- > 0) {

			int n = r.nextInt();

			res.append(false).append("\n");
		}

		System.out.print(res);

	}

	public static void main(String[] args) throws IOException {

//		solve1();

//		solve2();

		solve3();

//		solve4();

	}

}