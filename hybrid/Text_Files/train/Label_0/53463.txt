import java.util.*;
import java.math.*;
import java.io.*;

public class f {
	long modinv(long x) { return modpow(x, mod - 2); }
	long modpow(long b, long e) {
		if(e == 0) return 1;
		long r = modpow(b, e >> 1);
		if((e & 1) == 0) return mult(r, r);
		return mult(b, mult(r, r));
	}
	long add(long a, long b) { return a + b >= mod ? a + b - mod : a + b; }
	long mult(long a, long b) { return a * b >= mod ? a * b % mod : a * b; }
	boolean inrange(long[] r1, long[] r2) { // r1 in r2
		return (r2[0] <= r1[0] && r1[0] <= r2[1]) || (r2[0] <= r1[1] && r1[1] <= r2[1]); 
	}
	long go(int at1, int at2) {
		if(at2 == m) return at1 == n ? 1 : 0;
		if(at1 == n) return 1;
		if(dp[at1][at2] != -1) return dp[at1][at2];
		long res = go(at1, at2 + 1);
		for(int i = 1 ; at1 + i <= n ; i++) {
			if(!inrange(nranges[at2], ranges[at1 + i - 1])) break;
			long t = go(at1 + i, at2 + 1);
			res = add(res, mult(t, precmp[at2][i]));
		}
		return dp[at1][at2] = res;
	}
	final int mod = 998_244_353;
	long[][] ranges, nranges, precmp, dp;
	int n, m;
	public f() {
		long[] inv = new long[100];
		inv[1] = 1;
		for (int i = 2; i < inv.length; ++i)
			inv[i] = (mod - (mod / i) * inv[mod % i] % mod) % mod;
		FS scan = new FS();
		n = scan.nextInt();
		long[] bounds = new long[n * 2];
		ranges = new long[n][2];
		long all = 1;
		for(int i = 0 ; i < n ; i++) {
			ranges[i][0] = scan.nextLong();
			ranges[i][1] = scan.nextLong();
			bounds[i] = ranges[i][0];
			bounds[i + n] = ranges[i][1] + 1;
			all = mult(all, ranges[i][1] - ranges[i][0] + 1);
		}
		Arrays.sort(bounds);
		List<long[]> newranges = new ArrayList<>();
		for(int i = bounds.length - 1 ; i > 0 ; i--)
			if(bounds[i] != bounds[i - 1])
				newranges.add(new long[] {bounds[i - 1], bounds[i] - 1});
		m = newranges.size();
		nranges = new long[m][2];
		precmp = new long[m][n + 1];
		for(int i = 0 ; i < m ; i++) {
			nranges[i] = newranges.get(i);
			precmp[i][0] = 1;
			for(int j = 1 ; j <= n ; j++)
				precmp[i][j] = mult(mult(precmp[i][j - 1], nranges[i][1] - nranges[i][0] + 1 + j - 1), inv[j]);
		}
		dp = new long[n][m];
		for(int i = 0 ; i < n ; i++)
			Arrays.fill(dp[i], -1);
		long valid = go(0, 0);
		System.out.println(mult(valid, modinv(all)));
	}
	class FS {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer("");
		public String next() {
			while(!st.hasMoreTokens()) {
				try { st = new StringTokenizer(br.readLine()); }
				catch(Exception e) { e.printStackTrace(); }
			}
			return st.nextToken();
		}
		public int nextInt() { return Integer.parseInt(next()); }
		public long nextLong() { return Long.parseLong(next()); }
		public double nextDouble() { return Double.parseDouble(next()); }
	}
	public static void main(String[] args) throws Exception { new f(); }
}
