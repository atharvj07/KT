import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.NoSuchElementException;

public class Main implements Runnable {
	public static void main(String[] args) {
		new Thread(null, new Main(), "", Runtime.getRuntime().maxMemory()).start();
	}

	class DJSet {
		int n;
		int[] upper;
		int[] to;

		public DJSet(int n_) {
			n = n_;
			upper = new int[n];
			Arrays.fill(upper, -1);
		}

		int root(int x) {
			return upper[x] < 0 ? x : (upper[x] = root(upper[x]));
		}

		boolean equiv(int x, int y) {
			return root(x) == root(y);
		}

		void setUnion(int x, int y) {
			if (equiv(x, y))
				return;
			x = root(x);
			y = root(y);
			if (x < y) {
				x ^= y;
				y ^= x;
				x ^= y;
			}
			//x>y
			while (x > y) {
				upper[y] = root(y + 1);
				y = root(y + 1);
			}
		}
	}

	public void run() {
		Scanner sc = new Scanner();
		int N = sc.nextInt();
		int M = sc.nextInt();
		int Q = sc.nextInt();
		int[][] query = new int[M + Q][];
		for (int i = 0; i < M; ++i) {
			int d = sc.nextInt();
			int a = sc.nextInt() - 1;
			int b = sc.nextInt() - 1;
			query[i] = new int[] { d, 1, a, b };
		}
		boolean[] ans = new boolean[Q];
		for (int i = 0; i < Q; ++i) {
			int e = sc.nextInt();
			int s = sc.nextInt() - 1;
			int t = sc.nextInt() - 1;
			query[i + M] = new int[] { e, -1, s, t, i };
		}
		Arrays.sort(query, new Comparator<int[]>() {
			@Override
			public int compare(int[] arg0, int[] arg1) {
				if (arg0[0] != arg1[0]) {
					return Integer.compare(arg0[0], arg1[0]);
				} else {
					return Integer.compare(arg0[1], arg1[1]);
				}
			}
		});
		DJSet ds = new DJSet(N);
		for (int i = 0; i < query.length; ++i) {
			if (query[i][1] == 1) {
				ds.setUnion(query[i][2], query[i][3]);
			} else {
				ans[query[i][4]] = ds.equiv(query[i][2], query[i][3]) | query[i][2] >= query[i][3];
			}
		}
		PrintWriter pw = new PrintWriter(System.out);
		for (int i = 0; i < ans.length; ++i) {
			pw.println(ans[i] ? "Yes" : "No");
		}
		pw.close();
	}

	class Scanner {
		private final InputStream in = System.in;
		private final byte[] buffer = new byte[1024];
		private int ptr = 0;
		private int buflen = 0;

		private boolean hasNextByte() {
			if (ptr < buflen) {
				return true;
			} else {
				ptr = 0;
				try {
					buflen = in.read(buffer);
				} catch (IOException e) {
					e.printStackTrace();
				}
				if (buflen <= 0) {
					return false;
				}
			}
			return true;
		}

		private int readByte() {
			if (hasNextByte())
				return buffer[ptr++];
			else
				return -1;
		}

		private boolean isPrintableChar(int c) {
			return 33 <= c && c <= 126;
		}

		public boolean hasNext() {
			while (hasNextByte() && !isPrintableChar(buffer[ptr]))
				ptr++;
			return hasNextByte();
		}

		public String next() {
			if (!hasNext())
				throw new NoSuchElementException();
			StringBuilder sb = new StringBuilder();
			int b = readByte();
			while (isPrintableChar(b)) {
				sb.appendCodePoint(b);
				b = readByte();
			}
			return sb.toString();
		}

		public long nextLong() {
			if (!hasNext())
				throw new NoSuchElementException();
			long n = 0;
			boolean minus = false;
			int b = readByte();
			if (b == '-') {
				minus = true;
				b = readByte();
			}
			if (b < '0' || '9' < b) {
				throw new NumberFormatException();
			}
			while (true) {
				if ('0' <= b && b <= '9') {
					n *= 10;
					n += b - '0';
				} else if (b == -1 || !isPrintableChar(b)) {
					return minus ? -n : n;
				} else {
					throw new NumberFormatException();
				}
				b = readByte();
			}
		}

		public int nextInt() {
			long nl = nextLong();
			if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE)
				throw new NumberFormatException();
			return (int) nl;
		}

		public double nextDouble() {
			return Double.parseDouble(next());
		}
	}

	static void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}

