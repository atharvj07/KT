//package Problems;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.StringTokenizer;
import java.util.ArrayList;
//import com.sun.tools.javac.code.Attribute.Array;

public class Valerii {
	public static void main(String args[])
	{
		FastScanner fs=new FastScanner();
		int t=fs.nextInt();
		while(t>0)
		{
			int n=fs.nextInt();
			int []arr=new int[n];
			for(int i=0;i<n;i++)
				arr[i]=fs.nextInt();
			List<Integer> list=new ArrayList<Integer>();
			boolean flag=false;
			list.add(arr[0]);
			for(int i=1;i<arr.length;i++)
			{
				if(list.contains(arr[i]))
				{
					flag=true;;
					break;
				}
				else
					list.add(arr[i]);
			}
			if(flag)
				System.out.println("YES");
			else
				System.out.println("NO");
			t--;
			
		}
	}
	public static long sum(int start,int end,int []arr)
	{
		long sum=0;
		for(int i=start;i<=end;i++)
		{
			sum+=arr[i];
		}
		return sum;
	}
	private static int[] readArray(int n) {
		// TODO Auto-generated method stub
		return null;
	}
 
static final Random random=new Random();
	
	static void ruffleSort(int[] a) {
		int n=a.length;//shuffle, then sort 
		for (int i=0; i<n; i++) {
			int oi=random.nextInt(n), temp=a[oi];
			a[oi]=a[i]; a[i]=temp;
		}
		Arrays.sort(a);
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
}
