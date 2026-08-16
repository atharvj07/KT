
import java.awt.Point;
import java.io.*;
import java.util.*;

public class Main {
	FastScanner in = new FastScanner(System.in);
	PrintWriter out = new PrintWriter(System.out);

	public void run() {
		int n = in.nextInt(), u = in.nextInt(), v = in.nextInt(), m = in.nextInt();
		
		HashMap<Integer, Point> rabbit = new HashMap<Integer, Point>();
		HashMap<Integer, Point> cat = new HashMap<Integer, Point>();

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				int val = in.nextInt();
				rabbit.put(val, new Point(j, i));
			}
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				int val = in.nextInt();
				cat.put(val, new Point(j, i));
			}
		}
		
		int[] rowRsum = new int[n];
		int[] rowCsum = new int[n];
		int[] colRsum = new int[n];
		int[] colCsum = new int[n];
		
		int rightDiagRsum = 0;
		int leftDiagRsum = 0;
		int rightDiagCsum = 0;
		int leftDiagCsum = 0;
		
		int rabbitCnt = 0, catCnt = 0;
		for (int i = 0; i < m; i++) {
			int next = in.nextInt();
			if (rabbit.containsKey(next)) {
				Point p = rabbit.get(next);
				
				rowRsum[p.x]++;
				colRsum[p.y]++;
				if (p.x == p.y) rightDiagRsum++;			
				if (p.x + p.y + 1 == n) leftDiagRsum++;
		
				if (rowRsum[p.x] == n) { rabbitCnt++; rowRsum[p.x] = -1; }
				if (colRsum[p.y] == n && n != 1) { rabbitCnt++; colRsum[p.y] = -1; }
				if (rightDiagRsum == n && n != 1) { rabbitCnt++; rightDiagRsum = -1; }
				if (leftDiagRsum == n && n != 1) { rabbitCnt++; leftDiagRsum = -1; }
			}
			
			if (cat.containsKey(next)) {
				Point p = cat.get(next);
				
				rowCsum[p.x]++;
				colCsum[p.y]++;
				if (p.x == p.y) rightDiagCsum++;			
				if (p.x + p.y + 1 == n) leftDiagCsum++;
		
				if (rowCsum[p.x] == n) { catCnt++; rowCsum[p.x] = -1; }
				if (colCsum[p.y] == n && n != 1) { catCnt++; colCsum[p.y] = -1; }
				if (rightDiagCsum == n && n != 1) { catCnt++; rightDiagCsum = -1; }
				if (leftDiagCsum == n && n != 1) { catCnt++; leftDiagCsum = -1; }
			}
			
			if (rabbitCnt >= u && catCnt >= v) {
				System.out.println("DRAW");
				return;
			} else if (rabbitCnt >= u) {
				System.out.println("USAGI");
				return;
			} else if (catCnt >= v) {
				System.out.println("NEKO");
				return;
			}
		}
		
		System.out.println("DRAW");
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

		int[][] nextIntMap(int n, int m) {
			int[][] map = new int[n][m];
			for (int i = 0; i < n; i++) {
				map[i] = in.nextIntArray(m);
			}
			return map;
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

		long[][] nextLongMap(int n, int m) {
			long[][] map = new long[n][m];
			for (int i = 0; i < n; i++) {
				map[i] = in.nextLongArray(m);
			}
			return map;
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

		double[][] nextDoubleMap(int n, int m) {
			double[][] map = new double[n][m];
			for (int i = 0; i < n; i++) {
				map[i] = in.nextDoubleArray(m);
			}
			return map;
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