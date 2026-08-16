import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.InputMismatchException;

/**
 * http://codeforces.com/contest/276/problem/E
 * 
 * @author sultan.of.swing
 *
 */

public class TaskE {

	public FasterScanner mFScanner;
	public PrintWriter mOut;
	private int N, Q;
	private ArrayList<Integer> mAdj[];
	private int mNodeGroup[];
	private int mSize[];
	private int mLevel[];
	private int mBit[][];

	public TaskE() {
		mFScanner = new FasterScanner();
		mOut = new PrintWriter(System.out);
	}

	private void addBit(int idx, int val, int bitIndex, int MAX) {

		while (idx <= MAX) {
			mBit[bitIndex][idx] += val;
			idx += (idx & -idx);
		}
	}

	private int queryBit(int idx, int bitIndex, int MAX) {
		int sum = 0;

		while (idx > 0) {
			sum += mBit[bitIndex][idx];
			idx -= (idx & -idx);
		}

		return sum;
	}

	public void solve() {
		int u, v;
		int i;
		int res;
		int rootBitIndex;
		int bitIndex;
		int rootSum = 0;
		int type;
		int num;
		int dist;

		N = mFScanner.nextInt();
		Q = mFScanner.nextInt();

		mAdj = new ArrayList[N];
		mNodeGroup = new int[N];
		mLevel = new int[N];

		for (i = 0; i < N; i++) {
			mAdj[i] = new ArrayList<>();
		}

		for (i = 0; i < N - 1; i++) {
			u = mFScanner.nextInt() - 1;
			v = mFScanner.nextInt() - 1;
			mAdj[u].add(v);
			mAdj[v].add(u);
		}

		mSize = new int[mAdj[0].size()];
		mBit = new int[mAdj[0].size() + 1][];

		for (i = 0; i < mAdj[0].size(); i++)
			dfs(mAdj[0].get(i), 0, i, 1);

		for (i = 0; i < mSize.length; i++)
			mBit[i] = new int[mSize[i] + 1];

		mBit[i] = new int[N + 1];
		rootBitIndex = i;

		for (i = 0; i < Q; i++) {
			type = mFScanner.nextInt();
			v = mFScanner.nextInt() - 1;

			if (type == 0) {
				num = mFScanner.nextInt();
				dist = mFScanner.nextInt();

				if (v == 0) {
					rootSum += num;
					addBit(1, num, rootBitIndex, N);
					addBit(dist + 1, -num, rootBitIndex, N);
					continue;
				}

				if (dist >= mLevel[v]) {
					rootSum += num;
					int left = dist - mLevel[v];
					bitIndex = mNodeGroup[v];
					addBit(1, num, rootBitIndex, N);
					addBit(left + 1, -num, rootBitIndex, N);
					addBit(left + 1, num, bitIndex, mSize[bitIndex]);
					addBit(dist + mLevel[v] + 1, -num, bitIndex,
							mSize[bitIndex]);
				} else {
					bitIndex = mNodeGroup[v];
					addBit(mLevel[v] - dist, num, bitIndex, mSize[bitIndex]);
					addBit(mLevel[v] + dist + 1, -num, bitIndex,
							mSize[bitIndex]);
				}
			} else {
				if (v == 0)
					res = rootSum;
				else {
					bitIndex = mNodeGroup[v];
					res = queryBit(mLevel[v], bitIndex, mSize[bitIndex])
							+ queryBit(mLevel[v], rootBitIndex, N);
				}
				mOut.println(res);
			}

		}

	}

	public void dfs(int node, int parent, int num, int level) {

		mSize[num]++;
		mLevel[node] = level;
		mNodeGroup[node] = num;

		for (int u : mAdj[node]) {
			if (u != parent)
				dfs(u, node, num, level + 1);
		}

	}

	public void flush() {
		mOut.flush();
	}

	public void close() {
		mOut.close();
	}

	public static void main(String[] args) {
		TaskE mSol = new TaskE();
		mSol.solve();
		mSol.flush();
		mSol.close();
	}

	class FasterScanner {
		private InputStream mIs;
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;

		public FasterScanner() {
			this(System.in);
		}

		public FasterScanner(InputStream is) {
			mIs = is;
		}

		public int read() {
			if (numChars == -1)
				throw new InputMismatchException();
			if (curChar >= numChars) {
				curChar = 0;
				try {
					numChars = mIs.read(buf);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (numChars <= 0)
					return -1;
			}
			return buf[curChar++];
		}

		public String nextLine() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isEndOfLine(c));
			return res.toString();
		}

		public String nextString() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isSpaceChar(c));
			return res.toString();
		}

		public long nextLong() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			long res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public int nextInt() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			int res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}

		public double nextDouble() {
			Double next;
			next = Double.parseDouble(nextString());
			return next;
		}

		public boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		public boolean isEndOfLine(int c) {
			return c == '\n' || c == '\r' || c == -1;
		}

		public char[] nextCharArray(int N) {
			int i;
			char[] array;
			String str;

			array = new char[N];

			i = 0;

			str = nextLine();

			for (i = 0; i < N && i < str.length(); i++) {
				array[i] = str.charAt(i);
			}

			return array;
		}

		public char[][] nextChar2DArray(int M, int N) {
			int i;
			char[][] array;

			array = new char[M][N];

			i = 0;

			for (i = 0; i < M; i++) {
				array[i] = nextCharArray(N);
			}

			return array;
		}

		public int[] nextIntArray(int N) {
			int i;
			int[] array;

			array = new int[N];

			i = 0;

			for (i = 0; i < N; i++) {
				array[i] = nextInt();
			}

			return array;
		}

		public int[][] nextInt2DArray(int M, int N) {
			int i;
			int[][] array;

			array = new int[M][N];

			i = 0;

			for (i = 0; i < M; i++) {
				array[i] = nextIntArray(N);
			}

			return array;
		}

		public long[] nextLongArray(int N) {
			int i;
			long[] array;

			array = new long[N];

			i = 0;

			for (i = 0; i < N; i++) {
				array[i] = nextLong();
			}

			return array;
		}

		public long[][] nextLong2DArray(int M, int N) {
			int i;
			long[][] array;

			array = new long[M][N];

			i = 0;

			for (i = 0; i < M; i++) {
				array[i] = nextLongArray(N);
			}

			return array;
		}

		public double[] nextDoubleArray(int N) {
			int i;
			double[] array;

			array = new double[N];

			for (i = 0; i < N; i++) {
				array[i] = nextDouble();
			}

			return array;
		}

		public double[][] nextDouble2DArray(int M, int N) {
			int i;
			double[][] array;

			array = new double[M][N];

			for (i = 0; i < M; i++) {
				array[i] = nextDoubleArray(N);
			}

			return array;
		}

	}
}