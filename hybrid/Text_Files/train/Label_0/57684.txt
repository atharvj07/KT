import java.util.*;

import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception {

		int n=sc.nextInt();
		UnionFind u=new UnionFind(n+20);
		int[][]a=new int[n][n];
		for(int i=0;i<n;i++)a[i]=sc.nextIntArray(n);
		PriorityQueue<tuble>pq=new PriorityQueue<Main.tuble>();
		int[]ans=new int[300000];
		int[]ans2=new int[300000];
		int free=0;
		
		for(int i=0;i<n;i++) {
			ans2[free]=a[i][i];
			
			free++;
		}
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(i!=j) {
					pq.add(new tuble(a[i][j], i, j));
				}
			}
		}
		int num=n;
		HashMap<Integer, Integer>hm=new HashMap<Integer, Integer>();
		for(int i=0;i<n;i++) {
			hm.put(u.findSet(i), i);
		}
		while(!pq.isEmpty()) {
			tuble z=pq.poll();
			if(u.isSameSet(z.y, z.z))continue;
			if(ans2[hm.get(u.findSet(z.z))]==z.x) {
				ans[hm.get(u.findSet(z.y))]=hm.get(u.findSet(z.z));
				hm.put(u.findSet(z.y), hm.get(u.findSet(z.z)));
			}else if(ans2[hm.get(u.findSet(z.y))]==z.x) {
				ans[hm.get(u.findSet(z.z))]=hm.get(u.findSet(z.y));
				hm.put(u.findSet(z.z), hm.get(u.findSet(z.y)));
			}else {
			num++;
			ans2[free]=z.x;
			ans[hm.get(u.findSet(z.z))]=free;
			ans[hm.get(u.findSet(z.y))]=free;
			hm.put(u.findSet(z.z), free);
			hm.put(u.findSet(z.y), free);
			free++;
		
			}
			u.unionSet(z.y, z.z);
		}
		pw.println(num);
		for(int i=0;i<num;i++)pw.print(ans2[i]+" ");
		pw.println();
		pw.println(num);
		for(int i=0;i<num-1;i++) {
			pw.println(i+1+" "+(ans[i]+1));
		}
		pw.close();
	}

	public static class UnionFind {
		int[] p, rank, setSize;
		int numSets;

		public UnionFind(int N) {
			p = new int[numSets = N];
			rank = new int[N];
			setSize = new int[N];
			for (int i = 0; i < N; i++) {
				p[i] = i;
				setSize[i] = 1;
			}
		}

		public int findSet(int i) {
			return p[i] == i ? i : (p[i] = findSet(p[i]));
		}

		public boolean isSameSet(int i, int j) {
			return findSet(i) == findSet(j);
		}

		public void unionSet(int i, int j) {
			if (isSameSet(i, j))
				return;
			numSets--;
			int x = findSet(i), y = findSet(j);
			if (rank[x] > rank[y]) {
				p[y] = x;
				setSize[x] += setSize[y];
			} else {
				p[x] = y;
				setSize[y] += setSize[x];
				if (rank[x] == rank[y])
					rank[y]++;
			}
		}

		public int numDisjointSets() {
			return numSets;
		}

		public int sizeOfSet(int i) {
			return setSize[findSet(i)];
		}
	}
	static class Scanner {
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream s) {
			br = new BufferedReader(new InputStreamReader(s));
		}

		public Scanner(FileReader r) {
			br = new BufferedReader(r);
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public String nextLine() throws IOException {
			return br.readLine();
		}

		public double nextDouble() throws IOException {
			String x = next();
			StringBuilder sb = new StringBuilder("0");
			double res = 0, f = 1;
			boolean dec = false, neg = false;
			int start = 0;
			if (x.charAt(0) == '-') {
				neg = true;
				start++;
			}
			for (int i = start; i < x.length(); i++)
				if (x.charAt(i) == '.') {
					res = Long.parseLong(sb.toString());
					sb = new StringBuilder("0");
					dec = true;
				} else {
					sb.append(x.charAt(i));
					if (dec)
						f *= 10;
				}
			res += Long.parseLong(sb.toString()) / f;
			return res * (neg ? -1 : 1);
		}

		public long[] nextlongArray(int n) throws IOException {
			long[] a = new long[n];
			for (int i = 0; i < n; i++)
				a[i] = nextLong();
			return a;
		}

		public Long[] nextLongArray(int n) throws IOException {
			Long[] a = new Long[n];
			for (int i = 0; i < n; i++)
				a[i] = nextLong();
			return a;
		}

		public int[] nextIntArray(int n) throws IOException {
			int[] a = new int[n];
			for (int i = 0; i < n; i++)
				a[i] = nextInt();
			return a;
		}

		public Integer[] nextIntegerArray(int n) throws IOException {
			Integer[] a = new Integer[n];
			for (int i = 0; i < n; i++)
				a[i] = nextInt();
			return a;
		}

		public boolean ready() throws IOException {
			return br.ready();
		}

	}

	static class pair implements Comparable<pair> {
		long x;
		long y;

		public pair(long x, long y) {
			this.x = x;
			this.y = y;
		}

		public String toString() {
			return x + " " + y;
		}

		public boolean equals(Object o) {
			if (o instanceof pair) {
				pair p = (pair) o;
				return p.x == x && p.y == y;
			}
			return false;
		}

		public int hashCode() {
			return new Double(x).hashCode() * 31 + new Double(y).hashCode();
		}

		public int compareTo(pair other) {
			if (this.x == other.x) {
				return Long.compare(this.y, other.y);
			}
			return Long.compare(this.x, other.x);
		}
	}

	static class tuble implements Comparable<tuble> {
		int x;
		int y;
		int z;

		public tuble(int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}

		public String toString() {
			return x + " " + y + " " + z;
		}

		public int compareTo(tuble other) {
			if (this.x == other.x) {
				if (this.y == other.y) {
					return this.z - other.z;
				}
				return this.y - other.y;
			} else {
				return this.x - other.x;
			}
		}
	}

	static long mod = 1000000007;
	static Random rn = new Random();
	static Scanner sc = new Scanner(System.in);
	static PrintWriter pw = new PrintWriter(System.out);
}