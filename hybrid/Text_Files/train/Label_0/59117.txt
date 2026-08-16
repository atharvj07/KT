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
		int h = ni(), w = ni(), T = ni(), Q = ni();
		int[][] es = new int[2*Q][];
		int[][] co = new int[Q][];
		int q = 0;
		int p = 0;
		for(int i = 0;i < Q;i++){
			int t = ni();
			int type = ni();
			if(type == 0){
				int x = ni(), y = ni();
				es[p++] = new int[]{t, type, x, y};
				es[p++] = new int[]{t+T, 1, x, y};
				co[q++] = new int[]{x, y};
			}else if(type == 1){
				es[p++] = new int[]{t, 2, ni(), ni()};
				co[q++] = new int[]{es[p-1][2], es[p-1][3]};
			}else if(type == 2){
				es[p++] = new int[]{t, 3, ni(), ni(), ni(), ni()};
			}else{
				throw new RuntimeException();
			}
		}
		
		co = Arrays.copyOf(co, q);
		StaticRangeTreeRSQ st0 = new StaticRangeTreeRSQ(co, 2005);
		StaticRangeTreeRSQ st1 = new StaticRangeTreeRSQ(co, 2005);
		
		Arrays.sort(es, 0, p, new Comparator<int[]>() {
			public int compare(int[] a, int[] b) {
				if(a[0] != b[0])return a[0] - b[0];
				return a[1] - b[1];
			}
		});
		es = Arrays.copyOf(es, p);
		for(int[] e : es){
			if(e[1] == 0){
				long val0 = st0.sum(e[2], e[2]+1, e[3], e[3]+1);
				long val1 = st1.sum(e[2], e[2]+1, e[3], e[3]+1);
				if(val0 + val1 == 0){
					st0.add(e[2], e[3], 1);
				}
			}else if(e[1] == 1){
				long val0 = st0.sum(e[2], e[2]+1, e[3], e[3]+1);
				long val1 = st1.sum(e[2], e[2]+1, e[3], e[3]+1);
				if(val0 == 1 && val1 == 0){
					st0.add(e[2], e[3], -1);
					st1.add(e[2], e[3], 1);
				}
			}else if(e[1] == 2){
				long val1 = st1.sum(e[2], e[2]+1, e[3], e[3]+1);
				if(val1 == 1){
					st1.add(e[2], e[3], -1);
				}
			}else{
				out.println(
						st1.sum(e[2], e[4]+1, e[3], e[5]+1) + " " + 
						st0.sum(e[2], e[4]+1, e[3], e[5]+1)
						);
			}
		}
	}
	
	public static class StaticRangeTreeRSQ {
		public int M, H, N;
		public int[][] fts, maps;
		public int[] count;
		public int I = Integer.MAX_VALUE;
		
		public StaticRangeTreeRSQ(int[][] co, int n)
		{
			N = n;
			M = Integer.highestOneBit(Math.max(N-1, 1))<<2;
			H = M>>>1;
			
			Arrays.sort(co, new Comparator<int[]>(){
				public int compare(int[] a, int[] b){
					if(a[0] != b[0])return a[0] - b[0];
					return a[1] - b[1];
				}
			});
			maps = new int[M][];
			fts = new int[M][];
			count = new int[M];
			for(int i = 0;i < co.length;i++){
				count[H+co[i][0]]++;
			}
			
			int off = 0;
			for(int i = 0;i < n;i++){
				maps[H+i] = new int[count[H+i]];
				for(int j = 0;j < count[H+i];j++,off++){
					maps[H+i][j] = co[off][1];
				}
				fts[H+i] = new int[count[H+i]+1];
			}
			for(int i = H-1;i >= 1;i--){
				if(maps[2*i+1] == null){
					maps[i] = maps[2*i];
					count[i] = count[2*i];
				}else{
					count[i] = count[2*i] + count[2*i+1];
					maps[i] = new int[count[i]];
					int l = 0, j = 0, k = 0;
					while(j < count[2*i] && k < count[2*i+1]){
						if(maps[2*i][j] < maps[2*i+1][k]){
							maps[i][l++] = maps[2*i][j++];
						}else if(maps[2*i][j] > maps[2*i+1][k]){
							maps[i][l++] = maps[2*i+1][k++];
						}else{
							maps[i][l++] = maps[2*i][j++];
							k++;
						}
					}
					while(j < count[2*i])maps[i][l++] =maps[2*i][j++];
					while(k < count[2*i+1])maps[i][l++] =maps[2*i+1][k++];
					if(l != count[i]){
						count[i] = l;
						maps[i] = Arrays.copyOf(maps[i], l);
					}
				}
				fts[i] = new int[count[i]+1];
			}
		}
		
		public void add(int x, int y, int v)
		{
			for(int pos = H+x;pos >= 1;pos>>>=1){
				int ind = Arrays.binarySearch(maps[pos], y);
				if(ind >= 0){
					addFenwick(fts[pos], ind, v);
				}else{
				}
			}
		}
		
		public long gsum;
		
		public long sum(int xl, int xr, int yl, int yr){
			gsum = 0;
			sum(xl, xr, yl, yr, 0, H, 1);
			return gsum;
		}
		public void sum(int xl, int xr, int yl, int yr, int cl, int cr, int cur){
			if(xl <= cl && cr <= xr){
				int indl = Arrays.binarySearch(maps[cur], yl-1);
				int indr = Arrays.binarySearch(maps[cur], yr-1);
				if(indl < 0)indl=-indl-2;
				if(indr < 0)indr=-indr-2;
				gsum += sumFenwick(fts[cur], indr) - sumFenwick(fts[cur], indl);
			}else{
				int mid = cl+cr>>1;
				if(cl<xr && xl<mid)sum(xl,xr,yl,yr,cl,mid,2*cur);
				if(mid<xr && xl<cr)sum(xl,xr,yl,yr,mid,cr,2*cur+1);
			}
		}
		
		static int sumFenwick(int[] ft, int i)
		{
			int sum = 0;
			for(i++;i>0;i-=i&-i)sum += ft[i];
			return sum;
		}
		
		static void addFenwick(int[] ft, int i, int v)
		{
			if(v == 0 || i < 0)return;
			int n = ft.length;
			for(i++;i < n;i+=i&-i)ft[i] += v;
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