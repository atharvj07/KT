import java.io.*;
import java.math.BigInteger;
import java.util.*;
 
 
 
public class Main {
	
	static InputReader in = new InputReader(System.in);
	static PrintWriter out = new PrintWriter(System.out);
	
	static int oo = (int)1e9;
//	static long oo = (long)1e15;
	static int mod = 1_000_000_007;
//	static int mod = 998244353;
	
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, -1, 0, 1};
	
	static int M = 200005;
	static double EPS = 1e-13;
	static int[] memo;
	
	public static void main(String[] args) throws IOException {

		int n = in.nextInt();
		long[] a = new long[n];
		for(int i = 0; i < n; ++i)
			a[i] = in.nextLong();
		shuffle(a);
		Arrays.sort(a);
		HashSet<Long> done = new HashSet<>();
		memo = new int[2 * M];
		Arrays.fill(memo, -1);
		long ans = 0;
		for(int i = 0; i < n; ++i) {
			if(done.contains(a[i]))
				continue;
			long sum = 0;
			for(long j = 1; a[i] * j < M; ++j) {
				int cnt = cnt(a, a[i] * j, a[i] * (j+1));
				sum += a[i] * j * cnt;
			}
			ans = Math.max(ans, sum);
			done.add(a[i]);
		}
		System.out.println(ans);
		
		out.close();
	}
	
	static int cnt(long[] a, long s, long e) {
		int l = -1, r = -1;
		if(memo[(int)s] != -1)
			l = memo[(int)s];
		else {
			memo[(int)s] = l = lower_bound(a, a.length, s);
		}
		if(memo[(int)e] != -1)
			r = memo[(int)e];
		else
			memo[(int)e] = r = lower_bound(a, a.length, e);
		return r - l;
	}
	
	static void update(int[] f, int i) {
		while(i < f.length) {
			f[i]++;
			i += (i & -i);
		}
	}
	
	static int query(int[] f, int i) {
		int ret = 0;
		while(i > 0) {
			ret += f[i];
			i -= (i & -i);
		}
		return ret;
	}
	
	static long invmod(long a, long mod) {
		BigInteger b = BigInteger.valueOf(a);
		BigInteger m = BigInteger.valueOf(mod);
		return b.modInverse(m).longValue();
	}
	
	
	static int find(int[] g, int x) {
		return g[x] = g[x] == x ? x : find(g, g[x]);
	}
	
	static void union(int[] g, int[] size, int x, int y) {
		x = find(g, x); y = find(g, y);
		if(x == y)
			return;
		if(size[x] < size[y]) {
			g[x] = y;
			size[y] += size[x];
		}
		else {
			g[y] = x;
			size[x] += size[y];
		}
	}
	
	static class Segment {
		Segment left, right;
		int size;
//		int time, lazy;
		
		public Segment(long[] a, int l, int r) {
			super();
			if(l == r) {
				return;
			}
			int mid = (l + r) / 2;
			left = new Segment(a, l, mid);
			right = new Segment(a, mid+1, r);
		}
		
		boolean covered(int ll, int rr, int l, int r) {
			return ll <= l && rr >= r;
		}
		
		boolean noIntersection(int ll, int rr, int l, int r) {
			return ll > r || rr < l;
		}
		
//		void lazyPropagation() {
//			if(lazy != 0) {
//				if(left != null) {
//					left.setLazy(this.time, this.lazy);
//					right.setLazy(this.time, this.lazy);
//				}
//				else {
//					val = lazy;
//				}
//			}
//		}
		
//		void setLazy(int time, int lazy) {
//			if(this.time != 0 && this.time <= time)
//				return;
//			this.time = time;
//			this.lazy = lazy;
//		}
		
		
		int querySize(int ll, int rr, int l, int r) {
//			lazyPropagation();
			if(noIntersection(ll, rr, l, r))
				return 0;
			if(covered(ll, rr, l, r))
				return size;
			int mid = (l + r) / 2;
			int leftSize = left.querySize(ll, rr, l, mid);
			int rightSize = right.querySize(ll, rr, mid+1, r);
			return leftSize + rightSize;
		}
		
		int query(int k, int l, int r) {
			Segment trace = this;
			while(l < r) {
				int mid = (l + r) / 2;
				if(trace.left.size > k) {
					trace = trace.left;
					r = mid;
				}
				else {
					k -= trace.left.size;
					trace = trace.right;
					l = mid + 1;
				}
			}
			return l;
		}
		
		void update(int ll, int rr, int l, int r) {
//			lazyPropagation();
			if(noIntersection(ll, rr, l, r))
				return;
			if(covered(ll, rr, l, r)) {
//				setLazy(time, knight);
				this.size = 1;
				return;
			}
			int mid = (l + r) / 2;
			left.update(ll, rr, l, mid);
			right.update(ll, rr, mid+1, r);
			this.size = left.size + right.size;
		}
	}
	
	static long pow(long a, long n, long mod) {
		if(n == 0)
			return 1;
		if(n % 2 == 1)
			return a * pow(a, n-1, mod) % mod;
		long x = pow(a, n / 2, mod);
		return x * x % mod;
	}
	
	
	static int[] getPi(char[] a) {
		int m = a.length;
		int j = 0;
		int[] pi = new int[m];
		for(int i = 1; i < m; ++i) {
			while(j > 0 && a[i] != a[j])
				j = pi[j-1];
			if(a[i] == a[j]) {
				pi[i] = j + 1;
				j++;
			}
		}
		return pi;
	}
	
	static long lcm(long a, long b) {
		return a * b / gcd(a, b);
	}
	
	static BigInteger lcm2(long a, long b) {
		long g = gcd(a, b);
		BigInteger gg = BigInteger.valueOf(g);
		BigInteger aa = BigInteger.valueOf(a);
		BigInteger bb = BigInteger.valueOf(b);
		return aa.multiply(bb).divide(gg);
	}
	
	static boolean nextPermutation(int[] a) {
		for(int i = a.length - 2; i >= 0; --i) {
			if(a[i] < a[i+1]) {
				for(int j = a.length - 1; ; --j) {
					if(a[i] < a[j]) {
						int t = a[i];
						a[i] = a[j];
						a[j] = t;
						for(i++, j = a.length - 1; i < j; ++i, --j) {
							t = a[i];
							a[i] = a[j];
							a[j] = t;
						}
						return true;
					}
				}
			}
		}
		return false;
	}
	
	static void shuffle(Object[] a) {
		Random r = new Random();
		for(int i = a.length - 1; i > 0; --i) {
			int si = r.nextInt(i);
			Object t = a[si];
			a[si] = a[i];
			a[i] = t;
		}
	}
	
	static void shuffle(int[] a) {
		Random r = new Random();
		for(int i = a.length - 1; i > 0; --i) {
			int si = r.nextInt(i);
			int t = a[si];
			a[si] = a[i];
			a[i] = t;
		}
	}
	
	static void shuffle(long[] a) {
		Random r = new Random();
		for(int i = a.length - 1; i > 0; --i) {
			int si = r.nextInt(i);
			long t = a[si];
			a[si] = a[i];
			a[i] = t;
		}
	}
	
	static int lower_bound(int[] a, int n, int k) {
		int s = 0;
		int e = n;
		int m;
		while (e - s > 0) {
			m = (s + e) / 2;
			if (a[m] < k)
				s = m + 1;
			else
				e = m;
		}
		return e;
	}
	static int lower_bound(long[] a, int n, long k) {
		int s = 0;
		int e = n;
		int m;
		while (e - s > 0) {
			m = (s + e) / 2;
			if (a[m] < k)
				s = m + 1;
			else
				e = m;
		}
		return e;
	}
	
	static int gcd(int a, int b) {
		return b == 0 ? a : gcd(b, a % b);
	}
	static long gcd(long a, long b) {
		return b == 0 ? a : gcd(b, a % b);
	}
	static BigInteger gcd(BigInteger a, BigInteger b) {
		return b.compareTo(BigInteger.ZERO) == 0 ? a : gcd(b, a.mod(b));
	}
	
	static class Pair implements Comparable<Pair> {
		int first, second;
 
		public Pair(int first, int second) {
			super();
			this.first = first;
			this.second = second;
		}
 
		@Override
		public int compareTo(Pair o) {
			return this.first != o.first ? this.first - o.first : this.second - o.second;
		}
		
//		@Override
//		public int compareTo(Pair o) {
//			return this.first != o.first ? o.first - this.first : o.second - this.second;
//		}
 
		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + first;
			result = prime * result + second;
			return result;
		}
 
		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			Pair other = (Pair) obj;
			if (first != other.first)
				return false;
			if (second != other.second)
				return false;
			return true;
		}
	}
}
 
 
 
