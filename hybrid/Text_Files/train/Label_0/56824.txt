import java.io.*;
import java.util.*;
public class Main {
	 public static void main(String[] args) throws Exception {
	        InputReader in = new InputReader(System.in);
	        OutputWriter out = new OutputWriter(System.out);
	        Task Solver = new Task();
	        Solver.solve(in,out);
			out.close();
	 }
}
class Task{
	int m, d;
	final int M = 1000000007;
	String a, b;
	int dp[][][][];
	public void solve(InputReader in, OutputWriter out) {
		m = in.readInt();
        d = in.readInt();
        a = in.readString();
        b = in.readString();
        dp = new int [2][2][2002][2002];
        for(int i = 0; i < 2; ++i) {
        	for(int j = 0; j < 2; ++j) {
        		for(int k = 0; k < 2002; ++k) {
        			for(int l = 0; l < 2002; ++l) dp[i][j][k][l] =  -1;
        		}
        	}
        }
		out.printLine(solve(0,0,1,1));
	}
	private int solve(int pos, int mod, int lb, int rb) {
		if(pos == a.length())  return mod == 0 ? 1 : 0;
		if(dp[lb][rb][pos][mod] != -1) return dp[lb][rb][pos][mod];
		int ret = 0;
		int s = (lb == 1) ? a.charAt(pos) - '0' : 0;
		int e = (rb == 1) ? b.charAt(pos) - '0' : 9;
		for(int i = s; i <= e; ++i) {
			if((pos % 2 == 0) && (i == d)) continue;
			if((pos % 2 == 1) && (i != d)) continue;
			ret += solve(pos + 1, ((mod * 10 + i) % m), (lb & ((i == s) ? 1 : 0)), (rb & ((i == e) ? 1 : 0)) );
			ret %= M;
		}
		return dp[lb][rb][pos][mod] = ret;
	}
}
class InputReader {
	private InputStream stream;
	private byte[] buf = new byte[1024];
	private int curChar;
	private int numChars;
	private SpaceCharFilter filter;
	public InputReader(InputStream stream) {
		this.stream = stream;
	}
	public int read() {
		if (numChars == -1) {
			throw new InputMismatchException();
		}
		if (curChar >= numChars) {
			curChar = 0;
			try {
				numChars = stream.read(buf);
			} catch (IOException e) {
				throw new InputMismatchException();
			}
			if (numChars <= 0) {
				return -1;
			}
		}
		return buf[curChar++];
	}
	public int readInt() {
		int c = read();
		while (isSpaceChar(c)) {
			c = read();
		}
		int sgn = 1;
		if (c == '-') {
			sgn = -1;
			c = read();
		}
		int res = 0;
		do {
			if (c < '0' || c > '9') {
				throw new InputMismatchException();
			}
			res *= 10;
			res += c - '0';
			c = read();
		} while (!isSpaceChar(c));
		return res * sgn;
	}
	public String readString() {
		int c = read();
		while (isSpaceChar(c)) {
			c = read();
		}
		StringBuilder res = new StringBuilder();
		do {
			res.appendCodePoint(c);
			c = read();
		} while (!isSpaceChar(c));
		return res.toString();
	}
	public double readDouble() {
		int c = read();
		while (isSpaceChar(c)) {
			c = read();
		}
		int sgn = 1;
		if (c == '-') {
			sgn = -1;
			c = read();
		}
		double res = 0;
		while (!isSpaceChar(c) && c != '.') {
			if (c == 'e' || c == 'E') {
				return res * Math.pow(10, readInt());
			}
			if (c < '0' || c > '9') {
				throw new InputMismatchException();
			}
			res *= 10;
			res += c - '0';
			c = read();
		}
		if (c == '.') {
			c = read();
			double m = 1;
			while (!isSpaceChar(c)) {
				if (c == 'e' || c == 'E') {
					return res * Math.pow(10, readInt());
				}
				if (c < '0' || c > '9') {
					throw new InputMismatchException();
				}
				m /= 10;
				res += (c - '0') * m;
				c = read();
			}
		}
		return res * sgn;
	}
	public long readLong() {
		int c = read();
		while (isSpaceChar(c)) {
			c = read();
		}
		int sgn = 1;
		if (c == '-') {
			sgn = -1;
			c = read();
		}
		long res = 0;
		do {
			if (c < '0' || c > '9') {
				throw new InputMismatchException();
			}
			res *= 10;
			res += c - '0';
			c = read();
		} while (!isSpaceChar(c));
		return res * sgn;
	}
	
	public boolean isSpaceChar(int c) {
		if (filter != null) {
			return filter.isSpaceChar(c);
		}
		return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
	}
	public String next() {
		return readString();
	}
	
	public interface SpaceCharFilter {
		public boolean isSpaceChar(int ch);
	}
}
class OutputWriter {
	private final PrintWriter writer;
	
	public OutputWriter(OutputStream outputStream) {
		writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
	}
	public OutputWriter(Writer writer) {
		this.writer = new PrintWriter(writer);
	}
	public void print(Object... objects) {
		for (int i = 0; i < objects.length; i++) {
			if (i != 0) {
				writer.print(' ');
				}
				writer.print(objects[i]);
			}
			writer.flush();
		}
		public void printLine(Object... objects) {
			print(objects);
			writer.println();
			writer.flush();
		}
		public void close() {
			writer.close();
		}
		public void flush() {
			writer.flush();
		}
	}