
import java.io.*;
import java.math.*;
import java.util.*;

import static java.util.Arrays.*;

public class C {
	private static final int mod = (int)1e9+7;

	final Random random = new Random(0);
	final IOFast io = new IOFast();

	/// MAIN CODE
	int n, m;
	int[] times;
	SimpleAdjListGraph g;
	int[] path;
	int[] depth;
	boolean dfs(int d, int idx, int h) {
		final int MAX_DEPTH = 4 * g.V;
		h ^= 1<<idx;
//		System.err.println(d + " " + idx + " " + h);
		if(h == 0) return true;
		if(d >= MAX_DEPTH || depth[idx * (1<<g.V) + h] <= d) {
			return false;
		}
//		System.err.println(d + " " + idx + " " + h);
		depth[idx * (1<<g.V) + h] = d;
		for(int e = g.head[idx]; e != -1; e = g.next[e]) {
			if(dfs(d + 1, g.to[e], h)) {
				path[d] = idx;
				return true;
			}
		}
		return false;
	}
	boolean naive() {
		final int MAX_DEPTH = 4 * g.V;
		for(int v = 0; v < g.V; v++) {
			depth = new int[g.V * (1<<g.V)];
			path = new int[MAX_DEPTH];
			Arrays.fill(depth, Integer.MAX_VALUE);
			int h = 0;
			for(int i = 0; i < times.length; i++) {
				h |= times[i] << i;
			}
			if(h == 0 || dfs(0, v, h)) {
				io.out.println("find: " + Arrays.toString(path));
				return true;
			}
		}
		io.out.println("not find");
		return false;
	}
	
	public int[] dfs2(final int src) {
		final int[] parent = new int[n];
		final boolean[] vis = new boolean[n];
		final boolean[] vis2 = new boolean[n];
		final int[] cnt = new int[n];
		final int[] st = new int[2 * n + 10];
		int sp = 0;
		
		vis2[src] = true;
		parent[src] = -1;
		st[sp++] = src;
		while(sp != 0) {
			final int v = st[--sp];
//			System.err.println(v);
			if(vis[v]) {
				cnt[v] += times[v];
				if(parent[v] != -1) {
					cnt[parent[v]] += cnt[v];
				}
			}
			else {
				st[sp++] = v;
				for(int e = g.head[v]; e != -1; e = g.next[e]) {
					final int u = g.to[e];
					if(u != parent[v] && !vis2[u]) {
						vis2[u] = true;
						parent[u] = v;
						st[sp++] = u;
					}
				}
				vis[v] = true;
			}
		}
		return cnt;
	}
	
	public int[] dfs3(final int src) {
		final int[] cnt = dfs2(src);
		
		for(int i = 0; i < cnt.length; i++) {
			if(cnt[i] == 0 && times[i] == 1) {
				return null;
			}
		}
//		System.err.println(src + " " + Arrays.toString(cnt));
		final int[] parent = new int[n];
		final boolean[] vis = new boolean[n];
		final boolean[] vis2 = new boolean[n];
		int len = 0;
		final int[] path = new int[5 * n];
		final int[] st = new int[2 * n + 10];
		int sp = 0;

		vis2[src] = true;
		parent[src] = -1;
		st[sp++] = src;
		while(sp != 0) {
			final int v = st[--sp];
			if(cnt[v] == 0) continue;
			path[len++] = v;
			if(vis[v]) {
				times[v] ^= 1;
				if(times[v] == 1 && parent[v] != -1) {
					path[len++] = parent[v];
					path[len++] = v;
					times[v] ^= 1;
					times[parent[v]] ^= 1;
				}
			}
			else if((cnt[v] -= times[v]) > 0) {
				times[v] ^= 1;
				for(int e = g.head[v]; e != -1; e = g.next[e]) {
					final int u = g.to[e];
					if(u != parent[v] && !vis2[u] && cnt[u] > 0) {
						vis2[u] = true;
						parent[u] = v;
						st[sp++] = v;
						st[sp++] = u;
					}
				}
				vis[v] = true;
			}
			else {
				times[v] ^= 1;
			}
		}
		if(times[src] == 1) len--;
		return Arrays.copyOf(path, len);
	}

