
import java.io.*;
import java.math.*;
import java.util.*;

import static java.util.Arrays.fill;
import static java.lang.Math.*;
import static java.util.Arrays.sort;
import static java.util.Collections.sort;


public class C934 
{

	public static int mod = 1000000007;
	public static long INF = (1L << 60);
	static FastScanner2 in = new FastScanner2();
	static OutputWriter out = new OutputWriter(System.out);
	
	public static void main(String[] args) 
	{

		int n=in.nextInt();
		int[] arr=new int[n+1];
		for(int i=1;i<=n;i++)
		{
			arr[i]=in.nextInt();
		}
		int[] dp1=new int[n+1];
		int[] dp2=new int[n+1];
		int[] dp3=new int[n+1];
		int[] dp4=new int[n+1];
		for(int i=1;i<=n;i++)
		{
			dp4[i]=max(dp3[i-1], dp4[i-1])+((arr[i]==2)?1:0);
			dp3[i]=max(dp2[i-1], dp3[i-1])+((arr[i]==1)?1:0);
			dp2[i]=max(dp1[i-1], dp2[i-1])+((arr[i]==2)?1:0);
			dp1[i]=(arr[i]==1)?dp1[i-1]+1:dp1[i-1];
			//System.out.println(dp1[i]+" "+dp2[i]+" "+dp3[i]+" "+dp4[i]);
		}
		out.println(max(dp3[n], dp4[n]));
		out.close();

	}
	
	public static long pow(long x, long n) 
	{
		long res = 1;
		for (long p = x; n > 0; n >>= 1, p = (p * p)) 
		{
			if ((n & 1) != 0) 
			{
				res = (res * p);
			}
		}
		return res;
	}
	
	public static long pow(long x, long n, long mod) 
	{
		long res = 1;
		for (long p = x; n > 0; n >>= 1, p = (p * p) % mod) 
		{
			if ((n & 1) != 0) 
			{
				res = (res * p % mod);
			}
		}
		return res;
	}

	public static long gcd(long n1, long n2)
	{
		long r;
		while (n2 != 0) 
		{
			r = n1 % n2;
			n1 = n2;
			n2 = r;
		}
		return n1;
	}

	public static long lcm(long n1, long n2) 
	{
		long answer = (n1 * n2) / (gcd(n1, n2));
		return answer;
	}

	static class FastScanner2 
	{
		private byte[] buf = new byte[1024];
		private int curChar;
		private int snumChars;

		public int read() 
		{
			if (snumChars == -1)
				throw new InputMismatchException();
			if (curChar >= snumChars) 
			{
				curChar = 0;
				try 
				{
					snumChars = System.in.read(buf);
				} catch (IOException e) 
				{
					throw new InputMismatchException();
				}
				if (snumChars <= 0)
					return -1;
			}
			return buf[curChar++];
		}

		public String nextLine() 
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
			while (!isEndOfLine(c));
			return res.toString();
		}

		public String nextString() 
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

		public long nextLong()
		{
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
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

		public int nextInt() 
		{
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
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

		public int[] nextIntArray(int n)
		{
			int[] arr = new int[n];
			for (int i = 0; i < n; i++) 
			{
				arr[i] = nextInt();
			}
			return arr;
		}

		public long[] nextLongArray(int n)
		{
			long[] arr = new long[n];
			for (int i = 0; i < n; i++) 
			{
				arr[i] = nextLong();
			}
			return arr;
		}

		private boolean isSpaceChar(int c)
		{
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		private boolean isEndOfLine(int c) 
		{
			return c == '\n' || c == '\r' || c == -1;
		}
	}

	static class InputReader 
	{
		public BufferedReader reader;
		public StringTokenizer tokenizer;

		public InputReader(InputStream inputstream) 
		{
			reader = new BufferedReader(new InputStreamReader(inputstream));
			tokenizer = null;
		}

		public String nextLine() 
		{
			String fullLine = null;
			while (tokenizer == null || !tokenizer.hasMoreTokens())
			{
				try 
				{
					fullLine = reader.readLine();
				} catch (IOException e)
				{
					throw new RuntimeException(e);
				}
				return fullLine;
			}
			return fullLine;
		}

		public String next()
		{
			while (tokenizer == null || !tokenizer.hasMoreTokens()) 
			{
				try 
				{
					tokenizer = new StringTokenizer(reader.readLine());
				} catch (IOException e) 
				{
					throw new RuntimeException(e);
				}
			}
			return tokenizer.nextToken();
		}

		public long nextLong() 
		{
			return Long.parseLong(next());
		}

		public int[] nextIntArray(int n) 
		{
			int a[] = new int[n];
			for (int i = 0; i < n; i++) 
			{
				a[i] = nextInt();
			}
			return a;
		}

		public long[] nextLongArray(int n)
		{
			long a[] = new long[n];
			for (int i = 0; i < n; i++) 
			{
				a[i] = nextLong();
			}
			return a;
		}

		public int nextInt() 
		{
			return Integer.parseInt(next());
		}
	}

	static class OutputWriter 
	{
		private final PrintWriter writer;

		public OutputWriter(OutputStream outputStream) 
		{
			writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
		}

		public OutputWriter(Writer writer)
		{
			this.writer = new PrintWriter(writer);
		}

		public void print(Object... objects)
		{
			for (int i = 0; i < objects.length; i++) 
			{
				if (i != 0)
					writer.print(' ');
				writer.print(objects[i]);
			}
		}

		public void println(Object... objects)
		{
			print(objects);
			writer.println();
		}

		public void close() 
		{
			writer.close();
		}

		public void flush() 
		{
			writer.flush();
		}
	}

}