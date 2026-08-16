import java.io.*;
import java.util.*;

public class Main {

	static int INF = (int) 1e9;

	static int search(ArrayList<int[]> a, int x) {
		int ans = a.size();
		int lo = 0, hi = ans - 1;
		while (lo <= hi) {
			int mid = lo + hi >> 1;
			int[] tmp = a.get(mid);
			if (tmp[1] < x)
				lo = mid + 1;
			else if (tmp[1] > x)
				hi = mid - 1;
			else {
				ans = mid;
				hi = mid - 1;
			}
		}
		return ans;
	}

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner();
		PrintWriter out = new PrintWriter(System.out);
		int n = sc.nextInt(), m = sc.nextInt(), dist[] = new int[n];
		HashSet<Integer>[] sets = new HashSet[n];
		ArrayList<int[]>[] adj = new ArrayList[n];
		for (int i = 0; i < n; i++) {
			adj[i] = new ArrayList();
			sets[i] = new HashSet();
			dist[i] = i == 0 ? 0 : INF;
		}

		while (m-- > 0) {
			int u = sc.nextInt() - 1, v = sc.nextInt() - 1, c = sc.nextInt();
			adj[u].add(new int[] { v, c });
			adj[v].add(new int[] { u, c });
		}
		for (int i = 0; i < n; i++)
			Collections.sort(adj[i], (x, y) -> x[1] - y[1]);

		Deque<int[]> q = new LinkedList();
		q.add(new int[] { 0, INF, 0 });
		for (int d = 0; !q.isEmpty(); d++) {
			HashSet<Integer> process = new HashSet();
			while (!q.isEmpty() && q.peekFirst()[2] == d) {
				int[] curr = q.pollFirst();
				int u = curr[0], from = curr[1];
				process.add(u);
				// search for same
				for (int i = search(adj[u], from); i < adj[u].size() && adj[u].get(i)[1] == from; i++) {
					int v = adj[u].get(i)[0];
					if (dist[v] >= d && sets[v].add(from)) {
						q.addFirst(new int[] { v, from, d });
						dist[v] = d;
					}
				}

			}
			for (int u : process) {
				for (int[] v : adj[u])
					if (dist[v[0]] > d && sets[v[0]].add(v[1])) {
						dist[v[0]] = d + 1;
						q.addLast(new int[] { v[0], v[1], d + 1 });
					}
			}
		}
		System.out.println(dist[n - 1] == INF ? -1 : dist[n - 1]);
		out.close();

	}

	static class Scanner {
		BufferedReader br;
		StringTokenizer st;

		Scanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		Scanner(String fileName) throws FileNotFoundException {
			br = new BufferedReader(new FileReader(fileName));
		}

		String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		String nextLine() throws IOException {
			return br.readLine();
		}

		int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		long nextLong() throws NumberFormatException, IOException {
			return Long.parseLong(next());
		}

		double nextDouble() throws NumberFormatException, IOException {
			return Double.parseDouble(next());
		}

		boolean ready() throws IOException {
			return br.ready();
		}

		int[] nxtArr(int n) throws IOException {
			int[] ans = new int[n];
			for (int i = 0; i < n; i++)
				ans[i] = nextInt();
			return ans;
		}

	}

	static void sort(int[] a) {
		shuffle(a);
		Arrays.sort(a);
	}

	static void shuffle(int[] a) {
		int n = a.length;
		Random rand = new Random();
		for (int i = 0; i < n; i++) {
			int tmpIdx = rand.nextInt(n);
			int tmp = a[i];
			a[i] = a[tmpIdx];
			a[tmpIdx] = tmp;
		}
	}

}