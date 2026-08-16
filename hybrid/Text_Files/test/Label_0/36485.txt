import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Map;
import java.util.Queue;

public class Main {
	static InputStream is;
	static PrintWriter out;
	static String INPUT = "";
	
	static void solve()
	{
		int n = ni(), K = ni();
		int[] f = na(n);
		for(int i = 0;i < n;i++)f[i]--;
		int[] from = new int[n];
		for(int i = 0;i < n;i++){
			from[i] = i;
		}
		
		
		int[][] g = packU(n, from, f);
		int[][] pn = split(g);
		int[] par = pn[0], next = pn[1];
		int[] ord = makeOrder(g, par);
		long[] hs = new long[n];
		long[][] temp = new long[n][];
		Map<Long, Integer> hmap = new HashMap<>();
		int hgen = 0;
		long[] dp = new long[n];
		int mod = 1000000007;
		for(int i = n-1;i >= 0;i--){
			int cur = ord[i];
			int p = 0;
			// aaabb
			// aaabb+aaab+abb+abb
			for(int e : g[cur]){
				if(e == next[cur])continue;
				if(next[e] == cur)continue;
				if(par[cur] == e)continue;
				temp[p++] = new long[]{hs[e], dp[e]};
			}
			Arrays.sort(temp, 0, p, new Comparator<long[]>() {
				public int compare(long[] a, long[] b) {
					return Long.compare(a[0], b[0]);
				}
			});
			// k(k+1)(k+2)/6
			// k(k+1)/2*else

			long lh = p;
			for(int j = 0;j < p;j++){
				lh = lh * 1000000031L + temp[j][0];
			}
			
			dp[cur] = K;
			for(int j = 0;j < p;){
				int k = j;
				while(k < p && temp[k][0] == temp[j][0])k++;
				dp[cur] = dp[cur] * C(k-j+temp[j][1]-1, k-j, mod) % mod;
				j = k;
			}
			
			if(!hmap.containsKey(lh)){
				hmap.put(lh, hgen++);
			}
			hs[cur] = hmap.get(lh);
		}
		
		// rotate
		long[] ringh = new long[n];
		long[] ringd = new long[n];
		int p = 0;
		for(int i = 0;i < n;i++){
			if(par[i] == -1){
				ringh[p] = hs[i];
				ringd[p] = dp[i];
				if(dp[i] == 0){
					out.println(0);
					return;
				}
				p++;
				for(int x = next[i];x != i;x = next[x]){
					ringh[p] = hs[x];
					ringd[p] = dp[x];
					p++;
					if(dp[x] == 0){
						out.println(0);
						return;
					}
				}
				ringh = Arrays.copyOf(ringh, p);
				ringd = Arrays.copyOf(ringd, p);
				break;
			}
		}
		
		assert p > 0;
		int[] z = Z(ringh);
		long[] nums = new long[p];
		long[] pes = new long[p];
		long[] vals = new long[p];
		int q = 0;
		long val = 1;
		for(int pe = 1;pe <= p-1;pe++){
			val = val * ringd[pe-1] % mod;
			if(p % pe == 0 && z[pe] >= p-pe){
				nums[q] = p/pe-1;
				pes[q] = pe;
				vals[q] = val;
				q++;
			}
		}
		for(int i = q-1;i >= 0;i--){
			for(int j = i+1;j < q;j++){
				if(pes[j] % pes[i] == 0){
					nums[i] -= nums[j];
				}
			}
		}
		
		// flip
		ringh = Arrays.copyOf(ringh, 2*p);
		for(int i = 0;i < p;i++){
			ringh[i+p] = ringh[i];
		}
		int[] rads = palindrome(ringh);
		// abccbabccb
		long[] cumd = new long[4*p+1];
		cumd[0] = 1;
		for(int i = 0;i < 4*p;i++){
			if(i % 2 == 0){
				cumd[i+1] = cumd[i] * ringd[i/2%p] % mod;
			}else{
				cumd[i+1] = cumd[i];
			}
		}
		long[] fvals = new long[p];
		int r = 0;
		for(int i = 0;i < p;i++){
			if(rads[i] >= p || rads[i+2*p] >= p){
				long plus = cumd[i+3*p+1] * invl(cumd[i+2*p], mod) % mod;
				fvals[r++] = plus;
			}
		}
		
//		tr("ringh", ringh);
//		tr("ringd", ringd);
//		tr("nums", Arrays.copyOf(nums, q));
//		tr("pes", Arrays.copyOf(pes, q));
//		tr("vals", Arrays.copyOf(vals, q));
//		tr("fvals", Arrays.copyOf(fvals, r));
		
		// total
		long all = 1;
		long sum = cumd[2*p];
		for(int i = 0;i < q;i++){
			all += nums[i];
			sum += nums[i] * vals[i];
			sum %= mod;
		}
		for(int i = 0;i < r;i++){
			all += 1;
			sum += fvals[i];
		}
		sum %= mod;
		out.println(sum * invl(all, mod) % mod);
	}
	
