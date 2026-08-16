// package CodeForces;

import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;

public class Round50C {

	public static void solve() {
		int n = s.nextInt();
		long[] rl = new long[n];
		long[] rr = new long[n];
		for(int i = 0; i < n; i++) {
			rl[i] = s.nextLong();
			rr[i] = s.nextLong();
		}
		int k = s.nextInt();
		double[] yes = new double[n];
		double[] no = new double[n];
		for(int i = 0; i < n; i++) {
//			out.println(onesMsd(rr[i]));
			yes[i] = (double)(onesMsd(rr[i]) - onesMsd(rl[i] - 1))/(double)(rr[i] - rl[i] + 1);
			no[i] = 1. - yes[i];
		}
		double[][] dp = new double[n][n + 1];
		dp[0][0] = no[0];
		dp[0][1] = yes[0];
		for(int i = 1; i < n; i++) {
			for(int j = 0; j <= n; j++) {
				if(j == 0) {
					dp[i][j] = dp[i - 1][j] * no[i];
				}else {
					dp[i][j] = dp[i - 1][j - 1] * yes[i] + dp[i - 1][j] * no[i];
				}
			}
		}
		double ans = 0.0;
		for(int i = 0; i <= n; i++) {
			if(k * n <= 100 * i) {
				ans += dp[n - 1][i];
			}
		}
		out.println(ans);
	}

	public static long onesMsd(long x) {
		if(x == 0) return 0;
		long len = Long.toString(x).length();
		long ans = 0;
		long pow10 = 1;
		for(int i = 1; i < len; i++) {
			ans += pow10;
			pow10 *= 10;
		}
		if(x/pow10 > 1) {
			ans += pow10;
		}else {
			ans += x%pow10 + 1;
		}
		return ans;
	}
	
	public static void main(String[] args) {
		new Thread(null, null, "Thread", 1 << 27) {
			public void run() {
				try {
					out = new PrintWriter(new BufferedOutputStream(System.out));
					s = new FastReader(System.in);
					solve();
					out.close();
				} catch (Exception e) {
					e.printStackTrace();
					System.exit(1);
				}
			}
		}.start();
	}

	public static PrintWriter out;
	public static FastReader s;

	public static class FastReader {

		private InputStream stream;
		private byte[] buf = new byte[4096];
		private int curChar, snumChars;

		public FastReader(InputStream stream) {
			this.stream = stream;
		}

		public int read() {
			if (snumChars == -1) {
				throw new InputMismatchException();
			}
			if (curChar >= snumChars) {
				curChar = 0;
				try {
					snumChars = stream.read(buf);
				} catch (IOException E) {
					throw new InputMismatchException();
				}
			}
			if (snumChars <= 0) {
				return -1;
			}
			return buf[curChar++];
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
			int number = 0;
			do {
				number *= 10;
				number += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return number * sgn;
		}

		public long nextLong() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			long sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			long number = 0;
			do {
				number *= 10L;
				number += (long) (c - '0');
				c = read();
			} while (!isSpaceChar(c));
			return number * sgn;
		}

		public int[] nextIntArray(int n) {
			int[] arr = new int[n];
			for (int i = 0; i < n; i++) {
				arr[i] = this.nextInt();
			}
			return arr;
		}

		public long[] nextLongArray(int n) {
			long[] arr = new long[n];
			for (int i = 0; i < n; i++) {
				arr[i] = this.nextLong();
			}
			return arr;
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

		public String nextLine() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isEndofLine(c));
			return res.toString();
		}

		public boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		public boolean isEndofLine(int c) {
			return c == '\n' || c == '\r' || c == -1;
		}

	}

	
}
