import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Buns {

	static int n, m, c0, d0;
	static int[] a, b, c;
	static long[] d;
	static long[][] dp;

	static long solve(int curr, int i) {
		if (curr == 0 || i == m)
			return 0;
		if (dp[curr][i] != -1)
			return dp[curr][i];
		long ans = 0;
		int num = 1;
		while (num * c0 <= curr) {
			ans = Math.max(ans, num * d0 + solve(curr - num * c0, i));
			num++;
		}
		num = 1;
		while (num * b[i] <= a[i] && num * c[i] <= curr) {
			ans = Math.max(ans, num * d[i] + solve(curr - num * c[i], i + 1));
			num++;
		}
		ans = Math.max(ans, solve(curr, i + 1));
		return dp[curr][i] = ans;
	}

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out = new PrintWriter(System.out);
		sc = new StringTokenizer(br.readLine());
		n = nxtInt();
		m = nxtInt();
		c0 = nxtInt();
		d0 = nxtInt();
		a = new int[m];
		b = new int[m];
		c = new int[m];
		d = new long[m];
		for (int i = 0; i < m; i++) {
			a[i] = nxtInt();
			b[i] = nxtInt();
			c[i] = nxtInt();
			d[i] = nxtLng();
		}
		dp = new long[n + 1][m];
		for (int i = 0; i < n + 1; i++)
			Arrays.fill(dp[i], -1);
		out.println(solve(n, 0));
		br.close();
		out.close();
	}

	static BufferedReader br;
	static StringTokenizer sc;

	static String nxtTok() throws IOException {
		while (!sc.hasMoreTokens()) {
			String s = br.readLine();
			if (s == null)
				return null;
			sc = new StringTokenizer(s.trim());
		}
		return sc.nextToken();
	}

	static int nxtInt() throws IOException {
		return Integer.parseInt(nxtTok());
	}

	static long nxtLng() throws IOException {
		return Long.parseLong(nxtTok());
	}

	static double nxtDbl() throws IOException {
		return Double.parseDouble(nxtTok());
	}

	static int[] nxtIntArr(int n) throws IOException {
		int[] a = new int[n];
		for (int i = 0; i < n; i++)
			a[i] = nxtInt();
		return a;
	}

	static long[] nxtLngArr(int n) throws IOException {
		long[] a = new long[n];
		for (int i = 0; i < n; i++)
			a[i] = nxtLng();
		return a;
	}

	static char[] nxtCharArr() throws IOException {
		return nxtTok().toCharArray();
	}
}
