import java.util.*;
import java.io.*;

public class b
{
	public static void main(String[] arg) throws IOException
	{
		new b();
	}
	public b() throws IOException
	{
		FastScanner in = new FastScanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		int b = in.nextInt();
		int q = in.nextInt();
		int l = in.nextInt();
		int m = in.nextInt();
		if(q == 0)
		{
			HashSet<Integer> ans = new HashSet<Integer>();
			ans.add(0);
			ans.add(b);
			for(int i = 0; i < m; i++) ans.remove(in.nextInt());
			if(Math.abs(b) > l) out.println(0);
			else if(Math.abs(0) > l)
			{
				if(b != 0) out.println(1);
				else out.println(0);
			}
			else
			{
				if(ans.contains(0)) out.println("inf");
				else out.println(ans.size());
			}
		}
		else
		{
			HashSet<Long> ans = new HashSet<Long>();
			int inf = 0;
			for(long i = b; Math.abs(i) <= l && inf < 1000; i *= q, inf++)
			{
				ans.add(i);
			}
			for(int i = 0; i < m; i++)
			{
				long v = in.nextInt();
				if(ans.contains(v)) ans.remove(v);
			}
			if(inf >= 900)
			{
				if(ans.size() > 0) out.println("inf");
				else out.println(ans.size());
			}
			else out.println(ans.size());
		}
		in.close(); out.close();
	}
	class FastScanner
	{
		BufferedReader br;
		StringTokenizer st;
		public FastScanner(InputStream in)
		{
			br = new BufferedReader(new InputStreamReader(in));
			st = new StringTokenizer("");
		}
		public String next() throws IOException
		{
			while(!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}
		public int nextInt() throws IOException
		{
			return Integer.parseInt(next());
		}
		public long nextLong() throws IOException
		{
			return Long.parseLong(next());
		}
		public void close() throws IOException
		{
			br.close();
		}
	}
}