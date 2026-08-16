import java.util.*;
import java.io.*;

public class b {

	public static void main(String[] args) {
		new b();
	}
	
	public b() {
		FastScanner fs = new FastScanner();
		System.err.println("");

		int n = fs.nextInt(), m = fs.nextInt();
		long[] xs = new long[n], ys = new long[n];
		TreeSet<Long> vals = new TreeSet<>();
		int[] loc = new int[n];
		
		for(int i = 0; i < n; i++) {
			xs[i] = fs.nextInt();
			ys[i] = fs.nextInt();
			vals.add(ys[i]-xs[i]);
		}
		HashMap<Long, Integer> map = new HashMap<>();
		for(long ll : vals) map.put(ll, map.size());
		int N = map.size();
		
		long[] arr = new long[N];
		int ptr = 0;
		for(long ll : arr) arr[ptr++] = ll;
		for(int i = 0; i < n; i++) loc[i] = map.get(ys[i]-xs[i]);
		
		ArrayList<Integer>[] adj = new ArrayList[n];
		for(int i = 0; i < n; i++) adj[i] = new ArrayList<>();
		for(int i = 0; i < m; i++) {
			int u = fs.nextInt()-1, v = fs.nextInt()-1;
			adj[u].add(v); adj[v].add(u);
		}
		for(int i = 0; i < n; i++) adj[i].add(i);
		
		BIT cnt = new BIT(N);
		BIT sumX = new BIT(N), sumY = new BIT(N);
		for(int i = 0; i < n; i++) {
			int pos = loc[i];
			cnt.update(pos, 1);
			sumX.update(pos, xs[i]);
			sumY.update(pos, ys[i]);
		}
		
		long[] res = new long[n];
		for(int u = 0; u < n; u++) {
			for(int v : adj[u]) {
				int pos = loc[v];
				cnt.update(pos, -1);
				sumX.update(pos, -xs[v]);
				sumY.update(pos, -ys[v]);
			}
			
			long cntLess = 0, sumXMore = 0;
			long cntMore = 0, sumYLess = 0;
			int idx = -1;
			if(loc[u] > 0) {
				idx = loc[u]-1;
				cntLess = cnt.read(idx);
				sumYLess = sumY.range(0, idx);
			}
			cntMore = cnt.read(N-1)-cntLess;
			sumXMore = sumX.range(idx+1, N-1);
			
			res[u] = cntLess*xs[u] + cntMore*ys[u];
			res[u] += sumXMore + sumYLess;

			for(int v : adj[u]) {
				int pos = loc[v];
				cnt.update(pos, 1);
				sumX.update(pos, xs[v]);
				sumY.update(pos, ys[v]);
			}
		}
		
		PrintWriter out = new PrintWriter(System.out);
		for(int i = 0; i < n; i++) out.print(res[i] + " ");
		out.println();
		out.close();
	}
	
	class BIT {
		int n;
		long[] tree;
		
		public BIT(int n) {
			this.n = n;
			tree = new long[n + 2];
		}
		long read(int i) {
			i++;
			long sum = 0;
			while (i > 0) {
				sum += tree[i];
				i -= i & -i;
			}
			return sum;
		}
		
		long range(int i, int j) {
			long res = read(j);
			if(i > 0) res -= read(i-1);
			return res;
		}
		
		void update(int i, long val) {
			i++;
			while (i <= n) {
				tree[i] += val;
				i += i & -i;
			}
		}
	}
	
	class FastScanner {
		BufferedReader br;
		StringTokenizer st;
		public FastScanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
			st = new StringTokenizer("");
		}
		String next() {
			if(st.hasMoreTokens()) return st.nextToken();
			try { st = new StringTokenizer(br.readLine()); } catch (Exception e) {}
			return next();
		}
		int nextInt() {
			return Integer.parseInt(next());
		}
	}
	
}
