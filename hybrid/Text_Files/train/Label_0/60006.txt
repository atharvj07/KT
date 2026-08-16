import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.List;

public class Main {
	static InputStream is;
	static PrintWriter out;
	static String INPUT = "";
	
	static void solve()
	{
		int n = ni();
		int[] a = na(n);
		int[] b = na(n);
		int Q = ni();
		int[][] qs = new int[Q+2][];
		for(int i = 0;i < Q;i++){
			qs[i+2] = na(3);
		}
		qs[0] = new int[]{3, 1, 1};
		qs[1] = new int[]{4, 1, 1};
		int af = 0, bf = 1;
		Q += 2;
		
		int al = -1, bl = -1;
		int[] par = new int[Q];
		for(int i = 0;i < Q;i++){
			int[] q = qs[i];
			if(q[0] <= 4){
				if(q[0] % 2 == 1){
					par[i] = al;
					al = i;
				}else{
					par[i] = bl;
					bl = i;
				}
			}else{
				if(q[0] == 5){
					par[i] = bl;
					al = bl;
				}else{
					par[i] = al;
					bl = al;
				}
			}
		}
		
		List<List<Integer>> ch = new ArrayList<>();
		for(int i = 0;i < Q;i++){
			ch.add(new ArrayList<>());
		}
		for(int i = 0;i < Q;i++){
			if(par[i] != -1){
				ch.get(par[i]).add(i);
			}
		}
		
		int[] ans = new int[Q];
		dfs(af, ch, new SegmentTreeRMQ(a), qs, ans);
		dfs(bf, ch, new SegmentTreeRMQ(b), qs, ans);
		for(int i = 2;i < Q;i++){
			if(qs[i][0] >= 3 && qs[i][0] <= 4){
				out.println(ans[i]);
			}
		}
	}
	
	static void dfs(int cur, List<List<Integer>> ch, SegmentTreeRMQ st, int[][] qs, int[] ans)
	{
		if(cur < 0)return;
		int prev = -1;
		int[] q = qs[cur];
		if(q[0] <= 2){
			prev = st.minx(q[1]-1, q[1]);
			st.update(q[1]-1, q[2]);
		}else if(q[0] <= 4){
			ans[cur] = st.minx(q[1]-1, q[2]-1+1);
		}
		for(int e : ch.get(cur)){
			dfs(e, ch, st, qs, ans);
		}
		if(q[0] <= 2){
			st.update(q[1]-1, prev);
		}
	}
	
	public static class SegmentTreeRMQ {
		public int M, H, N;
		public int[] st;
	
		public SegmentTreeRMQ(int[] a)
		{
			N = a.length;
			M = Integer.highestOneBit(Math.max(N-1, 1))<<2;
			H = M>>>1;
			st = new int[M];
			for(int i = 0;i < N;i++)st[H+i] =a[i];
			Arrays.fill(st, H+N, M, Integer.MAX_VALUE);
			for(int i = H-1;i >= 1;i--)propagate(i);
		}
		
		public void update(int pos, int x)
		{
			st[H+pos] = x;
			for(int i = H+pos>>>1;i >= 1;i>>>=1)propagate(i);
		}
		
		private void propagate(int i)
		{
			st[i] = Math.min(st[2*i], st[2*i+1]);
		}
		
		public int minx(int l, int r)
		{
			int min = Integer.MAX_VALUE;
			if(l >= r)return min;
			while(l != 0){
				int f = l&-l;
				if(l+f > r)break;
				int v = st[(H+l)/f];
				if(v < min)min = v;
				l += f;
			}
			while(l < r){
				int f = r&-r;
				int v = st[(H+r)/f-1];
				if(v < min)min = v;
				r -= f;
			}
			return min;
		}
	}
	
	
	public static void main(String[] args) throws Exception
	{
		is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
		out = new PrintWriter(System.out);
		Thread t = new Thread(null, null, "~", Runtime.getRuntime().maxMemory()){
			@Override
			public void run() {
				long s = System.currentTimeMillis();
				solve();
				out.flush();
				if(!INPUT.isEmpty())tr(System.currentTimeMillis()-s+"ms");
			}
		};
		t.start();
		t.join();
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
	public static int lenbuf = 0, ptrbuf = 0;
	
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
	private static int skip() { int b; while((b = readByte()) != -1 && isSpaceChar(b)); return b; }
	
	private static double nd() { return Double.parseDouble(ns()); }
	private static char nc() { return (char)skip(); }
	
	private static String ns()
	{
		int b = skip();
		StringBuilder sb = new StringBuilder();
		while(!(isSpaceChar(b))){ // when nextLine, (isSpaceChar(b) && b != ' ')
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