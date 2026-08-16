import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;

public class Main {

	public static void main(String[] args) {
		IO io = new IO();
		int n = io.nextInt();
		double W = io.nextInt();
		double V = 0;
		ArrayList<Pair> al = new ArrayList<Pair>();
		for(int i=0;i<n;i++) {
			int w = io.nextInt();
			int v = io.nextInt();
			if (w <= 0 && v >= 0) {
				W -= w;
				V += v;
			}else if(w < 0 && v < 0) {
				W -= w;
				V += v;
				al.add(new Pair(-w, -v));
			}else if(w > 0 && v > 0) {
				al.add(new Pair(w, v));
			}
		}
		Collections.sort(al,new Comparator<Pair>() {
			public int compare(Pair o1, Pair o2) {
				return - Double.compare((double) o1.v / o1.w, (double) o2.v / o2.w) ;
			}
		});
		for(Pair p:al) {
			double m = Math.min(1, W / p.w);
			V += m * p.v;
			W -= m * p.w;
			if (W < 1E-10) {
				break;
			}
		}
		System.out.println(new DecimalFormat("0.00000").format(V));
	}

	static class Pair {
		int w,v;
		public Pair(int w,int v) {
			this.w = w;
			this.v = v;
		}
	}

}
class IO {
	private final InputStream in;
	private final PrintWriter out = new PrintWriter(System.out);
	private final byte[] buffer = new byte[1024];
	private int ptr = 0;
	private int buflen = 0;

	public IO() { this(System.in);}
	public IO(InputStream source) { this.in = source;}
	private boolean hasNextByte() {
		if (ptr < buflen) {
			return true;
		}else{
			ptr = 0;
			try {
				buflen = in.read(buffer);
			} catch (IOException e) {
				e.printStackTrace();
			}
			if (buflen <= 0) {
				return false;
			}
		}
		return true;
	}
	private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
	private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
	private static boolean isNewLine(int c) { return c == '\n' || c == '\r';}
	private void skipUnprintable() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;}
	private void skipNewLine() { while(hasNextByte() && isNewLine(buffer[ptr])) ptr++;}
	public boolean hasNext() { skipUnprintable(); return hasNextByte();}
	public boolean hasNextLine() { skipNewLine(); return hasNextByte();}
	public String next() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while(isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	public char[] nextCharArray(int len) {
		char[] s = new char[len];
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		int i = 0;
		int b = readByte();
		while(isPrintableChar(b)) {
			if (i == len) {
				throw new InputMismatchException();
			}
			s[i++] = (char) b;
			b = readByte();
		}
		return s;
	}
	public String nextLine() {
		if (!hasNextLine()) {
			throw new NoSuchElementException();
		}
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while(!isNewLine(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	public long nextLong() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		long n = 0;
		boolean minus = false;
		int b = readByte();
		if (b == '-') {
			minus = true;
			b = readByte();
		}
		if (b < '0' || '9' < b) {
			throw new NumberFormatException();
		}
		while(true){
			if ('0' <= b && b <= '9') {
				n *= 10;
				n += b - '0';
			}else if(b == -1 || !isPrintableChar(b)){
				return minus ? -n : n;
			}else{
				throw new NumberFormatException();
			}
			b = readByte();
		}
	}
	public int nextInt() {
		long nl = nextLong();
		if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) {
			throw new NumberFormatException();
		}
		return (int) nl;
	}
	public char nextChar() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		return (char) readByte();
	}
	public double nextDouble() { return Double.parseDouble(next());}
	public int[] arrayInt(int n) { int[] a = new int[n]; for(int i=0;i<n;i++) a[i] = nextInt(); return a;}
	public long[] arrayLong(int n) { long[] a = new long[n]; for(int i=0;i<n;i++) a[i] = nextLong(); return a;}
	public double[] arrayDouble(int n) { double[] a = new double[n]; for(int i=0;i<n;i++) a[i] = nextDouble(); return a;}
	public void arrayInt(int[]... a) {for(int i=0;i<a[0].length;i++) for(int j=0;j<a.length;j++) a[j][i] = nextInt();}
	public int[][] matrixInt(int n,int m) { int[][] a = new int[n][m]; for(int i=0;i<n;i++) a[i] = arrayInt(m); return a;}
	public char[][] charMap(int n,int m) { char[][] a = new char[n][m]; for(int i=0;i<n;i++) a[i] = nextCharArray(m); return a;}
	public void println(long x) { out.println(x);}
	public void println(double x) { out.println(x);}
	public void println(String s) { out.println(s);}
	public void println() { out.println(); }
	public void print(long x) { out.print(x); }
	public void print(double x) { out.print(x); }
	public void print(String s) { out.print(s); }
	public void print(char c) {out.print(c);}
	public void flush() {out.flush(); }
}