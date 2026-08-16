import java.io.*;
import java.math.*;
import java.util.*;
import java.util.stream.*;

public class Main {

	static class ModuloCombinatorics {
		/** maximal needed number, N itself is included **/
		final int N;

		/** prime modulo **/
		final int P;

		/** factorials **/
		final int[] fact;

		/** multiplicative inverses, take care to not touch inv[0] **/
		final int[] inv;

		/** inverse factorials **/
		final int[] invFact;

		public ModuloCombinatorics(int N, int P) {
			this.N = N;
			this.P = P;
			fact = new int[N + 1];
			fact[0] = 1;
			for (int i = 1; i <= N; i++) {
				fact[i] = (int) ((long) i * fact[i - 1] % P);
			}

			inv = new int[N + 1];
			inv[1] = 1;
			for (int i = 2; i <= N; i++) {
				inv[i] = P - (int) ((long) (P / i) * inv[P % i] % P);
			}

			invFact = new int[N + 1];
			invFact[0] = 1;
			for (int i = 1; i <= N; i++) {
				invFact[i] = (int) ((long) invFact[i - 1] * inv[i] % P);
			}
		}

		public int choose(int n, int k) {
			return (n < 0 || k < 0 || k > n) ? 0 : (int) ((long) fact[n]
					* invFact[k] % P * invFact[n - k] % P);
		}

		/** a^b modulo mod, mod is arbitrary **/
		static public int pow(int a, long b, int mod) {
			if (a < 0 || a >= mod || b < 0) {
				throw new IllegalArgumentException();
			}
			int ret = 1;
			for (; b > 0; b >>= 1) {
				if ((b & 1) == 1) {
					ret = (int) ((long) ret * a % mod);
				}
				a = (int) ((long) a * a % mod);
			}
			return ret;
		}

		/** a^b modulo P **/
		public int pow(int a, long b) {
			return pow(a, b, P);
		}
	}

	static final int P = 1_000_000_007;

	boolean isColorful(int[] a, int k) {
		if (a.length < k) {
			return false;
		}
		int[] b = new int[k];
		int sum = 0;
		for (int i = 0; i < k; i++) {
			int idx = a[i];
			sum -= Math.min(b[idx], 1);
			b[idx]++;
			sum += Math.min(b[idx], 1);
		}
		if (sum == k) {
			return true;
		}

		for (int i = k; i < a.length; i++) {
			int idx = a[i];
			sum -= Math.min(b[idx], 1);
			b[idx]++;
			sum += Math.min(b[idx], 1);

			idx = a[i - k];
			sum -= Math.min(b[idx], 1);
			b[idx]--;
			sum += Math.min(b[idx], 1);

			if (sum == k) {
				return true;
			}
		}
		
		return false;
	}

	void submit() {
		int n = nextInt();
		int k = nextInt();
		int m = nextInt();

		int[] a = new int[m];
		for (int i = 0; i < m; i++) {
			a[i] = nextInt() - 1;
		}

		ModuloCombinatorics mc = new ModuloCombinatorics(n, P);

		int total = (int) ((long) (n - m + 1) * mc.pow(k, n - m) % P);

		if (n < k) {
			out.println(0);
			return;
		}
		
		if (isColorful(a, k)) {
			out.println(total);
			return;
		}

		int valL = getVal(a, k);
		int valR = getVal(reverse(a), k);

		if (valL != -1) {
			int[] valsA = makeDP(valL, n + 1, k);
			int[] valsB = makeDP(valR, n + 1, k);

			// System.err.println(Arrays.toString(valsA));
			// System.err.println(Arrays.toString(valsB));

			int bad = 0;
			for (int i = 0; i <= n - m; i++) {
				bad += (int) ((long) valsA[i] * valsB[n - m - i] % P);
				if (bad >= P) {
					bad -= P;
				}
			}

			// System.err.println(total + " " + bad);

			int ret = total - bad;
			if (ret < 0) {
				ret += P;
			}

			out.println(ret);
			return;
		}
		
//		System.err.println("hi");
		
		int[] dp = new int[k - 1];
		dp[k - 2] = k;
		
		int[] dpSum = new int[k - 1];
		
		if (k - 1 - (k - 2) >= m) {
			dpSum[k - 2] = dp[k - 2];
		}
		
		for (int i = 1; i < n; i++) {
			int pref = 0;
			int prefSum = 0;
			for (int j = 0; j < k - 1; j++) {
				pref += dp[j];
				if (pref >= P) {
					pref -= P;
				}
				dp[j] = pref;
				if (j + 1 < k - 1) {
					dp[j] += (int) ((long) dp[j + 1] * (j + 2) % P);
					if (dp[j] >= P) {
						dp[j] -= P;
					}
				}
				
				prefSum += dpSum[j];
				if (prefSum >= P) {
					prefSum -= P;
				}
				dpSum[j] = prefSum;
				if (j + 1 < k - 1) {
					dpSum[j] += (int) ((long) dpSum[j + 1] * (j + 2) % P);
					if (dpSum[j] >= P) {
						dpSum[j] -= P;
					}
				}
				
				if (k - 1 - j >= m) {
					dpSum[j] += dp[j];
					if (dpSum[j] >= P) {
						dpSum[j] -= P;
					}
				}
			}
		}

		int bad = 0;
		for (int x : dpSum) {
			bad += x;
			if (bad >= P) {
				bad -= P;
			}
		}
		
		bad = (int)((long)bad * mc.invFact[k] % P * mc.fact[k - m] % P);
		
//		System.err.println(bad);
		
		int ret = total - bad;
		if (ret < 0) {
			ret += P;
		}

		out.println(ret);

	}	

