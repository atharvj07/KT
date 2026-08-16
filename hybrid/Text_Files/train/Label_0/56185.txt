import java.util.*;
import java.io.*;
public class B{
	public static void main(String[] args)
	{
		FastScanner fs = new FastScanner();
		PrintWriter out = new PrintWriter(System.out);
		int t = fs.nextInt();
		for(int tt=0;tt<t;tt++)
		{
			int n = fs.nextInt();
			int[] arr = fs.readArray(n);
			boolean flag = false;
			for(int i:arr)
			{
				int start = 0;
				while(start*start<i)start++;
				if(start*start != i)
				{
					flag = true;
					break;
				}
			}
			out.println(flag == true?"YES":"NO");
		}
		out.close();
	}
	static class FastScanner {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
		String next() {
			while (!st.hasMoreTokens())
				try {
					st=new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			return st.nextToken();
		}
		
		int nextInt() {
			return Integer.parseInt(next());
		}
		int[] readArray(int n) {
			int[] a=new int[n];
			for (int i=0; i<n; i++) a[i]=nextInt();
			return a;
		}
		long nextLong() {
			return Long.parseLong(next());
		}
	}
	public static int[] sort(int[] arr)
	{
		List<Integer> temp = new ArrayList();
		for(int i:arr)temp.add(i);
		Collections.sort(temp);
		int start = 0;
		for(int i:temp)arr[start++]=i;
		return arr;
	}
}