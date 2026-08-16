import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.InputMismatchException;

public class Main {
	static InputStream is;
	static PrintWriter out;
	static String INPUT = "";
	
	static void solve()
	{
		int n = ni();
		int[][] ls = new int[n][];
		for(int i = 0;i < n;i++){
			ls[i] = new int[]{ni(), ni(), ni(), -1};
		}
		
		{
			Arrays.sort(ls, new Comparator<int[]>() {
				public int compare(int[] a, int[] b) {
					return Double.compare(-(double)a[0] / a[1], 
							-(double)b[0] / b[1]);
				}
			});
			for(int i = 0;i < n;i++){
				ls[i][3] = i;
			}
			
			double low = -1e9, high = 2e9;
			for(int rep = 0;rep < 100;rep++){
				double x = low + (high-low)/2;
				if(count(ls, x) >= ((long)n*(n-1)/2+1)/2){
					high = x;
				}else{
					low = x;
				}
			}
			out.printf("%.14f ", low);
		}
		
		for(int i = 0;i < n;i++){
			int u = ls[i][0]; ls[i][0] = ls[i][1]; ls[i][1] = u;
		}
		{
			Arrays.sort(ls, new Comparator<int[]>() {
				public int compare(int[] a, int[] b) {
					return Double.compare(-(double)a[0] / a[1], 
							-(double)b[0] / b[1]);
				}
			});
			for(int i = 0;i < n;i++){
				ls[i][3] = i;
			}
			
			double low = -1e9, high = 2e9;
			for(int rep = 0;rep < 100;rep++){
				double x = low + (high-low)/2;
				if(count(ls, x) >= ((long)n*(n-1)/2+1)/2){
					high = x;
				}else{
					low = x;
				}
			}
			out.printf("%.14f\n", low);
		}
	}
	
	static long count(int[][] ls, double x)
	{
		int n = ls.length;
		double[][] ys = new double[n][];
		for(int i = 0;i < n;i++){
			ys[i] = new double[]{(ls[i][2] - ls[i][0] * x) / ls[i][1], ls[i][3]};
		}
		Arrays.sort(ys, new Comparator<double[]>() {
			public int compare(double[] a, double[] b) {
				return Double.compare(a[0], b[0]);
			}
		});
		int[] ft = new int[n+3];
		long ret = 0;
		for(double[] y : ys){
			int q = (int)y[1];
			ret += sumFenwick(ft, q);
			addFenwick(ft, q, 1);
		}
		return ret;
	}
	
	public static int sumFenwick(int[] ft, int i)
	{
		int sum = 0;
		for(i++;i > 0;i -= i&-i)sum += ft[i];
		return sum;
	}
	
	public static void addFenwick(int[] ft, int i, int v)
	{
		if(v == 0 || i < 0)return;
		int n = ft.length;
		for(i++;i < n;i += i&-i)ft[i] += v;
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
