
import java.io.*;
import java.math.*;
import java.util.*;

import static java.util.Arrays.*;

public class Main {
	private static final int mod = (int)1e9+7;

	final Random random = new Random(0);
	final IOFast io = new IOFast();

	/// MAIN CODE
	public void run() throws IOException {
//		int TEST_CASE = Integer.parseInt(new String(io.nextLine()).trim());
		int TEST_CASE = 1;
		while(TEST_CASE-- != 0) {
			Patricia p = new Patricia();
			int n = io.nextInt();
			char[][] cs = new char[n][];
			for(int i = 0; i < n; i++) {
				p.add(cs[i] = io.next());
//				if(i == n / 2) System.gc();
			}
			
			int[] prefix = new int[n];
			int[][] cnt = new int[n][26*26];
			for(int i = 0; i < n; i++) {
				Patricia cur = p;
				for(int j = 0; j < cs[i].length; ) {
					final int idx = Patricia.toIndex(cs[i][j]);
					for(int k = 0; k < Patricia.ALPHABET_SIZE; k++) {
						if(k != idx && cur.next[k] != null) {
							cnt[i][k*26+idx] += cur.next[k].cnt;
						}
					}
					cur = cur.next[Patricia.toIndex(cs[i][j])];
					j += cur.str.length;
					prefix[i] += cur.countTerminate();
//					dump(i, j, cur.str);
				}
			}
			
			int q = io.nextInt();
			for(int t = 0; t < q; t++) {
				int k = io.nextInt() - 1;
				char[] ps = io.next();
				int ans = prefix[k];
				for(int i = 0; i < ps.length; i++) {
					for(int j = i + 1; j < ps.length; j++) {
						ans += cnt[k][Patricia.toIndex(ps[i])*26+Patricia.toIndex(ps[j])];
					}
				}
				io.out.println(ans);
			}
		}
	}
	
	static
	public class Patricia {
		static int gid;
		static final int ALPHABET_SIZE = 26;
		
		final int id;
		int cnt;
		char[] str;
		Patricia[] next = new Patricia[ALPHABET_SIZE];
		
		public static int toIndex(char c) {
			return c - 'a';
		}
		
		public Patricia() {
			id = gid++;
			str = new char[0];
		}
		
		private Patricia(char[] cs, int start, int len) {
			str = Arrays.copyOfRange(cs, start, start + len);
			id = gid++;
		}
		
		public void add(char[] cs) {
			Patricia cur = this;
			cur.cnt++;
			if(cs.length == 0) return;
			for(int i = 0, j = 0; i < cs.length; ) {
				Patricia next = cur.next[toIndex(cs[j])];
				if(next == null) {
					cur.next[toIndex(cs[j])] = new Patricia(cs, j, cs.length - j);
					cur.next[toIndex(cs[j])].cnt++;
					return;
				}
				for(; ; i++) {
					if(i - j >= next.str.length) {
						break;
					}
					if(i >= cs.length || next.str[i - j] != cs[i]) {
						cur.next[toIndex(cs[j])] = next = next.split(i - j);
						break;
					}
				}
				j = i;
				next.cnt++;
				cur = next;
			}
		}
		
		private Patricia split(int len) {
			Patricia parent = new Patricia(str, 0, len);
			str = Arrays.copyOfRange(str, len, str.length);
			parent.next[toIndex(str[0])] = this;
			parent.cnt = this.cnt;
			return parent;
		}
		
		public int countTerminate() {
			int cnt = this.cnt;
			for(int i = 0; i < next.length; i++) {
				if(next[i] != null) {
					cnt -= next[i].cnt;
				}
			}
			return cnt;
		}
		
		public boolean find(char[] cs) {
			Patricia cur = this;
			int j = 0;
			for(int i = 0; i < cs.length; i++, j++) {
				if(i - j >= cur.str.length) {
					cur = cur.next[toIndex(cs[i])];
					if(cur == null) return false;
					j = 0;
				}
				if(cur.str[j] != cs[i]) {
					return false;
				}
			}
			if(j != cur.str.length) {
				return false;
			}
			return cur.countTerminate() != 0;
		}
		
		public void dump() {
			dump("");
		}
		
		public void dump(String indent) {
			Main.dump(indent, new String(str), cnt);
			for(int i = 0; i < next.length; i++) {
				if(next[i] != null) {
					next[i].dump(indent + "  ");
				}
			}
		}
	}
	
	/// TEMPLATE
	static int gcd(int n, int r) { return r == 0 ? n : gcd(r, n%r); }
	static long gcd(long n, long r) { return r == 0 ? n : gcd(r, n%r); }
	
	static <T> void swap(T[] x, int i, int j) { T t = x[i]; x[i] = x[j]; x[j] = t; }
	static void swap(int[] x, int i, int j) { int t = x[i]; x[i] = x[j]; x[j] = t; }

