import java.util.*;
import java.io.*;
public class f 
{
	public static void main(String[] arg) throws IOException
	{
		new f();
	}
	long MOD = 1_000_000_007;
	public f() throws IOException
	{
		FastScanner in = new FastScanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		int n = in.nextInt();
		int r = in.nextInt();
		int c = in.nextInt();
		String str = in.next();
		long ret = 0;
		if(r == 1 && c == 1)
		{
			out.println(1);
		}
		else
		{
			int idx = 0;
			int lr = 0;
			int ud = 0;
			int L = 0;
			int R = 0;
			int U = 0;
			int D = 0;
			int stop = 0;
			ArrayDeque<Long> q = new ArrayDeque<Long>();
			while(r >= 1 && c >= 1 && stop++ < 3*n)
			{
				if(str.charAt((int)(idx%n)) == 'L')
				{
					if(lr <= L)
					{
						c--;
						ret += (long)r*(long)(idx+1)%MOD;
						ret %= MOD;
						L--;
						if(stop > 2*n)
						{
							q.add((long)idx+(long)n);
						}
					}
					lr--;
				}
				else if(str.charAt((int)(idx%n)) == 'R')
				{
					if(lr >= R)
					{
						c--;
						ret += (long)r*(long)(idx+1)%MOD;
						ret %= MOD;
						R++;
						if(stop > 2*n)
						{
							q.add((long)idx+(long)n);
						}
					}
					lr++;
				}
				else if(str.charAt((int)(idx%n)) == 'U')
				{
					if(ud >= U)
					{
						r--;
						ret += (long)c*(long)(idx+1)%MOD;
						ret %= MOD;
						U++;
						if(stop > 2*n)
						{
							q.add((long)idx+(long)n);
						}
					}
					ud++;
				}
				else
				{
					if(ud <= D)
					{
						r--;
						ret += (long)c*(long)(idx+1)%MOD;
						ret %= MOD;
						D--;
						if(stop > 2*n)
						{
							q.add((long)idx+(long)n);
						}
					}
					ud--;
				}
				idx++;
			}
			while(q.size() > 0 && r >= 1 && c >= 1)
			{
				long cur = q.poll();
				if(str.charAt((int)(cur%n)) == 'U' || str.charAt((int)(cur%n)) == 'D')
				{
					r--;
					ret += (long)c*(long)(cur+1)%MOD;
					ret %= MOD;
				}
				else
				{
					c--;
					ret += (long)r*(long)(cur+1)%MOD;
					ret %= MOD;
				}
				q.add(cur+(long)n);
			}
			if(q.size() == 0 && r*c != 0) ret = -1;
			out.println(ret);
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