	int[] makeDP(int s0, int len, int sz) {
		int[] ret = new int[len];

		int[] cur = new int[sz - 1];
		cur[s0 - 1] = 1;

		for (int i = 0; i < len; i++) {
			int pref = 0;
			for (int j = 0; j < sz - 1; j++) {
				pref += cur[j];
				if (pref >= P) {
					pref -= P;
				}
				cur[j] = pref;
				if (j + 1 < sz - 1) {
					cur[j] += (int) ((long) cur[j + 1] * (j + 2) % P);
					if (cur[j] >= P) {
						cur[j] -= P;
					}
				}
			}
			ret[i] = pref;
		}

		return ret;
	}

	int getVal(int[] a, int k) {
		HashSet<Integer> seen = new HashSet<>();
		for (int i = 0; i < a.length; i++) {
			if (seen.contains(a[i])) {
				return k - i;
			} else {
				seen.add(a[i]);
			}
		}
		return -1;
	}

	int[] reverse(int[] a) {
		int[] b = new int[a.length];
		for (int i = 0, j = a.length - 1; i < a.length; i++, j--) {
			b[j] = a[i];
		}
		return b;
	}

	void test() {

	}

	void stress() {
		for (int tst = 0;; tst++) {
			if (false) {
				throw new AssertionError();
			}
			System.err.println(tst);
		}
	}

	Main() throws IOException {
		is = System.in;
		out = new PrintWriter(System.out);
		submit();
		// stress();
		// test();
		out.close();
	}

	static final Random rng = new Random();
	static final int C = 5;

	static int rand(int l, int r) {
		return l + rng.nextInt(r - l + 1);
	}

	public static void main(String[] args) throws IOException {
		new Main();
	}

	private InputStream is;
	PrintWriter out;

	private byte[] buf = new byte[1 << 14];
	private int bufSz = 0, bufPtr = 0;

	private int readByte() {
		if (bufSz == -1)
			throw new RuntimeException("Reading past EOF");
		if (bufPtr >= bufSz) {
			bufPtr = 0;
			try {
				bufSz = is.read(buf);
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
			if (bufSz <= 0)
				return -1;
		}
		return buf[bufPtr++];
	}

	private boolean isTrash(int c) {
		return c < 33 || c > 126;
	}

	private int skip() {
		int b;
		while ((b = readByte()) != -1 && isTrash(b))
			;
		return b;
	}

	String nextToken() {
		int b = skip();
		StringBuilder sb = new StringBuilder();
		while (!isTrash(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}

	String nextString() {
		int b = readByte();
		StringBuilder sb = new StringBuilder();
		while (!isTrash(b) || b == ' ') {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}

	double nextDouble() {
		return Double.parseDouble(nextToken());
	}

	char nextChar() {
		return (char) skip();
	}

	int nextInt() {
		int ret = 0;
		int b = skip();
		if (b != '-' && (b < '0' || b > '9')) {
			throw new InputMismatchException();
		}
		boolean neg = false;
		if (b == '-') {
			neg = true;
			b = readByte();
		}
		while (true) {
			if (b >= '0' && b <= '9') {
				ret = ret * 10 + (b - '0');
			} else {
				if (b != -1 && !isTrash(b)) {
					throw new InputMismatchException();
				}
				return neg ? -ret : ret;
			}
			b = readByte();
		}
	}

	long nextLong() {
		long ret = 0;
		int b = skip();
		if (b != '-' && (b < '0' || b > '9')) {
			throw new InputMismatchException();
		}
		boolean neg = false;
		if (b == '-') {
			neg = true;
			b = readByte();
		}
		while (true) {
			if (b >= '0' && b <= '9') {
				ret = ret * 10 + (b - '0');
			} else {
				if (b != -1 && !isTrash(b)) {
					throw new InputMismatchException();
				}
				return neg ? -ret : ret;
			}
			b = readByte();
		}
	}
}
