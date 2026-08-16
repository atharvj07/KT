import sun.print.resources.serviceui;

import java.io.*;
import java.util.StringTokenizer;

public class B {

	public static void main(String[] args) throws IOException {

		Scanner sc = new Scanner(System.in);

		PrintWriter out = new PrintWriter(System.out);

		int n = sc.nextInt();
		Point[] A = new Point[n];
		for(int i = 0; i < n; ++i)
			A[n - i - 1] = new Point(sc.nextInt(), sc.nextInt());
		A = fixPolygon(A);
		boolean good = true;
		int m = sc.nextInt();
		while(m-->0)
			good &= inPolygon(new Point(sc.nextInt(), sc.nextInt()), A);

		out.println(good ? "YES" : "NO");
		out.close();
	}

	static Point[] fixPolygon(Point[] A)
	{
		int best = 0;
		for(int i = 1; i < A.length; ++i)
			if(A[i].x < A[best].x || A[i].x == A[best].x && A[i].y < A[best].y)
				best = i;
		Point[] B = new Point[A.length];
		int j = 0;
		for(int i = best; i < A.length; ++i)
			B[j++] = A[i];
		for(int i = 0; i < best; ++i)
			B[j++] = A[i];
		return B;
	}

	static class Point
	{
		int x, y;

		Point(int a, int b) { x = a; y = b; }
	}

	static boolean inPolygon(Point p, Point[] g)   // O(log n), g[0] is the smallest point
	{
		if(g[0].x == p.x && g[0].y == p.y)
			return false;
		Point base = g[0];
		int belowPoint = -1, lo = 1, hi = g.length - 1;
		while(lo <= hi)
		{
			int mid = (lo + hi) / 2;
			if(onLeft(base, g[mid], p, true))
			{
				belowPoint = mid;
				lo = mid + 1;
			}
			else
				hi = mid - 1;
		}
		if(belowPoint == -1)
			return false;
		int abovePoint = belowPoint == g.length - 1 ? belowPoint : belowPoint + 1;
		return inside(base, g[belowPoint], g[abovePoint], p, belowPoint > 1, false, abovePoint < g.length - 1);

	}

	static boolean inside(Point a, Point b, Point c, Point p, boolean x, boolean y, boolean z)
	{
		return onLeft(a, b, p, x) && onLeft(b, c, p, y) && onLeft(c, a, p, z);
	}


	static boolean onLeft(Point p, Point q, Point r, boolean f)
	{
		if(f)
			return 1l * (q.x - p.x) * (r.y - p.y) - 1l * (q.y - p.y) * (r.x - p.x) >= 0;
		return 1l * (q.x - p.x) * (r.y - p.y) - 1l * (q.y - p.y) * (r.x - p.x) > 0;
	}




	static class Scanner
	{
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream s){	br = new BufferedReader(new InputStreamReader(s));}

		public Scanner(FileReader s) throws FileNotFoundException {	br = new BufferedReader(s);}

		public String next() throws IOException
		{
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public int nextInt() throws IOException {return Integer.parseInt(next());}

		public long nextLong() throws IOException {return Long.parseLong(next());}

		public String nextLine() throws IOException {return br.readLine();}

		public double nextDouble() throws IOException { return Double.parseDouble(next()); }

		public boolean ready() throws IOException {return br.ready();}
	}
}