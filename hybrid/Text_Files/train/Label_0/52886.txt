import java.io.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.*;

public class Main {
	static final int INF = (int) (1e9 + 10);
	static final int MOD = (int) (1e9 + 7);
	static final int N = (int) (4e5 + 5);
	// static ArrayList<Integer>[] graph;
	// static boolean visited[];
	// static long size[];

	public static void main(String[] args) throws NumberFormatException, IOException {
		FastReader sc = new FastReader();
		PrintWriter pr = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// Scanner scn = new Scanner(System.in);
		//
		int h = sc.nextInt();
		int w = sc.nextInt();
		int n = sc.nextInt();
		int x = sc.nextInt();
		int y = sc.nextInt();
		String s1 = sc.next();
		String s2 = sc.next();
		int left = y, right = y, up = x, down = x;
		int f = 0;
		for (int i = 0; i < n; i++) {
			if (s1.charAt(i) == 'L') {
				left--;
			}
			if (left>0 && s2.charAt(i) == 'R' && left <w)
				left++;

			if (s1.charAt(i) == 'R')
				right++;
			if (right<=w && s2.charAt(i) == 'L' && right > 1)
				right--;

			if (s1.charAt(i) == 'U')
				up--;
			if (up>0 && s2.charAt(i) == 'D' && up <h)
				up++;

			if (s1.charAt(i) == 'D')
				down++;
			if (down<=h && s2.charAt(i) == 'U' && down > 1)
				down--;
			//System.out.println(" "+left+" "+right+" "+up+" "+down);
			if (down > h || up <=0 || left <=0 || right > w) {
				f = 1;
				break;
			}
			
			
		}
		if (f == 0)
			pr.println("YES");
		else
			pr.println("NO");
		//
		// coded to perfection by Rohan Mukhija
		pr.flush();
		pr.close();
	}

	/*
	 * Template From Here
	 */
	public static class Pair implements Comparable<Pair> {
		int u;
		int v;

		Pair(int u, int v, int c) {
			this.u = u;
			this.v = v;

		}

		public int compareTo(Pair compareEdge) {
			return Long.compare(this.v, compareEdge.v);
		}
	};

	private static boolean possible(long[] arr, int[] f, long mid, long k) {
		long c = 0;

		for (int i = 0; i < arr.length; i++) {
			if ((arr[i] * f[f.length - i - 1]) > mid) {
				c += (arr[i] - (mid / f[f.length - i - 1]));
			}
		}
		// System.out.println(mid+" "+c);
		if (c <= k)
			return true;
		return false;
	}

	static void sort(long[] a) {
		ArrayList<Long> l = new ArrayList<>();
		for (long i : a)
			l.add(i);
		Collections.sort(l);
		for (int i = 0; i < a.length; i++)
			a[i] = l.get(i);
	}

	static void sort(int[] a) {
		ArrayList<Integer> l = new ArrayList<>();
		for (int i : a)
			l.add(i);
		Collections.sort(l);
		for (int i = 0; i < a.length; i++)
			a[i] = l.get(i);
	}

	public static int lowerBound(ArrayList<Integer> array, int length, long value) {
		int low = 0;
		int high = length;
		while (low < high) {
			final int mid = (low + high) / 2;
			if (value <= array.get(mid)) {
				high = mid;
			} else {
				low = mid + 1;
			}
		}
		return low;
	}

	static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());
		}

		long nextLong() {
			return Long.parseLong(next());
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}

		String nextLine() {
			String str = "";
			try {
				str = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return str;
		}
	}

	static long gcd(long a, long b) {
		if (a == 0)
			return b;
		return gcd(b % a, a);
	}

	static long lcm(long a, long b) {
		return (a * b) / gcd(a, b);
	}

	public static void sortbyColumn(int[][] att, int col) {
		// Using built-in sort function Arrays.sort
		Arrays.sort(att, new Comparator<int[]>() {

			@Override
			// Compare values according to columns
			public int compare(final int[] entry1, final int[] entry2) {

				// To sort in descending order revert
				// the '>' Operator
				// if (entry1[col] > entry2[col])
				// return 1;
				// else //(entry1[col] >= entry2[col])
				// return -1;
				return new Integer(entry1[col]).compareTo(entry2[col]);
				// return entry1[col].
			}
		}); // End of function call sort().
	}

	static class pair {
		int V, I;

		pair(int v, int i) {
			V = v;
			I = i;
		}
	}

	public static int[] swap(int data[], int left, int right) {
		int temp = data[left];
		data[left] = data[right];
		data[right] = temp;
		return data;
	}

	public static int[] reverse(int data[], int left, int right) {
		while (left < right) {
			int temp = data[left];
			data[left++] = data[right];
			data[right--] = temp;
		}
		return data;
	}

	public static boolean findNextPermutation(int data[]) {
		if (data.length <= 1)
			return false;

		int last = data.length - 2;
		while (last >= 0) {
			if (data[last] < data[last + 1]) {
				break;
			}
			last--;
		}
		if (last < 0)
			return false;

		int nextGreater = data.length - 1;
		for (int i = data.length - 1; i > last; i--) {
			if (data[i] > data[last]) {
				nextGreater = i;
				break;
			}
		}
		data = swap(data, nextGreater, last);
		data = reverse(data, last + 1, data.length - 1);
		return true;
	}

	static long ncr(long n, long r) {
		long p = 1, k = 1;
		if (n - r < r) {
			r = n - r;
		}

		if (r != 0) {
			while (r > 0) {
				p *= n;
				k *= r;

				// gcd of p, k
				long m = __gcd(p, k);

				p /= m;
				k /= m;

				n--;
				r--;
			}

		} else {
			p = 1;
		}

		// if our approach is correct p = ans and k =1
		return p;
	}

	static long __gcd(long n1, long n2) {
		long gcd = 1;

		for (int i = 1; i <= n1 && i <= n2; ++i) {
			// Checks if i is factor of both integers
			if (n1 % i == 0 && n2 % i == 0) {
				gcd = i;
			}
		}
		return gcd;
	}

	static long power(long prev, int y, int p) {
		long res = 1;

		prev = prev % p;

		if (prev == 0)
			return 0;
		while (y > 0) {

			if ((y & 1) == 1)
				res = (res * prev) % p;

			y = y >> 1;
			prev = (prev * prev) % p;
		}
		return res;
	}

	static long modInverse(long fac2, int p) {
		return power(fac2, p - 2, p);
	}

	static boolean isPrime(int n) {
		// Corner cases
		if (n <= 1)
			return false;
		if (n <= 3)
			return true;

		// This is checked so that we can skip
		// middle five numbers in below loop
		if (n % 2 == 0 || n % 3 == 0)
			return false;

		for (int i = 5; i * i <= n; i = i + 6)
			if (n % i == 0 || n % (i + 2) == 0)
				return false;

		return true;
	}

	public static BigInteger lcmm(String a, String b) {
		BigInteger s = new BigInteger(a);
		BigInteger s1 = new BigInteger(b);
		BigInteger mul = s.multiply(s1);
		BigInteger gcd = s.gcd(s1);
		BigInteger lcm = mul.divide(gcd);
		return lcm;
	}

}
