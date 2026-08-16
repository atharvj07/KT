import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.io.BufferedInputStream;
import java.util.concurrent.Callable;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		BufferedInputStream in = new BufferedInputStream(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskG solver = new TaskG();
		solver.solve(1, in, out);
		out.close();
	}

	static class TaskG {
		public void solve(int testNumber, BufferedInputStream _in, PrintWriter out) {

			InputReader in = new InputReader(_in);
			long startTime = System.currentTimeMillis();
			int nt = 1;
			Task t = new Task(1);
			t.readInput(in);
			t.call();
			t.writeOutput(out);
			in.close();
			System.err.println("Time: " + (System.currentTimeMillis() - startTime) + " miliseconds");
		}

	}

	static class MathUtils {
		public static void buildSumRangeMod(int[] a, int[] sum) {
			for (int i = 0; i < a.length; ++i) {
				sum[i] = a[i];
				sum[i] = Mod.addMod(sum[i], i > 0 ? sum[i - 1] : 0);
			}
		}

		public static int getSumRangeMod(int[] sum, int a, int b) {
			int ret = sum[b];
			ret = Mod.subMod(ret, a > 0 ? sum[a - 1] : 0);
			return ret;
		}

	}

	static class Mod {
		public static final long MOD = 1000000007L;
		public static final boolean DEBUG = false;

		public static int addMod(int a, int b) {
			if (DEBUG) return a + b;

			while (a < 0)
				a += MOD;
			while (b < 0)
				b += MOD;
			return (int) (((long) a + (long) b) % MOD);
		}

		public static int subMod(int a, int b) {
			if (DEBUG) return a - b;

			while (a < 0)
				a += MOD;
			while (b < 0)
				b += MOD;
			long temp = (long) a - (long) b;

			while (temp < 0)
				temp += MOD;
			return (int) temp;
		}

		public static int mulMod(int a, int b) {
			if (DEBUG) return a * b;

			while (a < 0)
				a += MOD;
			while (b < 0)
				b += MOD;
			return (int) (((long) a) * ((long) b) % MOD);
		}

	}

	static class Task implements Callable<Task> {
		Polygon poly = new Polygon();
		int n;
		int[] sx;
		int[] sy;
		int[] X;
		int[] Y;
		int RE = 0;
		int i;
		int j;
		int j1;
		long ar;
		long curs = 0;
		int sj;
		int Sj;
		int sj1;
		int Sj1;
		int testNumber;

		Task(int testNumber) {
			this.testNumber = testNumber;
		}

		public void readInput(InputReader in) {
	/* read input here */
			n = in.nextInt();
			sx = new int[n];
			sy = new int[n];

			X = new int[n];
			Y = new int[n];
			for (int i = 0; i < n; ++i) {
				int x = in.nextInt();
				int y = in.nextInt();
				poly.lp.add(new Point(x, y));

				X[i] = x;
				Y[i] = y;
			}

			MathUtils.buildSumRangeMod(X, sx);
			MathUtils.buildSumRangeMod(Y, sy);
		}

		int sumx(int[] s, int a, int b) {
			if (a <= b) return MathUtils.getSumRangeMod(s, a, b);
			else {
				return Mod.addMod(MathUtils.getSumRangeMod(s, 0, b), MathUtils.getSumRangeMod(s, a, n - 1));
			}
		}

		int next(int i) {
			return poly.next(i);
		}

		int prev(int i) {
			return poly.prev(i);
		}

		int calcseg(int from, int to) {

			int x1 = X[from];
			int y1 = Y[from];
			int x2 = X[to];
			int y2 = Y[to];
			return Mod.subMod(Mod.mulMod(x1, y2), Mod.mulMod(x2, y1));
		}

		long calcseg2(int from, int to) {

			long x1 = X[from];
			long y1 = Y[from];
			long x2 = X[to];
			long y2 = Y[to];
			return (x1 * y2) - (x2 * y1);
		}

		int distance(int a, int b) {
			if (a <= b) {
				return b - a;
			} else {
				return n - a + b;
			}
		}

		int getS() {
			int ret = 0;
			int tx = sumx(sx, next(i), j);
			int ty = sumx(sy, next(i), j);
			int t1 = Mod.mulMod(Y[i], tx);
			int t2 = Mod.mulMod(X[i], ty);
			int t3 = Mod.subMod(t1, t2);

			int t4 = Mod.addMod(Sj, t3);
			int t5 = Mod.subMod(0, t4);

			ret = t5;

			tx = sumx(sx, j1, prev(i));
			ty = sumx(sy, j1, prev(i));
			t1 = Mod.mulMod(Y[i], tx);
			t2 = Mod.mulMod(X[i], ty);
			t3 = Mod.subMod(t1, t2);
			t4 = Mod.addMod(Sj1, t3);
			ret = Mod.addMod(ret, t4);
			return ret;
		}

		void nextJ() {
			sj = Mod.addMod(sj, calcseg(j, next(j)));
			Sj = Mod.addMod(sj, Sj);
			Sj1 = Mod.subMod(Sj1, sj1);
			sj1 = Mod.subMod(sj1, calcseg(next(j1), j1));

			curs += calcseg2(j, next(j));

			j = next(j);
			j1 = next(j1);
		}

		void nextI() {
			int d = distance(i, j);
			int temp = calcseg(i, next(i));
			sj = Mod.subMod(sj, temp);
			Sj = Mod.subMod(Sj, Mod.mulMod(d, temp));

			d = distance(j1, next(i));
			temp = calcseg(next(i), i);
			sj1 = Mod.addMod(sj1, temp);
			Sj1 = Mod.addMod(Sj1, Mod.mulMod(temp, d));

			curs -= calcseg2(i, next(i));

			i = next(i);

		}

		public Task call() {
			ar = poly.area();
			int mn = 0;
			int ivm2 = 500000004;

			int total = (int) (ar % Mod.MOD);
			total = Mod.mulMod(total, n);
			total = Mod.mulMod(total, n - 3);
			total = Mod.mulMod(total, ivm2);


			i = 0;
			j = 1;
			j1 = 2;
			sj = Sj = calcseg(0, 1);
			curs = calcseg2(0, 1);

			for (int k = prev(i); true; k = prev(k)) {
				sj1 = Mod.addMod(sj1, calcseg(next(k), k));
				Sj1 = Mod.addMod(Sj1, sj1);
				if (k == j1) break;
			}


			while (true) {
				while (true) {
					long temp = calcseg2(next(j), i) + calcseg2(j, next(j));
					if (Math.abs(temp + curs) > ar / 2) break;
					nextJ();
				}
				mn = Mod.addMod(mn, getS());
				nextI();
				if (i == 0) break;
			}

			RE = Mod.subMod(total, mn);
			System.err.println("Test case: " + testNumber + " done!");
			return this;
		}

		public void writeOutput(PrintWriter out) {
			out.println(RE);
		}

	}

	static class Point implements Comparable<Point> {
		public long x;
		public long y;

		public Point(Point o) {
			this.x = o.x;
			this.y = o.y;

		}

		public Point(long x, long y) {
			super();

			this.x = x;
			this.y = y;
		}


		public int compareTo(Point o2) {
			int t = Long.compare(y, o2.y);
			if (t != 0) return t;
			return Long.compare(x, o2.x);
		}


		public String toString() {
			return x + " " + y;
		}


		public int hashCode() {
			return Long.hashCode(x) ^ Long.hashCode(y);
		}

		public boolean equals(Object obj) {
			if (obj instanceof Point) {
				return compareTo((Point) obj) == 0;
			}
			return false;
		}

	}

	static class InputReader {
		private InputStream stream;
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;

		public InputReader(InputStream stream) {
			this.stream = stream;
		}

		public int read() {
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

		public int nextInt() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			int res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public static boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		public void close() {

		}

	}

	static class Polygon {
		public ArrayList<Point> lp = new ArrayList<>();

		int next(int i) {
			return i == lp.size() - 1 ? 0 : i + 1;
		}

		int prev(int i) {
			return i == 0 ? lp.size() - 1 : i - 1;
		}

		long area() {
			long ret = 0;
			for (int i = 0; i < lp.size(); ++i) {
				ret += (lp.get(i).x * (lp.get(prev(i)).y - lp.get(next(i)).y));
			}
			return ret;
		}


		public String toString() {
			return "[" + lp + "]";
		}

	}
}