	void solve() {
		int v0 = -1;
		for(int i = 0; i < n; i++) {
			if(times[i] == 1) {
				v0 = i;
				break;
			}
		}
		if(v0 == -1) {
			io.out.println(0);
			return;
		}
		
//		int[] t0 = times.clone();
		final int[] ans = dfs3(v0);
		if(ans == null) {
//			times = t0.clone();
//			if(naive()) {
//				io.out.println("Crazy2" + " " + Arrays.toString(t0));
//				throw new RuntimeException();
//			}
			io.out.println(-1);
			return;
		}
//		for(int v : ans) t0[v] ^= 1;
//		for(int i = 0; i < t0.length; i++) {
//			if(ans.length > 4 * n || t0[i] != 0) {
//				io.out.println("Crazy" + " " + Arrays.toString(t0));
//				throw new RuntimeException();
//			}
//		}
		
		io.out.println(ans.length);
		for(int v : ans) {
			io.out.print((v+1) + " ");
		}
		io.out.println();
	}
	
	public void run() throws IOException {
//		int TEST_CASE = Integer.parseInt(new String(io.nextLine()).trim());
		int TEST_CASE = 1;
		while(TEST_CASE-- != 0) {
			n = io.nextInt();
			m = io.nextInt();
			g = new SimpleAdjListGraph(n, 2 * m);
			for(int i = 0; i < m; i++) {
				int s = io.nextInt() - 1;
				int t = io.nextInt() - 1;
				g.addEdge(s, t);
				g.addEdge(t, s);
			}
			times = io.nextIntArray(n);
			solve();
//			naive();
			
//			for(int T = 0; T < 1000000 && true; T++) {
//				n = random.nextInt(13)+2;
//				m = random.nextInt(100);
//				g = new SimpleAdjListGraph(n, 2 * m);
//				int[][] es = new int[m][];
//				for(int i = 0; i < m; i++) {
//					int s = random.nextInt(n);
//					int t = random.nextInt(n);
//					g.addEdge(s, t);
//					g.addEdge(t, s);
//					es[i] = new int[]{s, t,};
//				}
//				times = new int[n];
//				for(int i = 0; i < n; i++) times[i] = random.nextInt(2);
//				io.out.println(n + " " + m);
//				for(int i = 0; i < m; i++) {
//					io.out.println((es[i][0]+1) + " " + (es[i][1]+1));
//				}
//				for(int i = 0; i < n; i++) {
//					io.out.print(times[i] + " ");
//				}
//				io.out.println();
//// //				naive();
//				solve();
//			}
		}
	}
	
	static
	class UnionFind {
		private int[] data;
		
		public UnionFind(int size) {
			data = new int[size];
			clear();
		}
		
		public UnionFind(final UnionFind uf) {
			data = uf.data.clone();
		}
		
		public void clear() {
			Arrays.fill(data, -1);
		}
		
		public int root(int x) { return data[x] < 0 ? x : (data[x] = root(data[x])); }
		
		public void union(int x, int y) {
			if((x = root(x)) != (y = root(y))) {
				if(data[y] < data[x]) { final int t = x; x = y; y = t; }
				data[x] += data[y];
				data[y] = x;
			}
		}
		
		public boolean same(int x, int y) { return root(x) == root(y); }
		public int size(int x) { return -data[root(x)]; }
	}

	
	static
	class SimpleAdjListGraph {
		int m, V, E;
		int[] head, next, to;

		public SimpleAdjListGraph(int V, int E) {
			head = new int[V];
			next = new int[E];
			to = new int[E];
			this.V = V;
			this.E = E;
			clear();
		}

		public void clear() {
			m = 0;
			Arrays.fill(head, -1);
		}

