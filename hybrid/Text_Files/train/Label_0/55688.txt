public class Main implements Runnable {

	/** 確保するメモリの大きさ(単位: MB) */
	private static final long MEMORY = 56;

	public void solve(AtCoder.Input in, AtCoder.Output out, String[] args) {
		// write code here
		out.setAutoFlush(false);
		int N = in.nextInt(), Q = in.nextInt();
		long[] a = new long[N];
		for (int i = 0; i < N; ++i)
			a[i] = in.nextLong();
		AtCoder.LongFenwickTree bit = AtCoder.LongFenwickTree.create(a);
		for (int i = 0; i < Q; ++i) {
			if (in.nextInt() == 0) {
				int p = in.nextInt(), x = in.nextInt();
				bit.add(p, x);
			} else {
				int l = in.nextInt(), r = in.nextInt();
				out.println(bit.sum(l, r));
			}
		}
	}

	private final String[] args;

	public static void main(String[] args) {
		Thread.setDefaultUncaughtExceptionHandler((t, e) -> {
			e.printStackTrace();
			System.exit(1);
		});
		new Thread(null, new Main(args), "", MEMORY * 1048576L).start();
	}

	public Main(String[] args) {
		this.args = args;
	}

	@Override
	public void run() {
		try (AtCoder.Input in = new AtCoder.Input(System.in); AtCoder.Output out = new AtCoder.Output(System.out)) {
			solve(in, out, args);
			out.flush();
		} ;
	}
}

final class AtCoder {

	public static final class Input extends java.io.InputStream {

		private final java.io.InputStream in;
		private final byte[] buffer = new byte[1024];
		private int read = 0;
		private int length = 0;

		public Input(java.io.InputStream in) {
			this.in = in;
		}

		@Override
		public int available() {
			try {
				return in.available();
			} catch (java.io.IOException e) {
				e.printStackTrace();
			}
			return 0;
		}

		@Override
		public void close() {
			try {
				in.close();
				read = length = 0;
			} catch (java.io.IOException e) {
				e.printStackTrace();
			}
		}

		@Override
		public int read() {
			if (hasNextByte()) return nextByte();
			return 0;
		}

		private boolean hasNextByte() {
			if (read < length) return true;
			read = 0;
			try {
				length = in.read(buffer);
			} catch (java.io.IOException e) {
				e.printStackTrace();
			}
			return length > 0;
		}

		private static boolean isPrintableChar(byte c) {
			return 32 < c || c < 0;
		}

		private static boolean isNumber(int c) {
			return '0' <= c && c <= '9';
		}

		private boolean readNewLine() {
			if (hasNextByte()) {
				if (buffer[read] == '\r') {
					++read;
					if (hasNextByte() && buffer[read] == '\n') ++read;
					return true;
				}
				if (buffer[read] == '\n') {
					++read;
					return true;
				}
			}
			return false;
		}

		public boolean hasNext() {
			while (hasNextByte() && !isPrintableChar(buffer[read]))
				read++ ;
			return hasNextByte();
		}

		public boolean nextBoolean() {
			return Boolean.valueOf(next());
		}

		public byte nextByte() {
			if (hasNextByte()) return buffer[read++ ];
			throw new java.util.NoSuchElementException();
		}

		public short nextShort() {
			if (!hasNext()) throw new java.util.NoSuchElementException();
			short n = 0;
			try {
				byte b = nextByte();
				if (b == '-') {
					while (isNumber(b = nextByte()))
						n = (short)(n * 10 + '0' - b);
					return n;
				} else if (!isNumber(b)) throw new NumberFormatException();
				do
					n = (short)(n * 10 + b - '0');
				while (isNumber(b = nextByte()));
				return n;
			} catch (java.util.NoSuchElementException e) {
				return n;
			}
		}

		public int nextInt() {
			if (!hasNext()) throw new java.util.NoSuchElementException();
			int n = 0;
			try {
				byte b = nextByte();
				if (b == '-') {
					while (isNumber(b = nextByte()))
						n = n * 10 + '0' - b;
					return n;
				} else if (!isNumber(b)) throw new NumberFormatException();
				do
					n = n * 10 + b - '0';
				while (isNumber(b = nextByte()));
				return n;
			} catch (java.util.NoSuchElementException e) {
				return n;
			}
		}

