
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.BitSet;
import java.util.Locale;
import java.util.NoSuchElementException;

public class Main {

	public static void main(String[] args) {
		new Main();
	}

	public Main() {
		FastIO io = new FastIO();
		/*
		 * 考察
		 * 連続してるなら使えばいいじゃない
		 * 自分の右側と自分の左側に、自分より弱い人が勝ち残れれば2戦で勝てる
		 * よってこれが可能かだけ考えれば良い
		 * dpl[i][j]は区間[i, j]についてiが優勝する
		 * dpr[i][j]は区間[i, j]についてjが優勝する
		 * これで遷移を組んでみる
		 * まず自明にdpl[i][i]=dpr[i][i]=true、これが初期値
		 * で、次に遷移
		 * ・dpl[i][j] = or[k = i + 1, j](A[i][k] & dpr[i + 1][k] & dpl[k][j])
		 * これはあるkについて、iがkに勝てるときにこの対象が生き残ってくれればいいわけで
		 * それは[i + 1, k]でkが優勝し、[k, j]でkが優勝しているなら[i + 1, j]でkが優勝できるということ
		 * 後はこのkにiが勝って終わり！
		 * 同様に次の遷移も言える
		 * ・dpr[i][j] = or[k = i, j - 1](A[j][k] & dpr[i][k] & dpl[k][j - 1])
		 * これはあるkについて、[i, k]でkが優勝し[k, j - 1]でkが優勝しているという場合
		 * この場合は、[i, j-1]でkが優勝してるので、あとはこのkにjが勝って終わり！
		 * 後は答えに関しては、全区間について見て優勝してれば終わり
		 * さて、これはどう計算できるか？
		 * 区間DPなので、j-iの値を少しずつ大きくしていけば良い
		 * 見れば分かるように区間を1個以上縮めた奴から導出してるからね、そりゃそう
		 * これはO(N^3)だがまぁうん、BitSet高速化を考えていく
		 * 計算式について、どれもindexが連続しているなら一気に計算できるので考える
		 * キャッシュ連続性も考えると、最後にkが持ち込まれるのが理想
		 * dpl[l][r]は[l, r]においてrが勝つ確率
		 * dpr[r][l]は[l, r]においてlが勝つ確率
		 * とする
		 * dpl[l][r] = A[r][k] & dpl[l][k] & dpr[r - 1][k](k=[l, r))という式に変形できる
		 * dpr[r][l] = A[l][k] & dpl[l+1][k] & dpr[r][k](k=(l, r])となり、これで無事に解けた
		 * 勿論答えはdpl[0][i] & dpr[N-1][i]なので
		 *
		 */
		int N = io.nextInt();
		BitSet[] A = new BitSet[N];
		for (int i = 0;i < N;++ i) A[i] = new BitSet();
		for (int i = 1;i < N;++ i) {
			char[] s = io.next().toCharArray();
			for (int j = 0;j < i;++ j) {
				 A[i].set(j, s[j] == '1');
				 A[j].set(i, !A[i].get(j));
			}
		}
		BitSet[] dpl = new BitSet[N], dpr = new BitSet[N];
		for (int i = 0;i < N;++ i) {
			dpl[i] = new BitSet(N);
			dpl[i].set(i);
			dpr[i] = new BitSet(N);
			dpr[i].set(i);
		}
		for (int i = 1;i < N;++ i) {
			for (int r = i;r < N;++ r) {
				int l = r - i;
				BitSet tmp = A[r].get(0, N);
				tmp.and(dpl[l]);
				tmp.and(dpr[r - 1]);
				dpl[l].set(r, !tmp.get(l, r).isEmpty());
				tmp = A[l].get(0, N);
				tmp.and(dpl[l + 1]);
				tmp.and(dpr[r]);
				dpr[r].set(l, !tmp.get(l + 1, r + 1).isEmpty());
			}
		}
		int ans = 0;
		for (int i = 0;i < N;++ i) if (dpl[0].get(i) && dpr[N - 1].get(i)) ++ ans; // [0, N)でiが勝ったなら勝ち
		io.print(ans);
		io.flush();
	}

