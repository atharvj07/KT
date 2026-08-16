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
	
	static long[] pows;
	
	static void solve()
	{
		int L = 30;
		pows = new long[31];
		pows[0] = 1;
		for(int i = 1;i < 31;i++)pows[i] = pows[i-1] * 3;
		for(int Q = ni();Q > 0;Q--){
			long A = nl()-1, B = nl()-1;
			long C = nl()-1, D = nl()-1;
			out.println(dfs(A, B, C, D, L));
		}
	}
	
	static Map<Long, Long> cache = new HashMap<>();
	
	static long dfs(long A, long B, long C, long D, int L)
	{
//		tr(A, B, C, D, L);
		if(L == 0){
			if(A == C && B == D)return 0;
			if(B == D && B == 1){
				return Math.abs(C-A) + 2;
			}else if(A == C && (A == 1 || A == 4)){
				return Math.abs(B-D) + 2;
			}
			return Math.abs(C-A) + Math.abs(D-B);
		}
		
		long code = 0;
		code = code * 1000000009 + A;
		code = code * 1000000009 + B;
		code = code * 1000000009 + C;
		code = code * 1000000009 + D;
		code = code * 1000000009 + L;
		if(cache.containsKey(code)){
			return cache.get(code);
		}
		long xa = A/pows[L-1];
		long ya = B/pows[L-1];
		long xb = C/pows[L-1];
		long yb = D/pows[L-1];
		if(xa > xb || xa == xb && ya > yb){
			return dfs(C, D, A, B, L);
		}
		if(xa == xb && ya == yb){
			return dfs(A-xa*pows[L-1], 
					B-ya*pows[L-1], 
					C-xb*pows[L-1], 
					D-yb*pows[L-1], L-1);
		}
		if(xa == 1 && xb == 1){
			return dfs(B, A, D, C, L);
		}
		long AA = A-xa*pows[L-1];
		long BB = B-ya*pows[L-1];
		long CC = C-xb*pows[L-1];
		long DD = D-yb*pows[L-1];
		if(ya == 1 && yb == 1){
//			if(xa > xb){
//				{long u = A; A = C; C = u;}
//				{long u = B; B = D; D = u;}
//				{long u = xa; xa = xb; xb = u;}
//			}
			if(xb - xa == 1){
				return dfs(AA, BB, CC + pows[L-1], DD, L-1);
			}
			long res = Math.min(
					dfs(
					A-xa*pows[L-1], B-ya*pows[L-1], 
					pows[L-1]-1, 0, L-1) + 
					dfs(0, 0, 
							C-xb*pows[L-1], D-yb*pows[L-1], L-1)
					+ (xb - xa - 1) * pows[L-1] + 3,
					dfs(
					A-xa*pows[L-1], B-ya*pows[L-1], 
					pows[L-1]-1, pows[L-1]-1, L-1) + 
					dfs(0, pows[L-1]-1, 
							C-xb*pows[L-1], D-yb*pows[L-1], L-1)
					+ (xb - xa - 1) * pows[L-1] + 3
					);
			cache.put(code, res);
			return res;
		}
//		tr(xa, ya, xb, yb);
		if(xa < xb){
			if(ya < yb){
				long res = dfs(AA, BB, pows[L-1]-1, pows[L-1]-1, L-1) +
						dfs(0, 0, CC, DD, L-1) + 2 + (xb-xa+yb-ya-2) *pows[L-1];
				cache.put(code, res);
				return res;
			}else if(ya > yb){
				long res = dfs(AA, BB, pows[L-1]-1, 0, L-1) +
						dfs(0, pows[L-1]-1, CC, DD, L-1) + 2 + (xb-xa+ya-yb-2) *pows[L-1];
				cache.put(code, res);
				return res;
			}else{
				long res = dfs(A, BB, C, DD, L-1);
				cache.put(code, res);
				return res;
			}
		}else{
//			long res = dfs(BB, AA, DD + pows[L-1], CC, L-1) + (yb-ya-1) * pows[L-1];
			long res = dfs(B, AA, D, CC, L-1);
			cache.put(code, res);
			return res;
		}
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
