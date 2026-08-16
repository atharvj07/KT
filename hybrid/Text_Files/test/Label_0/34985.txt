	
	
	
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;


	
		
	
	
	public class COVID {
	
		static long mod = 998244353 ;
		static PrintWriter pw;
			static int n,m;
			
			static ArrayList<Integer>[] adjList;
			
		static int INF=(int)1e8;
		static double EPS=1e-6;


public static void main(String[] args) throws Exception {
				Scanner sc = new Scanner(System.in);
				PrintWriter pw = new PrintWriter(System.out);
				int n=sc.nextInt();
				int arr[]=sc.nextIntArr(2*n);
				shuffle(arr);
				Arrays.sort(arr);
				long sum=0;
				for(int i=0;i<n;i++)
					sum+=arr[2*n-1-i]-arr[i];
				long c=1;for(int i=1;i<=n;i++)c=mul(c, i);
				c=c*c%mod;
				c=powmod(c,mod-2,(int)mod);
				for(int i=1;i<=2*n;i++)c=mul(c, i);
				pw.println(mul(c, sum));
				
				pw.flush();
			}
public static long getAns(long p , long q) {
	long ans=0;
	for(long i=1;i*i<=p;i++) {
		if(p%i==0) {
			long div=p/i;
			if(div%q!=0) {
				return div;
			}else {
				if(i%q!=0) {
					ans=Math.max(ans, i);
				}
			}
		}
	}
	return ans;
}

static boolean[] isPrime;
static ArrayList<Integer> primes;
public static void sieve(int N) {// O( n log( log n ) )
	isPrime= new boolean[N+1];//u can save half the memory by neglecting all even numbers since they aren't primes
	primes= new ArrayList<>(N);
	Arrays.fill(isPrime, true);
	isPrime[0]=isPrime[1]=false;
	for(int i=2;i*i<=N;i++) {
		if(isPrime[i]) {
			for(int j=i*i;j<=N;j+=i) {
				isPrime[j]=false;
			}
		}
	}
	for(int i=2;i<=N;i++) {
		if(isPrime[i])primes.add(i);
	}
}
public static class Segment{
	Point a,b;
	int id;
	public Segment(Point s,Point e,int id) {
		a=s;b=e;
		this.id=id;
	}
	public  double getY(int x) {
		return b.y+(x-b.x)*1.0*(a.y-b.y)/(a.x-b.x);
	}
	public String toString() {
		return a.x+" "+a.y+" "+b.x+" "+b.y;
	}
}
public static class Point{
	int x,y;
	public Point(int a,int b) {
		x=a;y=b;
	}
}
static int pow(int b, long e) {
	int ans = 1;
	while (e > 0) {
		if ((e & 1) == 1)
			ans = (int) ((ans * 1l * b));
		e >>= 1;
		{

		}
		b = (int) ((b * 1l * b));
	}
	return ans;
}

static long powmod(long b, long e, int mod) {
	long ans = 1;
	b %= mod;
	while (e > 0) {
		if ((e & 1) == 1)
			ans = (int) ((ans * 1l * b) % mod);
		e >>= 1;
		b = (int) ((b * 1l * b) % mod);
	}
	return ans;
}


	public static long add(long a, long b) {
		return (a + b) % mod;
	}

	public static long sub(long a, long b) {
		return (a - b + mod) % mod;
	}

	public static long mul(long a, long b) {
		return ((a % mod) * (b % mod)) % mod;
	}


	
			
			static class longPair implements Comparable<longPair> {
			long x, y;
	
			public longPair(long a, long b) {
				x = a;
				y = b;
			}
	
			public int compareTo(longPair p) {
				return (p.x == x) ? ((p.y == y) ? 0 : (y > p.y) ? 1 : -1) : (x > p.x) ? 1 : -1;
			}
		}
	
	
		static class Pair implements Comparable<Pair> {
			int x;
			int y;
	
			public Pair(int a, int b) {
				this.x = a;
				y = b;
			}
	
	
			public int compareTo(Pair o) {
				return (x == o.x) ? ((y > o.y) ? 1 : (y == o.y) ? 0 : -1) : ((x > o.x) ? 1 : -1);
			}
	
			@Override
	
			public int hashCode() {
				final int prime = 31;
				int result = 1;
				result = prime * result + x;
				result = prime * result + y;
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
				if (x != other.x)
					return false;
				if (y != other.y)
					return false;
				return true;
			}
	
		}
	
		static class Scanner {
			StringTokenizer st;
			BufferedReader br;
	
			public Scanner(InputStream s) {
				br = new BufferedReader(new InputStreamReader(s));
			}
	
			public Scanner(String s) throws FileNotFoundException {
				br = new BufferedReader(new FileReader(s));
			}
	
			public long[] nextLongArr(int n) throws IOException {
				long[] arr = new long[n];
				for (int i = 0; i < n; i++)
					arr[i] = nextLong();
				return arr;
			}
	
			public int[] nextIntArr(int n) throws IOException {
				int[] arr = new int[n];
				for (int i = 0; i < n; i++)
					arr[i] = nextInt();
				return arr;
			}
	
			public String next() throws IOException {
				while (st == null || !st.hasMoreTokens())
					st = new StringTokenizer(br.readLine(), " ,");
				return st.nextToken();
			}
	
			public int nextInt() throws IOException {
				return Integer.parseInt(next());
			}
	
			public long nextLong() throws IOException {
				return Long.parseLong(next());
			}
	
			public String nextLine() throws IOException {
				return br.readLine();
			}
	
			public double nextDouble() throws IOException {
				String x = next();
				StringBuilder sb = new StringBuilder("0");
				double res = 0, f = 1;
				boolean dec = false, neg = false;
				int start = 0;
				if (x.charAt(0) == '-') {
					neg = true;
					start++;
				}
				for (int i = start; i < x.length(); i++) {
					if (x.charAt(i) == '.') {
						res = Long.parseLong(sb.toString());
						sb = new StringBuilder("0");
						dec = true;
					} else {
						sb.append(x.charAt(i));
						if (dec)
							f *= 10;
					}
					if (sb.length() == 18) {
						res += Long.parseLong(sb.toString()) / f;
						sb = new StringBuilder("0");
					}
				}
				res += Long.parseLong(sb.toString()) / f;
				return res * (neg ? -1 : 1);
			}
	
			public boolean ready() throws IOException {
				return br.ready();
			}
	
		}
	
		public static void shuffle(int[] a) {
			int n = a.length;
			for (int i = 0; i < n; i++) {
				int r = i + (int) (Math.random() * (n - i));
				int tmp = a[i];
				a[i] = a[r];
				a[r] = tmp;
			}
		}
	
	}