class InputReader {
 
	private final InputStream stream;
	private final byte[] buf = new byte[8192];
	private int curChar, snumChars;
 
	public InputReader(InputStream st) {
		this.stream = st;
	}
 
	public int read() {
		if (snumChars == -1)
			throw new InputMismatchException();
		if (curChar >= snumChars) {
			curChar = 0;
			try {
				snumChars = stream.read(buf);
			} catch (IOException e) {
				throw new InputMismatchException();
			}
			if (snumChars <= 0)
				return -1;
		}
		return buf[curChar++];
	}
 
	public int nextInt() {
		int c = read();
		while (isSpaceChar(c)) {
			c = read();
		}
		int sgn = 1;
		if (c == '-') {
			sgn = -1;
			c = read();
		}
		int res = 0;
		do {
			res *= 10;
			res += c - '0';
			c = read();
		} while (!isSpaceChar(c));
		return res * sgn;
	}
 
	public long nextLong() {
		int c = read();
		while (isSpaceChar(c)) {
			c = read();
		}
		int sgn = 1;
		if (c == '-') {
			sgn = -1;
			c = read();
		}
		long res = 0;
		do {
			res *= 10;
			res += c - '0';
			c = read();
		} while (!isSpaceChar(c));
		return res * sgn;
	}
 
	public int[] nextIntArray(int n) {
		int a[] = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = nextInt();
		}
		return a;
	}
 
	public String readString() {
		int c = read();
		while (isSpaceChar(c)) {
			c = read();
		}
		StringBuilder res = new StringBuilder();
		do {
			res.appendCodePoint(c);
			c = read();
		} while (!isSpaceChar(c));
		return res.toString();
	}
 
	public String nextLine() {
		int c = read();
		while (isSpaceChar(c))
			c = read();
		StringBuilder res = new StringBuilder();
		do {
			res.appendCodePoint(c);
			c = read();
		} while (!isEndOfLine(c));
		return res.toString();
	}
 
	public boolean isSpaceChar(int c) {
		return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
	}
 
	private boolean isEndOfLine(int c) {
		return c == '\n' || c == '\r' || c == -1;
	}
 
}