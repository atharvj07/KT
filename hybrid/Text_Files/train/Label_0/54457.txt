import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.ObjectInputStream.GetField;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Random;
import java.util.SortedSet;
import java.util.Stack;
import java.util.TreeMap;
import java.util.TreeSet;

public class Q21 {
	static int MOD = 1000000007;
	static boolean b[], c1 = false;
	static int m, bo, c, di;
	static ArrayList<Integer>[] amp;
	static ArrayList<Integer>[][] amp2;
	static int sum[], dist[];
	static long pow[], ans = 0;
	static int p = 10000, time = 0, p1 = -1, p2 = -1;
	static FasterScanner sc = new FasterScanner();
	static Queue<Integer> q = new LinkedList<>();
	static ArrayList<Pair>[] amp1;
	static int arr[];
	static ArrayList<Integer> parent = new ArrayList<>();
	static BufferedWriter log;
	static HashMap<Pair, Integer> hm;
	static HashSet<Integer> hs = new HashSet<>();
	static TreeMap<Integer, Pair> hsm;
	static Stack<Integer> s = new Stack<>();
	static Pair prr[];
	static Random r = new Random();
	static long dp[];

	public static void main(String[] args) throws IOException {
		log = new BufferedWriter(new OutputStreamWriter(System.out));
		String str1 = sc.nextLine(), str2 = sc.nextLine();
		int n = str1.length();
		int arr1[] = new int[str2.length()];
		int arr2[] = new int[str2.length()];
		Arrays.fill(arr1, 1000000);
		Arrays.fill(arr2, -1);
		int j = 0;
		int ans = Integer.MAX_VALUE / 2, ans2 = Integer.MAX_VALUE, temp11 = -1, temp12 = -1, temp1 = -1, temp2 = -1;
		for (int i = 0; i < n && j < str2.length(); i++) {
			if (str1.charAt(i) == str2.charAt(j)) {
				// System.out.println(i);
				arr1[j] = i;
				ans = str2.length() - j - 1;
				temp1 = 0;
				temp2 = j;
				j++;
			}
		}
		// for(int i = 0;i<str2.length();i++) System.out.print(arr1[i]+" ");
		j = str2.length() - 1;
		for (int i = n - 1; i >= 0 && j >= 0; i--) {
			if (str1.charAt(i) == str2.charAt(j)) {
				// System.out.println(i);
				arr2[j] = i;
				if (j < ans) {
					ans = j;
					temp1 = j;
					temp2 = str2.length() - 1;
				}
				j--;
			}
		}
		// for(int i = 0;i<str2.length();i++) System.out.print(arr2[i]+" ");
		// System.out.println(ans);
		for (int i = 0; i < n - 1 && i<str2.length()-1; i++) {
			if (arr1[i] >= 1000000)
				break;
			int y = Arrays.binarySearch(arr2, i + 1, str2.length() - 1,
					arr1[i] + 1);
			if (y < 0)
				y = -(y + 1);
			if (arr2[y] >= 0 && (y - 1 - i) < ans2) {
				
				if (arr2[y] > arr1[i]) {
					temp11 = i;
					ans2 = y - 1 - i;
					temp12 = y;
				}
			}
			// System.out.println(i+" "+y+" "+ans2);
		}
		// System.out.println(ans2);
		if (ans <= ans2) {
			if (ans == Integer.MAX_VALUE / 2)
				System.out.println("-");
			else {
				for (int i = temp1; i <= temp2; i++) {
					System.out.print(str2.charAt(i));
				}
			}
		} else {
			for (int i = 0; i <= temp11; i++) {
				System.out.print(str2.charAt(i));
			}
			for (int i = temp12; i <= str2.length() - 1; i++) {
				System.out.print(str2.charAt(i));
			}
		}
		log.close();
	}

	public static void recur2(int n, int m, int k) {
		if (k == 0 && n >= 0 && m >= 0) {
			ans++;
			return;
		}
		if (n < 0 || m < 0 || k <= 0)
			return;
		recur2(n - k, m, k - 1);
		recur2(n, m - k, k - 1);
	}

	public static void recur1(int n, int cnt) {
		if (n == 0 && cnt == 0) {
			ans = (ans + 1) % MOD;
		}
		if (cnt < 0)
			return;
		long temp = 0;
		for (int i = n - 1; i >= 0; i--) {
			if ((arr[n] - m) > arr[i])
				break;
			else
				recur1(i, cnt - 1);
		}
	}

