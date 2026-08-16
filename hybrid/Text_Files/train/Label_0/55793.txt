import java.util.*;
import java.io.*;

public class Main
{
	public static void main(String[] args)
	{
		FastReader reader = new FastReader();
		PrintWriter writer = new PrintWriter(System.out);

		int n = reader.nextInt();
		int k = reader.nextInt();

		MyList[] graph = new MyList[n];
		for (int i=0; i<n; i++)
			graph[i] = new MyList();

		for (int i=1; i<n; i++)
		{
			int u = reader.nextInt()-1;
			int v = reader.nextInt()-1;

			graph[u].list.add(v);
			graph[v].list.add(u);
		}

		boolean ans = true;
		HashSet<Integer> set = new HashSet<>();

		int[] sub = new int[n];
		int[] size = new int[n];

		for (int i=0; i<n; i++)
		{
			size[i] = graph[i].list.size();

			if (graph[i].list.size()==1)
				set.add(i);
		}

		for (int i=0; i<k; i++)
		{
			if (set.size() < 3)
				ans = false;
				
			HashSet<Integer> temp = new HashSet<>();

			for (int j : set)
			{
				if (graph[j].list.size() != 1)
					ans = false;

				if (sub[j]==1 || sub[j]==2)
					ans = false;
			}

			if (!ans)
				break;

			for (int j : set)
				for (int x : graph[j].list)
				{
					temp.add(x);
					graph[x].list.remove(j);
					sub[x]++;
				}

			set = temp;
		}

		if (set.size() != 1)
			ans = false;
		else
			for (int i : set)
				if (graph[i].list.size() != 0)
					ans = false;

		if (ans)
			writer.print("Yes");
		else
			writer.print("No");

		writer.close();
	}

	static class FastReader
	{
		BufferedReader br;
		StringTokenizer st;

		public FastReader()
		{
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next()
		{
			while (st == null || !st.hasMoreElements())
			{
				try
				{
					st = new StringTokenizer(br.readLine());
				}
				catch (IOException e)
				{
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt()
		{
			return Integer.parseInt(next());
		}

		long nextLong()
		{
			return Long.parseLong(next());
		}

		double nextDouble()
		{
			return Double.parseDouble(next());
		}

		String nextLine()
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
	}
}

class MyList
{
	HashSet<Integer> list = new HashSet<Integer>();
}