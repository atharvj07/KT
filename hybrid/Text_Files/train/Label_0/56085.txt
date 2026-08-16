import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.InputMismatchException;
 
public class Main {
	static InputStream is;
	static PrintWriter out;
	static String INPUT = "";
	
	static void solve()
	{
		int n = ni(), m = ni();
		int[][] es = new int[m][];
		for(int i = 0;i < m;i++){
			es[i] = new int[]{ni()-1, ni()-1, ni()};
		}
		Arrays.sort(es, new Comparator<int[]>() {
			public int compare(int[] a, int[] b) {
				return a[2] - b[2];
			}
		});
 
		DJSet ds = new DJSet(n);
		int[] from = new int[n-1];
		int[] to = new int[n-1];
		int[] w = new int[n-1];
		long wsum = 0;
		int p = 0;
		for(int i = 0;i < m;i++){
			if(!ds.union(es[i][0], es[i][1])){
				from[p] = es[i][0];
				to[p] = es[i][1];
				w[p] = -es[i][2];
				p++;
				wsum += es[i][2];
			}
		}
		assert p == n-1;
		int[][][] g = packWU(n, from, to, w);
		int[][] pars = parents(g, 0);
		int[] par = pars[0], ord = pars[1], dep = pars[2], pw = pars[4];
		int[][] spar = logstepParents(par);
		int[][] sargmins = logstepArgmins(spar, pw);
		for(int Q = ni();Q > 0;Q--){
			int s = ni()-1, t = ni()-1;
			int arg = argmin(s, t, spar, sargmins, pw, dep);
			out.println(wsum+pw[arg]);
		}
	}
	
	public static int[][] logstepArgmins(int[][] sp, int[] pw)
	{
		int m = sp.length;
		int n = sp[0].length;
		int[][] mins = new int[m][n];
		for(int i = 0;i < n;i++){
			mins[0][i] = i;
		}
		for(int j = 1;j < m;j++){
			for(int i = 0;i < n;i++){
				if(sp[j-1][i] != -1){
					int lower = mins[j-1][i];
					int upper = mins[j-1][sp[j-1][i]];
					if(upper == -1 || pw[lower] < pw[upper]){
						mins[j][i] = lower;
					}else{
						mins[j][i] = upper;
					}
				}else{
					mins[j][i] = -1;
				}
			}
		}
		return mins;
	}
	
	public static int argmin(int a, int b, int[][] spar, int[][] sargmin, int[] vs, int[] dep)
	{
		int lca = lca2(a, b, spar, dep);
		int a0 = argminAnc(a, lca, spar, sargmin, vs, dep);
		int a1 = argminAnc(b, lca, spar, sargmin, vs, dep);
		int min = Integer.MAX_VALUE;
		int arg = -1;
		if(a0 != -1 && vs[a0] < min){
			min = vs[a0];
			arg = a0;
		}
		if(a1 != -1 && vs[a1] < min){
			min = vs[a1];
			arg = a1;
		}
		return arg; // or min
	}
	
	public static int argminAnc(int a, int anc, int[][] spar, int[][] sargmin, int[] vs, int[] dep)
	{
		if(a == anc)return -1;
		int cur = a;
		int min = vs[a];
		int arg = a;
		for(int i = dep[a] - dep[anc], k = 0;i > 0;i /= 2, k++){
			if((i&1)==1){
				int lv = vs[sargmin[k][cur]];
				if(lv < min){
					min = lv;
					arg = sargmin[k][cur];
				}
				cur = spar[k][cur];
			}
		}
		return arg;
	}
 
 
	
	public static int lca2(int a, int b, int[][] spar, int[] depth) {
		if (depth[a] < depth[b]) {
			b = ancestor(b, depth[b] - depth[a], spar);
		} else if (depth[a] > depth[b]) {
			a = ancestor(a, depth[a] - depth[b], spar);
		}
 
		if (a == b)
			return a;
		int sa = a, sb = b;
		for (int low = 0, high = depth[a], t = Integer.highestOneBit(high), k = Integer
				.numberOfTrailingZeros(t); t > 0; t >>>= 1, k--) {
			if ((low ^ high) >= t) {
				if (spar[k][sa] != spar[k][sb]) {
					low |= t;
					sa = spar[k][sa];
					sb = spar[k][sb];
				} else {
					high = low | t - 1;
				}
			}
		}
		return spar[0][sa];
	}
 
	protected static int ancestor(int a, int m, int[][] spar) {
		for (int i = 0; m > 0 && a != -1; m >>>= 1, i++) {
			if ((m & 1) == 1)
				a = spar[i][a];
		}
		return a;
	}
 
	public static int[][] logstepParents(int[] par) {
		int n = par.length;
		int m = Integer.numberOfTrailingZeros(Integer.highestOneBit(n - 1)) + 1;
		int[][] pars = new int[m][n];
		pars[0] = par;
		for (int j = 1; j < m; j++) {
			for (int i = 0; i < n; i++) {
				pars[j][i] = pars[j - 1][i] == -1 ? -1 : pars[j - 1][pars[j - 1][i]];
			}
		}
		return pars;
	}
 
	
	public static int[][] parents(int[][][] g, int root) {
		int n = g.length;
		int[] par = new int[n];
		Arrays.fill(par, -1);
		int[] dw = new int[n];
		int[] pw = new int[n];
		int[] dep = new int[n];
 
		int[] q = new int[n];
		q[0] = root;
		for (int p = 0, r = 1; p < r; p++) {
			int cur = q[p];
			for (int[] nex : g[cur]) {
				if (par[cur] != nex[0]) {
					q[r++] = nex[0];
					par[nex[0]] = cur;
					dep[nex[0]] = dep[cur] + 1;
					dw[nex[0]] = dw[cur] + nex[1];
					pw[nex[0]] = nex[1];
				}
			}
		}
		return new int[][] { par, q, dep, dw, pw };
	}
 
	
	public static int[][][] packWU(int n, int[] from, int[] to, int[] w) {
		int[][][] g = new int[n][][];
		int[] p = new int[n];
		for (int f : from)
			p[f]++;
		for (int t : to)
			p[t]++;
		for (int i = 0; i < n; i++)
			g[i] = new int[p[i]][2];
		for (int i = 0; i < from.length; i++) {
			--p[from[i]];
			g[from[i]][p[from[i]]][0] = to[i];
			g[from[i]][p[from[i]]][1] = w[i];
			--p[to[i]];
			g[to[i]][p[to[i]]][0] = from[i];
			g[to[i]][p[to[i]]][1] = w[i];
		}
		return g;
	}
 
	
	public static class DJSet {
		public int[] upper;
 
		public DJSet(int n) {
			upper = new int[n];
			Arrays.fill(upper, -1);
		}
 
		public int root(int x) {
			return upper[x] < 0 ? x : (upper[x] = root(upper[x]));
		}
 
		public boolean equiv(int x, int y) {
			return root(x) == root(y);
		}
 
		public boolean union(int x, int y) {
			x = root(x);
			y = root(y);
			if (x != y) {
				if (upper[y] < upper[x]) {
					int d = x;
					x = y;
					y = d;
				}
				upper[x] += upper[y];
				upper[y] = x;
			}
			return x == y;
		}
 
		public int count() {
			int ct = 0;
			for (int u : upper)
				if (u < 0)
					ct++;
			return ct;
		}
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