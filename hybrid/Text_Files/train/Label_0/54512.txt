
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.List;
import java.util.PriorityQueue;
import java.util.stream.Stream;
public class Main {
	static InputStream is;
	static PrintWriter out;
	static String INPUT = "";
	static final int INF = Integer.MAX_VALUE / 2;
	private static void solve() {
		int V = ni();
		int E = ni();
		int r = ni();
		@SuppressWarnings("unchecked")
		List<Edge>[] edges = Stream.generate(ArrayList::new).limit(V).toArray(List[]::new);
		for(int i=0;i<E;i++){
			edges[ni()].add(new Edge(ni(), ni()));
		}
		int[] dist = new int[V];
		int[] pred = new int[V];
		if(!bellmanFord(edges, r, dist, pred)){
			System.out.println("NEGATIVE CYCLE");
			return ;
		}
		//System.out.println(Arrays.toString(findNegativeCycle(edges)));
		//shortestPaths(edges, r, dist, pred);
		for(int i=0;i<V;i++){
			if(Math.abs(dist[i])==Integer.MAX_VALUE/2){
				System.out.println("INF");
				continue;
			}
			System.out.println(dist[i]);
		}
	}
	public static void shortestPaths(List<Edge>[] edges, int s, int[] prio, int[] pred) {
		Arrays.fill(pred, -1);
		Arrays.fill(prio, Integer.MAX_VALUE);
		prio[s] = 0;
		PriorityQueue<Long> q = new PriorityQueue<>();
		q.add((long) s);
		while (!q.isEmpty()) {
			long cur = q.remove();
			int curu = (int) cur;
			if (cur >>> 32 != prio[curu])
				continue;
			for (Edge e : edges[curu]) {
				int v = e.t;
				int nprio = prio[curu] + e.cost;
				if (prio[v] > nprio) {
					prio[v] = nprio;
					pred[v] = curu;
					q.add(((long) nprio << 32) + v);
				}
			}
		}
	}

	static class Edge {
		int t;
		int cost;

		public Edge(int t, int cost) {
			this.t = t;
			this.cost = cost;
		}
	}
	public static int[] findNegativeCycle(List<Edge>[] graph) {
		int n = graph.length;
		int[] pred = new int[n];
		Arrays.fill(pred, -1);
		int[] dist = new int[n];
		int last = -1;
		for (int step = 0; step < n; step++) {
			last = -1;
			for (int u = 0; u < n; u++) {
				if (dist[u] == INF) continue;
				for (Edge e : graph[u]) {
					if (dist[e.t] > dist[u] + e.cost) {
						dist[e.t] = Math.max(dist[u] + e.cost, -INF);
						dist[e.t] = Math.max(dist[e.t], -INF);
						pred[e.t] = u;
						last = e.t;
					}
				}
			}
			if (last == -1)
				return null;
		}
		for (int i = 0; i < n; i++) {
			last = pred[last];
		}
		int[] p = new int[n];
		int cnt = 0;
		for (int u = last; u != last || cnt == 0; u = pred[u]) {
			p[cnt++] = u;
		}
		int[] cycle = new int[cnt];
		for (int i = 0; i < cycle.length; i++) {
			cycle[i] = p[--cnt];
		}
		return cycle;
	}
	public static boolean bellmanFord(List<Edge>[] graph, int s, int[] dist, int[] pred) {
		Arrays.fill(pred, -1);
		Arrays.fill(dist, INF);
		dist[s] = 0;
		int n = graph.length;
		boolean updated = false;
		for (int step = 0; step < n; step++) {
			updated = false;
			for (int u = 0; u < n; u++) {
				if (dist[u] == INF) continue;
				for (Edge e : graph[u]) {
					if (dist[e.t] > dist[u] + e.cost) {
						dist[e.t] = dist[u] + e.cost;
						dist[e.t] = Math.max(dist[e.t], -INF);
						pred[e.t] = u;
						updated = true;
					}
				}
			}
			if (!updated)
				break;
		}
		// if updated is true then a negative cycle exists
		return updated == false;
	}
	public static void main(String[] args) throws Exception
	{
		long S = System.currentTimeMillis();
		is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
		out = new PrintWriter(System.out);
		
		solve();
		out.flush();
		long G = System.currentTimeMillis();
		tr(G-S+"ms");
	}
	
	private static boolean eof()
	{
		if(lenbuf == -1)return true;
		int lptr = ptrbuf;
		while(lptr < lenbuf)if(!isSpaceChar(inbuf[lptr++]))return false;
		
		try {
			is.mark(1000);
			while(true){
				int b = is.read();
				if(b == -1){
					is.reset();
					return true;
				}else if(!isSpaceChar(b)){
					is.reset();
					return false;
				}
			}
		} catch (IOException e) {
			return true;
		}
	}
	
	private static byte[] inbuf = new byte[1024];
	static int lenbuf = 0, ptrbuf = 0;
	
	private static int readByte()
	{
		if(lenbuf == -1)throw new InputMismatchException();
		if(ptrbuf >= lenbuf){
			ptrbuf = 0;
			try { lenbuf = is.read(inbuf); } catch (IOException e) { throw new InputMismatchException(); }
			if(lenbuf <= 0)return -1;
		}
		return inbuf[ptrbuf++];
	}
	
	private static boolean isSpaceChar(int c) { return !(c >= 33 && c <= 126); }
//	private static boolean isSpaceChar(int c) { return !(c >= 32 && c <= 126); }
	private static int skip() { int b; while((b = readByte()) != -1 && isSpaceChar(b)); return b; }
	
	private static double nd() { return Double.parseDouble(ns()); }
	private static char nc() { return (char)skip(); }
	
	private static String ns()
	{
		int b = skip();
		StringBuilder sb = new StringBuilder();
		while(!(isSpaceChar(b))){
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	
	private static char[] ns(int n)
	{
		char[] buf = new char[n];
		int b = skip(), p = 0;
		while(p < n && !(isSpaceChar(b))){
			buf[p++] = (char)b;
			b = readByte();
		}
		return n == p ? buf : Arrays.copyOf(buf, p);
	}
	
	private static char[][] nm(int n, int m)
	{
		char[][] map = new char[n][];
		for(int i = 0;i < n;i++)map[i] = ns(m);
		return map;
	}
	
	private static int[] na(int n)
	{
		int[] a = new int[n];
		for(int i = 0;i < n;i++)a[i] = ni();
		return a;
	}
	
	private static int ni()
	{
		int num = 0, b;
		boolean minus = false;
		while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
		if(b == '-'){
			minus = true;
			b = readByte();
		}
		
		while(true){
			if(b >= '0' && b <= '9'){
				num = num * 10 + (b - '0');
			}else{
				return minus ? -num : num;
			}
			b = readByte();
		}
	}
	
	private static long nl()
	{
		long num = 0;
		int b;
		boolean minus = false;
		while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
		if(b == '-'){
			minus = true;
			b = readByte();
		}
		
		while(true){
			if(b >= '0' && b <= '9'){
				num = num * 10 + (b - '0');
			}else{
				return minus ? -num : num;
			}
			b = readByte();
		}
	}
	
	private static void tr(Object... o) { if(INPUT.length() != 0)System.out.println(Arrays.deepToString(o)); }
}