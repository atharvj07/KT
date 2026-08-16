import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class R414C_
{
	public static void main(String[] args) throws IOException
	{
		Scanner sc = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(System.out);
		
		String Oleg = sc.next();
		String Igor = sc.next();
		int n = Oleg.length();
		Integer[] a = new Integer[n];
		Integer[] b = new Integer[n];
		int[] name = new int[n];
		
		for (int i = 0; i < a.length; i++)
		{
			a[i] = Oleg.charAt(i) - 'a';
			b[i] = Igor.charAt(i) - 'a';
		}
		
		Arrays.sort(a);
		Arrays.sort(b);
		
		int os = 0;
		int on = (n+1)/2 - 1;
		int is = n - ((n)/2);
		int in = n-1;
		int turn = 0;
		Arrays.fill(name, -1);
		int nameend = n-1;
		int namest = 0;
		int rem = n;
		for (int j = 0; j < name.length; j++)
		{
			rem--;
			if(rem == 0 && turn == 0)
			{
				if(name[namest] != -1)
					name[namest++] = a[os++];
				else
					name[nameend++] = a[os++];
				continue;
			}
			
			if(turn == 0)
			{
				if(b[in] <= a[os])
					name[nameend--] = a[on--];
				else
					name[namest++] = a[os++];
				turn = 1;
			}
			else
			{
				if(a[os] >= b[in])
					name[nameend--] = b[is++];
				else
					name[namest++] = b[in--];
				turn = 0;
			}
		}
		
		
		for (int j = 0; j < name.length; j++)
		{
			pw.print((char)(name[j]+ 'a'));
		}
		pw.println();
		pw.flush();
		pw.close();
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