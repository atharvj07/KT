
import java.io.*;
import java.util.*;


// fast i/o & modInverse is taken from gfg(https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/)
public class D {
	static class pair implements Comparable<pair> {

		int f = 0;
		int s = 0;

		public pair() {

		}

		public pair(int a, int b) {
			f = a;
			s = b;

		}

		@Override
		public int compareTo(pair o) {
			// TODO Auto-generated method stub
			return this.s - o.s;
		}

	}

	static int mod = (int)1e9+7;
	static int ar[];
//	static Scanner sc = new Scanner(System.in);
	static StringBuilder out = new StringBuilder();
	static ArrayList<Integer> gr[] = new ArrayList[100000];

	static void buildGraph(int n, int m) throws IOException {

		gr = new ArrayList[n];

		for (int i = 0; i < n; i++) {

			gr[i] = new ArrayList<>();

		}

		for (int i = 0; i < m; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();

			u--;
			v--;
			gr[u].add(v);
			gr[v].add(u);
		}

	}

	static void sort(int a[], int n) {

		ArrayList<Integer> al = new ArrayList<>();

		for (int i = 0; i < n; i++) {

			al.add(a[i]);
		}

		Collections.sort(al);

		for (int i = 0; i < n; i++) {

			a[i] = al.get(i);
		}
	}

	static void sort(long a[], int n) {

		ArrayList<Long> al = new ArrayList<>();

		for (int i = 0; i < n; i++) {

			al.add(a[i]);
		}

		Collections.sort(al);

		for (int i = 0; i < n; i++) {

			a[i] = al.get(i);
		}
	}

	static long[] inl(int n) throws IOException {

		long a[] = new long[n];
		for (int i = 0; i < n; i++)
			a[i] = sc.nextInt();
		return a;
	}

	static int[] in(int n) throws IOException {

		int a[] = new int[n];
		for (int i = 0; i < n; i++)
			a[i] = sc.nextInt();
		return a;
	}

	public static void main(String[] args) throws IOException {

		 sieve();

		D run = new D();

		run.run();

		System.out.println(out);
	}

	static void pla() {

		int a = 0;
		int b = 2;
		int c = 0;
		int d = 0;

		a = (int) Math.pow(2, 32);

		c = a + b;
		b = c / a;
		d = a + b + c;

	}
	
	
	static int pri[]=new int [(int)1e6+5];
	static void sieve() {
		pri[1]=1;
		for(int i=2;i<pri.length;i++) {
			pri[i]=i;
		}
		for(int i=2;i<Math.sqrt(pri.length);i++) {
			if(pri[i]!=i)continue;
			
				for(int j=i*i;j<pri.length;j+=i) {
					if(pri[j]==j)pri[j]=i;
				}
			
		}
	}
	
	public void run() throws IOException {

		long dp[][] = new long[(int) (2e5 + 5)][10];
		int maxElement = dp.length;
		Arrays.fill(dp[0], 1);
		for (int i = 0; i < 10; i++) {
			int predigit[] = new int[10];
			predigit[i] = 1;
			int id = 1;
			while (id < maxElement) {
				int newDp[] = new int[10];
				for (int g = 0; g < 9; g++)
					newDp[g + 1] = predigit[g];
				if (predigit[9] != 0) {
					newDp[0] += predigit[9];
					newDp[1] += predigit[9];
					newDp[0] %= mod;
					newDp[1] %= mod;
					
				}
				long cnt = 0;
				for (long v : newDp) {
					cnt += v;
					cnt %= mod;
				}
				dp[id][i] = cnt;
				predigit = newDp;
				id++;
			}
		}

		int t = sc.nextInt();
		while (t-- > 0) {

			pla();
			int n = sc.nextInt();
			int m = sc.nextInt();
			int digit[] = new int[10];
			while (n != 0) {
				digit[n % 10]++;
				n /= 10;
			}
			int mod = (int) (1e9 + 7);
			pla();
			long ans = 0;
			for (int i = 0; i < 10; i++) {
				if (digit[i] == 0)
					continue;
				long val = digit[i] * dp[m][i];
				val %= mod;
				ans += val;
				ans %= mod;
			}
			out.append(ans);
			out.append("\n");
			
			
		}

	}
	 static Reader sc = new Reader();

	static class Reader {
		final private int BUFFER_SIZE = 1 << 16;
		private DataInputStream din;
		private byte[] buffer;
		private int bufferPointer, bytesRead;

		public Reader() {
			din = new DataInputStream(System.in);
			buffer = new byte[BUFFER_SIZE];
			bufferPointer = bytesRead = 0;
		}

		public Reader(String file_name) throws IOException {
			din = new DataInputStream(new FileInputStream(file_name));
			buffer = new byte[BUFFER_SIZE];
			bufferPointer = bytesRead = 0;
		}

		public String readLine() throws IOException {
			byte[] buf = new byte[64]; // line length
			int cnt = 0, c;
			while ((c = read()) != -1) {
				if (c == '\n')
					break;
				buf[cnt++] = (byte) c;
			}
			return new String(buf, 0, cnt);
		}

		public int nextInt() throws IOException {
			int ret = 0;
			byte c = read();
			while (c <= ' ')
				c = read();
			boolean neg = (c == '-');
			if (neg)
				c = read();
			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');

			if (neg)
				return -ret;
			return ret;
		}

		public long nextLong() throws IOException {
			long ret = 0;
			byte c = read();
			while (c <= ' ')
				c = read();
			boolean neg = (c == '-');
			if (neg)
				c = read();
			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');
			if (neg)
				return -ret;
			return ret;
		}

		public double nextDouble() throws IOException {
			double ret = 0, div = 1;
			byte c = read();
			while (c <= ' ')
				c = read();
			boolean neg = (c == '-');
			if (neg)
				c = read();

			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');

			if (c == '.') {
				while ((c = read()) >= '0' && c <= '9') {
					ret += (c - '0') / (div *= 10);
				}
			}

			if (neg)
				return -ret;
			return ret;
		}

		private void fillBuffer() throws IOException {
			bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
			if (bytesRead == -1)
				buffer[0] = -1;
		}

		private byte read() throws IOException {
			if (bufferPointer == bytesRead)
				fillBuffer();
			return buffer[bufferPointer++];
		}

		public void close() throws IOException {
			if (din == null)
				return;
			din.close();
		}
	}

}
