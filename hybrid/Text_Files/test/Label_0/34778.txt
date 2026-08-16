// package CodeForces;

import java.io.*;
import java.util.*;

public class Problem_385C {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner();
		PrintWriter pw = new PrintWriter(System.out);
		p=new ArrayList<>();
		hs=new HashSet<>();
		a=new int[10000001];
		ans=new int[10000001];
		int n=sc.nextInt();
		for(int i=0;i<n;i++)a[sc.nextInt()]++;
		modified_seive(10000001);
		int sol[]=new int[10000001];
		for(int i=1;i<10000001;i++)
		{
			sol[i]+=sol[i-1]+ans[i];
		}
		int t=sc.nextInt();
		while(t-->0)
		{
			int l=sc.nextInt(),r=Math.min(sc.nextInt(), 10000000);
			if(l>10000000)
				pw.println(0);
			else
				pw.println(sol[r]-sol[l-1]);
		}
		pw.close();
	}
	static int ans[],a[];
	static ArrayList<Integer>p;
	static HashSet<Integer>hs;
	public static void modified_seive(int size)
	{
		boolean f[]=new boolean[size];
		f[0]=true;
		f[1]=true;
		for(int i=2;i<f.length;i++)
		{	
			if(!f[i])
			{
				p.add(i);
				hs.add(i);
				for(int j=i;j<f.length;j+=i)
				{
					f[j]=true;
					ans[i]+=a[j];
				}
			}
		}
	}
	static class Scanner {
		BufferedReader br;
		StringTokenizer st;

		Scanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() throws IOException {
			while (st == null || !st.hasMoreTokens()) {
				st = new StringTokenizer(br.readLine());
			}
			return st.nextToken();
		}

		int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		String nextLine() throws IOException {
			return br.readLine();
		}

		boolean hasnext() throws IOException {
			return br.ready();
		}

	}
}
