//################################################################################################################
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.io.Writer;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.InputMismatchException;

//################################################################################################################
public class R271D2B {
	public static void main(String[] args) {
		R271D2B b = new R271D2B();
		InputReader1 reader = b.new InputReader1(System.in);
		OutputWriter writer = b.new OutputWriter(System.out);
		// put your code here
		int n = reader.readInt();
		int[] csum = new int[n];
		csum[0] = reader.readInt();
		for (int i = 1; i < csum.length; i++) {
			csum[i] = csum[i - 1] + reader.readInt();
		}
		int m = reader.readInt();
		for (int i = 0; i < m; i++) {
			int tmp = reader.readInt();
			int index = Arrays.binarySearch(csum, tmp);
			if (index >= 0) {
				writer.println(index + 1);
			} else {
				index = ~index;
				writer.println(index + 1);
			}
		}
		reader.close();
		writer.close();
	}

	class InputReader1 {
		// private final boolean finished = false;

		private InputStream stream;
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;

		public InputReader1(InputStream stream) {
			this.stream = stream;
		}

		public int read() {
			if (numChars == -1)
				throw new InputMismatchException();
			if (curChar >= numChars) {
				curChar = 0;
				try {
					numChars = stream.read(buf);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (numChars <= 0)
					return -1;
			}
			return buf[curChar++];
		}

		public int peek() {
			if (numChars == -1)
				return -1;
			if (curChar >= numChars) {
				curChar = 0;
				try {
					numChars = stream.read(buf);
				} catch (IOException e) {
					return -1;
				}
				if (numChars <= 0)
					return -1;
			}
			return buf[curChar];
		}

		public int readInt() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			int res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public long readLong() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			long res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public String readString() {
			int length = readInt();
			if (length < 0)
				return null;
			byte[] bytes = new byte[length];
			for (int i = 0; i < length; i++)
				bytes[i] = (byte) read();
			try {
				return new String(bytes, "UTF-8");
			} catch (UnsupportedEncodingException e) {
				return new String(bytes);
			}
		}

		public boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		private String readLine0() {
			StringBuffer buf = new StringBuffer();
			int c = read();
			while (c != '\n' && c != -1) {
				if (c != '\r')
					buf.appendCodePoint(c);
				c = read();
			}
			return buf.toString();
		}

		public String readLine() {
			String s = readLine0();
			while (s.trim().length() == 0)
				s = readLine0();
			return s;
		}

		public String readLine(boolean ignoreEmptyLines) {
			if (ignoreEmptyLines)
				return readLine();
			else
				return readLine0();
		}

		public BigInteger readBigInteger() {
			try {
				return new BigInteger(readString());
			} catch (NumberFormatException e) {
				throw new InputMismatchException();
			}
		}

		public char readCharacter() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			return (char) c;
		}

		public double readDouble() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			double res = 0;
			while (!isSpaceChar(c) && c != '.') {
				if (c == 'e' || c == 'E')
					return res * Math.pow(10, readInt());
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}
			if (c == '.') {
				c = read();
				double m = 1;
				while (!isSpaceChar(c)) {
					if (c == 'e' || c == 'E')
						return res * Math.pow(10, readInt());
					if (c < '0' || c > '9')
						throw new InputMismatchException();
					m /= 10;
					res += (c - '0') * m;
					c = read();
				}
			}
			return res * sgn;
		}

		public boolean isExhausted() {
			int value;
			while (isSpaceChar(value = peek()) && value != -1)
				read();
			return value == -1;
		}

		public String next() {
			return readString();
		}

		public boolean readBoolean() {
			return readInt() == 1;
		}

		public void close() {
			try {
				stream.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}

	class OutputWriter {
		private final PrintWriter writer;

		public OutputWriter(OutputStream stream) {
			writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(
					stream)));
		}

		public OutputWriter(Writer writer) {
			this.writer = new PrintWriter(writer);
		}

		public void println(String s) {
			writer.println(s);
		}

		public void println(int x) {
			writer.println(x);
		}

		public void print(int x) {
			writer.print(x);
		}

		public void println(long x) {
			writer.println(x);
		}

		public void printSpace() {
			writer.print(" ");
		}

		public void close() {
			writer.close();
		}
	}
}