		public long nextLong() {
			if (!hasNext()) throw new java.util.NoSuchElementException();
			long n = 0;
			try {
				byte b = nextByte();
				if (b == '-') {
					while (isNumber(b = nextByte()))
						n = n * 10 + '0' - b;
					return n;
				} else if (!isNumber(b)) throw new NumberFormatException();
				do
					n = n * 10 + b - '0';
				while (isNumber(b = nextByte()));
				return n;
			} catch (java.util.NoSuchElementException e) {
				return n;
			}
		}

		public float nextFloat() {
			return Float.parseFloat(next());
		}

		public double nextDouble() {
			return Double.parseDouble(next());
		}

		public char nextChar() {
			byte b = nextByte();
			if ((b & 0x80) == 0) return (char)b;
			if ((b & 0x20) == 0) return (char)((b & 0x1F) << 6 | (nextByte() & 0x3F));
			return (char)((b & 0xF) << 12 | (nextByte() & 0x3F) << 6 | (nextByte() & 0x3F));
		}

		public String next() {
			if (!hasNext()) throw new java.util.NoSuchElementException();
			StringBuilder sb = new StringBuilder();
			do
				sb.append(nextChar());
			while (hasNextByte() && isPrintableChar(buffer[read]));
			return sb.toString();
		}

		public String nextLine() {
			StringBuilder sb = new StringBuilder();
			while (!readNewLine())
				sb.append(nextChar());
			return sb.toString();
		}

	}

	public static final class Output extends java.io.OutputStream {

		private final java.io.OutputStream out;
		private final byte[] buffer = new byte[1 << 16];
		private int read = 0;
		private boolean autoFlush = true;
		private static final int READ_STRING_TO_BYTE_ARRAY;

		public Output(java.io.OutputStream out) {
			this.out = out;
		}

		public void setAutoFlush(boolean autoFlush) {
			this.autoFlush = autoFlush;
		}

		static {
			int flag = -1;
			try {
				String test = "test";
				java.lang.reflect.Field strValueField = test.getClass().getDeclaredField("value");
				strValueField.setAccessible(true);
				Object value = strValueField.get(test);
				strValueField.setAccessible(false);
				if (value instanceof byte[]) flag = 0;
				else flag = 1;
			} catch (Exception e) {}
			READ_STRING_TO_BYTE_ARRAY = flag;
		}

		@Override
		public void close() {
			try {
				flush();
				out.close();
			} catch (java.io.IOException e) {
				e.printStackTrace();
			}
		}

		@Override
		public void flush() {
			try {
				write();
				out.flush();
			} catch (java.io.IOException e) {
				e.printStackTrace();
			}
		}

		@Override
		public void write(byte[] b) {
			try {
				out.write(b);
			} catch (java.io.IOException e) {
				e.printStackTrace();
			}
		}

		@Override
		public void write(byte[] b, int off, int len) {
			try {
				out.write(b, off, len);
			} catch (java.io.IOException e) {
				e.printStackTrace();
			}
		}

		@Override
		public void write(int b) {
			try {
				out.write(b);
			} catch (java.io.IOException e) {
				e.printStackTrace();
			}
		}

		private void write() {
			write(buffer, 0, read);
			read = 0;
		}

		public void print(boolean b) {
			if (b) {
				print((byte)'t');
				print((byte)'r');
				print((byte)'u');
				print((byte)'e');
			} else {
				print((byte)'f');
				print((byte)'a');
				print((byte)'l');
				print((byte)'s');
				print((byte)'e');
			}
		}

		public void print(byte b) {
			if (read == buffer.length) write();
			buffer[read++ ] = b;
		}