		public void addEdge(int s, int t) {
			next[m] = head[s];
			head[s] = m;
			to[m++] = t;
		}
	}


	/// TEMPLATE
	static int gcd(int n, int r) { return r == 0 ? n : gcd(r, n%r); }
	static long gcd(long n, long r) { return r == 0 ? n : gcd(r, n%r); }
	
	static <T> void swap(T[] x, int i, int j) {
		T t = x[i];
		x[i] = x[j];
		x[j] = t;
	}
	
	static void swap(int[] x, int i, int j) {
		int t = x[i];
		x[i] = x[j];
		x[j] = t;
	}
	

	static void radixSort(int[] xs) {
		int[] cnt = new int[(1<<16)+1];
		int[] ys = new int[xs.length];
		
		for(int j = 0; j <= 16; j += 16) {
			Arrays.fill(cnt, 0);
			for(int x : xs) { cnt[(x>>j&0xFFFF)+1]++; }
			for(int i = 1; i < cnt.length; i++) { cnt[i] += cnt[i-1]; }
			for(int x : xs) { ys[cnt[x>>j&0xFFFF]++] = x; }
			{ final int[] t = xs; xs = ys; ys = t; }
		}
	}
	
	static void radixSort(long[] xs) {
		int[] cnt = new int[(1<<16)+1];
		long[] ys = new long[xs.length];
		
		for(int j = 0; j <= 48; j += 16) {
			Arrays.fill(cnt, 0);
			for(long x : xs) { cnt[(int)(x>>j&0xFFFF)+1]++; }
			for(int i = 1; i < cnt.length; i++) { cnt[i] += cnt[i-1]; }
			for(long x : xs) { ys[cnt[(int)(x>>j&0xFFFF)]++] = x; }
			{ final long[] t = xs; xs = ys; ys = t; }
		}
	}
	

	static void arrayIntSort(int[][] x, int... keys) {
		Arrays.sort(x, new ArrayIntsComparator(keys));
	}
	
	static class ArrayIntsComparator implements Comparator<int[]> {
		final int[] KEY;
		
		public ArrayIntsComparator(int... key) {
			KEY = key;
		}
		
		@Override
		public int compare(int[] o1, int[] o2) {
			for(int k : KEY) if(o1[k] != o2[k]) return o1[k] - o2[k];
			return 0;
		}
	}
	
	static class ArrayIntComparator implements Comparator<int[]> {
		final int KEY;
		
		public ArrayIntComparator(int key) {
			KEY = key;
		}
		
		@Override
		public int compare(int[] o1, int[] o2) {
			return o1[KEY] - o2[KEY];
		}
	}
	
	
	void main() throws IOException {
		//		IOFast.setFileIO("rle-size.in", "rle-size.out");
		try {
			run();
		}
		catch (EndOfFileRuntimeException e) { }
		io.out.flush();
	}

	public static void main(String[] args) throws IOException {
		new C().main();
	}
	
	static class EndOfFileRuntimeException extends RuntimeException {
		private static final long serialVersionUID = -8565341110209207657L; }

	static
	public class IOFast {
		private BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		private PrintWriter out = new PrintWriter(System.out);

		void setFileIO(String ins, String outs) throws IOException {
			out.flush();
			out.close();
			in.close();
			in = new BufferedReader(new FileReader(ins));
			out = new PrintWriter(new FileWriter(outs));
			System.err.println("reading from " + ins);
		}

		//		private static final int BUFFER_SIZE = 50 * 200000;
		private static int pos, readLen;
		private static final char[] buffer = new char[1024 * 8];
		private static char[] str = new char[500*8*2];
		private static boolean[] isDigit = new boolean[256];
		private static boolean[] isSpace = new boolean[256];
		private static boolean[] isLineSep = new boolean[256];

		static {
			for(int i = 0; i < 10; i++) { isDigit['0' + i] = true; }
			isDigit['-'] = true;
			isSpace[' '] = isSpace['\r'] = isSpace['\n'] = isSpace['\t'] = true;
			isLineSep['\r'] = isLineSep['\n'] = true;
		}

