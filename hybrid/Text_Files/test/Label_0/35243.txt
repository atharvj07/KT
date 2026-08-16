// Are we Real
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.StringTokenizer;
import java.util.List;
import java.util.Collections;
import java.util.Map;
import java.util.HashMap;
import java.util.Comparator;
import java.util.stream.IntStream;
import java.util.ArrayDeque;
public class Solution {
 	private static FastScanner fs=new FastScanner();
 	private static PrintWriter out = new PrintWriter(System.out);
	public static void main(String[] args) {
		int t = fs.nextInt();
		while(t-->0)
		{
			int n = fs.nextInt();
			String str = fs.next();
			int cnt =0;
			for(int i=0;i<n;i++)
			{
				if(str.charAt(i)=='1')cnt++;
			}
			if(cnt%2==1 || str.charAt(0)=='0' || str.charAt(n-1)=='0')
			{
				out.println("NO");
				continue;
			}

			boolean flip = false;
			StringBuilder a  = new StringBuilder();
			StringBuilder b  = new StringBuilder();  
			int k =0;
			for(int i=0;i<n;i++)
			{
				if(str.charAt(i)=='1')
				{
					if(2*k<cnt)
					{
						a.append("(");
						b.append("(");
						
					}
					else 
					{
						a.append(")");
						b.append(")");
					}
					k++;
				}
				else 
				{
					if(!flip)
					{
						a.append(")");
						b.append("(");
						
					}
					else 
					{
						a.append("(");
						b.append(")");
						
					}
					flip = !flip;

				}
			}
			out.println("YES");
			out.println(a);
			out.println(b);
		}
		out.close();

	}
	
	private static int gcd(int number1, int number2) { //
		 if(number2 == 0){ return number1; } 

		 return gcd(number2, number1%number2); 

	}
	
  

	static final Random random=new Random();
	
	static void ruffleSort(int [] a) {
		int n=a.length;//shuffle, then sort 
		for (int i=0; i<n; i++) {
			int oi=random.nextInt(n); int temp=a[oi];
			a[oi]=a[i]; a[i]=temp;
		}
		Arrays.sort(a);
	}
	static int findGCD(int a, int b)   
	{   
		if (b == 0)   
		return a;     
		return findGCD(b, a % b);   
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
		int [] sort(int [] arr)
		{
			List<Integer> list = new ArrayList<>();
			for(int i : arr) list.add(i);	
		
			Collections.sort(list);
			int res[] = new int[arr.length];
			for(int i=0;i<arr.length;i++) res[i] = list.get(i);
			

			return res;
		}
		void debug(int a)
		{
			System.out.println("This is var "+a);
		}
	}
}	