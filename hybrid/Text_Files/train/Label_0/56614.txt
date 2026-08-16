import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P219C
{
	public static void main(String[] args)
	{
		FastScanner scan = new FastScanner();
		int n = scan.nextInt(), k = scan.nextInt();
		char[] in = scan.next().toCharArray();
		if (k == 2)
		{
			char[] s1 = alt(n, 0);
			char[] s2 = alt(n, 1);
			int c1 = 0, c2 = 0;
			for (int i = 0; i < n; i++)
				if (s1[i] != in[i])
					c1++;
			for (int i = 0; i < n; i++)
				if (s2[i] != in[i])
					c2++;
			System.out.println(Math.min(c1, c2));
			System.out.println(c1 < c2 ? new String(s1) : new String(s2));
		}
		else
		{
			int c = 0;
			for (int i = 1; i < n; i++)
			{
				if (in[i] == in[i-1])
				{
					c++;
					if ('A' != in[i-1] && (i == n-1 || 'A' != in[i+1]))
						in[i] = 'A';
					else if ('B' != in[i-1] && (i == n-1 || 'B' != in[i+1]))
						in[i] = 'B';
					else
						in[i] = 'C';
				}
			}
			System.out.println(c);
			System.out.println(new String(in));
		}
	}
	
	private static char[] alt(int n, int start)
	{
		char[] c = new char[n];
		for (int i = 0; i < n; i++)
			c[i] = (i % 2 == start ? 'A' : 'B');
		return c;
	}

	static class FastScanner
	{
		BufferedReader br;
		StringTokenizer st;

		public FastScanner()
		{
			try
			{
				br = new BufferedReader(new InputStreamReader(System.in));
				st = new StringTokenizer(br.readLine());
			} catch (Exception e)
			{
				e.printStackTrace();
			}
		}

		public String next()
		{
			if (st.hasMoreTokens())
				return st.nextToken();
			try
			{
				st = new StringTokenizer(br.readLine());
			} catch (Exception e)
			{
				e.printStackTrace();
			}
			return st.nextToken();
		}

		public int nextInt()
		{
			return Integer.parseInt(next());
		}

		public long nextLong()
		{
			return Long.parseLong(next());
		}

		public String nextLine()
		{
			String line = "";
			try
			{
				line = br.readLine();
			} catch (Exception e)
			{
				e.printStackTrace();
			}
			return line;
		}
	}
}
