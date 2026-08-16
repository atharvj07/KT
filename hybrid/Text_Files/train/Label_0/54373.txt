import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P893D
{
	public static void main(String[] args)
	{
		FastScanner scan = new FastScanner();
		int n = scan.nextInt();
		int d = scan.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++)
			arr[i] = scan.nextInt();
		int dep = 0;
		int lo = 0, hi = 0;
		for (int i = 0; i < n; i++)
		{
			int p = arr[i];
			if (p < 0)
			{
				lo += p;
				hi += p;
			}
			else if (p > 0)
			{
				lo += p;
				hi = Math.min(d, hi+p);
				if (lo > d)
				{
					System.out.println(-1);
					return;
				}
			}
			else
			{
				if (hi >= 0) //Don't deposit
				{
					lo = Math.max(0, lo);
				}
				else //Deposit
				{
					dep++;
					lo = 0;
					hi = d;
				}
			}
		}
		System.out.println(dep);
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
