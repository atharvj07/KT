
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.StringTokenizer;

public class C {

	static ArrayList<Integer>[] adjList;

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		adjList = new ArrayList[n];
		for (int i = 0; i < n; i++)
			adjList[i] = new ArrayList<Integer>();
		boolean[][] con = new boolean[n][n];
		for (int i = 0; i < m; i++) {
			int u = sc.nextInt() - 1;
			int v = sc.nextInt() - 1;
			adjList[u].add(v);
			adjList[v].add(u);
			con[u][v] = con[v][u] = true;
		}

		// i -> v , u -> v
		int min = 5000;
		for (int i = 0; i < n; i++) {
			for (int v : adjList[i]) {
				for (int u : adjList[v]) {
					if (u == v)
						continue;
					if (con[i][u]) {
						min = Math.min(adjList[i].size() + adjList[v].size() + adjList[u].size() - 6, min);
					}
				}
			}
		}
		System.out.println(min == 5000 ? -1 : min);

	}

	static class Scanner {
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream s) {
			br = new BufferedReader(new InputStreamReader(s));
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
			return Double.parseDouble(next());
		}

		public boolean ready() throws IOException {
			return br.ready();
		}

		public int[] nextIntArray(int n) throws IOException {
			int[] a = new int[n];
			for (int i = 0; i < n; i++)
				a[i] = nextInt();
			return a;
		}

		public int[] nextIntArray1(int n) throws IOException {
			int[] a = new int[n + 1];
			for (int i = 1; i <= n; i++)
				a[i] = nextInt();
			return a;
		}

		public int[] nextIntArraySorted(int n) throws IOException {
			int[] a = nextIntArray(n);
			Random r = new Random();
			for (int i = 0; i < n; i++) {
				int j = i + r.nextInt(n - i);
				int t = a[i];
				a[i] = a[j];
				a[j] = t;
			}
			Arrays.sort(a);
			return a;
		}

		public long[] nextLongArray(int n) throws IOException {
			long[] a = new long[n];
			for (int i = 0; i < n; i++)
				a[i] = nextLong();
			return a;
		}

		public long[] nextLongArray1(int n) throws IOException {
			long[] a = new long[n + 1];
			for (int i = 1; i <= n; i++)
				a[i] = nextLong();
			return a;
		}

		public long[] nextLongArraySorted(int n) throws IOException {
			long[] a = nextLongArray(n);
			Random r = new Random();
			for (int i = 0; i < n; i++) {
				int j = i + r.nextInt(n - i);
				long t = a[i];
				a[i] = a[j];
				a[j] = t;
			}
			Arrays.sort(a);
			return a;
		}
	}
}