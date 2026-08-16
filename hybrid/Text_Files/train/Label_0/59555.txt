import java.io.*;
import java.util.*;

public class Solution {

	static final int mod = (int) 1e9 + 7;
	static final int proMod = (int) 1e9 + 6;
	static long fac[], ifac[], DR[] = new long[101];
	static int MOD = (int) (1e9 + 7);
	static boolean[] isPrime;
	static int minPrime[];
	static long dp[][];
	static int n;
	static int d, x, y;

	public static void main(String args[]) {
		InputReader in = new InputReader(System.in);
		PrintWriter w = new PrintWriter(System.out);

		int n = in.nextInt();
		String st = in.readString();
		int b[] = new int[26];
		int a[][] = new int[n + 1][26];
		for (int i = 0; i < n; i++) {
			b[st.charAt(i) - 'a']++;
			a[b[st.charAt(i) - 'a']][st.charAt(i) - 'a'] = i;

		}
		int t = in.nextInt();
		while (t-- > 0) {
			String m = in.readString();
			int[] bb = new int[26];
			for (int j = 0; j < m.length(); j++) {
				bb[m.charAt(j) - 'a']++;
			}
			int ans = 0;
			for (int j = 0; j < 26; j++) {
				ans = Math.max(a[bb[j]][j] + 1, ans);
			}
			w.println(ans);
		}
		w.close();
	}

	static long fastPow(int a, int b) {
		if (b == 0)
			return 1;
		long t = fastPow(a, b >> 1);
		t = (t * t) % mod;
		if ((b & 1) != 0)
			t = (t * a) % mod;
		return t;
	}

	static void Dr() {
		DR[0] = 1;
		DR[1] = 0;
		DR[2] = 1;
		for (int i = 3; i < 101; i++) {
			DR[i] = ((i - 1) * (DR[i - 1] + DR[i - 2]) % MOD) % MOD;
		}

	}

	static long mp(long a, long b) {
		long ans = 1;

		while (b != 0) {
			if (b % 2 == 1)
				ans = (ans * a) % MOD;

			a = (a * a) % MOD;
			b /= 2;

		}
		return ans % MOD;
	}

	static void precompute() {
		int i;
		int N = 1000005;
		fac = new long[N];
		ifac = new long[N];
		fac[0] = 1;
		for (i = 1; i < N; i++) {
			fac[i] = (i * fac[i - 1]) % MOD;
		}
		ifac[N - 1] = mp(fac[N - 1], MOD - 2);
		for (i = N - 2; i >= 0; i--) {
			ifac[i] = ((i + 1) * ifac[i + 1]) % MOD;

		}
	}

	public static long combine(int n, int k) {
		if (k > n - k) {
			k = n - k;
		}
		long result = 1;
		for (int i = 0; i < k; i++) {
			result *= (n - i);
			result /= (i + 1);
		}
		return result;
	}

	static long mInv(long A) {

		return mp(A, MOD - 2);

	}

	static long mC(int n, int k) {
		// calculates C(n,k) mod p (assuming p is prime).
		// if(k>n-k)k=n-k;
		long an; // n * (n-1) * ... * (n-k+1)
		if (k <= 0)
			return 1;
		if (n < k)
			return 0;

		an = fac[n] % MOD;
		an *= ifac[n - k];
		an %= MOD;
		an *= ifac[k];
		an %= MOD;

		// numerator / denominator mod p.
		return an;
	}

	static int gcd(int num1, int num2) {
		if (num1 > num2) {
			int temp = num1;
			num1 = num2;
			num2 = temp;
		}
		while (num1 != 0) {
			int temp = num1;
			num1 = num2 % num1;
			num2 = temp;
		}
		return num2;
	}

	static long gcd(long A, long B) {
		if (B == 0)
			return A;
		else
			return gcd(B, A % B);
	}

	static void extendedEuclid(int A, int B) {
		if (B == 0) {
			d = A;
			x = 1;
			y = 0;
		} else {
			extendedEuclid(B, A % B);
			int temp = x;
			x = y;
			y = temp - (A / B) * y;
		}
	}

	// if(gcd(A,M)==1)
	static int mInv2(int A, int M) {
		extendedEuclid(A, M);
		return (x % M + M) % M;
	}

	static void sieve() {

		int N = 100005;

		isPrime = new boolean[N + 1];
		minPrime = new int[N + 1];

		for (int i = 0; i <= N; ++i) {
			isPrime[i] = true;
			minPrime[i] = i;
		}
		isPrime[0] = false;
		isPrime[1] = false;
		for (int i = 2; i * i <= N; ++i) {
			if (isPrime[i] == true) {
				for (int j = i * i; j <= N; j += i) {
					isPrime[j] = false;
					minPrime[j] = i;
				}
			}
		}

	}

	static class InputReader {

		private InputStream stream;
		private byte[] buf = new byte[8192];
		private int curChar;
		private int snumChars;
		private SpaceCharFilter filter;

		public InputReader(InputStream stream) {
			this.stream = stream;
		}

		public int snext() {
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
			int c = snext();
			while (isSpaceChar(c))
				c = snext();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = snext();
			}

			int res = 0;

			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = snext();
			} while (!isSpaceChar(c));

			return res * sgn;
		}

		public long nextLong() {
			int c = snext();
			while (isSpaceChar(c))
				c = snext();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = snext();
			}

			long res = 0;

			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = snext();
			} while (!isSpaceChar(c));

			return res * sgn;
		}

		public String readString() {
			int c = snext();
			while (isSpaceChar(c))
				c = snext();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = snext();
			} while (!isSpaceChar(c));
			return res.toString();
		}

		public boolean isSpaceChar(int c) {
			if (filter != null)
				return filter.isSpaceChar(c);
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		public interface SpaceCharFilter {
			public boolean isSpaceChar(int ch);
		}
	}

}
