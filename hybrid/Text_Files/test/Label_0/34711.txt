import java.awt.Point;
import java.io.*;
import java.util.*;

public class C
{

	static StringBuilder st = new StringBuilder();
	
	public static void main(String[] args) throws Exception 
	{
		Scanner sc = new Scanner(System.in) ; 
		PrintWriter out = new PrintWriter(System.out) ; 
		
		int sum = sc.nextInt() , limit = sc.nextInt() ; 
		
		ArrayList<Integer> ans = new ArrayList<>();
		
		Pair [] p = new Pair[limit] ;
		
		for(int i = 1 ; i <= limit ; i++)
			p[i - 1] = new Pair(i) ; 
		
		Arrays.sort(p);
		
		for(int i = limit - 1 ; i >= 0 ; i--)
		{
			if(p[i].lst <= sum)
			{
				sum -= p[i].lst ; 
				ans.add(p[i].val);
			}
		}
		
		if(sum == 0)
		{
			out.println(ans.size());
			for(int x : ans)
				out.print(x+" ");
		}
		else 
			out.println(-1);
		out.flush();
		out.close(); 
		
	}
	
	static class Pair implements Comparable<Pair>
	{
		int lst , val;
		Pair(int a)
		{
			val = a ; 
			lst = a & -a ; 
		}
		@Override
		public int compareTo(Pair p) 
		{
			return lst - p.lst;
		}
		
	}
	
	static class Scanner 
	{
		BufferedReader br;
		StringTokenizer st;

		Scanner(InputStream in) 
		{
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() throws Exception 
		{
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		int nextInt() throws Exception { return Integer.parseInt(next()); }

		long nextLong() throws Exception { return Long.parseLong(next()); }

		double nextDouble() throws Exception { return Double.parseDouble(next());}

	}

	static void shuffle(int[] a) 
	{
		int n = a.length;
		for (int i = 0; i < n; i++) 
		{
			int r = i + (int) (Math.random() * (n - i));
			int tmp = a[i];
			a[i] = a[r];
			a[r] = tmp;
		}
	}

}