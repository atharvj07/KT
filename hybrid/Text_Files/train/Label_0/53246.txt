import java.io.*;
import java.math.*;
import java.util.*;
import java.util.stream.*;

public class cfGlobal2H {

	static final int P = 998244353;
	static final int INV2 = (P + 1) / 2;

	void fwhtJust(int[] a) {
		int n = a.length;
		for (int s = 1; s < n; s <<= 1) {
			for (int i = 0; i < n; i += s << 1) {
				for (int j = i; j < i + s; j++) {
					int k = j + s;

					int v = a[j];
					int u = a[k];

					a[j] += u;
//					if (a[j] >= P) {
//						a[j] -= P;
//					}

					a[k] = v - u;
//					if (a[k] < 0) {
//						a[k] += P;
//					}

				}
			}
		}
	}
	
	void fwhtMod(int[] a) {
		int n = a.length;
		for (int s = 1; s < n; s <<= 1) {
			for (int i = 0; i < n; i += s << 1) {
				for (int j = i; j < i + s; j++) {
					int k = j + s;

					int v = a[j];
					int u = a[k];

					a[j] += u;
					if (a[j] >= P) {
						a[j] -= P;
					}

					a[k] = v - u;
					if (a[k] < 0) {
						a[k] += P;
					}

				}
			}
		}
	}

	void submit() {
		int n = nextInt();
		int k = nextInt();

		long x = nextInt();
		long y = nextInt();
		long z = nextInt();

		int[] m1 = new int[n];
		int[] m2 = new int[n];

		int xorAll = 0;

		for (int i = 0; i < n; i++) {
			int a = nextInt();
			int b = nextInt();
			int c = nextInt();
			xorAll ^= a;
			m1[i] = a ^ b;
			m2[i] = a ^ c;
		}

		int[] justB = new int[1 << k];
		int[] justC = new int[1 << k];
		int[] justXor = new int[1 << k];
		for (int i = 0; i < n; i++) {
			justB[m1[i]]++;
			justC[m2[i]]++;
			justXor[m1[i] ^ m2[i]]++;
		}

		fwhtJust(justB);
		fwhtJust(justC);
		fwhtJust(justXor);

		int[][] ps = { pows(f(x + y + z), n), pows(f(x - y + z), n),
				pows(f(x + y - z), n), pows(f(x - y - z), n) };

		int[] arr = new int[1 << k];
		for (int i = 0; i < 1 << k; i++) {
			int[] xs = solve(n, justB[i], justC[i], justXor[i]);
			arr[i] = 1;
			for (int j = 0; j < 4; j++) {
				arr[i] = (int) ((long) arr[i] * ps[j][xs[j]] % P);
			}
		}

		fwhtMod(arr);

		long inv2k = 1;
		for (int i = 0; i < k; i++) {
			inv2k = inv2k * INV2 % P;
		}

		for (int i = 0; i < arr.length; i++) {
			out.print(arr[i ^ xorAll] * inv2k % P + " ");
		}
		out.println();
	}

	int[] solve(int all, int yw, int zw, int yz) {
		yw = (all - yw) / 2;
		zw = (all - zw) / 2;
		yz = (all - yz) / 2;

		int yzw = (yw + zw + yz) / 2;
		int y = yzw - zw;
		int z = yzw - yw;
		int w = yzw - yz;

		int x = all - y - z - w;
		return new int[] { x, y, z, w };
	}

	int[] pows(int x, int b) {
		int[] ret = new int[b + 1];
		ret[0] = 1;
		for (int i = 1; i < ret.length; i++) {
			ret[i] = (int) ((long) ret[i - 1] * x % P);
		}
		return ret;
	}

	int f(long x) {
		return (int) Math.floorMod(x, P);
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

	cfGlobal2H() throws IOException {
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
		new cfGlobal2H();
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