	static class Pair implements Comparable<Pair> {
		long u;
		long v;

		public Pair() {

		}

		public Pair(long u, long v) {
			this.u = u;
			this.v = v;
		}

		public int hashCode() {
			int hu = (int) (u ^ (u >>> 32));
			int hv = (int) (v ^ (v >>> 32));
			return 31 * hu + hv;
		}

		public boolean equals(Object o) {
			Pair other = (Pair) o;
			return (u == other.u && v == other.v);
		}

		public int compareTo(Pair other) {
			return Long.compare(u, other.u) != 0 ? (Long.compare(u, other.u))
					: (Long.compare(v, other.v));
		}

		public String toString() {
			return "[u=" + u + ", v=" + v + "]";
		}
	}

	public static int getParent(int x, int parent[]) {
		while (parent[x] != x) {
			parent[x] = parent[parent[x]];
			x = parent[x];
		}
		return x;
	}

	public static void bfs(int x) {
		b[x] = true;
		q.add(x);
		while (!q.isEmpty()) {
			int y = q.poll();
			for (int i = 0; i < amp[y].size(); i++) {
				if (!b[amp[y].get(i)]) {
					q.add(amp[y].get(i));
					dist[amp[y].get(i)] = dist[y] + 1;
					b[amp[y].get(i)] = true;
				}
			}
		}
	}

	public static void seive(long n) {
		b = new boolean[(int) (n + 1)];
		Arrays.fill(b, true);
		b[0] = false;
		b[1] = false;
		for (int i = 2; i * i <= n; i++) {
			if (b[i]) {
				for (int p = 2 * i; p <= n; p += i) {
					b[p] = false;
				}
			}
		}
	}

	public static void buildGraph(int n) {
		for (int i = 0; i < n; i++) {
			int x = sc.nextInt(), y = sc.nextInt();
			amp[--x].add(--y);
			amp[y].add(x);
		}
	}

	public static void dfs(int x) {
		b[x] = true;
		for (int i = 0; i < amp[x].size(); i++) {
			if (!b[amp[x].get(i)]) {
				dfs(amp[x].get(i));
			}
			sum[amp[x].get(i)]++;
		}
	}

	public static void multiBfs() {
		// System.out.println(hs);
		while (!q.isEmpty()) {
			int x = q.poll();
			for (int e : amp[x]) {
				if (!b[e]) {
					q.add(e);
					b[e] = true;
					sum[e] = x;
				} else {
					if (!hs.contains(x) && e != sum[x]) {
						System.out.println("NO");
						System.exit(0);
					}
				}
			}
		}
	}

	public static void getCycle(int x) {
		b[x] = true;
		for (int e : amp[x]) {
			if (b[e]) {
				p2 = x;
				if (e != sum[x]) {
					p1 = e;
					c1 = true;
					return;
				}
			} else {
				sum[e] = x;
				// System.out.print(e+" ");
				getCycle(e);
				if (c1)
					return;
			}
		}
		if (c1)
			return;
	}

	public static long count(long x, boolean b, long ans) {
		String str = Long.toString(x, 2);
		if (x == 1)
			return (ans + 1) % MOD;
		if (x == 0 && b)
			return (ans + 1) % MOD;
		else if (x == 0)
			return ans;
		if (str.length() > 1)
			ans = (long) ((ans + Math.pow(2, str.length() - 2) % MOD) % MOD);
		return count((long) (x - Math.pow(2, str.length() - 1)), !b, ans);
	}

	static boolean KMP(String pat, String txt) {
		int M = pat.length();
		int N = txt.length();

		// create lps[] that will hold the longest
		// prefix suffix values for pattern
		int lps[] = new int[M];
		int j = 0; // index for pat[]

		// Preprocess the pattern (calculate lps[]
		// array)
		computeLPSArray(pat, M, lps);

		int i = 0; // index for txt[]
		while (i < N) {
			if (pat.charAt(j) == txt.charAt(i)) {
				j++;
				i++;
			}
			if (j == M) {

				j = lps[j - 1];
				return true;
			}

			// mismatch after j matches
			else if (i < N && pat.charAt(j) != txt.charAt(i)) {
				// Do not match lps[0..lps[j-1]] characters,
				// they will match anyway
				if (j != 0)
					j = lps[j - 1];
				else
					i = i + 1;
			}
		}
		return false;
	}