		public void print(short s) {
			if (s < 0) {
				print((byte)'-');
				if (s == -32768) {
					print((byte)'3');
					print((byte)'2');
					print((byte)'7');
					print((byte)'6');
					print((byte)'8');
					return;
				}
				s = (short)-s;
			}
			if (s >= 100) {
				if (s >= 1000) {
					if (s >= 10000) {
						print((byte)(s / 10000 % 10 + '0'));
					}
					print((byte)(s / 1000 % 10 + '0'));
				}
				print((byte)(s / 100 % 10 + '0'));
				print((byte)(s / 10 % 10 + '0'));
			} else {
				if (s >= 10) print((byte)(s / 10 % 10 + '0'));
			}
			print((byte)(s % 10 + '0'));
		}

		public void print(int i) {
			if (i < 0) {
				print((byte)'-');
				if (i == -2147483648) {
					print((byte)'2');
					print((byte)'1');
					print((byte)'4');
					print((byte)'7');
					print((byte)'4');
					print((byte)'8');
					print((byte)'3');
					print((byte)'6');
					print((byte)'4');
					print((byte)'8');
					return;
				}
				i = -i;
			}
			if (i >= 1000000000) print((byte)(i / 1000000000 % 10 + '0'));
			if (i >= 100000000) print((byte)(i / 100000000 % 10 + '0'));
			if (i >= 10000000) print((byte)(i / 10000000 % 10 + '0'));
			if (i >= 1000000) print((byte)(i / 1000000 % 10 + '0'));
			if (i >= 100000) print((byte)(i / 100000 % 10 + '0'));
			if (i >= 10000) print((byte)(i / 10000 % 10 + '0'));
			if (i >= 1000) print((byte)(i / 1000 % 10 + '0'));
			if (i >= 100) print((byte)(i / 100 % 10 + '0'));
			if (i >= 10) print((byte)(i / 10 % 10 + '0'));
			print((byte)(i % 10 + '0'));
		}

		public void print(long l) {
			if (l < 0) {
				print((byte)'-');
				if (l == -9223372036854775808L) {
					print((byte)'9');
					print((byte)'2');
					print((byte)'2');
					print((byte)'3');
					print((byte)'3');
					print((byte)'7');
					print((byte)'2');
					print((byte)'0');
					print((byte)'3');
					print((byte)'6');
					print((byte)'8');
					print((byte)'5');
					print((byte)'4');
					print((byte)'7');
					print((byte)'7');
					print((byte)'5');
					print((byte)'8');
					print((byte)'0');
					print((byte)'8');
					return;
				}
				l = -l;
			}
			if (l >= 1000000000000000000L) print((byte)(l / 1000000000000000000L % 10 + '0'));
			if (l >= 100000000000000000L) print((byte)(l / 100000000000000000L % 10 + '0'));
			if (l >= 10000000000000000L) print((byte)(l / 10000000000000000L % 10 + '0'));
			if (l >= 1000000000000000L) print((byte)(l / 1000000000000000L % 10 + '0'));
			if (l >= 100000000000000L) print((byte)(l / 100000000000000L % 10 + '0'));
			if (l >= 10000000000000L) print((byte)(l / 10000000000000L % 10 + '0'));
			if (l >= 1000000000000L) print((byte)(l / 1000000000000L % 10 + '0'));
			if (l >= 100000000000L) print((byte)(l / 100000000000L % 10 + '0'));
			if (l >= 10000000000L) print((byte)(l / 10000000000L % 10 + '0'));
			if (l >= 1000000000L) print((byte)(l / 1000000000L % 10 + '0'));
			if (l >= 100000000L) print((byte)(l / 100000000L % 10 + '0'));
			if (l >= 10000000L) print((byte)(l / 10000000L % 10 + '0'));
			if (l >= 1000000L) print((byte)(l / 1000000L % 10 + '0'));
			if (l >= 100000L) print((byte)(l / 100000L % 10 + '0'));
			if (l >= 10000L) print((byte)(l / 10000L % 10 + '0'));
			if (l >= 1000L) print((byte)(l / 1000L % 10 + '0'));
			if (l >= 100L) print((byte)(l / 100L % 10 + '0'));
			if (l >= 10L) print((byte)(l / 10L % 10 + '0'));
			print((byte)(l % 10 + '0'));
		}

