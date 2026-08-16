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
		int n = ni(), D = ni();
		int[][] f = new int[D][D];
		for(int i = 0;i < n;i++){
			int x = ni(), y = ni();
			x %= D; y %= D;
			if(x < 0)x += D;
			if(y < 0)y += D;
			f[x][y]++;
		}
		
		int low = -1, high = D*1000;
		while(high - low > 1){
			int h = high+low>>1;
			if(ok(h, f)){
				high = h;
			}else{
				low = h;
			}
		}
		out.println(high);
	}
	
	static boolean ok(int h, int[][] f)
	{
		int D = f.length;
		// f <= ((h-dx)/D+1)*((h-dy)/D+1)
		int[][] imos = new int[2*D+1][2*D+1];
		int dx = h%D;
		// [0,dx],[0,dx]
		for(int i = 0;i < D;i++){
			for(int j = 0;j < D;j++){
				if((long)(h/D+1)*(h/D+1) >= f[i][j]){
					imos[D+i-dx][D+j-dx]++;
					imos[D+i+1][D+j-dx]--;
					imos[D+i-dx][D+j+1]--;
					imos[D+i+1][D+j+1]++;
				}
				if((long)(h/D+1)*(h/D) >= f[i][j]){
					imos[i+1][D+j-dx]++;
					imos[D+i-dx][D+j-dx]--;
					imos[i+1][D+j+1]--;
					imos[D+i-dx][D+j+1]++;
					
					imos[D+i-dx][j+1]++;
					imos[D+i+1][j+1]--;
					imos[D+i-dx][D+j-dx]--;
					imos[D+i+1][D+j-dx]++;
				}
				if((long)(h/D)*(h/D) >= f[i][j]){
					imos[i+1][j+1]++;
					imos[D+i-dx][j+1]--;
					imos[i+1][D+j-dx]--;
					imos[D+i-dx][D+j-dx]++;
				}
			}
		}
		for(int i = 0;i <= 2*D;i++){
			for(int j = 0;j <= 2*D;j++){
				if(i > 0)imos[i][j] += imos[i-1][j];
				if(j > 0)imos[i][j] += imos[i][j-1];
				if(i > 0 && j > 0)imos[i][j] -= imos[i-1][j-1];
			}
		}
		for(int i = 0;i < D;i++){
			for(int j = 0;j < D;j++){
				if(imos[i][j] + imos[i+D][j] + imos[i][j+D] + imos[i+D][j+D] == D*D){
					return true;
				}
			}
		}
		return false;
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
