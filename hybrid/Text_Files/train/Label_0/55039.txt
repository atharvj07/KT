import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	MyScanner sc = new MyScanner();
	Scanner sc2 = new Scanner(System.in);
	final int MOD = 1000000007;
	int[] dx = { 1, 0, 0, -1 };
	int[] dy = { 0, 1, -1, 0 };

	void run() {
		for (;;) {
			String in = sc.next();
			if (in.equals("#")) {
				return;
			}
			int ncnt = 0;
			int wcnt = 0;
			ArrayList<Character> dir = new ArrayList<Character>();
			for (int i = 0; i < in.length(); i++) {
				if (in.charAt(i) == 'n') {
					dir.add('n');
					i += 4;
				} else {
					dir.add('w');
					i += 3;
				}
			}
			long numerator = 1;
			long denominator = 1;
			if (dir.get(dir.size() - 1) == 'n') {
				numerator = 0;
				denominator = 1;
			} else {
				numerator = 90;
				denominator = 1;
			}
			int div = 2;
			for (int i = dir.size() - 2; i >= 0; i--) {
				long base = 90;
				long tmpDiv = div;
				if (base % tmpDiv == 0) {
					base = base / tmpDiv;
					tmpDiv = 0;
				} else {
					long gcd = gcd(base, tmpDiv);
					base /= gcd;
					tmpDiv /= gcd;
				}
				if (dir.get(i) == 'n') {
					if (tmpDiv == 0) {
						numerator -= base;
					} else {
						long lcm = tmpDiv * denominator
								/ gcd(tmpDiv, denominator);
						base *= denominator;
						numerator *= tmpDiv;
						denominator *= lcm;
						tmpDiv *= lcm;
						numerator -= base;
					}
				} else {
					if (tmpDiv == 0) {
						numerator += base;
					} else {
						long lcm = tmpDiv * denominator
								/ gcd(tmpDiv, denominator);
						base *= denominator;
						numerator *= tmpDiv;
						denominator *= lcm;
						tmpDiv *= lcm;
						numerator += base;
					}
				}
				long d = gcd(numerator, denominator);
				numerator /= d;
				denominator /= d;
				div *= 2;
			}
			if (numerator % denominator == 0) {
				System.out.println(numerator / denominator);
			} else {
				long d = gcd(numerator, denominator);
				System.out.println(numerator / d + "/" + denominator / d);
			}
		}
	}

	long gcd(long a, long b) {
		return a % b == 0 ? b : gcd(b, a % b);
	}

	public static void main(String[] args) {
		new Main().run();
	}

	void debug(Object... o) {
		System.out.println(Arrays.deepToString(o));
	}

	void debug2(int[][] array) {
		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < array[i].length; j++) {
				System.out.print(array[i][j]);
			}
			System.out.println();
		}
	}

	boolean inner(int h, int w, int lim) {
		return 0 <= h && h < lim && 0 <= w && w < lim;
	}

	void swap(int[] x, int a, int b) {
		int tmp = x[a];
		x[a] = x[b];
		x[b] = tmp;
	}

	// find minimum i (a[i] >= border)
	int lower_bound(int a[], int border) {
		int l = -1;
		int r = a.length;

		while (r - l > 1) {
			int mid = (l + r) / 2;
			if (border <= a[mid]) {
				r = mid;
			} else {
				l = mid;
			}
		}
		// r = l + 1
		return r;
	}

	class MyScanner {
		int nextInt() {
			try {
				int c = System.in.read();
				while (c != '-' && (c < '0' || '9' < c))
					c = System.in.read();
				if (c == '-')
					return -nextInt();
				int res = 0;
				do {
					res *= 10;
					res += c - '0';
					c = System.in.read();
				} while ('0' <= c && c <= '9');
				return res;
			} catch (Exception e) {
				return -1;
			}
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}

		long nextLong() {
			return Long.parseLong(next());
		}

		String next() {
			try {
				StringBuilder res = new StringBuilder("");
				int c = System.in.read();
				while (Character.isWhitespace(c))
					c = System.in.read();
				do {
					res.append((char) c);
				} while (!Character.isWhitespace(c = System.in.read()));
				return res.toString();
			} catch (Exception e) {
				return null;
			}
		}

		int[] nextIntArray(int n) {
			int[] in = new int[n];
			for (int i = 0; i < n; i++) {
				in[i] = nextInt();
			}
			return in;
		}

		int[][] nextInt2dArray(int n, int m) {
			int[][] in = new int[n][m];
			for (int i = 0; i < n; i++) {
				in[i] = nextIntArray(m);
			}
			return in;
		}

		double[] nextDoubleArray(int n) {
			double[] in = new double[n];
			for (int i = 0; i < n; i++) {
				in[i] = nextDouble();
			}
			return in;
		}

		long[] nextLongArray(int n) {
			long[] in = new long[n];
			for (int i = 0; i < n; i++) {
				in[i] = nextLong();
			}
			return in;
		}
	}
}