	static void computeLPSArray(String pat, int M, int lps[]) {
		// length of the previous longest prefix suffix
		int len = 0;
		int i = 1;
		lps[0] = 0; // lps[0] is always 0

		// the loop calculates lps[i] for i = 1 to M-1
		while (i < M) {
			if (pat.charAt(i) == pat.charAt(len)) {
				len++;
				lps[i] = len;
				i++;
			} else // (pat[i] != pat[len])
			{
				// This is tricky. Consider the example.
				// AAACAAAA and i = 7. The idea is similar
				// to search step.
				if (len != 0) {
					len = lps[len - 1];

					// Also, note that we do not increment
					// i here
				} else // if (len == 0)
				{
					lps[i] = len;
					i++;
				}
			}
		}
	}

	static long power(long x, long y, long m) {
		if (y == 0)
			return 1;
		long p = power(x, y / 2, m) % m;
		p = (p * p) % m;

		return (y % 2 == 0) ? p : (x * p) % m;
	}

	private static void permutation(String prefix, String str) {
		int n = str.length();
		// if (n == 0) hs.add(prefix);
		// else {
		for (int i = 0; i < n; i++)
			permutation(prefix + str.charAt(i),
					str.substring(0, i) + str.substring(i + 1, n));
		// }
	}

	public static char give(char c1, char c2) {
		if (c1 != 'a' && c2 != 'a')
			return 'a';
		if (c1 != 'b' && c2 != 'b')
			return 'b';
		return 'c';
	}

	static class Graph {
		int vertex;
		long weight;
	}

	public static void buildTree(int n) {
		int arr[] = sc.nextIntArray(n);
		for (int i = 0; i < n; i++) {
			int x = arr[i] - 1;
			amp[i + 1].add(x);
			amp[x].add(i + 1);
		}
	}

	static class SegmentTree {
		long st[][];
		long lazy[];

		SegmentTree(int n) {
			int size = 4 * n;
			st = new long[size][3];
			lazy = new long[size];
			build(0, n - 1, 1);
		}

		long[] build(int ss, int se, int si) {
			if (ss == se) {
				st[si][0] = 1;
				st[si][1] = 1;
				st[si][2] = 1;
				return st[si];
			}
			int mid = (ss + se) / 2;
			long a1[] = build(ss, mid, si * 2), a2[] = build(mid + 1, se,
					si * 2 + 1);
			long ans[] = new long[3];
			if (arr[mid] < arr[mid + 1]) {
				ans[1] = Math.max(a2[1], Math.max(a1[1], a1[2] + a2[0]));
				if (a1[1] == (mid - ss + 1))
					ans[0] = ans[1];
				else
					ans[0] = a1[0];
				if (a2[2] == (se - mid))
					ans[2] = ans[1];
				else
					ans[2] = a2[2];
			} else {
				ans[1] = Math.max(a1[1], a2[1]);
				ans[0] = a1[0];
				ans[2] = a2[2];
			}
			st[si] = ans;
			return st[si];
		}

		void update(int si, int ss, int se, int idx, int val) {
			if (ss == se) {
				arr[idx] += val;
			} else {
				int mid = (ss + se) / 2;
				if (ss <= idx && idx <= mid) {
					update(si * 2, ss, mid, idx, val);
				} else
					update(si * 2 + 1, mid + 1, se, idx, val);
				if (arr[mid] < arr[mid + 1]) {
					st[si][1] = Math.max(
							st[si * 2][1],
							Math.max(st[si * 2 + 1][1], st[si * 2][2]
									+ st[si * 2 + 1][0]));
					if (st[si * 2][1] == (mid - ss + 1))
						st[si][0] = st[si][1];
					else
						st[si][0] = st[si * 2][0];
					if (st[si * 2 + 1][1] == (se - mid))
						st[si][2] = st[si][1];
					else
						st[si][2] = st[si * 2 + 1][2];
				} else {
					st[si][1] = Math.max(st[si * 2][1], st[si * 2 + 1][1]);
					st[si][0] = st[si * 2][0];
					st[si][2] = st[si * 2 + 1][2];
				}
			}
		}

