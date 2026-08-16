
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.InputMismatchException;

public class Main {
	static InputStream is;
	static PrintWriter out;
	static String INPUT = "";
	
	static void solve()
	{
		int Q = ni();
		int[][] qs = new int[Q][];
		for(int z = 0;z < Q;z++){
			qs[z] = new int[]{ni(), ni()};
		}
		
		int[] primes = sieveEratosthenes(300);
		int[][][][][][][] dp = new int[9][6][4][3][3][3][3];
		int[][] mfs = new int[305][7];
		int[] rem = new int[305];
		for(int i = 1;i <= 300;i++){
			int j = i;
			for(int k = 0;k < 7;k++){
				while(j % primes[k] == 0){
					j /= primes[k];
					mfs[i][k]++;
				}
			}
			rem[i] = j;
		}
		
		for(int[] q : qs){
			if(rem[q[0]] == 1){
				for(int i = mfs[q[0]][0];i < 9;i++){
					for(int j = mfs[q[0]][1];j < 6;j++){
						for(int k = mfs[q[0]][2];k < 4;k++){
							for(int l = mfs[q[0]][3];l < 3;l++){
								for(int m = mfs[q[0]][4];m < 3;m++){
									for(int n = mfs[q[0]][5];n < 3;n++){
										for(int o = mfs[q[0]][6];o < 3;o++){
											dp[i][j][k][l][m][n][o] += q[1];
										}
									}
								}
							}
						}
					}
				}
			}
		}
		
		for(int p : primes){
			if(p >= 19){
				int[][][][][][][] plus = new int[9][6][4][3][3][3][3];
				for(int[] q : qs){
					if(rem[q[0]] == p){
						int r = q[0] / rem[q[0]];
						int x = q[1];
//						plus[mfs[r][0]][mfs[r][1]][mfs[r][2]][mfs[r][3]][mfs[r][4]][mfs[r][5]][mfs[r][6]] += x;
						for(int i = mfs[r][0];i < 9;i++){
							for(int j = mfs[r][1];j < 6;j++){
								for(int k = mfs[r][2];k < 4;k++){
									for(int l = mfs[r][3];l < 3;l++){
										for(int m = mfs[r][4];m < 3;m++){
											for(int n = mfs[r][5];n < 3;n++){
												for(int o = mfs[r][6];o < 3;o++){
													plus[i][j][k][l][m][n][o] += q[1];
												}
											}
										}
									}
								}
							}
						}
					}
				}
				for(int i = 8;i >= 0;i--){
					for(int j = 5;j >= 0;j--){
						for(int k = 3;k >= 0;k--){
							for(int l = 2;l >= 0;l--){
								for(int m = 2;m >= 0;m--){
									for(int n = 2;n >= 0;n--){
										for(int o = 2;o >= 0;o--){
//											int my = 0;//plus[i][j][k][l][m][n][o];
//											if(i+1 < 9){
//												my = Math.max(my, plus[i+1][j][k][l][m][n][o]);
//											}
//											if(j+1 < 6){
//												my = Math.max(my, plus[i][j+1][k][l][m][n][o]);
//											}
//											if(k+1 < 4){
//												my = Math.max(my, plus[i][j][k+1][l][m][n][o]);
//											}
//											if(l+1 < 3){
//												my = Math.max(my, plus[i][j][k][l+1][m][n][o]);
//											}
//											if(m+1 < 3){
//												my = Math.max(my, plus[i][j][k][l][m+1][n][o]);
//											}
//											if(n+1 < 3){
//												my = Math.max(my, plus[i][j][k][l][m][n+1][o]);
//											}
//											if(o+1 < 3){
//												my = Math.max(my, plus[i][j][k][l][m][n][o+1]);
//											}
//											my += plus[i][j][k][l][m][n][o];
//											plus[i][j][k][l][m][n][o] = my;
											dp[i][j][k][l][m][n][o] += Math.max(0, plus[i][j][k][l][m][n][o]);
										}
									}
								}
							}
						}
					}
				}
			}
		}
		
		int ans = Integer.MIN_VALUE;
		for(int i = 8;i >= 0;i--){
			for(int j = 5;j >= 0;j--){
				for(int k = 3;k >= 0;k--){
					for(int l = 2;l >= 0;l--){
						for(int m = 2;m >= 0;m--){
							for(int n = 2;n >= 0;n--){
								for(int o = 2;o >= 0;o--){
									ans = Math.max(ans, dp[i][j][k][l][m][n][o]);
								}
							}
						}
					}
				}
			}
		}
		
		out.println(ans);
//		
//		tr(primes.length);
	}
	
	
	public static int[][] factorFast(int n, int[] lpf)
	{
		int[][] f = new int[9][];
		int q = 0;
		while(lpf[n] > 0){
			int p = lpf[n];
			if(q == 0 || p != f[q-1][0]){
				f[q++] = new int[]{p, 1};
			}else{
				f[q-1][1]++;
			}
			n /= p;
		}
		if(n > 1){
			// big prime
			return new int[][]{{n, 1}};
		}
		return Arrays.copyOf(f, q);
	}

	
	public static int[] enumLowestPrimeFactors(int n)
	{
		int tot = 0;
		int[] lpf = new int[n+1];
		int u = n+32;
		double lu = Math.log(u);
		int[] primes = new int[(int)(u/lu+u/lu/lu*1.5)];
		for(int i = 2;i <= n;i++)lpf[i] = i;
		for(int p = 2;p <= n;p++){
			if(lpf[p] == p)primes[tot++] = p;
			int tmp;
			for(int i = 0;i < tot && primes[i] <= lpf[p] && (tmp = primes[i]*p) <= n;i++){
				lpf[tmp] = primes[i];
			}
		}
		return lpf;
	}

	
	public static int[] sieveEratosthenes(int n) {
		if (n <= 32) {
			int[] primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 };
			for (int i = 0; i < primes.length; i++) {
				if (n < primes[i]) {
					return Arrays.copyOf(primes, i);
				}
			}
			return primes;
		}

