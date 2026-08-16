import java.util.*;
import java.io.*;

public class E_1454 {
	
	static ArrayList<Integer>[] adjList;
	static int s, d;
	static boolean[] path, vis;
	
	public static boolean findPath(int u) {
		vis[u] = true;
		if(u == d)
			return path[u] = true;
		boolean flag = false;
		for(int v : adjList[u])
			if(!vis[v])
				flag |= findPath(v);
		
		return path[u] = flag;
	}
	
	public static int dfs(int u) {
		vis[u] = true;
		int cnt = 1;
		for(int v : adjList[u])
			if(!vis[v])
				cnt += dfs(v);
		return cnt;
	}
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(System.out);
		
		int t = sc.nextInt();
		while(t-->0) {
			int n = sc.nextInt();
			adjList = new ArrayList[n];
			for(int i = 0; i < n; i++)
				adjList[i] = new ArrayList<>();
			DSU set = new DSU(n);
			
			for(int i = 0; i < n; i++) {
				int u = sc.nextInt() - 1, v = sc.nextInt() - 1;
				if(set.union(u, v)) {
					adjList[u].add(v);
					adjList[v].add(u);
				} else {
					s = u;
					d = v;
				}
			}
			
			path = new boolean[n];
			vis = new boolean[n];
			findPath(s);
			
			ArrayList<Integer> nodes = new ArrayList<>();
			for(int i = 0; i < n; i++)
				if(path[i])
					nodes.add(i);
			
			ArrayList<Integer> count = new ArrayList<>();
			vis = new boolean[n];
			for(int u : nodes)
				vis[u] = true;
			
			long cnt = 0;
			for(int u : nodes) {
				vis[u] = false;
				int x = dfs(u);
				count.add(x);
				cnt += x;
			}
			
			long ans = 0;
			for(int i = 0; i < count.size(); i++) {
				cnt -= count.get(i);
				ans += 1l * count.get(i) * cnt;
			}
			
			pw.println(ans + 1l * n * (n - 1) / 2);
		}
		
		pw.flush();
	}
	
	public static class DSU {
		
		int sets;
		int[] parent, rank;
		
		public DSU(int size) {
			sets = size;
			parent = new int[size];
			rank = new int[size];
			
			for(int i = 0; i < parent.length; i++)
				parent[i] = i;
		}
		
		public int findParent(int u) {
			return parent[u] == u ? u : (parent[u] = findParent(parent[u]));
		}
		
		public boolean union(int u, int v) {
			int x = findParent(u);
			int y = findParent(v);
			
			if(x == y)
				return false;
			
			if(rank[x] >= rank[y]) {
				parent[y] = x;
				if(rank[x] == rank[y])
					rank[x]++;
			} else {
				parent[x] = y;
			}
			
			sets--;
			return true;
		}
	}


	public static class Scanner {
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream system) {
			br = new BufferedReader(new InputStreamReader(system));
		}

		public Scanner(String file) throws Exception {
			br = new BufferedReader(new FileReader(file));
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public String nextLine() throws IOException {
			return br.readLine();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		public char nextChar() throws IOException {
			return next().charAt(0);
		}

		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public int[] nextIntArray(int n) throws IOException {
			int[] array = new int[n];
			for (int i = 0; i < n; i++)
				array[i] = nextInt();
			return array;
		}

		public Integer[] nextIntegerArray(int n) throws IOException {
			Integer[] array = new Integer[n];
			for (int i = 0; i < n; i++)
				array[i] = new Integer(nextInt());
			return array;
		}

		public long[] nextLongArray(int n) throws IOException {
			long[] array = new long[n];
			for (int i = 0; i < n; i++)
				array[i] = nextLong();
			return array;
		}

		public double[] nextDoubleArray(int n) throws IOException {
			double[] array = new double[n];
			for (int i = 0; i < n; i++)
				array[i] = nextDouble();
			return array;
		}

		public static int[] shuffle(int[] a) {
			int n = a.length;
			Random rand = new Random();
			for (int i = 0; i < n; i++) {
				int tmpIdx = rand.nextInt(n);
				int tmp = a[i];
				a[i] = a[tmpIdx];
				a[tmpIdx] = tmp;
			}
			return a;
		}

		public boolean ready() throws IOException {
			return br.ready();
		}

		public void waitForInput() throws InterruptedException {
			Thread.sleep(3000);
		}
	}
}
