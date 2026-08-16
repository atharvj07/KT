import java.util.*;
import java.io.*;

public class E
{

	static FastIO f;

	public static void main(String args[]) throws IOException
	{
		f = new FastIO();

		int t, n, m, i, j;
		PriorityQueue<Point> h;
		char[][] g;
		char cs;
		Point x, y, temp;
		ArrayList<Pair> a;
		boolean xa, ya, c;
		
		t = f.ni();
		
		while(t-->0)
		{
			n = f.ni();
			m = f.ni();
			g = new char[n][];
			h = new PriorityQueue<>(Point.comp);
			a = new ArrayList<>();

			for(i = 0; i < n; i++)
				g[i] = f.nca();

			for(i = 0; i < n; i++)
			{
				for(j = 0; j < m; j++)
				{
					if(g[i][j] != '.')
					{
						h.add(new Point(g[i][j], i, j));
					}
				}
			}

			// f.err(h + "\n");

			if(h.isEmpty())
			{
				f.out("YES\n0\n");
				continue;
			}

			c = xa = ya = true;
			x = y = h.poll();
			cs = 'a';
			while(!h.isEmpty())
			{
				temp = h.poll();

				if(x.s != temp.s)
				{
					c = check(g, x, y);
					if((xa || ya) && c)
					{
						while(cs <= x.s)
						{
							a.add(new Pair(x, y));
							cs++;
						}
					}
					else
						break;

					x = y = temp;
					xa = ya = true;
				}
				else
				{
					y = temp;
					xa = xa && x.x == y.x;
					ya = ya && x.y == y.y;
				}
			}

			if((!xa && !ya) || !c)
			{
				f.out("NO\n");
				continue;
			}

			if((xa || ya) && check(g, x, y))
			{
				while(cs <= x.s)
				{
					a.add(new Pair(x, y));
					cs++;
				}
			}
			else
			{
				f.out("NO\n");
				continue;
			}

			// f.err(a + "\n");

			f.out("YES\n" + (a.size()) + "\n");

			for(Pair p : a)
			{
				f.out((p.s.x+1) + " " + (p.s.y+1) + " " + (p.e.x+1) + " " + (p.e.y+1) + "\n");
			}

			f.err("\n");
		}

		f.flush();
	}

	public static boolean check(char[][] g, Point x, Point y) throws IOException
	{
		int i;

		if(x.x == y.x)
		{
			for(i = x.y; i <= y.y; i++)
				if(g[x.x][i] < g[x.x][x.y])
					return false;
		}
		else
		{
			for(i = x.x; i <= y.x; i++)
				if(g[i][x.y] < g[x.x][x.y])
					return false;
		}

		f.err(x + " to " + y + " is clear.\n");

		return true;
	}

	static class Pair
	{
		Point s, e;
	
		Pair(Point x, Point y)
		{
			s = x;
			e = y;
		}
	
		@Override
		public int hashCode()
		{
			return super.hashCode();
		}
	
		@Override
		public boolean equals(Object obj)
		{
			Pair that = (Pair)obj;
	
			return super.equals(obj);
		}
	
		@Override
		public String toString()
		{
			return "[" + s + ", " + e + "]";
		}
	}

	static class Point
	{
		char s;
		int x, y;

		static Comparator<Point> comp = new Comparator<>(){

			@Override
			public int compare(Point a, Point b)
			{
				return (a.s != b.s) ? a.s-b.s : (a.x != b.x) ? a.x-b.x : a.y-b.y;
			}
		};
	
		Point(char a, int b, int c)
		{
			s = a;
			x = b;
			y = c;
		}
	
		@Override
		public int hashCode()
		{
			return Objects.hash(s, x, y);
		}
	
		@Override
		public boolean equals(Object obj)
		{
			Point that = (Point)obj;
	
			return s == that.s && x == that.x && y == that.y;
		}
	
		@Override
		public String toString()
		{
			return "[" + s + ", (" + x + ", " + y + ")" + "]";
		}
	}

	public static class FastIO
	{
		BufferedReader br;
		BufferedWriter bw, be;
		StringTokenizer st;

		public FastIO()
		{
			br = new BufferedReader(new InputStreamReader(System.in));
			bw = new BufferedWriter(new OutputStreamWriter(System.out));
			be = new BufferedWriter(new OutputStreamWriter(System.err));
			st = new StringTokenizer("");
		}

		private void read() throws IOException
		{
			st = new StringTokenizer(br.readLine());
		}

		public String ns() throws IOException
		{
			while(!st.hasMoreTokens())
				read();
			return st.nextToken();
		}

		public int ni() throws IOException
		{
			return Integer.parseInt(ns());
		}

		public long nl() throws IOException
		{
			return Long.parseLong(ns());
		}

		public float nf() throws IOException
		{
			return Float.parseFloat(ns());
		}

		public double nd() throws IOException
		{
			return Double.parseDouble(ns());
		}

		public char nc() throws IOException
		{
			return ns().charAt(0);
		}

		public int[] nia(int n) throws IOException
		{
			int[] a = new int[n];
			for(int i = 0; i < n; i++)
				a[i] = ni();

			return a;
		}

		public long[] nla(int n) throws IOException
		{
			long[] a = new long[n];
			for(int i = 0; i < n; i++)
				a[i] = nl();

			return a;
		}

		public char[] nca() throws IOException
		{
			return ns().toCharArray();
		}

		public void out(String s) throws IOException
		{
			bw.write(s);
		}

		public void flush() throws IOException
		{
			bw.flush();
			be.flush();
		}

		public void err(String s) throws IOException
		{
			be.write(s);
		}
	}
}