	void printArrayLn(int[] xs) { for(int i = 0; i < xs.length; i++) io.out.print(xs[i] + (i==xs.length-1?"\n":" ")); }
	void printArrayLn(long[] xs) { for(int i = 0; i < xs.length; i++) io.out.print(xs[i] + (i==xs.length-1?"\n":" ")); }
	
	static void dump(Object... o) { System.err.println(Arrays.deepToString(o)); } 
	
	void main() throws IOException {
		//		IOFast.setFileIO("rle-size.in", "rle-size.out");
		try { run(); }
		catch (EndOfFileRuntimeException e) { }
		io.out.flush();
	}
	public static void main(String[] args) throws IOException { new Main().main(); }
	
	static class EndOfFileRuntimeException extends RuntimeException {
		private static final long serialVersionUID = -8565341110209207657L; }

	static
	public class IOFast {
		private BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		private PrintWriter out = new PrintWriter(System.out);

		void setFileIn(String ins) throws IOException { in.close(); in = new BufferedReader(new FileReader(ins)); }
		void setFileOut(String outs) throws IOException { out.flush(); out.close(); out = new PrintWriter(new FileWriter(outs)); }
		void setFileIO(String ins, String outs) throws IOException { setFileIn(ins); setFileOut(outs); }

		private static int pos, readLen;
		private static final char[] buffer = new char[1024 * 8];
		private static char[] str = new char[500*8*2];
		private static boolean[] isDigit = new boolean[256];
		private static boolean[] isSpace = new boolean[256];
		private static boolean[] isLineSep = new boolean[256];

		static { for(int i = 0; i < 10; i++) { isDigit['0' + i] = true; } isDigit['-'] = true; isSpace[' '] = isSpace['\r'] = isSpace['\n'] = isSpace['\t'] = true; isLineSep['\r'] = isLineSep['\n'] = true; }
		public int read() throws IOException { if(pos >= readLen) { pos = 0; readLen = in.read(buffer); if(readLen <= 0) { throw new EndOfFileRuntimeException(); } } return buffer[pos++]; }
		public int nextInt() throws IOException { int len = 0; str[len++] = nextChar(); len = reads(len, isSpace); int i = 0; int ret = 0; if(str[0] == '-') { i = 1; } for(; i < len; i++) ret = ret * 10 + str[i] - '0'; if(str[0] == '-') { ret = -ret; } return ret; }
		public long nextLong() throws IOException { int len = 0; str[len++] = nextChar(); len = reads(len, isSpace); int i = 0; long ret = 0; if(str[0] == '-') { i = 1; } for(; i < len; i++) ret = ret * 10 + str[i] - '0'; if(str[0] == '-') { ret = -ret; } return ret; }
		public char nextChar() throws IOException { while(true) { final int c = read(); if(!isSpace[c]) { return (char)c; } } }
		int reads(int len, boolean[] accept) throws IOException { try { while(true) { final int c = read(); if(accept[c]) { break; } if(str.length == len) { char[] rep = new char[str.length * 3 / 2]; System.arraycopy(str, 0, rep, 0, str.length); str = rep; } str[len++] = (char)c; } } catch(EndOfFileRuntimeException e) { ; } return len; }
		int reads(char[] cs, int len, boolean[] accept) throws IOException { try { while(true) { final int c = read(); if(accept[c]) { break; } cs[len++] = (char)c; } } catch(EndOfFileRuntimeException e) { ; } return len; }
		public char[] nextLine() throws IOException { int len = 0; str[len++] = nextChar(); len = reads(len, isLineSep); try { if(str[len-1] == '\r') { len--; read(); } } catch(EndOfFileRuntimeException e) { ; } return Arrays.copyOf(str, len); }
		public String nextString() throws IOException { return new String(next()); }
		public char[] next() throws IOException { int len = 0; str[len++] = nextChar(); len = reads(len, isSpace); return Arrays.copyOf(str, len); }
//		public int next(char[] cs) throws IOException { int len = 0; cs[len++] = nextChar(); len = reads(cs, len, isSpace); return len; }
		public double nextDouble() throws IOException { return Double.parseDouble(nextString()); }
		public long[] nextLongArray(final int n) throws IOException { final long[] res = new long[n]; for(int i = 0; i < n; i++) { res[i] = nextLong(); } return res; }
		public int[] nextIntArray(final int n) throws IOException { final int[] res = new int[n]; for(int i = 0; i < n; i++) { res[i] = nextInt(); } return res; }
		public int[][] nextIntArray2D(final int n, final int k) throws IOException { final int[][] res = new int[n][]; for(int i = 0; i < n; i++) { res[i] = nextIntArray(k); } return res; }
		public int[][] nextIntArray2DWithIndex(final int n, final int k) throws IOException { final int[][] res = new int[n][k+1]; for(int i = 0; i < n; i++) { for(int j = 0; j < k; j++) { res[i][j] = nextInt(); } res[i][k] = i; } return res; }
		public double[] nextDoubleArray(final int n) throws IOException { final double[] res = new double[n]; for(int i = 0; i < n; i++) { res[i] = nextDouble(); } return res; }
	}
}