		/*
		 * void updateRange(int si, int ss, int se, int qs, int qe, int val){
		 * if(lazy[si]!=0){ st[si] = (se - ss + 1) - st[si]; if(ss!=se){
		 * lazy[si*2] ^= lazy[si]; lazy[si*2+1] ^= lazy[si]; } lazy[si] = 0; }
		 * if(ss>se || ss>qe || se<qs) return; if(ss>=qs && se<=qe){ st[si] =
		 * (se - ss + 1) - st[si]; if(ss!=se){ lazy[si*2+1] ^= val; lazy[si*2]
		 * ^= val; } return; } int mid = (ss+se)/2; updateRange(2*si, ss, mid,
		 * qs, qe, val); updateRange(2*si+1, mid+1, se, qs, qe, val); st[si] =
		 * st[si*2+1]+st[si*2]; } long queryRange(int si, int ss, int se, int
		 * qs, int qe){ //System.out.println(si +" "+ ss+ " "+ se+
		 * " "+qs+" "+qe); if(ss>se || ss>qe || qs>se){ return 0; }
		 * if(lazy[si]!=0){ st[si] = (se - ss + 1) - st[si]; if(ss!=se){
		 * lazy[si*2+1] ^= lazy[si]; lazy[si*2] ^= lazy[si]; } lazy[si] = 0; }
		 * if(ss>=qs && se<=qe) return st[si]; int mid = (ss+se)/2; return
		 * queryRange(2*si, ss, mid, qs, qe) + queryRange(2*si+1, mid+1, se, qs,
		 * qe); }
		 */
		long[] get(int qs, int qe, int ss, int se, int si) {
			if (qs <= ss && qe >= se) {
				return st[si];
			}
			int mid = (ss + se) / 2;
			if (qe <= mid)
				return get(qs, qe, ss, mid, si * 2);
			else if (qs > mid)
				return get(qs, qe, mid + 1, se, si * 2 + 1);
			long a1[] = get(qs, qe, ss, mid, si * 2), a2[] = get(qs, qe,
					mid + 1, se, si * 2 + 1);
			long ans[] = new long[3];
			if (arr[mid] < arr[mid + 1]) {
				ans[1] = Math.max(a2[1], Math.max(a1[1], a1[2] + a2[0]));
				if (a1[1] == (mid - ss + 1))
					ans[0] = ans[1];
				else
					ans[0] = a1[0];
				if (a2[2] == (se - mid))
					ans[2] = ans[1];
				else
					ans[2] = a2[2];
			} else {
				ans[1] = Math.max(a1[1], a2[1]);
				ans[0] = a1[0];
				ans[2] = a2[2];
			}
			return ans;
		}

		void print() {
			for (int i = 0; i < st.length; i++) {
				System.out.println(st[i][0] + " " + st[i][1] + " " + st[i][2]);
			}
			System.out.println();
		}
	}

