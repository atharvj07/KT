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
	
	static void solve()
	{
		int n = ni();
		int[][] co = new int[n][];
		int[] dx = { 1, 0, -1, 0 };
		int[] dy = { 0, 1, 0, -1 };
		String D = "RULD";
		
		for(int i = 0;i < n;i++){
			int x = ni(), y = ni();
			int dir = D.indexOf(nc());
			co[i] = new int[]{x, y, dx[dir], dy[dir]};
		}
		
		int ans = Integer.MAX_VALUE;
		ans = Math.min(ans, xcor(co));
		for(int i = 0;i < n;i++){
			{int d = co[i][0]; co[i][0] = co[i][1]; co[i][1] = d;}
			{int d = co[i][2]; co[i][2] = co[i][3]; co[i][3] = d;}
		}
		ans = Math.min(ans, xcor(co));
		
		ans = Math.min(ans, xycor(co));
		for(int i = 0;i < n;i++){
			co[i][0] = -co[i][0];
			co[i][2] = -co[i][2];
		}
		ans = Math.min(ans, xycor(co));
		for(int i = 0;i < n;i++){
			co[i][1] = -co[i][1];
			co[i][3] = -co[i][3];
		}
		ans = Math.min(ans, xycor(co));
		for(int i = 0;i < n;i++){
			co[i][0] = -co[i][0];
			co[i][2] = -co[i][2];
		}
		ans = Math.min(ans, xycor(co));
		
		if(ans == Integer.MAX_VALUE){
			out.println("SAFE");
		}else{
			out.println(ans);
		}
	}
	
	static int xcor(int[][] co)
	{
		Arrays.sort(co, (x, y) -> {
			if(x[1] != y[1])return x[1] - y[1];
			return x[0] - y[0];
		});
		int n = co.length;
		int ans = Integer.MAX_VALUE;
		for(int i = 0;i < n;){
			int j = i;
			while(j < n && co[j][1] == co[i][1])j++;
			
			int pre = Integer.MIN_VALUE;
			for(int k = i;k < j;k++){
				if(co[k][2] == 1){
					pre = co[k][0];
				}else if(co[k][2] == -1){
					if(pre > Integer.MIN_VALUE){
						ans = Math.min(ans, (co[k][0] - pre) * 5);
					}
				}
			}
			
			i = j;
		}
		return ans;
	}
	
	static int xycor(int[][] co)
	{
		Arrays.sort(co, (x, y) -> {
			return x[0] - y[0];
		});
		int n = co.length;
		int ans = Integer.MAX_VALUE;
		// (s,t) (u,v)
		// s+t=u+v
		Map<Integer, Integer> map = new HashMap<>();
		for(int[] c : co){
			if(c[2] == 1){
				map.put(c[0]+c[1], c[0]);
			}else if(c[3] == 1){
				if(map.containsKey(c[0]+c[1])){
					ans = Math.min(ans, (c[0] - map.get(c[0]+c[1])) * 10);
				}
			}
		}
		return ans;
	}
	
	public static void main(String[] args) throws Exception
	{
//		int n = 200000, m = 99999;
//		Random gen = new Random();
//		StringBuilder sb = new StringBuilder();
//		sb.append(n + " ");
//		for (int i = 0; i < n; i++) {
//			sb.append(gen.nextInt(200001) + " ");
//			sb.append(gen.nextInt(200001) + " ");
//			sb.append("URDL".charAt(gen.nextInt(4)) + " ");
//		}
//		INPUT = sb.toString();

		
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
