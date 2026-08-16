import java.awt.geom.Point2D;
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
//		int Z = 5000000;
//		double[] ras = new double[Z];
//		for(int i = 1;i < Z;i++){
//			ras[i] = (1-Math.sin(Math.PI/i))/(1+Math.sin(Math.PI/i));
//		}
//		tr(ras);
		// c+1/(c-R),c+1/(c+R)
		// c+1/(c+r),c+1/(c-r)
		// 1/(c+R)-1/(c-R)=RB
		// 1/(c-r)-1/(c+r)=RA
		// distance = (sum(c+1/(c+r),c+1/(c-r))-sum(c+1/(c-R),c+1/(c+R)))/2
		// (1/(c+r)+1/(c-r)-1/(c-R)-1/(c+R))/2 = D
		// 2D+RA+RB = 2/(c-r)-2/(c-R)
		// 2D-RA-RB = 2/(c+r)-2/(c+R)
		
		// A-B=RB
		// C-D=RA
		
		// -2R/(c+R)(c-R)=RB
		// 2r/(c+r)(c-r)=RA
		// c/(c+r)(c-r)-c/(c-R)(c+R) = D
		
		for(int T = ni();T > 0;T--){
			double xa = nd();
			double ya = nd();
			double ra = nd();
			double xb = nd();
			double yb = nd();
			double rb = nd();
			if(ra > rb){
				double du = ra; ra = rb; rb = du;
			}
			double D = Point2D.distance(xa, ya, xb, yb);
			// (0,0,ra)
			// (d,0,rb)
			double low = 0, high = 1e8;
			for(int rep = 0;rep < 100;rep++){
				double c = (low+high)/2;
				// 1/(c+R)-1/(c-R)=2RB=-2R/(c+R)(c-R)
				// c^2*2RB-R^2*2RB=-2R
				// R^2=(c^2*RB+R)/RB=(c^2+R/RB)
				// 1/(c-r)-1/(c+r)=2RA=2r/(c+r)(c-r)
				// c^2*2RA-r^2*2RA=2r
				// r^2=(-r/RA+c^2)
				// (1/(c+r)+1/(c-r)-1/(c-R)-1/(c+R))/2 = D
				double R = (1./2/rb+Math.sqrt(1/rb/rb/4+c*c));
				double r = (-1./2/ra+Math.sqrt(1/ra/ra/4+c*c));
//				double R = (1+Math.sqrt(1+4*rb*rb*c*c))/2/rb;
//				double r = (-1+Math.sqrt(1+4*ra*ra*c*c))/2/ra;
//				tr(c, r < c, c < R, (1./(c+r)+1./(c-r)-1./(c-R)-1./(c+R))/2-D);
//				double comp = (c/(c*c-r*r)-c/(c*c-R*R))-D;
				double comp = (c*ra/r+c*rb/R)-D;
//				tr(c, comp);
				if(comp > 0){
					low = c;
				}else{
					high = c;
				}
			}
			double c = low;
			double R = (1./2/rb+Math.sqrt(1/rb/rb/4+c*c));
			double r = (-1./2/ra+Math.sqrt(1/ra/ra/4+c*c));
//			tr((1./(c+r)+1./(c-r)-1./(c-R)-1./(c+R))/2);
			
			double ratio = r/R;
			
//			tr(ratio);
			long llow = 2, lhigh = 1000000000L;
			while(lhigh - llow > 1){
				long lh = lhigh+llow>>1;
				double si = Math.sin(Math.PI/lh);
				double rz = (1-si)/(1+si);
				if(rz < ratio){
					llow = lh;
				}else{
					lhigh = lh;
				}
			}
			out.println(llow);
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