	public class FastIO {
		private final InputStream in = System.in;
		private final byte[] buffer = new byte[1024];
		private int read = 0;
		private int length = 0;
		public final PrintWriter out = new PrintWriter(System.out, false);
		public final PrintWriter err = new PrintWriter(System.err, false);

		private boolean hasNextByte() {
			if (read < length) return true;
			else {
				try {
					read = 0;
					length = in.read(buffer);
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return length > 0;
		}

		private int readByte() {
			return hasNextByte() ? buffer[read++] : -1;
		}

		private boolean isPrintableChar(int c) {
			return 33 <= c && c <= 126;
		}

		private boolean isNumber(int c) {
			return '0' <= c && c <= '9';
		}

		public boolean hasNext() {
			while (hasNextByte() && !isPrintableChar(buffer[read])) read++;
			return hasNextByte();
		}

		public char nextChar() {
			if (!hasNextByte())  throw new NoSuchElementException();
			return (char)readByte();
		}

		public String next() {
			if (!hasNext()) throw new NoSuchElementException();
			StringBuilder sb = new StringBuilder();
			int b;
			while (isPrintableChar(b = readByte())) sb.appendCodePoint(b);
			return sb.toString();
		}

		public long nextLong() {
			if (!hasNext()) throw new NoSuchElementException();
			long n = 0;
			boolean minus = false;
			int b = readByte();
			if (b == '-') {
				minus = true;
				b = readByte();
			}
			if (!isNumber(b)) throw new NumberFormatException();
			while (true) {
				if (isNumber(b)) {
					n *= 10;
					n += b - '0';
				} else if (b == -1 || !isPrintableChar(b)) return minus ? -n : n;
				else throw new NumberFormatException();
				b = readByte();
			}
		}

		public int nextInt() {
			long nl = nextLong();
			if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
			return (int) nl;
		}

		public double nextDouble() {
			return Double.parseDouble(next());
		}

		public int[] nextInt(int width) {
			int[] ret = new int[width];
			for (int i = 0;i < width;++ i) ret[i] = nextInt();
			return ret;
		}

		public long[] nextLong(int width) {
			long[] ret = new long[width];
			for (int i = 0;i < width;++ i) ret[i] = nextLong();
			return ret;
		}

		public int[][] nextInt(int width, int height) {
			int[][] ret = new int[height][width];
			for (int i = 0, j;i < height;++ i) for (j = 0;j < width;++ j) ret[i][j] = nextInt();
			return ret;
		}

		public long[][] nextLong(int width, int height) {
			long[][] ret = new long[height][width];
			for (int i = 0, j;i < height;++ i) for (j = 0;j < width;++ j) ret[j][i] = nextLong();
			return ret;
		}

		public boolean[] nextBoolean(char T) {
			char[] s = next().toCharArray();
			boolean[] ret = new boolean[s.length];
			for (int i = 0;i < ret.length;++ i) ret[i] = s[i] == T;
			return ret;
		}

		@Override
		protected void finalize() throws Throwable {
			try {
				super.finalize();
			} finally {
				in.close();
				out.close();
				err.close();
			}
		}

		public void print(boolean b) {
			out.print(b);
		}

		public void print(char c) {
			out.print(c);
		}

		public void print(char[] s) {
			out.print(s);
		}

		public void print(double d) {
			out.print(d);
		}

		public void print(float f) {
			out.print(f);
		}

		public void print(int i) {
			out.print(i);
		}

		public void print(long l) {
			out.print(l);
		}

		public void print(Object obj) {
			out.print(obj);
		}

		public void print(String s) {
			out.print(s);
		}

		public void printf(String format, Object... args) {
			out.printf(format, args);
		}

		public void printf(Locale l, String format, Object... args) {
			out.printf(l, format, args);
		}

		public void println() {
			out.println();
		}

		public void println(boolean b) {
			out.println(b);
		}

		public void println(char c) {
			out.println(c);
		}

		public void println(char[] s) {
			out.println(s);
		}

		public void println(double d) {
			out.println(d);
		}

		public void println(float f) {
			out.println(f);
		}

		public void println(int i) {
			out.println(i);
		}

		public void println(long l) {
			out.println(l);
		}

		public void println(Object obj) {
			out.println(obj);
		}

		public void println(String s) {
			out.println(s);
		}

		public void flush() {
			out.flush();
			err.flush();
		}
	}
}