		int u = n + 32;
		double lu = Math.log(u);
		int[] ret = new int[(int) (u / lu + u / lu / lu * 1.5)];
		ret[0] = 2;
		int pos = 1;

		int[] isnp = new int[(n + 1) / 32 / 2 + 1];
		int sup = (n + 1) / 32 / 2 + 1;

		int[] tprimes = { 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 };
		for (int tp : tprimes) {
			ret[pos++] = tp;
			int[] ptn = new int[tp];
			for (int i = (tp - 3) / 2; i < tp << 5; i += tp)
				ptn[i >> 5] |= 1 << (i & 31);
			for (int j = 0; j < sup; j += tp) {
				for (int i = 0; i < tp && i + j < sup; i++) {
					isnp[j + i] |= ptn[i];
				}
			}
		}

		// 3,5,7
		// 2x+3=n
		int[] magic = { 0, 1, 23, 2, 29, 24, 19, 3, 30, 27, 25, 11, 20, 8, 4, 13, 31, 22, 28, 18, 26, 10, 7, 12, 21, 17,
				9, 6, 16, 5, 15, 14 };
		int h = n / 2;
		for (int i = 0; i < sup; i++) {
			for (int j = ~isnp[i]; j != 0; j &= j - 1) {
				int pp = i << 5 | magic[(j & -j) * 0x076be629 >>> 27];
				int p = 2 * pp + 3;
				if (p > n)
					break;
				ret[pos++] = p;
				if ((long) p * p > n)
					continue;
				for (int q = (p * p - 3) / 2; q <= h; q += p)
					isnp[q >> 5] |= 1 << q;
			}
		}

		return Arrays.copyOf(ret, pos);
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