	static int convert(int x) {
		int cnt = 0;
		String str = Integer.toBinaryString(x);
		// System.out.println(str);
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == '1') {
				cnt++;
			}
		}
		int ans = (int) Math.pow(3, 6 - cnt);
		return ans;
	}

	static class Node2 {
		Node2 left = null;
		Node2 right = null;
		Node2 parent = null;
		int data;
	}

	static class BinarySearchTree {
		Node2 root = null;
		int height = 0;
		int max = 0;
		int cnt = 1;
		ArrayList<Integer> parent = new ArrayList<>();
		HashMap<Integer, Integer> hm = new HashMap<>();

		public void insert(int x) {
			Node2 n = new Node2();
			n.data = x;
			if (root == null) {
				root = n;
			} else {
				Node2 temp = root, temp2 = null;
				while (temp != null) {
					temp2 = temp;
					if (x > temp.data)
						temp = temp.right;
					else
						temp = temp.left;
				}
				if (x > temp2.data)
					temp2.right = n;
				else
					temp2.left = n;
				n.parent = temp2;
				parent.add(temp2.data);
			}
		}

		public Node2 getSomething(int x, int y, Node2 n) {
			if (n.data == x || n.data == y)
				return n;
			else if (n.data > x && n.data < y)
				return n;
			else if (n.data < x && n.data < y)
				return getSomething(x, y, n.right);
			else
				return getSomething(x, y, n.left);
		}

		public Node2 search(int x, Node2 n) {
			if (x == n.data) {
				max = Math.max(max, n.data);
				return n;
			}
			if (x > n.data) {
				max = Math.max(max, n.data);
				return search(x, n.right);
			} else {
				max = Math.max(max, n.data);
				return search(x, n.left);
			}
		}

		public int getHeight(Node2 n) {
			if (n == null)
				return 0;
			height = 1 + Math.max(getHeight(n.left), getHeight(n.right));
			return height;
		}
	}

	static long findDiff(long[] arr, long[] brr, int m) {
		int i = 0, j = 0;
		long fa = 1000000000000L;
		while (i < m && j < m) {
			long x = arr[i] - brr[j];
			if (x >= 0) {
				if (x < fa)
					fa = x;
				j++;
			} else {
				if ((-x) < fa)
					fa = -x;
				i++;
			}
		}
		return fa;
	}

	public static long max(long x, long y, long z) {
		if (x >= y && x >= z)
			return x;
		if (y >= x && y >= z)
			return y;
		return z;
	}

	static long modInverse(long a, long mOD2) {
		return power(a, mOD2 - 2, mOD2);
	}

	static long power2(long x, BigInteger y, long m) {
		long ans = 1;
		BigInteger two = new BigInteger("2");
		while (y.compareTo(BigInteger.ZERO) > 0) {
			if (y.getLowestSetBit() == y.bitCount()) {
				x = (x * x) % MOD;
				y = y.divide(two);
			} else {
				ans = (ans * x) % MOD;
				y = y.subtract(BigInteger.ONE);
			}
		}
		return ans;
	}

	static BigInteger power2(BigInteger x, BigInteger y, BigInteger m) {
		BigInteger ans = new BigInteger("1");
		BigInteger one = new BigInteger("1");
		BigInteger two = new BigInteger("2");
		BigInteger zero = new BigInteger("0");
		while (y.compareTo(zero) > 0) {
			// System.out.println(y);
			if (y.mod(two).equals(one)) {
				ans = ans.multiply(x).mod(m);
				y = y.subtract(one);
			} else {
				x = x.multiply(x).mod(m);
				y = y.divide(two);
			}
		}
		return ans;
	}

	static BigInteger power(BigInteger x, BigInteger y, BigInteger m) {
		if (y.equals(0))
			return (new BigInteger("1"));
		BigInteger p = power(x, y.divide(new BigInteger("2")), m).mod(m);
		p = (p.multiply(p)).mod(m);

		return (y.mod(new BigInteger("2")).equals(0)) ? p : (p.multiply(x))
				.mod(m);
	}

	static long d, x, y;

	public static void extendedEuclidian(long a, long b) {
		if (b == 0) {
			d = a;
			x = 1;
			y = 0;
		} else {
			extendedEuclidian(b, a % b);
			int temp = (int) x;
			x = y;
			y = temp - (a / b) * y;
		}
	}

	public static long gcd(long n, long m) {
		if (m != 0)
			return gcd(m, n % m);
		else
			return n;
	}

	public static class FasterScanner {
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;

		public int read() {
			if (numChars == -1)
				throw new InputMismatchException();
			if (curChar >= numChars) {
				curChar = 0;
				try {
					numChars = System.in.read(buf);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (numChars <= 0)
					return -1;
			}
			return buf[curChar++];
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

		public String nextString() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isSpaceChar(c));
			return res.toString();
		}

		public long nextLong() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			long res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public int nextInt() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			int res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public int[] nextIntArray(int n) {
			return nextIntArray(n, 0);
		}

		public int[] nextIntArray(int n, int off) {
			int[] arr = new int[n + off];
			for (int i = 0; i < n; i++) {
				arr[i + off] = nextInt();
			}
			return arr;
		}

		public long[] nextLongArray(int n) {
			return nextLongArray(n, 0);
		}

		public long[] nextLongArray(int n, int off) {
			long[] arr = new long[n + off];
			for (int i = 0; i < n; i++) {
				arr[i + off] = nextLong();
			}
			return arr;
		}

		private boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		private boolean isEndOfLine(int c) {
			return c == '\n' || c == '\r' || c == -1;
		}
	}
}