	public static int[] palindrome(long[] str)
	{
		int n = str.length;
		int[] r = new int[2*n];
		int k = 0;
		for(int i = 0, j = 0;i < 2*n;i += k, j = Math.max(j-k, 0)){
			// normally
			while(i-j >= 0 && i+j+1 < 2*n && str[(i-j)/2] == str[(i+j+1)/2])j++;
			r[i] = j;
			
			// skip based on the theorem
			for(k = 1;i-k >= 0 && r[i]-k >= 0 && r[i-k] != r[i]-k;k++){
				r[i+k] = Math.min(r[i-k], r[i]-k);
			}
		}
		return r;
	}

	
	public static int[] Z(long[] str)
	{
		int n = str.length;
		int[] z = new int[n];
		if(n == 0)return z;
		z[0] = n;
		int l = 0, r = 0;
		for(int i = 1;i < n;i++){
			if(i > r){
				l = r = i;
				while(r < n && str[r-l] == str[r])r++;
				z[i] = r-l; r--;
			}else{
				if(z[i-l] < r-i+1){
					z[i] = z[i-l];
				}else{
					l = i;
					while(r < n && str[r-l] == str[r])r++;
					z[i] = r-l; r--;
				}
			}
		}
		
		return z;
	}

	
	static long C(long n, long r, int mod)
	{
		if(n < r || n < 0 || r < 0)return 0L;
		long ret = 1;
		long num = 1, den = 1;
		for(int i = 0;i < r;i++){
			num = num * (n-i) % mod;
			den = den * (i+1) % mod;
		}
		assert den != 0;
		return num * invl(den, mod) % mod;
	}
	
	public static long invl(long a, long mod) {
		long b = mod;
		long p = 1, q = 0;
		while (b > 0) {
			long c = a / b;
			long d;
			d = a;
			a = b;
			b = d % b;
			d = p;
			p = q;
			q = d - c * q;
		}
		return p < 0 ? p + mod : p;
	}

	
	static int[][] packU(int n, int[] from, int[] to) {
		int[][] g = new int[n][];
		int[] p = new int[n];
		for (int f : from)
			p[f]++;
		for (int t : to)
			p[t]++;
		for (int i = 0; i < n; i++)
			g[i] = new int[p[i]];
		for (int i = 0; i < from.length; i++) {
			g[from[i]][--p[from[i]]] = to[i];
			g[to[i]][--p[to[i]]] = from[i];
		}
		return g;
	}
	
	public static int[][] split(int[][] g)
	{
		int n = g.length;
		int[] deg = new int[n];
		int[] par = new int[n];
		Arrays.fill(par, -1);
		for(int i = 0;i < n;i++){
			deg[i] = g[i].length;
		}
		Queue<Integer> q = new ArrayDeque<Integer>();
		for(int i = 0;i < n;i++){
			if(deg[i] == 1){
				q.add(i);
			}
		}
		while(!q.isEmpty()){
			int cur = q.poll();
			deg[cur] = -9999999;
			for(int e : g[cur]){
				deg[e]--;
				if(deg[e] >= 0){
					par[cur] = e;
				}
				if(deg[e] >= 0 && deg[e] <= 1){
					q.add(e);
				}
			}
		}
		boolean[] ved = new boolean[n];
		int[] next = new int[n];
		Arrays.fill(next, -1);
		for(int i = 0;i < n;i++){
			if(!ved[i] && deg[i] == 2){
				ved[i] = true;
				int cur = i;
				outer:
				while(true){
					for(int e : g[cur]){
						if(deg[e] == 2 && !ved[e]){
							next[cur] = e;
							ved[e] = true;
							cur = e;
							continue outer;
						}
					}
					next[cur] = i;
					break;
				}
			}
		}
		
		return new int[][]{par, next};
	}
	
	public static int[] makeOrder(int[][] g, int[] par)
	{
		int n = g.length;
		int[] ord = new int[n];
		int p = 0;
		boolean[] ved = new boolean[n];
		for(int i = 0;i < n;i++){
			if(par[i] == -1){
				ord[p++] = i;
				ved[i] = true;
			}
		}
		for(int r = 0;r < n;r++){
			for(int e : g[ord[r]]){
				if(!ved[e]){
					ved[e] = true;
					ord[p++] = e;
				}
			}
		}
		return ord;
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
