import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Map;

public class Main {
	static InputStream is;
	static PrintWriter out;
	static String INPUT = "";
	
	// 1000
	// 1???
	// ?1?1
	// 0??1
	
	
	static void solve()
	{
		int n = ni(), m = ni();
		int[][] co = new int[m][];
		for(int i = 0;i < m;i++){
			co[i] = na(3);
		}
		Map<Long, Integer> map = new HashMap<>();
		for(int[] c : co){
			map.put((long)c[0]<<32|c[1], c[2]);
		}
		int[] udiag = new int[n-1];
		int[] ddiag = new int[n-1];
		int[] diag = new int[n];
		Arrays.fill(diag, -1);
		Arrays.fill(udiag, -1);
		Arrays.fill(ddiag, -1);
		
		int mod = 998244353;
		for(int i = 1;i <= n;i++){
			if(!map.containsKey((long)i<<32|i)){
			}else{
				diag[i-1] = map.get((long)i<<32|i);
			}
		}
		int np = 0;
		for(int i = 0;i < m;i++){
			int[] c = co[i];
			if(c[1] == c[0] + 1){
				udiag[c[0]-1] = c[2];
				continue;
			}else if(c[1] == c[0] - 1){
				ddiag[c[1]-1] = c[2];
				continue;
			}
			if(c[1] == c[0])continue;
			long inv = (long)c[1]<<32|c[0];
			if(map.containsKey(inv)){
				np += 1;
				int u = map.get(inv);
				if(u+c[2] == 1){
					if(Math.abs(c[0]-c[1]) > 2){
						out.println(0);
						return;
					}
					
					if(Math.abs(c[0]-c[1]) == 2){
						int r = (c[0]+c[1])/2;
						if(!map.containsKey((long)r<<32|r)){
							diag[r-1] = 1;
						}else{
							int q = map.get((long)r<<32|r);
							if(q == 0){
								out.println(0);
								return;
							}
						}
					}
				}else{
					if(Math.abs(c[0]-c[1]) == 2){
						int r = (c[0]+c[1])/2;
						if(!map.containsKey((long)r<<32|r)){
							diag[r-1] = 0;
						}else{
							int q = map.get((long)r<<32|r);
							if(q == 1){
								out.println(0);
								return;
							}
						}
					}
				}
			}else{
				np += 2;
			}
		}
		long free = (long)(n-1)*(n-2)/2-np/2;
		
//		tr(free);
//		tr(udiag);
//		tr(diag);
//		tr(ddiag);
		
		long[] dp = new long[2];
		if(diag[0] == 0){
			dp[0] = 1;
		}else if(diag[0] == 1){
			dp[1] = 1;
		}else{
			dp[0] = dp[1] = 1;
		}
		
		for(int i = 1;i < n;i++){
			{
				int fi = (udiag[i-1] >= 0 ? 1 : 0) + (ddiag[i-1] >= 0 ? 1 : 0);
				int fs = udiag[i-1] ^ ddiag[i-1];
				long[] ndp = new long[2];
				if(fi == 2){
					for(int j = 0;j < 2;j++){
						ndp[j^fs] += dp[j];
					}
				}else if(fi == 1){
					ndp[0] = (dp[0] + dp[1]) % mod;
					ndp[1] = (dp[0] + dp[1]) % mod;
				}else{
					ndp[0] = (dp[0] + dp[1])*2L % mod;
					ndp[1] = (dp[0] + dp[1])*2L % mod;
				}
				dp = ndp;
			}
			long[] ndp = new long[2];
			if(diag[i] == 0){
				ndp[0] = dp[0];
			}else if(diag[i] == 1){
				ndp[1] = dp[1];
			}else{
				ndp[0] = dp[0];
				ndp[1] = dp[1];
			}
			dp = ndp;
		}
		
		out.println((dp[0]+dp[1])%mod * pow(2, free, mod) % mod);
	}
	// ??1
	// ??1
	// 010
	
	public static long pow(long a, long n, long mod) {
		//		a %= mod;
		long ret = 1;
		int x = 63 - Long.numberOfLeadingZeros(n);
		for (; x >= 0; x--) {
			ret = ret * ret % mod;
			if (n << 63 - x < 0)
				ret = ret * a % mod;
		}
		return ret;
	}

	
	public static void main(String[] args) throws Exception
	{
		long S = System.currentTimeMillis();
		is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
		out = new PrintWriter(System.out);
		
		solve();
		out.flush();
		long G = System.currentTimeMillis();
		tr(G-S+"ms");
	}
	
	private static boolean eof()
	{
		if(lenbuf == -1)return true;
		int lptr = ptrbuf;
		while(lptr < lenbuf)if(!isSpaceChar(inbuf[lptr++]))return false;
		
		try {
			is.mark(1000);
			while(true){
				int b = is.read();
				if(b == -1){
					is.reset();
					return true;
				}else if(!isSpaceChar(b)){
					is.reset();
					return false;
				}
			}
		} catch (IOException e) {
			return true;
		}
	}
	
	private static byte[] inbuf = new byte[1024];
	static int lenbuf = 0, ptrbuf = 0;
	
	private static int readByte()
	{
		if(lenbuf == -1)throw new InputMismatchException();
		if(ptrbuf >= lenbuf){
			ptrbuf = 0;
			try { lenbuf = is.read(inbuf); } catch (IOException e) { throw new InputMismatchException(); }
			if(lenbuf <= 0)return -1;
		}
		return inbuf[ptrbuf++];
	}
	
	private static boolean isSpaceChar(int c) { return !(c >= 33 && c <= 126); }
//	private static boolean isSpaceChar(int c) { return !(c >= 32 && c <= 126); }
	private static int skip() { int b; while((b = readByte()) != -1 && isSpaceChar(b)); return b; }
	
	private static double nd() { return Double.parseDouble(ns()); }
	private static char nc() { return (char)skip(); }
	
	private static String ns()
	{
		int b = skip();
		StringBuilder sb = new StringBuilder();
		while(!(isSpaceChar(b))){
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	
	private static char[] ns(int n)
	{
		char[] buf = new char[n];
		int b = skip(), p = 0;
		while(p < n && !(isSpaceChar(b))){
			buf[p++] = (char)b;
			b = readByte();
		}
		return n == p ? buf : Arrays.copyOf(buf, p);
	}
	
	private static char[][] nm(int n, int m)
	{
		char[][] map = new char[n][];
		for(int i = 0;i < n;i++)map[i] = ns(m);
		return map;
	}
	
	private static int[] na(int n)
	{
		int[] a = new int[n];
		for(int i = 0;i < n;i++)a[i] = ni();
		return a;
	}
	
	private static int ni()
	{
		int num = 0, b;
		boolean minus = false;
		while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
		if(b == '-'){
			minus = true;
			b = readByte();
		}
		
		while(true){
			if(b >= '0' && b <= '9'){
				num = num * 10 + (b - '0');
			}else{
				return minus ? -num : num;
			}
			b = readByte();
		}
	}
	
	private static long nl()
	{
		long num = 0;
		int b;
		boolean minus = false;
		while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
		if(b == '-'){
			minus = true;
			b = readByte();
		}
		
		while(true){
			if(b >= '0' && b <= '9'){
				num = num * 10 + (b - '0');
			}else{
				return minus ? -num : num;
			}
			b = readByte();
		}
	}
	
	private static void tr(Object... o) { if(INPUT.length() != 0)System.out.println(Arrays.deepToString(o)); }
}
