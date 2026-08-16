import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.NoSuchElementException;

public class Main {
	public static void main(String[] args) {
		new Main().run();
	}

	@SuppressWarnings("unchecked")
	int solve(int N, int[][] cap, int s, int t) {
		int tot = 0;
		int[][] flow = new int[N][N];
		while (true) {
			int[] pre = new int[N];
			Arrays.fill(pre, -1);
			ArrayDeque<Integer> que = new ArrayDeque();
			que.add(s);
			while (!que.isEmpty()) {
				int cur = que.pollFirst();
				for (int dst = 0; dst < N; ++dst) {
					if (res(cur, dst, flow, cap) <= 0) {
						continue;
					}
					if (dst == s || pre[dst] != -1)
						continue;
					pre[dst] = cur;
					que.addLast(dst);
				}
			}
			if (pre[t] == -1) {
				break;
			}
			int inc = Integer.MAX_VALUE / 3;
			for (int i = t; pre[i] != -1; i = pre[i]) {
				inc = Math.min(inc, res(pre[i], i, flow, cap));
			}
			for (int i = t; pre[i] != -1; i = pre[i]) {
				flow[pre[i]][i] += inc;
				flow[i][pre[i]] -= inc;
			}
			tot += inc;
		}
		return tot;
	}

	void run() {
		Scanner sc = new Scanner();
		int N = sc.nextInt();
		int A = sc.nextInt();
		int B = sc.nextInt();
		int[] a = new int[N];
		int[] b = new int[N];
		int[] c = new int[N];
		int ans = 0;
		boolean[] used = new boolean[N];
		for (int i = 0; i < N; ++i) {
			a[i] = sc.nextInt();
			b[i] = sc.nextInt();
			c[i] = a[i] - b[i];
			if (Math.abs(c[i]) <= A || (B <= Math.abs(c[i]) && Math.abs(c[i]) <= 2 * A)) {
				++ans;
				used[i] = true;
			}
		}
		int[][] cap = new int[N + 2][N + 2];
		for (int i = 0; i < N; ++i) {
			for (int j = i + 1; j < N; ++j) {
				if (used[i] || used[j])
					continue;
				if (Math.abs(c[i] + c[j]) <= A || (B <= Math.abs(c[i] + c[j]) && Math.abs(c[i] + c[j]) <= 2 * A)) {
					cap[i][j] = 1;
					cap[j][i] = 1;
				}
			}
		}
		for (int i = 0; i < N; ++i) {
			if (used[i])
				continue;
			if (c[i] > 0) {
				cap[N][i] = 1;
			} else {
				cap[i][N + 1] = 1;
			}
		}
		ans += solve(N + 2, cap, N, N + 1);
		System.out.println(ans);
	}

	//src->dstにあとどれだけ流せるか。
	int res(int src, int dst, int[][] flow, int[][] cap) {
		return cap[src][dst] - flow[src][dst];
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

