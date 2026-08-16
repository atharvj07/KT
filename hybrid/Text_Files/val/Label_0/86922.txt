import java.io.*;
import java.util.*;

public class Main
{
	static final boolean INPUT_FROM_FILE = false;
	static final String INPUT_FILE = "input/input.txt";
	static final String OUTPUT_FILE = "input/output.txt";
	static FastReader in;
	static FastWriter out;

	static
	{
		try
		{
			in = new FastReader();
			out = new FastWriter();
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}

	public static void main(String[] args) throws IOException
	{

		int t = in.nextInt();
		while (t-- > 0) solve();
		out.close();
	}


	private static void solve()
	{
		int a = in.nextInt();
		int b = in.nextInt();
		int c = in.nextInt();
		int d = in.nextInt();
		out.println(Math.max(a+b, c+d));
	}


	static class FastReader
	{
		private InputStream stream;
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;
		private SpaceCharFilter filter;
		private BufferedReader br;

		public FastReader() throws FileNotFoundException
		{
			if (INPUT_FROM_FILE)
			{
				this.stream = new FileInputStream(INPUT_FILE);
				br = new BufferedReader(new FileReader(INPUT_FILE));
			} else
			{
				this.stream = System.in;
				br = new BufferedReader(new InputStreamReader(System.in));
			}
		}

		public int read()
		{
			if (numChars == -1)
				throw new InputMismatchException();

			if (curChar >= numChars)
			{
				curChar = 0;
				try
				{
					numChars = stream.read(buf);
				}
				catch (IOException e)
				{
					throw new InputMismatchException();
				}

				if (numChars <= 0)
					return -1;
			}
			return buf[curChar++];
		}

		public String nextLine()
		{
			String str = "";
			try
			{
				str = br.readLine();
			}
			catch (IOException e)
			{
				e.printStackTrace();
			}
			return str;
		}

		public int nextInt()
		{
			int c = read();

			while (isSpaceChar(c))
				c = read();

			int sgn = 1;

			if (c == '-')
			{
				sgn = -1;
				c = read();
			}

			int res = 0;
			do
			{
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}
			while (!isSpaceChar(c));

			return res * sgn;
		}

		public long nextLong()
		{
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-')
			{
				sgn = -1;
				c = read();
			}
			long res = 0;

			do
			{
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}
			while (!isSpaceChar(c));
			return res * sgn;
		}

		public double nextDouble()
		{
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-')
			{
				sgn = -1;
				c = read();
			}
			double res = 0;
			while (!isSpaceChar(c) && c != '.')
			{
				if (c == 'e' || c == 'E')
					return res * Math.pow(10, nextInt());
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}
			if (c == '.')
			{
				c = read();
				double m = 1;
				while (!isSpaceChar(c))
				{
					if (c == 'e' || c == 'E')
						return res * Math.pow(10, nextInt());
					if (c < '0' || c > '9')
						throw new InputMismatchException();
					m /= 10;
					res += (c - '0') * m;
					c = read();
				}
			}
			return res * sgn;
		}

		public String readString()
		{
			int c = read();
			while (isSpaceChar(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do
			{
				res.appendCodePoint(c);
				c = read();
			}
			while (!isSpaceChar(c));

			return res.toString();
		}

		public boolean isSpaceChar(int c)
		{
			if (filter != null)
				return filter.isSpaceChar(c);
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		public String next()
		{
			return readString();
		}

		public interface SpaceCharFilter
		{
			boolean isSpaceChar(int ch);
		}
	}

	static class FastWriter
	{
		BufferedWriter writer;
		StringBuilder sb;

		public FastWriter() throws IOException
		{
			if (INPUT_FROM_FILE) writer = new BufferedWriter(new FileWriter(OUTPUT_FILE));
			else writer = new BufferedWriter(new PrintWriter(System.out));
			sb = new StringBuilder();
		}

		public void print(Object obj)
		{
			sb.append(obj);
		}

		public void println(Object obj)
		{
			sb.append(obj).append('\n');
		}

		public void close() throws IOException
		{
			writer.write(sb.toString());
			writer.close();
		}
	}
}

