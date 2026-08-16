import java.io.*;
import java.util.*;
import java.lang.*;

public class Main {
	int mod = 1000000007;

	static FastScanner sc = new FastScanner();

	public static void main(String[] args) {
		out = new PrintWriter(new BufferedOutputStream(System.out));
		int x = sc.nextInt();
		int y = sc.nextInt();
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int p[] = new int[a];
		int q[] = new int[b];
		int r[] = new int[c];

		PriorityQueue<Integer> pq1 = new PriorityQueue<Integer>(Collections.reverseOrder());
		PriorityQueue<Integer> pq2 = new PriorityQueue<Integer>(Collections.reverseOrder());
		PriorityQueue<Integer> pq3 = new PriorityQueue<Integer>(Collections.reverseOrder());
		long ans = 0;
		for (int i = 0; i < a; i++) {
			p[i] = sc.nextInt();
			pq1.add(p[i]);
		}
		for (int i = 0; i < b; i++) {
			q[i] = sc.nextInt();
			pq2.add(q[i]);
		}
		for (int i = 0; i < c; i++) {
			r[i] = sc.nextInt();
			pq3.add(r[i]);
		}
		for (int i = 0; i < x; i++) {
			pq3.add(pq1.poll());
		}
		for (int i = 0; i < y; i++) {
			pq3.add(pq2.poll());
		}
		for (int i = 0; i < x+y; i++) {
			ans+=pq3.poll();
		}
		out.println(ans);
		out.close();
	}

	// ----------------------------------------------------------

	static int l_min(int[] a) {
		Arrays.sort(a);
		return a[0];
	}

	static int l_max(int[] a) {
		int l = a.length;
		Arrays.sort(a);
		return a[l - 1];
	}

	static int gcd(int a, int b) {

		if (a == 0) {
			return b;
		}
		return gcd(b % a, a);

	}

	static int[] fill(int[] a) {
		int n = a.length;
		for (int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}
		return a;
	}

	public static PrintWriter out;

}

class UnionFind {
	int parent[];
	int rank[];
	int size[];

	UnionFind(int n) {
		parent = new int[n];
		rank = new int[n];
		size = new int[n];
		for (int i = 0; i < n; i++) {
			parent[i] = i;
			rank[i] = 0;
			size[i] = 1;
		}
	}

	void union(int x, int y) {
		int xRoot = find(x);
		int yRoot = find(y);

		if (xRoot != yRoot) {

			if (rank[xRoot] > rank[yRoot]) {
				parent[yRoot] = xRoot;
				size[xRoot] += size[yRoot];

			} else if (rank[xRoot] < rank[yRoot]) {
				parent[xRoot] = yRoot;
				size[yRoot] += size[xRoot];

			} else {
				parent[yRoot] = xRoot;
				rank[xRoot]++;
				size[xRoot] += size[yRoot];
			}
		}

	}

	int find(int x) {
		if (parent[x] == x) {
			return x;
		} else {
			return find(parent[x]);
		}

	}

	boolean same(int x, int y) {
		return find(x) == find(y);
	}

}

class FastScanner {
	private final InputStream in = System.in;
	private final byte[] buffer = new byte[1024];
	private int ptr = 0;
	private int buflen = 0;

	private boolean hasNextByte() {
		if (ptr < buflen) {
			return true;
		} else {
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

	private int readByte() {
		if (hasNextByte())
			return buffer[ptr++];
		else
			return -1;
	}

	private static boolean isPrintableChar(int c) {
		return 33 <= c && c <= 126;
	}

	public boolean hasNext() {
		while (hasNextByte() && !isPrintableChar(buffer[ptr]))
			ptr++;
		return hasNextByte();
	}

	public String next() {
		if (!hasNext())
			throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while (isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}

	public long nextLong() {
		if (!hasNext())
			throw new NoSuchElementException();
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
		while (true) {
			if ('0' <= b && b <= '9') {
				n *= 10;
				n += b - '0';
			} else if (b == -1 || !isPrintableChar(b)) {
				return minus ? -n : n;
			} else {
				throw new NumberFormatException();
			}
			b = readByte();
		}
	}

	public int nextInt() {
		long nl = nextLong();
		if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE)
			throw new NumberFormatException();
		return (int) nl;
	}

	public double nextDouble() {
		return Double.parseDouble(next());
	}
}
