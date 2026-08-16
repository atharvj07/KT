import java.util.*;
import java.io.*;

public class E1397 {

	static int n;
	static long r1, r2, r3, d;
	static long[] a;
	static long[][] dp;

	public static long dp(int idx, int state) {
		long gun = a[idx] * r1;
		if (idx == a.length - 1 && (state == 0 || state == 4 || state == 5)) {
			if (state == 0) {
				return Math.min(gun + 2 * d + r1 + r1, Math.min(gun + r3, r2 + 2 * d + r1));
			} else if (state == 4) {
				return r1;
			} else if (state == 5) {
				return 0;
			}
		}
		if (idx == a.length - 2 && state == 2) {
			return r1;
		}
		if (dp[state][idx] != -1)
			return dp[state][idx];
		long ans = (long) 1e18;
		if (state == 0) {

			ans = Math.min(ans, d + gun + r3 + dp(idx + 1, 0));
			ans = Math.min(ans, d + gun + r1 + dp(idx + 1, 1));
			ans = Math.min(ans, d + r2 + dp(idx + 1, 1));
		} else if (state == 1) {
			ans = Math.min(ans, d + gun + r3 + dp(idx - 1, 2));
			ans = Math.min(ans, d + gun + r1 + dp(idx - 1, 3));
			ans = Math.min(ans, d + r2 + dp(idx - 1, 3));
		} else if (state == 2) {
			ans = Math.min(ans, d + r1 + dp(idx + 1, 5));
		} else if (state == 3) {
			ans = Math.min(ans, d + r1 + dp(idx + 1, 4));
		} else if (state == 4) {
			ans = Math.min(ans, d + r1 + dp(idx + 1, 0));
		} else if (state == 5) {
			ans = Math.min(ans, d + dp(idx + 1, 0));
		}

		return dp[state][idx] = ans;
	}

	public static void trace(int idx, int state) {
		long gun = a[idx] * r1;
		if (idx == a.length - 1 && (state == 0 || state == 4 || state == 5)) {
			if (state == 0) {
				System.out.println("end 0");

			} else if (state == 4) {
				System.out.println("end 4");
			} else if (state == 5) {
				System.out.println("end 5");
			}
			return;
		}
		if (idx == a.length - 2 && state == 2) {
			System.out.println("end 2");
			return;
		}

		long ans = (long) 1e18;
		if (state == 0) {
			if (dp(idx, 0) == d + gun + r3 + dp(idx + 1, 0)) {
				System.out.println(idx + " " + "gun and amw move forward");
				System.out.println("spent " + " " + d + " " + gun + " " + r3);
				trace(idx + 1, 0);
			} else if (dp(idx, 0) == d + gun + r1 + dp(idx + 1, 1)) {
				System.out.println(idx + " " + "gun and gun move forward");
				System.out.println("spent " + (d + gun + r1));
				trace(idx + 1, 1);
			} else {
				System.out.println(idx + " " + "ray move forward");
				System.out.println("spent " + (r2 + d));
				trace(idx + 1, 1);
			}

		} else if (state == 1) {
			if (dp(idx, 1) == d + gun + r3 + dp(idx - 1, 2)) {
				System.out.println(idx + " " + "gun and amw move back");
				trace(idx - 1, 2);
			} else if (dp(idx, 1) == d + gun + r1 + dp(idx - 1, 3)) {
				System.out.println(idx + " " + "gun and gun move back");
				trace(idx - 1, 3);
			} else {
				System.out.println(idx + " " + "ray move back");
				trace(idx - 1, 3);
			}

		} else if (state == 2) {
			System.out.println(idx + " " + "shoot boss move forward");
			trace(idx + 1, 5);
		} else if (state == 3) {
			System.out.println(idx + " " + "shoot boss move forward");
			trace(idx + 1, 4);
		} else if (state == 4) {
			System.out.println(idx + " " + "shoot boss move forward");
			trace(idx + 1, 0);
		} else {
			System.out.println(idx + " " + "move forward");
			trace(idx + 1, 0);
		}

	}

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(System.out);
		n = sc.nextInt();
		r1 = sc.nextLong();
		r2 = sc.nextLong();
		r3 = sc.nextLong();
		d = sc.nextLong();
		a = new long[n];
		for (int i = 0; i < a.length; i++) {
			a[i] = sc.nextLong();
		}
		dp = new long[6][n];
		for (long[] x : dp)
			Arrays.fill(x, -1);
		for (int idx = n - 5; idx >= 0; idx -= 100) {
			for (int i = 0; i < 6; i++) {
				dp(idx, i);
			}
		}
		pw.println(dp(0, 0));
//		trace(0, 0);
		pw.close();
	}

	static class Scanner {
		BufferedReader br;
		StringTokenizer st;

		public Scanner(InputStream s) {
			br = new BufferedReader(new InputStreamReader(s));
		}

		public Scanner(FileReader f) {
			br = new BufferedReader(f);
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		public int[] nextIntArr(int n) throws IOException {
			int[] arr = new int[n];
			for (int i = 0; i < n; i++) {
				arr[i] = Integer.parseInt(next());
			}
			return arr;
		}

	}

}
