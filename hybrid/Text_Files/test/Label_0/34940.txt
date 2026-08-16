
import java.awt.Point;
import java.io.*;
import java.util.*;

public class Main {
	FastScanner in = new FastScanner(System.in);
	PrintWriter out = new PrintWriter(System.out);
	
	int CENTER = 20;
	public void run() {
		while (true) {
			int r = in.nextInt(), n = in.nextInt();
			if (r == 0) break;
			
			int[] height = new int[CENTER*2+1];
			
			for (int i = 0; i < n; i++) {
				int xl = in.nextInt(), xr = in.nextInt(), h = in.nextInt();
				for (int j = CENTER + xl; j < CENTER + xr; j++) {
					height[j] = Math.max(height[j], h);
				}
			}
			
			ArrayList<Point> plist = new ArrayList<Point>();
			int prev = 0;
			for (int i = 0; i < height.length; i++) {
				if (prev != height[i]) {
					plist.add(new Point(i-CENTER, height[i]));
					plist.add(new Point(i-CENTER, prev));
				} else if (i == CENTER) {
					plist.add(new Point(0, height[i]));
				}
				prev = height[i];
			}
			
			for (double t = 0; t <= 40; t += 0.0001) {
				double y = -r + t;
				boolean ok = true;
				for (Point pt : plist) {
					double dx = pt.x, dy = pt.y - y;
					if (dx * dx + dy * dy < r * r) ok = false; 
				}
				
				if (!ok) {
					System.out.println(t-0.0001);
					break;
				}
			}
			plist.clear();
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