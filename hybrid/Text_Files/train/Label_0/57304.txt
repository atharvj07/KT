
import java.io.*;
import java.util.*;

public class B {

	public static void main(String[] args) throws IOException {

		Scanner sc = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);

		int n = sc.nextInt(), k = sc.nextInt();
		int[] a = new int[n];
		for(int i = 0; i < n; ++i)
			a[i] = sc.nextInt();
		int[][] DP = new int[k + 1][n + 1];
		int[] pos = new int[n + 1];
		Arrays.fill(pos, n);
		for(int i = n - 1, cnt = 0; i >= 0; --i)
		{
			if(pos[a[i]] == n)
				++cnt;
			pos[a[i]] = i;
			DP[1][i] = cnt;
		}
		for(int j = 2; j <= k; ++j)
		{
			SegmentTree st = new SegmentTree(DP[j - 1]);
			Arrays.fill(pos, n);
			for(int i = n - 1; i >= 0; --i)
			{
				st.update(i + 1, pos[a[i]]);
				DP[j][i] = st.query(i + 1);
				pos[a[i]] = i;
			}
		}
		
		out.println(DP[k][0]);
		out.close();
	}

	static class SegmentTree
	{
		int[] tree, lazy, arr;
		int N;

		SegmentTree(int[] arr)
		{
			this.arr = arr;
			N = 1; while(N < arr.length) N <<= 1;
			tree = new int[N << 1];
			lazy = new int[N << 1];
			for(int i = 0; i < arr.length; ++i)
				tree[i + N] = arr[i];
			for(int i = N - 1; i > 0; --i)
				tree[i] = Math.max(tree[i << 1], tree[i << 1 | 1]);
		}

		void update(int l, int r) { update(1, 1, N, l + 1, r + 1); }

		void update(int v, int b, int e, int l, int r)
		{
			if(r < b || e < l)
				return;
			if(l <= b && e <= r)
			{
				tree[v] += 1;
				lazy[v] += 1;
				return;
			}
			int mid = (b + e >> 1);
			push(v, b, mid, e);
			update(v << 1, b, mid, l, r);
			update(v << 1 | 1, mid + 1, e, l, r);
			tree[v] = Math.max(tree[v << 1], tree[v << 1 | 1]);
		}

		int query(int l) { return query(1, 1, N, l); }

		int query(int v, int b, int e, int l)
		{
			if(l > e)
				return 0;
			if(l <= b)
				return tree[v];
			int mid = (b + e >> 1);
			push(v, b, mid, e);
			int q1 = query(v << 1, b, mid, l);
			int q2 = query(v << 1 | 1, mid + 1, e, l);
			return Math.max(q1, q2);
		}

		void push(int v, int b, int mid, int e)
		{
			if(lazy[v] == 0)
				return;
			tree[v << 1] += lazy[v];
			tree[v << 1 | 1] += lazy[v];
			lazy[v << 1] += lazy[v];
			lazy[v << 1 | 1] += lazy[v];
			lazy[v] = 0;
		}
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