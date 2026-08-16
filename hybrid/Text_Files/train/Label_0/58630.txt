
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.*;

public class D {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int k = sc.nextInt();
		int g = sc.nextInt();		//green
		int b = sc.nextInt();		//black

		StringBuilder ans =new StringBuilder();
		char last = '_';
		int cnt = 0;
		boolean ok = true;
		for(int i=0;i<n;i++)
		{
			if(cnt==k)
			{
				char cur='o';
				if(last == '_')
					cur = (g<b)?'B':'G';
				else
					cur = last == 'G'?'B':'G';
				last = cur;
				cnt = 0;
				if((cur == 'G' && g<=0) || (cur == 'B' && b<=0))
				{
					//System.out.println(g+" " + b + " " + last + " " + cnt) ;
					ok = false;
					break;
				}
				else
				{
					ans.append(cur);
					if(cur=='G')g--; else b--;
					cnt++;
				}
			}
			else
			{
				if(g>b)
				{
					ans.append('G');
					if(last == 'G')
					{
						cnt++;
						g--;
					}
					else
					{
						last = 'G';
						g--;
						cnt=1;
					}
				}
				else
				{
					ans.append('B');
					if(last == 'B')
					{
						cnt++;
						b--;
					}
					else
					{
						last = 'B';
						b--;
						cnt=1;
					}
				}
			}
		}
		if(!ok)
			System.out.println("NO");
		else
			System.out.println(ans);

	}

	static class Scanner 
	{
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream s){	br = new BufferedReader(new InputStreamReader(s));}

		public String next() throws IOException 
		{
			while (st == null || !st.hasMoreTokens()) 
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public int nextInt() throws IOException {return Integer.parseInt(next());}

		public long nextLong() throws IOException {return Long.parseLong(next());}

		public String nextLine() throws IOException {return br.readLine();}

		public double nextDouble() throws IOException
		{
			String x = next();
			StringBuilder sb = new StringBuilder("0");
			double res = 0, f = 1;
			boolean dec = false, neg = false;
			int start = 0;
			if(x.charAt(0) == '-')
			{
				neg = true;
				start++;
			}
			for(int i = start; i < x.length(); i++)
				if(x.charAt(i) == '.')
				{
					res = Long.parseLong(sb.toString());
					sb = new StringBuilder("0");
					dec = true;
				}
				else
				{
					sb.append(x.charAt(i));
					if(dec)
						f *= 10;
				}
			res += Long.parseLong(sb.toString()) / f;
			return res * (neg?-1:1);	
		}

		public boolean ready() throws IOException {return br.ready();}
	}


}