		public void print(float f) {
			print(Float.toString(f));
		}

		public void print(double d) {
			print(Double.toString(d));
		}

		public void print(double d, int n) {
			if (d < 0) {
				print((byte)'-');
				d = -d;
			}
			d += Math.pow(10, -n) / 2;
			long l = (long)d;
			print(l);
			print((byte)'.');
			d -= l;
			for (int i = 0; i < n; i++ ) {
				d *= 10;
				int in = (int)d;
				print((byte)(in + '0'));
				d -= in;
			}
		}

		public void print(char c) {
			if (c < 0x80) {
				print((byte)c);
			} else if (c < 0x07FF) {
				print((byte)(c >> 6 & 0x3F | 0x80));
				print((byte)(c & 0x3F | 0x80));
			} else {
				print((byte)(c >> 12 & 0xF | 0xE0));
				print((byte)(c >> 6 & 0x3F | 0x80));
				print((byte)(c & 0x3F | 0x80));
			}
		}

		public void print(char[] s) {
			for (char i : s)
				print(i);
		}

		public void print(String s) {
			try {
				if (READ_STRING_TO_BYTE_ARRAY == 0) {
					java.lang.reflect.Field strValueField = s.getClass().getDeclaredField("value");
					strValueField.setAccessible(true);
					byte[] c = (byte[])strValueField.get(s);
					strValueField.setAccessible(false);
					strValueField = s.getClass().getDeclaredField("coder");
					strValueField.setAccessible(true);
					byte coder = (byte)strValueField.get(s);
					strValueField.setAccessible(false);
					if (coder == 0) {
						for (byte b : c)
							print(b);
					} else if (coder == 1) {
						for (int i = 0; i < c.length; i += 2)
							print((char)(c[i] | c[i + 1] << 8));
					} else {
						print(s.toCharArray());
					}
				} else if (READ_STRING_TO_BYTE_ARRAY == 1) {
					java.lang.reflect.Field strValueField = s.getClass().getDeclaredField("value");
					strValueField.setAccessible(true);
					print((char[])strValueField.get(s));
					strValueField.setAccessible(false);
				} else {
					print(s.toCharArray());
				}
			} catch (Exception e) {
				print(s.toCharArray());
			}
		}

		public void print(Object o) {
			print(o.toString());
		}

		public void printf(java.util.Locale l, String format, Object... args) {
			print(String.format(l, format, args));
		}

		public void printf(String format, Object... args) {
			print(String.format(format, args));
		}

		public void println() {
			print((byte)'\n');
			if (autoFlush) flush();
		}

		public void println(boolean b) {
			print(b);
			println();
		}

		public void println(byte b) {
			print(b);
			println();
		}

		public void println(short s) {
			print(s);
			println();
		}

		public void println(int i) {
			print(i);
			println();
		}

		public void println(long l) {
			print(l);
			println();
		}

		public void println(float f) {
			print(f);
			println();
		}

		public void println(double d) {
			print(d);
			println();
		}

		public void println(double d, int n) {
			print(d, n);
			println();
		}

		public void println(char c) {
			print(c);
			println();
		}

		public void println(char[] s) {
			print(s);
			println();
		}

		public void println(String s) {
			print(s);
			println();
		}

		public void println(Object o) {
			print(o);
			println();
		}

		public Output append(char c) {
			print(c);
			return this;
		}

		public Output append(CharSequence csq) {
			if (csq == null) csq = "null";
			print(csq.toString());
			return this;
		}

		public Output append(CharSequence csq, int start, int end) {
			if (csq == null) csq = "null";
			print(csq.subSequence(start, end).toString());
			return this;
		}
	}

	public static final class DisjointSetUnion {

		private final int[] parent;

		private DisjointSetUnion(int n) {
			parent = new int[n];
			java.util.Arrays.fill(parent, -1);
		}

		public static DisjointSetUnion create(int n) {
			return new DisjointSetUnion(n);
		}

