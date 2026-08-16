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

	static IntList ans;

	static void go(int pos, int mask) {
		ans.push(pos + 1);
		ans.push(0);
		if ((mask & (1 << pos)) != 0) {
			ans.push(pos + 1);
			ans.push(1);
			ans.push(pos);
			ans.push(1);
			if (mask != 1 << pos) {
				int submask = mask ^ (1 << pos);
				ans.push(pos);
				ans.push(0);
				ans.push(pos + 1);
				ans.push(0);
				go(pos + 1, submask);
				ans.push(pos);
				ans.push(0);
				ans.push(pos);
				ans.push(1);
				ans.push(pos + 1);
				ans.push(1);
				ans.push(pos + 1);
				ans.push(0);
				goInv(pos + 1, submask);
			}
		} else {
			go(pos + 1, mask);
		}
		ans.push(pos);
		ans.push(0);
	}

	static void goInv(int pos, int mask) {
		if ((mask & (1 << pos)) != 0) {
			if (mask != 1 << pos) {
				int submask = mask ^ (1 << pos);
				ans.push(pos + 1);
				ans.push(0);
				go(pos + 1, submask);
				ans.push(pos + 1);
				ans.push(1);
				ans.push(pos);
				ans.push(1);
				ans.push(pos);
				ans.push(0);
				ans.push(pos + 1);
				ans.push(0);
				goInv(pos + 1, submask);
				ans.push(pos);
				ans.push(0);
			}
			ans.push(pos);
			ans.push(1);
			ans.push(pos + 1);
			ans.push(1);
			ans.push(pos + 1);
			ans.push(0);
		} else {
			ans.push(pos + 1);
			ans.push(0);
			goInv(pos + 1, mask);
		}
		ans.push(pos);
		ans.push(0);
	}

	static void solve() throws Exception {
		int n = scanInt();
		String a = scanString();
		ans = new IntList();
		ans.push(0);
		ans.push(0);
		for (int i = 0; i < 1 << n; i++) {
			if (a.charAt(i) == '0') {
				boolean sm = true;
				for (int j = 0; j < n; j++) {
					if ((i & (1 << j)) == 0) {
						if (a.charAt(i | (1 << j)) != '0') {
							out.print("Impossible");
							return;
						}
					} else {
						if (a.charAt(i ^ (1 << j)) == '0') {
							sm = false;
						}
					}
				}
				if (sm) {
					go(0, i);
				}
			}
		}
		out.println("Possible");
		out.println(ans.size / 2 - 1);
		for (int i = 0; i < ans.size; i += 2) {
			out.println(ans.data[i] + " " + ans.data[i + 1]);
		}
//		if (ans.data[0] != 0 || ans.data[1] != 0 || ans.data[ans.size - 2] != 0 || ans.data[ans.size - 1] != 0) {
//			throw new AssertionError();
//		}
//		for (int i = 0; i < ans.size - 2; i += 2) {
//			if (abs(ans.data[i] - ans.data[i + 2]) + abs(ans.data[i + 1] - ans.data[i + 3]) != 1) {
//				throw new AssertionError();
//			}
//		}
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