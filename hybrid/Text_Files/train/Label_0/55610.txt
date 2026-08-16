import java.io.*;
import java.util.*;

public class Main {
	private static boolean _READ_FROM_FILE = System.getProperty("ONLINE_JUDGE") == null;
	private static Scanner in;
	private static void core() {
		int nRows = in.nextInt(), nCols = in.nextInt();
		long[][] a = new long[nRows][nCols];
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				a[i][j] = in.nextInt();
			}
		}
		for (int i = 0; i < a.length; i++) {
			for (int j = 1; j < a[i].length; j++) {
				a[i][j] += a[i][j - 1];
			}
		}
		long[][] dp = new long[nRows][nCols];
		for (int j = 0; j < dp[0].length; j++) {
			dp[0][j] = a[0][j];
		}
		Long res = Long.MIN_VALUE;
		for (int row = 1; row < dp.length; row++) {
			if (row % 2 == 1) {
				TreeSet<Long> all = new TreeSet<Long>();
				all.add(dp[row - 1][dp[row].length - 1]);
				for (int col = dp[row].length - 2; col >= 0; col--) {
					dp[row][col] = a[row][col] + all.last();
					all.add(dp[row - 1][col]);
					if (row + 1 == dp.length)
						res = Math.max(res, dp[row][col]);
				}
			}
			else {
				TreeSet<Long> all = new TreeSet<Long>();
				all.add(dp[row - 1][0]);
				for (int col = 1; col < dp[row].length; col++) {
					dp[row][col] = a[row][col] + all.last();
					all.add(dp[row - 1][col]);
					if (row + 1 == dp.length)
						res = Math.max(res, dp[row][col]);
				}
			}
		}
		System.out.println(res);
	}
	static void debug(Object...os) {
		System.out.println(Arrays.deepToString(os));
	}
	public static void main(String[] args) throws FileNotFoundException {
		if (_READ_FROM_FILE)
			System.setIn(new FileInputStream("in.in"));
		in = new Scanner(System.in);
		core();
	}
	static class Scanner {
		BufferedReader reader;
		StringTokenizer tokenizer;
		public Scanner(InputStream in) {
			reader = new BufferedReader(new InputStreamReader(in));
			tokenizer = new StringTokenizer("");
		}
		public String next() {
			try {
				while(!tokenizer.hasMoreElements())
					tokenizer = new StringTokenizer(reader.readLine());
				return tokenizer.nextToken();
			} catch (Exception e) {
				e.printStackTrace();
				throw new RuntimeException(e);
			}
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
	}

}
