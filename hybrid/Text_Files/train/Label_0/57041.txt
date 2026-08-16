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
	
	static Map<Long, Integer> dp = new HashMap<>();
	
	static void solve()
	{
		int n = ni();
		char[][] map = nm(n,n);
		int[][] cum = new int[n+1][n+1];
		for(int i = 0;i < n;i++){
			for(int j = 0;j < n;j++){
				cum[i+1][j+1] = (map[i][j]=='x'?1:0) + cum[i][j+1] + cum[i+1][j] - cum[i][j];
			}
		}
		out.println(dfs(0, 0, n, n, cum));
	}
	
	static int dfs(int r1, int c1, int r2, int c2, int[][] cum)
	{
		long code = (long)r1<<24|c1<<16|r2<<8|c2;
		if(dp.containsKey(code))return dp.get(code);
		if(cum[r2][c2] + cum[r1][c1] - cum[r2][c1] - cum[r1][c2] == 0){
			dp.put(code, 0);
			return 0;
		}
		
		int min = 999999999;
		for(int i = r1;i < r2;i++){
			for(int j = c1;j < c2;j++){
				// i,c1,i+1,c2
				if(cum[i+1][c2] + cum[i][c1] - cum[i+1][c1] - cum[i][c2] == c2 - c1){
					if(cum[r2][j+1] + cum[r1][j] - cum[r1][j+1] - cum[r2][j] == r2 - r1){
						int u = 1;
						{
							int v = dfs(r1, c1, i, j, cum);
							if(v < 0)continue;
							u += v;
						}
						{
							int v = dfs(r1, j+1, i, c2, cum);
							if(v < 0)continue;
							u += v;
						}
						{
							int v = dfs(i+1, c1, r2, j, cum);
							if(v < 0)continue;
							u += v;
						}
						{
							int v = dfs(i+1, j+1, r2, c2, cum);
							if(v < 0)continue;
							u += v;
						}
						min = Math.min(min, u);
					}
				}
			}
		}
		if(min < 9999999){
			dp.put(code, min);
			return min;
		}
		
		dp.put(code, -1);
		return -1;
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
	public static int lenbuf = 0, ptrbuf = 0;
	
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
	private static int skip() { int b; while((b = readByte()) != -1 && isSpaceChar(b)); return b; }
	
	private static double nd() { return Double.parseDouble(ns()); }
	private static char nc() { return (char)skip(); }
	
	private static String ns()
	{
		int b = skip();
		StringBuilder sb = new StringBuilder();
		while(!(isSpaceChar(b))){ // when nextLine, (isSpaceChar(b) && b != ' ')
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