import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class E {
	BufferedReader in;
	StringTokenizer str;
	PrintWriter out;
	String SK;

	String next() throws IOException {
		while ((str == null) || (!str.hasMoreTokens())) {
			SK = in.readLine();
			if (SK == null)
				return null;
			str = new StringTokenizer(SK);
		}
		return str.nextToken();
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

	class Tower implements Comparable<Tower> {
		int col;
		long len;
		int num;

		public Tower(int col, int len, int num) {
			this.col = col;
			this.len = len;
			this.num = num;
		}

		@Override
		public int compareTo(Tower o) {
			if (col == o.col)
				return (int) Math.signum(o.len - len);
			return col - o.col;
		}

	}

	void solve() throws IOException {
		int n = nextInt();
		Tower[] a = new Tower[n];
		for (int i = 0; i < n; i++) {
			a[i] = new Tower(nextInt(), nextInt(), i);
		}
		Arrays.sort(a);
		long res = Integer.MIN_VALUE;
		int col1 = 0, col2 = 0, take1 = 0, take2 = 0;
		long[] resul = new long[n + 2];
		int[] col = new int[n + 2];
		Arrays.fill(resul, Integer.MIN_VALUE);
		for (int i = 0; i < n;) {
			int j;
			int num = 1;
			long cursum = 0;
			for (j = i; j < n && (a[j].col == a[i].col); j++, num++) {
				cursum = cursum + a[j].len;
				int curopt = num - 1;
				if (resul[num] > resul[curopt]) {
					curopt = num;
				}
				if (resul[num + 1] > resul[curopt]) {
					curopt = num + 1;
				}
				if (cursum + resul[curopt] > res) {
					res = cursum + resul[curopt];
					col1 = col[curopt];
					col2 = a[i].col;
					take1 = curopt;
					take2 = num;
				}
			}
			for (j = i, num = 1, cursum = 0; j < n && (a[j].col == a[i].col); j++, num++) {
				cursum = cursum + a[j].len;
				if (resul[num] < cursum) {
					resul[num] = cursum;
					col[num] = a[i].col;
				}
			}
			i = j;
		}
		int[] b = new int[take1 + take2];
		if (take1 < take2) {
			int t = take1;
			take1 = take2;
			take2 = t;
			t = col1;
			col1 = col2;
			col2 = t;
		}
		int t = 0;
		for (int i = 0; i < n; i++) {
			if (a[i].col == col1 && take1 > 0) {
				b[t] = a[i].num + 1;
				t += 2;
				take1--;
			}
		}
		t = 1;
		for (int i = 0; i < n; i++) {
			if (a[i].col == col2 && take2 > 0) {
				b[t] = a[i].num + 1;
				t += 2;
				take2--;
			}
		}
		out.println(res);
		out.println(b.length);
		for (int i = 0; i < b.length; i++) {
			out.print(b[i] + " ");
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

}