import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;

public class Main {
	public static int MOD = 1000000007;
	public static void main(String[] args) {
		IO io = new IO();
		int n = io.nextInt();
		int m = io.nextInt();
		Graph g = new Graph(n);
		for(int i=0;i<m;i++) {
			int s = io.nextInt() - 1;
			int d = io.nextInt() - 1;
			g.addEdge(d, s, 1);
		}
		Graph f = g.noSCCGraph(); //根付き森になる
		int n2 = f.n;
		boolean[] used = new boolean[n2];
		long ans = 1;
		for(int i=n2-1;i>=0;i--) {
			if (used[i]) continue;
			ans = ans * count(i,f,used) % MOD;
		}
//		System.err.println(f);
		io.println(ans);
		io.flush();
	}

	public static long count(int v, Graph f, boolean[] used) {
		used[v] = true;
		long res = 1;
		for(Graph.Edge e: f.graph[v]) {
			res = res * count(e.to, f, used) % MOD;
		}
		res++;
		if (res >= MOD) res -= MOD;
		return res;
	}

}
class Graph {
	public static final int INF = 1<<29;
	int n;
	ArrayList<Edge>[] graph;

	@SuppressWarnings("unchecked")
	public Graph(int n) {
		this.n = n;
		this.graph = new ArrayList[n];
		for(int i=0;i<n;i++) {
			graph[i] = new ArrayList<Edge>();
		}
	}

	public void addBidirectionalEdge(int from,int to,int cost) {
		addEdge(from,to,cost);
		addEdge(to,from,cost);
	}
	public void addEdge(int from,int to,int cost) {
		graph[from].add(new Edge(to, cost));
	}

	public ArrayList<ArrayList<Integer>> stronglyConnectedComponents() {
		ArrayList<ArrayList<Integer>> scc = new ArrayList<ArrayList<Integer>>();
		int[] num = new int[n];
		int[] low = new int[n];
		int[] time = new int[1];
		ArrayDeque<Integer> s = new ArrayDeque<Integer>();
		boolean[] inS = new boolean[n];
		for(int u=0;u<n;u++) {
			if (num[u] == 0) {
				visitSCC(u,scc,s,inS,low,num,time);
			}
		}
		return scc;
	}
	private void visitSCC(int v, ArrayList<ArrayList<Integer>> scc,
			ArrayDeque<Integer> s, boolean[] inS, int[] low, int[] num, int[] time) {
		low[v] = num[v] = ++time[0];
		s.push(v);
		inS[v] = true;
		for(Edge e:graph[v]) {
			int w = e.to;
			if (num[w] == 0) {
				visitSCC(w,scc,s,inS,low,num,time);
				low[v] = Math.min(low[v],low[w]);
			}else if (inS[w]) {
				low[v] = Math.min(low[v],num[w]);
			}
		}
		if (low[v] == num[v]) {
			ArrayList<Integer> scc1 = new ArrayList<Integer>();
			while(true) {
				int w = s.poll();
				inS[w] = false;
				scc1.add(w);
				if (v == w) {
					break;
				}
			}
			scc.add(scc1);
		}
	}

	public Graph mergedGraph(ArrayList<ArrayList<Integer>> scc) {
		int[] map = new int[n];
		int m = scc.size();
		for(int i=0;i<m;i++) {
			ArrayList<Integer> l = scc.get(i);
			for(int v: l) {
				map[v] = i;
			}
		}
		Graph g2 = new Graph(m);
		HashSet<Long> edge = new HashSet<Long>();
		for(int u=0;u<n;u++) {
			for(Edge e:graph[u]) {
				int v = e.to;
				if (map[u] == map[v]) {
					continue;
				}
				edge.add(((long) map[u]<<32) + map[v]);
			}
		}
		for(long e:edge) {
			g2.addEdge((int) (e>>32), (int) (e & 0xffff), 1);
		}
		return g2;
	}

	public Graph noSCCGraph() {
		return mergedGraph(stronglyConnectedComponents());
	}

	class Edge {
		int to;
		int cost;
		public Edge(int to,int cost) {
			this.to = to;
			this.cost = cost;
		}
	}

	public String toString() {
		StringBuilder sb = new StringBuilder();
		for(int i=0;i<n;i++) {
			for(Edge e: graph[i]) {
				sb.append("(" + i + "," + e.to + ")");
			}
		}
		return sb.toString();
	}
}

class IO extends PrintWriter {
	private final InputStream in;
	private final byte[] buffer = new byte[1024];
	private int ptr = 0;
	private int buflen = 0;

	public IO() { this(System.in);}
	public IO(InputStream source) { super(System.out); this.in = source;}
	private boolean hasNextByte() {
		if (ptr < buflen) {
			return true;
		}else{
			ptr = 0;
			try {
				buflen = in.read(buffer);
			} catch (IOException e) {
				e.printStackTrace();
			}
			if (buflen <= 0) {
				return false;
			}
		}
		return true;
	}
	private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
	private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
	private static boolean isNewLine(int c) { return c == '\n' || c == '\r';}
	public boolean hasNext() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++; return hasNextByte();}
	public boolean hasNextLine() { while(hasNextByte() && isNewLine(buffer[ptr])) ptr++; return hasNextByte();}
	public String next() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while(isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	public char[] nextCharArray(int len) {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		char[] s = new char[len];
		int i = 0;
		int b = readByte();
		while(isPrintableChar(b)) {
			if (i == len) {
				throw new InputMismatchException();
			}
			s[i++] = (char) b;
			b = readByte();
		}
		return s;
	}
	public String nextLine() {
		if (!hasNextLine()) {
			throw new NoSuchElementException();
		}
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while(!isNewLine(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	public long nextLong() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		long n = 0;
		boolean minus = false;
		int b = readByte();
		if (b == '-') {
			minus = true;
			b = readByte();
		}
		if (b < '0' || '9' < b) {
			throw new NumberFormatException();
		}
		while(true){
			if ('0' <= b && b <= '9') {
				n *= 10;
				n += b - '0';
			}else if(b == -1 || !isPrintableChar(b)){
				return minus ? -n : n;
			}else{
				throw new NumberFormatException();
			}
			b = readByte();
		}
	}
	public int nextInt() {
		long nl = nextLong();
		if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) {
			throw new NumberFormatException();
		}
		return (int) nl;
	}
	public char nextChar() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		return (char) readByte();
	}
	public double nextDouble() { return Double.parseDouble(next());}
	public int[] nextIntArray(int n) { int[] a = new int[n]; for(int i=0;i<n;i++) a[i] = nextInt(); return a;}
	public long[] nextLongArray(int n) { long[] a = new long[n]; for(int i=0;i<n;i++) a[i] = nextLong(); return a;}
	public double[] nextDoubleArray(int n) { double[] a = new double[n]; for(int i=0;i<n;i++) a[i] = nextDouble(); return a;}
	public void nextIntArrays(int[]... a) { for(int i=0;i<a[0].length;i++) for(int j=0;j<a.length;j++) a[j][i] = nextInt();}
	public int[][] nextIntMatrix(int n,int m) { int[][] a = new int[n][]; for(int i=0;i<n;i++) a[i] = nextIntArray(m); return a;}
	public char[][] nextCharMap(int n,int m) { char[][] a = new char[n][]; for(int i=0;i<n;i++) a[i] = nextCharArray(m); return a;}
	public void close() { super.close(); try {in.close();} catch (IOException e) {}}
}


