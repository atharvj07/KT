import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.concurrent.ConcurrentHashMap;

class Main {

	public static void main(String[] args) {
		new Main().run();
	}

	// 2^18=2.6*1e5

	// i | j = K のときの Ai + Aj のmaxを求めたい
	void run() {
		Scanner sc = new Scanner();
		int N = sc.nextInt();
		long[] A = new long[1 << N];
		long[] ans = new long[(1 << N)];
		long[][][] max2 = new long[1 << N][2][2];
		for (int i = 0; i < 1 << N; ++i) {
			max2[i][0][0] = -Integer.MAX_VALUE / 3;
			max2[i][0][1] = -1;
			max2[i][1][0] = -Long.MAX_VALUE / 3;
			max2[i][1][1] = -1;
		}
		for (int i = 0; i < 1 << N; ++i) {
			A[i] = sc.nextLong();
			max2add(max2, i, A[i], i);
			// for (int j = 0; j < N; ++j) {
			// if ((i & (1 << j)) > 0)
			// continue;
			// max2add(max2, i | (1 << j), A[i]);
			// }
		}
		for (int i = 0; i < 1 << N; ++i) {
			for (int j = 0; j < N; ++j) {
				if ((i & (1 << j)) > 0)
					continue;
				max2add(max2, i | (1 << j), max2[i][0][0], (int) max2[i][0][1]);
				max2add(max2, i | (1 << j), max2[i][1][0], (int) max2[i][1][1]);
			}
		}
		for (int i = 1; i < (1 << N); ++i) {
			ans[i] = max2[i][0][0] + max2[i][1][0];
			ans[i] = Math.max(ans[i], (i == 0 ? 0 : ans[i - 1]));
		}
		PrintWriter pw = new PrintWriter(System.out);
		for (int i = 1; i < ans.length; ++i) {
			pw.println(ans[i]);
		}
		pw.close();
	}

	void max2add(long[][][] max2, int go_idx, long a, int from_idx) {
		if (from_idx == max2[go_idx][0][1] || from_idx == max2[go_idx][1][1])
			return;
		if (max2[go_idx][0][0] <= a) {
			max2[go_idx][1][0] = max2[go_idx][0][0];
			max2[go_idx][1][1] = max2[go_idx][0][1];
			max2[go_idx][0][0] = a;
			max2[go_idx][0][1] = from_idx;
		} else if (max2[go_idx][1][0] <= a) {
			max2[go_idx][1][0] = a;
			max2[go_idx][1][1] = from_idx;
		}
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

		private void skipUnprintable() {
			while (hasNextByte() && !isPrintableChar(buffer[ptr]))
				ptr++;
		}

		public boolean hasNext() {
			skipUnprintable();
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

		int nextInt() {
			return (int) nextLong();
		}
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}