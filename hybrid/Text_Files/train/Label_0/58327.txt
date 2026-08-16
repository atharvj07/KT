import java.io.*;
import java.util.*;
public class D33 {
public static void main(String[] args) throws IOException {
	input.init(System.in);
	PrintWriter out = new PrintWriter(System.out);
	int n = input.nextInt(), m = input.nextInt(), k = input.nextInt();
	Point[] control = new Point[n];
	for(int i = 0; i<n; i++) control[i] = new Point(input.nextLong(), input.nextLong());
	int[] nodes = new int[n];
	Point[] circs = new Point[m];
	long[] rs = new long[m];
	for(int i = 0; i<m; i++)
	{
		rs[i] = input.nextLong();
		circs[i] = new Point(input.nextLong(), input.nextLong());
	}
	for(int i = 0; i<n; i++)
	{
		nodes[i] = m;
		for(int j = 0; j<m; j++)
		{
			boolean good = control[i].d2(circs[j]) < rs[j] * rs[j];
			if(good)
			{
				if(nodes[i] == m || rs[j] < rs[nodes[i]]) nodes[i] = j;
			}
		}
	}
	//out.println(Arrays.toString(nodes));
	ArrayList<Integer>[] g = new ArrayList[m+1];
	for(int i = 0; i<=m; i++) g[i] = new ArrayList<Integer>();
	for(int i = 0; i<m; i++)
	{
		int p = m;
		for(int j = 0; j<m; j++)
		{
			if(j == i || rs[j] <= rs[i]) continue;
			boolean good = circs[i].d2(circs[j]) < rs[j] * rs[j];
			if(good)
			{
				if(p == m || rs[j] < rs[p]) p = j;
			}
		}
		g[i].add(p);
		g[p].add(i);
	}
	
	int[][] ds = new int[1+m][1+m];
	for(int i = 0; i<=m; i++)
	{
		Arrays.fill(ds[i], 987654321);
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(i);
		ds[i][i] = 0;
		while(!q.isEmpty())
		{
			int at = q.poll();
			for(int e : g[at])
			{
				if(ds[i][e] > 1 + ds[i][at])
				{
					ds[i][e] = 1 + ds[i][at];
					q.add(e);
				}
			}
		}
	}
	for(int i = 0; i<k; i++)
	{
		int a = input.nextInt()-1, b = input.nextInt()-1;
		out.println(ds[nodes[a]][nodes[b]]);
	}
	out.close();
}
static class Point
{
	long x, y;
	public Point(long xx, long yy)
	{
		x = xx; y = yy;
	}
	Point minus(Point p)
	{
		return new Point(x - p.x, y - p.y);
	}
	long mag2()
	{
		return x*x+y*y;
	}
	double d2(Point p)
	{
		return minus(p).mag2();
	}
}
public static class input {
	static BufferedReader reader;
	static StringTokenizer tokenizer;

	static void init(InputStream input) {
		reader = new BufferedReader(new InputStreamReader(input));
		tokenizer = new StringTokenizer("");
	}

	static String next() throws IOException {
		while (!tokenizer.hasMoreTokens())
			tokenizer = new StringTokenizer(reader.readLine());
		return tokenizer.nextToken();
	}

	static int nextInt() throws IOException {
		return Integer.parseInt(next());
	}

	static double nextDouble() throws IOException {
		return Double.parseDouble(next());
	}

	static long nextLong() throws IOException {
		return Long.parseLong(next());
	}
}
}

