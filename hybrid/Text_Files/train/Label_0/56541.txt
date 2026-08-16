import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.InputMismatchException;

public class A915{

	void solve()
	{
		int n = ni(), k = ni();
		int[] a = ia(n);
		int m = -1>>>1;
		for(int x : a)
			if(k % x == 0)
				m = Math.min(m, k / x);
		out.println(m);
	}
	
	public static void main(String[] args){new A915().run();}
	
	private byte[] bufferArray = new byte[1024];
	private int bufLength = 0;
	private int bufCurrent = 0;
	InputStream inputStream;
	PrintWriter out;
	
	public void run()
	{
		inputStream = System.in;
		out = new PrintWriter(System.out);
		solve();
		out.flush();
	}
	
	int nextByte()
	{
		if(bufLength == -1)
			throw new InputMismatchException();
		if(bufCurrent >= bufLength)
		{
			bufCurrent = 0;
			try
			{bufLength = inputStream.read(bufferArray);}
			catch(IOException e)
			{ throw new InputMismatchException();}
			if(bufLength <= 0)
				return -1;
		}
		return bufferArray[bufCurrent++];
	}
	
	boolean isSpaceChar(int x)	{return (x < 33 || x > 126);}
	
	boolean isDigit(int x)	{return (x >= '0' && x <= '9');}
	
	int nextNonSpace()
	{
		int x;
		while((x=nextByte()) != -1 && isSpaceChar(x));
		return x;
	}
	
	int ni()
	{
		long ans = nl();
		if (ans >= Integer.MIN_VALUE && ans <= Integer.MAX_VALUE)
			return (int)ans;
		throw new InputMismatchException();
	}
	
	long nl()
	{
		long ans = 0;
		boolean neg = false;
		int x = nextNonSpace();
		if(x == '-') 
		{
			neg = true;
			x = nextByte();
		}
		while(!isSpaceChar(x))
		{
			if(isDigit(x))
			{
				ans = ans * 10 + x -'0';
				x = nextByte();
			}
			else
				throw new InputMismatchException();
		}
		return neg ? -ans : ans;
	}
	
	String ns()
	{
		StringBuilder sb = new StringBuilder();
		int x = nextNonSpace();
		while(!isSpaceChar(x))
		{
			sb.append((char)x);
			x = nextByte();
		}
		return sb.toString();
	}
	
	char nc()	{ return (char)nextNonSpace();}
	
	double nd()	{ return (double)Double.parseDouble(ns()); }
	
	char[] ca()	{ return ns().toCharArray();}
	
	char[][] ca(int n)
	{
		char[][] ans = new char[n][];
		for(int i=0;i<n;i++)
			ans[i] = ca();
		return ans;
	}
	
	int[] ia(int n)
	{
		int[] ans = new int[n];
		for(int i=0;i<n;i++)
			ans[i] = ni();
		return ans;
	}
	
	void db(Object... o) {System.out.println(Arrays.deepToString(o));}
	
}
