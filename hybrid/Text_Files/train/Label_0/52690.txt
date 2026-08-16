import java.util.*;
import java.io.*;
public class c {
	static final char nah = (char)0;
	static final int mod = 998_244_353;
	
	static int n, m;
	static char[] s, t;
	static long[][] dp;
	public static void main(String[] args) {
		FS sc = new FS();
		PrintWriter pw = new PrintWriter(System.out);
		s = sc.next().toCharArray();
		n = s.length;
		t = new char[n];
		char[] temp = sc.next().toCharArray();
		m = temp.length;
		for(int i = 0; i < m; ++i) t[i] = temp[i];
		
		dp = new long[n + 1][n];
		for(long[] z : dp) Arrays.fill(z, -1);
		
		long out = 0;
		for(int i = 0; i < n; ++i) {
			if(t[i] == nah || t[i] == s[0]) out = (out + 2 * go(1, i)) % mod;
		}
		
		System.out.println(out);
	}
	static long go(int idx, int l) {
		if(dp[idx][l] != -1) return dp[idx][l];
		
		int r = l + idx - 1;
		long out = (l == 0 && r >= m - 1 ? 1 : 0);
		if(l - 1 >= 0 && (t[l - 1] == nah || t[l - 1] == s[idx])) out = (out + go(idx + 1, l - 1)) % mod;
		if(r + 1 < n && (t[r + 1] == nah || t[r + 1] == s[idx])) out = (out + go(idx + 1, l)) % mod;
		
		return dp[idx][l] = out;
	}
	static class FS {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer("");
		String next() {
			while(!st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch(Exception e) {}
			}
			return st.nextToken();
		}
		int nextInt() {
			return Integer.parseInt(next());
		}
		long nextLong() {
			return Long.parseLong(next());
		}
	}
}