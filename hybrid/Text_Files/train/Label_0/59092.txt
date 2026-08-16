import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class XOR {

	public static void main(String[] args) throws IOException {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int N = 1;
		while (N < n)
			N <<= 1; // padding

		int[] in = new int[N + 1];
		for (int i = 1; i <= n; i++)
			in[i] = sc.nextInt();
		SegmentTree sgt = new SegmentTree(in);
		int m = sc.nextInt();
		for (int i = 0; i < m; i++) {
			int op = sc.nextInt();
			if (op == 1) {
				int n1 = sc.nextInt();
				int n2 = sc.nextInt();
				System.out.println(sgt.query(n1, n2));
			} else {
				int n1 = sc.nextInt();
				int n2 = sc.nextInt();
				int x = sc.nextInt();
				sgt.update_range(n1, n2, x);
			}
		}

	}

	private static int[] intToArray(int i) {
		int[] a = new int[32];
		for (int i1 = 0; i1 < 32; i1++) {
			if ((i & (1l << i1)) != 0) {
				a[i1] = 1;
			}
		}
		return a;
	}

	private static long getValue(int[] a) {
		long s = 0;
		for (int i = 0; i < a.length; i++) {
			s += (long) a[i] * (1l << i);
		}
		return s;
	}

	private static void add(int[] node1, int[] node2, int[] node) {
		for (int i = 0; i < node.length; i++) {
			node[i] = node1[i] + node2[i];
		}

	}

	public static void xor(int[] arr, int v, int l) {
		for (int i = 0; i < arr.length; i++) {
			if ((v & (1 << i)) != 0) {
				arr[i] = l - arr[i];
			}
		}
	}

	static class SegmentTree { // 1-based DS, OOP

		int N; // the number of elements in the array as a power of 2 (i.e. after padding)
		int[] array, lazy;
		int[][] sTree;

		SegmentTree(int[] in) {
			array = in;
			N = in.length - 1;
			sTree = new int[N << 1][32]; // no. of nodes = 2*N - 1, we add one to cross out index zero
			lazy = new int[N << 1];
			build(1, 1, N);
		}

		void build(int node, int b, int e) // O(n)
		{
			if (b == e)
				sTree[node] = intToArray(array[b]);
			else {
				int mid = b + e >> 1;
				build(node << 1, b, mid);
				build(node << 1 | 1, mid + 1, e);
				add(sTree[node << 1], sTree[node << 1 | 1], sTree[node]);
			}
		}

		void update_range(int i, int j, int val) // O(log n)
		{
			update_range(1, 1, N, i, j, val);
		}

		void update_range(int node, int b, int e, int i, int j, int val) {
			if (i > e || j < b)
				return;
			if (b >= i && e <= j) {
				xor(sTree[node], val, e - b + 1);
				lazy[node] ^= val;
			} else {
				int mid = b + e >> 1;
				propagate(node, b, mid, e);
				update_range(node << 1, b, mid, i, j, val);
				update_range(node << 1 | 1, mid + 1, e, i, j, val);
				add(sTree[node << 1], sTree[node << 1 | 1], sTree[node]);

			}

		}

		void propagate(int node, int b, int mid, int e) {
			lazy[node << 1] ^= lazy[node];
			lazy[node << 1 | 1] ^= lazy[node];
			xor(sTree[node << 1], lazy[node], (mid - b + 1));
			xor(sTree[node << 1 | 1], lazy[node], ((e - mid)));
			lazy[node] = 0;
		}

		long query(int i, int j) {
			return query(1, 1, N, i, j);
		}

		long query(int node, int b, int e, int i, int j) // O(log n)
		{
			if (i > e || j < b)
				return 0;
			if (b >= i && e <= j)
				return getValue(sTree[node]);
			int mid = b + e >> 1;
			propagate(node, b, mid, e);
			long q1 = query(node << 1, b, mid, i, j);
			long q2 = query(node << 1 | 1, mid + 1, e, i, j);
			return q1 + q2;

		}

	}

	static class Scanner {
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream s) {
			br = new BufferedReader(new InputStreamReader(s));
		}

		public Scanner(String file) throws FileNotFoundException {
			br = new BufferedReader(new FileReader(file));
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
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
			return Double.parseDouble(next());
		}

		public boolean ready() throws IOException {
			return br.ready();
		}

		public int[] nextIntArr(int n) throws IOException {
			int[] arr = new int[n];
			for (int i = 0; i < n; i++) {
				arr[i] = Integer.parseInt(next());
			}
			return arr;
		}
	}
}
