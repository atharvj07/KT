import java.io.IOException;
import java.io.InputStream;
import java.util.*;
import java.lang.*;

public class Main{
	public static void main(String[] args) {
		FastScanner sc = new FastScanner();
		int w = sc.nextInt();
		int d = sc.nextInt();
		int n = sc.nextInt();
		int[] x = new int[n];
		int[] y = new int[n];
		int[] z = new int[n];
		for (int i = 0; i < n; i++) {
			x[i] = sc.nextInt();
			y[i] = sc.nextInt();
			z[i] = sc.nextInt();
		}
		ArrayList<TreeSet<Integer>> list = new ArrayList<>(100 * w + d);
		for (int i = 0; i < 100 * w + d; i++) {
			list.add(new TreeSet<Integer>());
		}
		for (int i = 0; i < n; i++) {
			ArrayDeque<Integer> deque = new ArrayDeque<>();
			int now = z[i];
			if (now < 0) {
				deque.add(10000000 + 10000 * -now + 100 * x[i] + y[i]);
			} else {
				deque.add(10000 * now + 100 * x[i] + y[i]);
			}
			boolean[][] visited = new boolean[w][d];
			for (int j = 0; j < n; j++) {
				list.get(100 * (x[j] - 1) + (y[j] - 1)).add(z[j]);
				visited[x[j] - 1][y[j] - 1] = true;
			}
			while (!deque.isEmpty()) {
				int tmp = deque.remove();
				int mai = tmp / 10000000;
				int tnow = tmp % 10000000 / 10000;
				int tx = tmp % 10000 / 100;
				int ty = tmp % 100;
				if (mai == 1) {
					tnow = -tnow;
				}
				list.get(100 * (tx - 1) + (ty - 1)).add(tnow);
				if (tx + 1 <= w && !visited[tx + 1 - 1][ty - 1]) {
					if (tnow - 1 < 0) {
						deque.add(10000000 + 10000 * -(tnow - 1) + 100 * (tx + 1) + ty);
					} else {
						deque.add(10000 * (tnow - 1) + 100 * (tx + 1) + ty);
					}
					visited[tx + 1 - 1][ty - 1] = true;
				}
				if (tx - 1 >= 1 && !visited[tx - 1 - 1][ty - 1]) {
					if (tnow - 1 < 0) {
						deque.add(10000000 + 10000 * -(tnow - 1) + 100 * (tx - 1) + ty);
					} else {
						deque.add(10000 * (tnow - 1) + 100 * (tx - 1) + ty);
					}
					visited[tx - 1 - 1][ty - 1] = true;
				}
				if (ty + 1 <= d && !visited[tx - 1][ty + 1 - 1]) {
					if (tnow - 1 < 0) {
						deque.add(10000000 + 10000 * -(tnow - 1) + 100 * tx + (ty + 1));
					} else {
						deque.add(10000 * (tnow - 1) + 100 * tx + (ty + 1));
					}
					visited[tx - 1][ty + 1 - 1] = true;
				}
				if (ty - 1 >= 1 && !visited[tx- 1][ty - 1 - 1]) {
					if (tnow - 1 < 0) {
						deque.add(10000000 + 10000 * -(tnow - 1) + 100 * tx + (ty - 1));
					} else {
						deque.add(10000 * (tnow - 1) + 100 * tx + (ty - 1));
					}
					visited[tx - 1][ty - 1 - 1] = true;
				}
			}
		}
		long ans = 0;
		for (int i = 0; i < w; i++) {
			for (int j = 0; j < d; j++) {
				ans += list.get(100 * i + j).last();
			}
		}
		for (int i = 0; i < w; i++) {
			for (int j = 0; j < d - 1; j++) {
				if (Math.abs(list.get(100 * i + j).last() - list.get(100 * i + (j + 1)).last()) > 1) {
					System.out.println("No");
					return;
				}
			}
		}
		for (int i = 0; i < d; i++) {
			for (int j = 0; j < w - 1; j++) {
				if (Math.abs(list.get(100 * j + i).last() - list.get(100 * (j + 1) + i).last()) > 1) {
					System.out.println("No");
					return;
				}
			}
		}
		System.out.println(ans);
	}
}

class FastScanner {
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
		if (hasNextByte()) {
			return buffer[ptr++];
		} else {
			return -1;
		}
	}
	private static boolean isPrintableChar(int c) {
		return 33 <= c && c <= 126;
	}
	public boolean hasNext() {
		while (hasNextByte() && !isPrintableChar(buffer[ptr])) {
			ptr++;
		}
		return hasNextByte();
	}
	public String next() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while (isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	public long nextLong() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
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
		if (nl < Integer.MIN_VALUE || Integer.MAX_VALUE < nl) {
			throw new NumberFormatException();
		}
		return (int) nl;
	}
	public double nextDouble() {
		return Double.parseDouble(next());
	}
}

