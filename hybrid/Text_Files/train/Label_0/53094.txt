import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.System.arraycopy;
import static java.lang.System.exit;
import static java.util.Arrays.copyOf;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {

	static class IntList {

		int data[] = new int[3];
		int size = 0;

		boolean isEmpty() {
			return size == 0;
		}

		int size() {
			return size;
		}

		int get(int index) {
			if (index < 0 || index >= size) {
				throw new IndexOutOfBoundsException();
			}
			return data[index];
		}

		void clear() {
			size = 0;
		}

		void set(int index, int value) {
			if (index < 0 || index >= size) {
				throw new IndexOutOfBoundsException();
			}
			data[index] = value;
		}

		void expand() {
			if (size >= data.length) {
				data = copyOf(data, (data.length << 1) + 1);
			}
		}

		void insert(int index, int value) {
			if (index < 0 || index > size) {
				throw new IndexOutOfBoundsException();
			}
			expand();
			arraycopy(data, index, data, index + 1, size++ - index);
			data[index] = value;
		}

		int delete(int index) {
			if (index < 0 || index >= size) {
				throw new IndexOutOfBoundsException();
			}
			int value = data[index];
			arraycopy(data, index + 1, data, index, --size - index);
			return value;
		}

		void push(int value) {
			expand();
			data[size++] = value;
		}

		int pop() {
			if (size == 0) {
				throw new NoSuchElementException();
			}
			return data[--size];
		}

		void unshift(int value) {
			expand();
			arraycopy(data, 0, data, 1, size++);
			data[0] = value;
		}

		int shift() {
			if (size == 0) {
				throw new NoSuchElementException();
			}
			int value = data[0];
			arraycopy(data, 1, data, 0, --size);
			return value;
		}
	}

	static final int MOD = 998244353;
	static final int MUL = 716070898;
	static final int HALF = 499122177;

	static int add(int a, int b) {
		int res = a + b;
		return res >= MOD ? res - MOD : res;
	}

	static int sub(int a, int b) {
		int res = a - b;
		return res < 0 ? res + MOD : res;
	}

	static int mul(int a, int b) {
		int res = (int) ((long) a * b % MOD);
		return res < 0 ? res + MOD : res;
	}

	static void hadamard(int n, int a[]) {
		for (int i = 0; i < n; i++) {
			for (int j = 1 << i; j < 1 << n; j = (j + 1) | (1 << i)) {
				int x = a[j - (1 << i)], y = a[j];
				a[j - (1 << i)] = add(x, y);
				a[j] = sub(x, y);
			}
		}
	}

	static int[] readGraph(int n) throws IOException {
		int m = scanInt();
		IntList edges[] = new IntList[n];
		for (int i = 0; i < n; i++) {
			edges[i] = new IntList();
		}
		for (int i = 0; i < m; i++) {
			int a = scanInt() - 1, b = scanInt() - 1;
			if (a > b) {
				int t = a;
				a = b;
				b = t;
			}
			if (a != b) {
				edges[a].push(b);
			}
		}
		int gr[] = new int[n];
		boolean mex[] = new boolean[n];
		for (int i = n - 1; i >= 0; i--) {
			for (int j = 0; j < edges[i].size; j++) {
				mex[gr[edges[i].data[j]]] = true;
			}
			for (int j = 0;; j++) {
				if (!mex[j]) {
					gr[i] = j;
					break;
				}
			}
			for (int j = 0; j < edges[i].size; j++) {
				mex[gr[edges[i].data[j]]] = false;
			}
		}
		int p2 = Integer.highestOneBit(n - 1) << 1;
		int cnt[] = new int[p2];
		for (int i = 0, v = MUL; i < n; i++, v = mul(v, MUL)) {
			cnt[gr[i]] = add(cnt[gr[i]], v);
		}
		hadamard(Integer.numberOfTrailingZeros(p2), cnt);
		return cnt;
	}

	static void solve() throws Exception {
		int n = scanInt();
		int a[] = readGraph(n), b[] = readGraph(n), c[] = readGraph(n);
		int mul = 1;
		for (int i = Integer.numberOfTrailingZeros(a.length); i > 0; i--) {
			mul = mul(mul, HALF);
		}
		int ans = 0;
		for (int i = 0; i < a.length; i++) {
			ans = add(ans, mul(mul(mul(a[i], b[i]), c[i]), mul));
		}
		out.print(ans);
	}

	static int scanInt() throws IOException {
		return parseInt(scanString());
	}

	static long scanLong() throws IOException {
		return parseLong(scanString());
	}

	static String scanString() throws IOException {
		while (tok == null || !tok.hasMoreTokens()) {
			tok = new StringTokenizer(in.readLine());
		}
		return tok.nextToken();
	}

	static BufferedReader in;
	static PrintWriter out;
	static StringTokenizer tok;

	public static void main(String[] args) {
		try {
			in = new BufferedReader(new InputStreamReader(System.in));
			out = new PrintWriter(System.out);
			solve();
			in.close();
			out.close();
		} catch (Throwable e) {
			e.printStackTrace();
			exit(1);
		}
	}
}