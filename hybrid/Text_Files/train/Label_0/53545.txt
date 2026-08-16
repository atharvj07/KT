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
		int n = ni(), K = ni();
		int[] a = na(n);

		int[][] ai = new int[n][];
		for(int i = 0;i < n;i++){
			ai[i] = new int[]{a[i], i};
		}
		Arrays.sort(ai, (x, y) -> {
			if (x[0] != y[0]) return x[0] - y[0];
			return (x[1] - y[1]);
		});

		int mod = 998244353;
		long P = mod+1-invl(K, mod);
		P %= mod;

		long[] pows = enumPows(P, n+5, mod);
		long[] ft = new long[n+5];
		long[] ift = new long[n+5];
		long[] nft = new long[n+5];
		long ans = invl(2, mod) * ((long)n*(n-1)/2%mod) % mod;
		long escp = 0;
		for(int[] u : ai){
			int pos = Math.max(u[1], K-1);
			{
				long nh = sumFenwick(nft, n) - sumFenwick(nft, pos) + mod;
				long h = sumFenwick(ft, n) - sumFenwick(ft, pos) + mod;
				h = h * invl(pows[pos], mod) % mod;
				escp += nh;
				escp -= h;
			}
			{
				long nh = sumFenwick(nft, pos-1);
				long h = sumFenwick(ift, pos-1);
				h = h * pows[pos] % mod;
				escp -= nh;
				escp += h;
			}
			addFenwick(ft, pos, pows[pos]);
			addFenwick(ift, pos, invl(pows[pos], mod));
			addFenwick(nft, pos, 1);
//			tr(escp%mod, guessFrac(escp, mod));
		}
		// 3/2
		// -1/4

		escp %= mod;
		if(escp < 0)escp += mod;
		out.println((escp * invl(2, mod) % mod + ans) % mod);
	}

	public static long[] guessFrac(long n, int mod)
	{
		long min = mod;
		long argnum = -1, argden = 0;
		for(int den = 1;den <= 200000;den++){
			long num = n*den%mod;
			if(num*2 >= mod)num -= mod;
			if(Math.abs(num) + den < min){
				min = Math.abs(num) + den;
				argnum = num;
				argden = den;
			}
		}
		return argden == 0 ? null : new long[]{argnum, argden};
	}


	public static long[] enumPows(long a, int n, int mod)
	{
		a %= mod;
		long[] pows = new long[n+1];
		pows[0] = 1;
		for(int i = 1;i <= n;i++)pows[i] = pows[i-1] * a % mod;
		return pows;
	}


	public static final int mod = 998244353;

	public static long sumFenwick(long[] ft, int i)
	{
		long sum = 0;
		for(i++;i > 0;i -= i&-i){
			sum += ft[i];
			if(sum >= mod)sum -= mod;
		}
		return sum;
	}

	public static void addFenwick(long[] ft, int l, int r, long v)
	{
		addFenwick(ft, l, v);
		addFenwick(ft, r, -v);
	}

	public static void addFenwick(long[] ft, int i, long v)
	{
		v %= mod;
		if(v < 0)v += mod;
		if(v == 0)return;
		int n = ft.length;
		for(i++;i < n;i += i&-i){
			ft[i] += v;
			if(ft[i] >= mod)ft[i] -= mod;
		}
	}


	public static long invl(long a, long mod) {
		long b = mod;
		long p = 1, q = 0;
		while (b > 0) {
			long c = a / b;
			long d;
			d = a;
			a = b;
			b = d % b;
			d = p;
			p = q;
			q = d - c * q;
		}
		return p < 0 ? p + mod : p;
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
