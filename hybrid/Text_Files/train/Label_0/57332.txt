import java.io.*;
import java.util.*;
import java.util.Map.Entry;

import static java.lang.Math.*;

public class Ans implements Runnable {

	// public static void main(String args[]) throws Exception {
	//
	// new Thread(null, new Ans(), "Check2", 1 << 28).start();
	//
	// }

	public static void main(String args[]) {
		Ans s = new Ans();
		s.run();
	}

	static void debug(Object... o) {
		System.out.println(Arrays.deepToString(o));
	}

	InputReader sc = null;
	PrintWriter pw = null;
	
	static long[] a = new long[(int)(1e5+2)];
	static long[] pSum = new long[(int)(1e5+2)];

	public void run() {
			// InputStream is = new FileInputStream(new File("input.txt"));
			sc = new InputReader(System.in);
			pw = new PrintWriter(System.out);
			int T = sc.nextInt();
			while (T-- > 0) {
				int n = sc.nextInt();
				int k = sc.nextInt();
				int z = sc.nextInt();
				for(int i = 0; i < n; i ++){
					a[i] = sc.nextLong();
				}
				Arrays.fill(pSum, 0);
				pSum[0] = a[0];
				for(int i = 1; i <= k; i++){
					 pSum[i] += pSum[i-1] + a[i]; 
				}
				long ans = pSum[k];
				for(int i = 1;i <= k; i++){
					long tempAns = pSum[i];
					int tofro = min(2*z, k-i);
					tempAns += (tofro/2)*a[i];
					tempAns += ((tofro+1)/2)*a[i-1];
					int remSteps = k - (i+tofro);
					if(tofro % 2 == 0){						
						tempAns += pSum[i+remSteps] - pSum[i];
					}else{
						tempAns += pSum[i+remSteps-1] - pSum[i-1];
					}					
					
					ans = max(tempAns, ans);
				}
				pw.println(ans);
				
			}

			// is.close();
			pw.close();
		
	}
	
	

	static class InputReader {
		private InputStream stream;
		private byte[] buf = new byte[5];
		private int curChar;
		private int numChars;
		private SpaceCharFilter filter;

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

		public String nextLine() {
			BufferedReader br = new BufferedReader(new InputStreamReader(stream));
			String stock = "";
			try {
				stock = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return stock;
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

		public long nextLong() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			long res = 0;

			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public double nextDouble() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			double res = 0;
			while (!isSpaceChar(c) && c != '.') {
				if (c == 'e' || c == 'E')
					return res * Math.pow(10, nextInt());
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}
			if (c == '.') {
				c = read();
				double m = 1;
				while (!isSpaceChar(c)) {
					if (c == 'e' || c == 'E')
						return res * Math.pow(10, nextInt());
					if (c < '0' || c > '9')
						throw new InputMismatchException();
					m /= 10;
					res += (c - '0') * m;
					c = read();
				}
			}
			return res * sgn;
		}

		public String readString() {
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

		public boolean isSpaceChar(int c) {
			if (filter != null)
				return filter.isSpaceChar(c);
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		public String next() {
			return readString();
		}

		public interface SpaceCharFilter {
			public boolean isSpaceChar(int ch);
		}
	}
}