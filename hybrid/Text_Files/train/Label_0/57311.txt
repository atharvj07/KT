import java.io.*;
import java.util.*;
public class a
{
	public static void main(String[] args) throws IOException {
		input.init(System.in);
		PrintWriter out = new PrintWriter(System.out);
		int n = input.nextInt(), m = input.nextInt();
		int gcost = input.nextInt(), scost = input.nextInt();
		Edge[] es = new Edge[m];
		for(int i = 0; i<m; i++) es[i] = new Edge(input.nextInt()-1, input.nextInt()-1, input.nextInt(), input.nextInt());
		Arrays.sort(es);
		int[] as = new int[m], bs= new int[m], gs = new int[m], ss = new int[m];
		for(int i = 0; i<m; i++)
		{
			as[i] = es[i].a;
			bs[i] = es[i].b;
			gs[i] = es[i].g;
			ss[i] = es[i].s;
		}
		ArrayList<Integer> mst = new ArrayList<Integer>();
		DisjointSet ds = new DisjointSet(n);
		for(int i = 0; i<m; i++)
		{
			if(ds.find(as[i]) != ds.find(bs[i]))
			{
				ds.union(as[i], bs[i]);
				mst.add(i);
			}
		}
		int maxG = 0, maxS = 0;
		for(int e : mst)
		{
			maxG = Math.max(maxG, gs[e]);
			maxS = Math.max(maxS, ss[e]);
		}
		long res = (long)gcost * maxG + (long)scost * maxS;
//		sortByG = true;
//		Arrays.sort(es);
		//ArrayList<Integer>[] curg = new ArrayList[n];
		int[][] curg = new int[n][n];
		int[] degs = new int[n];
		for(int e = 0; e<m; e++)
		{
			if(gs[e] >= maxG) continue;
			degs = new int[n];
			for(int ee : mst)
			{
				curg[as[ee]][degs[as[ee]]++] = bs[ee];
				curg[bs[ee]][degs[bs[ee]]++] = as[ee];
				//curg[ee.a].add(ee.b);
				//curg[ee.b].add(ee.a);
			}
			int a = as[e], b = bs[e];
			if(a == b) continue;
			int[] da = bfs(a, curg, degs), db = bfs(b, curg, degs);
			int max = -1;
			int maxi = -1;
			for(int ii = 0; ii<mst.size(); ii++)
			{
				int ee = mst.get(ii);
				if(Math.min(da[as[ee]], da[bs[ee]]) + Math.min(db[as[ee]], db[bs[ee]]) + 1 == da[b])
				{
					if(max == -1 || gs[ee] > gs[max])
					{
						maxi = ii;
						max = ee;
					}
				}
			}
			if(gs[max] < gs[e])
			{
				continue;
			}
			mst.remove(maxi);
			mst.add(e);
			maxG = maxS = 0;
			for(int ee : mst)
			{
				maxG = Math.max(maxG, gs[ee]);
				maxS = Math.max(maxS, ss[ee]);
			}
			res = Math.min(res, (long)gcost * maxG + (long)scost * maxS);
		}
		out.println(mst.size() == n-1 ? res : -1);
		out.close();
	}
	static int[] bfs(int start, int[][] g, int[] degs)
	{
		int n = g.length;
		int[] ds = new int[n];
		Arrays.fill(ds, n+1);
		ds[start] = 0;
		int[] q = new int[n+1];
		int s = 0, e = 0;
		q[e++] = start;
		while(s < e)
		{
			int at = q[s++];
			for(int i = 0; i<degs[at]; i++)
			{
				int to = g[at][i];
				if(ds[to] > 1 + ds[at])
				{
					ds[to] = 1 + ds[at];
					q[e++] = to;
				}
			}
		}
		return ds;
	}
	static boolean sortByG = false;
	static class Edge implements Comparable<Edge>
	{
		int a, b, g, s;
		public Edge(int aa, int bb, int gg, int ss)
		{
			a = aa; b = bb; g = gg; s = ss;
		}
		@Override
		public int compareTo(Edge o) {
			// TODO Auto-generated method stub
			if(sortByG) return g - o.g;
			return s - o.s;
		}
	}
	public static class DisjointSet
	{
		int[] map; //negative if root, more negative means bigger set; if nonnegative, then it indicates the parent 
		public DisjointSet(int n)
		{
			map = new int[n+1];
			Arrays.fill(map, -1);
		}
		public int find(int x)
		{
			if(map[x] < 0) return x;
		    return map[x] = find(map[x]);
		}
		public void union(int a, int b)
		{
			int roota = find(a), rootb = find(b);
			if(roota == rootb)
				return;
			if(map[roota] < map[rootb])
			{
				map[roota] += map[rootb]; //add the sizes
				map[rootb] = roota; //connect the smaller to the bigger
			}
			else
			{
				map[rootb] += map[roota];
				map[roota] = rootb;
			}
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