import java.io.*;
import java.util.*;

public class E {

	void solve() throws IOException {
		int n = nextInt();
		int q = nextInt();
		long[] a = new long[n];
		for (int i = 0; i < n; i++) {
			a[i] = nextLong();
		}
		long[] sum = new long[n + 1];
		for (int i = n - 1; i >= 0; i--) {
			sum[i] = a[i] + sum[i + 1];
		}
		for (int it = 0; it < q; it++) {
			int[] res = new int[n];
			long[] last = new long[n];
			long b = nextLong();
			int lastIndex = n;
			for (int i = n - 1; i >= 0; i--) {
				while (sum[i] - sum[lastIndex] > b) {
					lastIndex--;
				}
				if (lastIndex == n) {
					res[i] = 1;
					last[i] = sum[i];
				} else {
					res[i] = res[lastIndex]+1;
					last[i] = last[lastIndex];
				}
			}
			int result = Integer.MAX_VALUE / 2;
			long summ = 0;
			for (int i = 0; i < n; i++) {
				summ += a[i];
				if (summ > b) {
					break;
				}
				if (i == n - 1) {
					result = 1;
					break;
				}
				if (summ + last[i + 1] <= b) {
					result = Math.min(result, res[i + 1]);
				} else {
					result = Math.min(result, res[i + 1]+1);
				}
			}
			out.println(result);
		}
	}

	void run() throws IOException {
		in = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		solve();
		out.close();
	}

	public static void main(String[] args) throws IOException {
		new E().run();
	}

	BufferedReader in;
	PrintWriter out;
	StringTokenizer st;

	String next() throws IOException {
		while (st == null || !st.hasMoreTokens()) {
			String temp = in.readLine();
			if (temp == null) {
				return null;
			}
			st = new StringTokenizer(temp);
		}
		return st.nextToken();
	}

	int nextInt() throws IOException {
		return Integer.parseInt(next());
	}

	double nextDouble() throws IOException {
		return Double.parseDouble(next());
	}

	long nextLong() throws IOException {
		return Long.parseLong(next());
	}

}