		public int getLeader(int a) {
			int p1, p2;
			while ((p1 = parent[a]) >= 0) {
				if ((p2 = parent[p1]) >= 0) a = parent[a] = p2;
				else return p1;
			}
			return a;
		}

		public int merge(int a, int b) {
			a = getLeader(a);
			b = getLeader(b);
			if (a == b) return a;
			if (parent[a] < parent[b]) {
				parent[b] += parent[a];
				parent[a] = b;
				return b;
			}
			parent[a] += parent[b];
			parent[b] = a;
			return a;
		}

		public boolean isSame(int a, int b) {
			return getLeader(a) == getLeader(b);
		}

		public int getSize(int a) {
			return -parent[getLeader(a)];
		}

		public java.util.ArrayList<java.util.ArrayList<Integer>> getGroups() {
			Object[] group = new Object[parent.length];
			java.util.ArrayList<java.util.ArrayList<Integer>> ret = new java.util.ArrayList<>();
			for (int i = 0; i < parent.length; ++i) {
				int leader = getLeader(i);
				Object put = group[leader];
				if (put == null) {
					java.util.ArrayList<Integer> list = new java.util.ArrayList<>();
					list.add(i);
					ret.add(list);
					group[leader] = list;
				} else {
					@SuppressWarnings("unchecked")
					java.util.ArrayList<Integer> list = (java.util.ArrayList<Integer>)put;
					list.add(i);
				}
			}
			return ret;
		}

		@Override
		public String toString() {
			return getGroups().toString();
		}
	}

	public static class IntFenwickTree {

		private final int[] array;

		private IntFenwickTree(int n) {
			array = new int[n + 1];
		}

		private IntFenwickTree(int[] array) {
			this(array.length);
			System.arraycopy(array, 0, this.array, 1, array.length);
			for (int i = 1; i < this.array.length; ++i)
				if (i + (i & -i) < this.array.length) this.array[i + (i & -i)] += this.array[i];
		}

		public static IntFenwickTree create(int n) {
			return new IntFenwickTree(n);
		}

		public static IntFenwickTree create(int[] array) {
			return new IntFenwickTree(array);
		}

		public void add(int index, int add) {
			++index;
			while (index < array.length) {
				array[index] += add;
				index += index & -index;
			}
		}

		private int sum(int index) {
			int sum = 0;
			while (index > 0) {
				sum += array[index];
				index -= index & -index;
			}
			return sum;
		}

		public int sum(int l, int r) {
			return sum(r) - sum(l);
		}

		@Override
		public String toString() {
			return java.util.stream.IntStream.range(0, array.length - 1).mapToObj(i -> String.valueOf(sum(i + 1) - sum(i))).collect(
					java.util.stream.Collectors.joining(", ", "[", "]"));
		}
	}

	public static class LongFenwickTree {

		private final long[] array;

		private LongFenwickTree(int n) {
			array = new long[n + 1];
		}

		private LongFenwickTree(long[] array) {
			this(array.length);
			System.arraycopy(array, 0, this.array, 1, array.length);
			for (int i = 1; i < this.array.length; ++i)
				if (i + (i & -i) < this.array.length) this.array[i + (i & -i)] += this.array[i];
		}

		public static LongFenwickTree create(int n) {
			return new LongFenwickTree(n);
		}

		public static LongFenwickTree create(long[] array) {
			return new LongFenwickTree(array);
		}

		public void add(int index, long add) {
			++index;
			while (index < array.length) {
				array[index] += add;
				index += index & -index;
			}
		}

		private long sum(int index) {
			long sum = 0;
			while (index > 0) {
				sum += array[index];
				index -= index & -index;
			}
			return sum;
		}

		public long sum(int l, int r) {
			return sum(r) - sum(l);
		}

		@Override
		public String toString() {
			return java.util.stream.IntStream.range(0, array.length - 1).mapToObj(i -> String.valueOf(sum(i + 1) - sum(i))).collect(
					java.util.stream.Collectors.joining(", ", "[", "]"));
		}
	}

}
