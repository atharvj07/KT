import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.StringTokenizer;

public class P764B
{
	public static void main(String[] args)
	{
		FastScanner scan = new FastScanner();
		PrintWriter pw = new PrintWriter(System.out);
		int n = scan.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++)
		{
			arr[i] = scan.nextInt();
		}
		for (int i = 0; i < n/2; i += 2)
		{
			int temp = arr[i];
			arr[i] = arr[n-1-i];
			arr[n-1-i] = temp;
		}
		for (int i = 0; i < n; i++)
		{
			pw.print(arr[i] + " ");
		}
		pw.flush();
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
