import java.io.IOException;
import java.util.InputMismatchException;

public class C {
	long f(long x, long X, long Y, long MOD) {
		return (x * X + Y) % MOD;
	}

	long g(long x, long X, long Y, long MOD, long c) {
		long res = f(x, X, Y, MOD);
		for (int i = 0; i < c - 1; i++) {
			res = f(res, X, Y, MOD);
		}
		return res;
	}

	void run() {
		MyScanner sc = new MyScanner();

		long m = sc.nextInt();
		long h1 = sc.nextInt();
		long a1 = sc.nextInt();
		long x1 = sc.nextInt();
		long y1 = sc.nextInt();
		long h2 = sc.nextInt();
		long a2 = sc.nextInt();
		long x2 = sc.nextInt();
		long y2 = sc.nextInt();

		long time1 = 0;
		while (h1 != a1) {
			h1 = (h1 * x1 + y1) % m;
			h2 = (h2 * x2 + y2) % m;
			time1++;
			if (m + 1 < time1) {
				System.out.println(-1);
				return;
			}
		}
		if (h2 == a2) {
			System.out.println(time1);
			return;
		}
		long time2 = 1;
		h1 = (h1 * x1 + y1) % m;
		while (h1 != a1) {
			h1 = (h1 * x1 + y1) % m;
			time2++;
			if (m + 1 < time2) {
				System.out.println(-1);
				return;
			}
		}

		long time3 = 0;
		long s = 1, t = 0;
		for (int i = 0; i < time2; i++) {
			s = (s * x2) % m;
			t = (t * x2 + y2) % m;
		}
		while (h2 != a2) {
			h2 = (h2 * s + t) % m;
			time3++;
			if (m + 1 < time3) {
				System.out.println(-1);
				return;
			}
		}
		System.out.println(time1 + time2 * time3);
	}

	public static void main(String[] args) {
		new C().run();
	}

	public void mapDebug(int[][] a) {
		System.out.println("--------map display---------");
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				System.out.printf("%3d ", a[i][j]);
			}
			System.out.println();
		}
		System.out.println("----------------------------" + '\n');
	}

	class MyScanner {
		int read() {
			try {
				return System.in.read();
			} catch (IOException e) {
				throw new InputMismatchException();
			}
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
