import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class Ladder {
	static int mod = 1000000007;

	static class Reader {
		final private int BUFFER_SIZE = 1 << 16;
		private DataInputStream din;
		private byte[] buffer;
		private int bufferPointer, bytesRead;

		public Reader() {
			din = new DataInputStream(System.in);
			buffer = new byte[BUFFER_SIZE];
			bufferPointer = bytesRead = 0;
		}

		public Reader(String file_name) throws IOException {
			din = new DataInputStream(new FileInputStream(file_name));
			buffer = new byte[BUFFER_SIZE];
			bufferPointer = bytesRead = 0;
		}

		public String readLine() throws IOException {
			byte[] buf = new byte[10005]; // line length
			int cnt = 0, c;
			while ((c = read()) != -1) {
				if (c == '\n')
					break;
				buf[cnt++] = (byte) c;
			}
			return new String(buf, 0, cnt);
		}

		public int nextInt() throws IOException {
			int ret = 0;
			byte c = read();
			while (c <= ' ')
				c = read();
			boolean neg = (c == '-');
			if (neg)
				c = read();
			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');

			if (neg)
				return -ret;
			return ret;
		}

		public long nextLong() throws IOException {
			long ret = 0;
			byte c = read();
			while (c <= ' ')
				c = read();
			boolean neg = (c == '-');
			if (neg)
				c = read();
			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');
			if (neg)
				return -ret;
			return ret;
		}

		public double nextDouble() throws IOException {
			double ret = 0, div = 1;
			byte c = read();
			while (c <= ' ')
				c = read();
			boolean neg = (c == '-');
			if (neg)
				c = read();

			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');

			if (c == '.') {
				while ((c = read()) >= '0' && c <= '9') {
					ret += (c - '0') / (div *= 10);
				}
			}

			if (neg)
				return -ret;
			return ret;
		}

		private void fillBuffer() throws IOException {
			bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
			if (bytesRead == -1)
				buffer[0] = -1;
		}

		private byte read() throws IOException {
			if (bufferPointer == bytesRead)
				fillBuffer();
			return buffer[bufferPointer++];
		}

		public void close() throws IOException {
			if (din == null)
				return;
			din.close();
		}
	}

	public static void main(String[] args) throws IOException {
		Reader in = new Reader();
		int l, r, i, t, n, m;
		n = in.nextInt();
		m = in.nextInt();
		StringBuilder ans = new StringBuilder();
		int arr[] = new int[n + 1];
		for (i = 1; i <= n; i++)
			arr[i] = in.nextInt();
		int inc[] = new int[n + 1];
		int dec[] = new int[n + 1];
		inc[n] = n;
		dec[n] = n;
		for (i = n - 1; i > 0; i--) {
			if (arr[i] > arr[i + 1]) {
				inc[i] = i;
				dec[i] = dec[i + 1];
			} else if (arr[i] < arr[i + 1]) {
				dec[i] = i;
				inc[i] = inc[i + 1];
			} else {
				inc[i] = inc[i + 1];
				dec[i] = dec[i + 1];
			}
		}

		for (i = 1; i <= m; i++) {
			l = in.nextInt();
			r = in.nextInt();
			if (dec[inc[l]] >= r)
				ans.append("Yes\n");
			else
				ans.append("No\n");
		}
		System.out.println(ans);
	}
}