		public int read() throws IOException {
			if(pos >= readLen) {
				pos = 0;
				readLen = in.read(buffer);
				if(readLen <= 0) { throw new EndOfFileRuntimeException(); }
			}
			return buffer[pos++];
		}

		public int nextInt() throws IOException {
			int len = 0;
			str[len++] = nextChar();
			len = reads(len, isSpace);
			
			int i = 0;
			int ret = 0;
			if(str[0] == '-') { i = 1; }
			for(; i < len; i++) ret = ret * 10 + str[i] - '0';
			if(str[0] == '-') { ret = -ret; }
			return ret;
//			return Integer.parseInt(nextString());
		}

		public long nextLong() throws IOException {
			int len = 0;
			str[len++] = nextChar();
			len = reads(len, isSpace);
			
			int i = 0;
			long ret = 0;
			if(str[0] == '-') { i = 1; }
			for(; i < len; i++) ret = ret * 10 + str[i] - '0';
			if(str[0] == '-') { ret = -ret; }
			return ret;
//			return Long.parseLong(nextString());
		}

		public char nextChar() throws IOException {
			while(true) {
				final int c = read();
				if(!isSpace[c]) { return (char)c; }
			}
		}
		
		int reads(int len, boolean[] accept) throws IOException {
			try {
				while(true) {
					final int c = read();
					if(accept[c]) { break; }
					
					if(str.length == len) {
						char[] rep = new char[str.length * 3 / 2];
						System.arraycopy(str, 0, rep, 0, str.length);
						str = rep;
					}
					
					str[len++] = (char)c;
				}
			}
			catch(EndOfFileRuntimeException e) { ; }
			
			return len;
		}
		
		int reads(char[] cs, int len, boolean[] accept) throws IOException {
			try {
				while(true) {
					final int c = read();
					if(accept[c]) { break; }
					cs[len++] = (char)c;
				}
			}
			catch(EndOfFileRuntimeException e) { ; }
			
			return len;
		}

		public char[] nextLine() throws IOException {
			int len = 0;
			str[len++] = nextChar();
//			str[len++] = (char)read();
			len = reads(len, isLineSep);
			
			try {
				if(str[len-1] == '\r') { len--; read(); }
			}
			catch(EndOfFileRuntimeException e) { ; }
			
			return Arrays.copyOf(str, len);
		}

		public String nextString() throws IOException {
			return new String(next());
		}

		public char[] next() throws IOException {
			int len = 0;
			str[len++] = nextChar();
			len = reads(len, isSpace);
			return Arrays.copyOf(str, len);
		}

		public int next(char[] cs) throws IOException {
			int len = 0;
			cs[len++] = nextChar();
			len = reads(cs, len, isSpace);
			return len;
		}

		public double nextDouble() throws IOException {
			return Double.parseDouble(nextString());
		}

		public long[] nextLongArray(final int n) throws IOException {
			final long[] res = new long[n];
			for(int i = 0; i < n; i++) {
				res[i] = nextLong();
			}
			return res;
		}

		public int[] nextIntArray(final int n) throws IOException {
			final int[] res = new int[n];
			for(int i = 0; i < n; i++) {
				res[i] = nextInt();
			}
			return res;
		}

		public int[][] nextIntArray2D(final int n, final int k) throws IOException {
			final int[][] res = new int[n][];
			for(int i = 0; i < n; i++) {
				res[i] = nextIntArray(k);
			}
			return res;
		}

		public int[][] nextIntArray2DWithIndex(final int n, final int k) throws IOException {
			final int[][] res = new int[n][k+1];
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < k; j++) {
					res[i][j] = nextInt();
				}
				res[i][k] = i;
			}
			return res;
		}

		public double[] nextDoubleArray(final int n) throws IOException {
			final double[] res = new double[n];
			for(int i = 0; i < n; i++) {
				res[i] = nextDouble();
			}
			return res;
		}

	}

}
