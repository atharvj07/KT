import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;

public class Main {
	static boolean debug = false;

	public static void main(String[] args) throws IOException {

		UserScanner scan = new UserScanner(System.in);
		PrintWriter pwriter = new PrintWriter(System.out);

		int n = scan.nextInt();
		int m = scan.nextInt();
		Ball ball = new Ball(n, m, debug);

		for (int i = 0; i < m; i++)
			ball.setDancePosition(scan.nextInt(), scan.nextInt());
		for (int i = 0; i < n - m; i++)
			ball.setDance(scan.nextInt());

		pwriter.println(ball.getMaxDance());

		pwriter.flush();

		scan.close();
		System.exit(0);
	}
}

class Ball {
	boolean debug;

	class Gr {
		int[] ch = new int[3]; // if leaf is true, then set dance skill,
								// otherwise child group number
		boolean[] leaf = new boolean[3];
	}

	Gr[] gr;
	int root;

	int[] pool;
	int px = 0;
	int[] allNoble;
	int ax = 0;

	public Ball(int n, int m, boolean debug) {
		this.debug = debug;
		// number of group is N/3 + N/3/3 + N/3/3/3 + ... <= N/2
		gr = new Gr[(n / 2) + 1];
		root = -1;
		int c = 0, p = 0;
		for (int i = 0; root == -1; i++) {
			gr[i] = new Gr();
			for (int j = 0; j < 3; j++)
				if (c < n) {
					gr[i].leaf[j] = true;
					gr[i].ch[j] = -1;
					c++;
				} else if (p == i)
					root = i - 1;
				else {
					gr[i].leaf[j] = false;
					gr[i].ch[j] = p++;
				}
		}

		pool = new int[n - m];
		allNoble = new int[n];
	}

	public int getMaxDance() {
		if (debug)
			printGr(root);

		Arrays.sort(pool); // not allocated nobles
		Arrays.sort(allNoble);
		if (debug)
			for (int i = 0; i < allNoble.length; i++)
				System.out.println("noble " + i + ", d=" + allNoble[i]);

		int hi = 1;
		for (int i = allNoble.length / 3; i > 0; i /= 3)
			hi *= 2; // possible best dancer, if 3 persons then 2nd, if 9
						// persons then 4th, if 27 persons 8th is possible.
						// (it's not accurate)
		hi = allNoble.length - hi;
		int lo = 0, maxDance = -1, midDance = -1;
		boolean down = true;

		while (hi >= lo) { // search max dance skill
			int mid = lo + (hi - lo) / 2;
			if (debug)
				System.out.println("hi=" + hi + ", lo=" + lo + ", mid=" + mid);
			if (midDance == allNoble[mid])
				if (down) {
					hi = mid - 1;
					continue;
				} else {
					lo = mid + 1;
					continue;
				}

			midDance = allNoble[mid];
			if (isPossible(midDance, getPoolNoble(midDance))) {
				// if it possible to assign this dance skill
				// check more higher
				maxDance = midDance;
				down = false;
				lo = mid + 1;
			} else {
				down = true;
				hi = mid - 1;
			}
		}

		return maxDance;
	}

	private boolean isPossible(int d, int f) {
		if (debug)
			System.out.println("d=" + d + ", f=" + f + ", demand=" + getLeastNoble(root, d));

		// dance skill d, and f is free nobles which have dance skill >= d
		if (getLeastNoble(root, d) <= f)
			return true;
		else
			return false;
	}

	private int getLeastNoble(int p, int d) {
		// count the noble which are required to allocate
		int[] a = new int[3];
		for (int i = 0; i < 3; i++)
			if (gr[p].leaf[i])
				if (gr[p].ch[i] >= d)
					a[i] = 0; // already allocated
				else if (gr[p].ch[i] > 0)
					a[i] = pool.length + 1; // sign for not applicable
				else
					a[i] = 1; // need to allocate
			else
				a[i] = getLeastNoble(gr[p].ch[i], d); // child group check by
														// recursive

		// need 2 nobles (highest skill and middle)
		return Math.min(pool.length + 1, a[0] + a[1] + a[2] - Math.max(a[0], Math.max(a[1], a[2])));

	}

	private int getPoolNoble(int d) {
		// count free nobles which have higher dance skill
		if (pool[0] >= d)
			return pool.length;
		if (pool[pool.length - 1] < d)
			return 0;
		return getPoolN(d, 0, pool.length);
	}

	private int getPoolN(int d, int lo, int hi) {
		if (hi <= lo)
			if (pool[lo] >= d)
				return pool.length - lo;
			else
				return pool.length - lo - 1;
		int mid = lo + (hi - lo) / 2;
		if (pool[mid] >= d)
			return getPoolN(d, lo, mid);
		else
			return getPoolN(d, lo + (hi - lo + 1) / 2, hi);
	}

	public void setDance(int d) {
		pool[px++] = d;
		allNoble[ax++] = d;
	}

	public void setDancePosition(int d, int p) {
		p--;
		gr[p / 3].ch[p % 3] = d;
		allNoble[ax++] = d;
	}

	private void printGr(int p) {
		System.out.println(" Gr=" + p);
		System.out.print("   ");
		if (gr[p].leaf[0])
			System.out.print(gr[p].ch[0]);
		else
			System.out.print("Gr=" + gr[p].ch[0]);
		if (gr[p].leaf[1])
			System.out.print(", " + gr[p].ch[1]);
		else
			System.out.print(", Gr=" + gr[p].ch[1]);
		if (gr[p].leaf[2])
			System.out.print(", " + gr[p].ch[2]);
		else
			System.out.print(", Gr=" + gr[p].ch[2]);
		System.out.println();
		if (!gr[p].leaf[0])
			printGr(gr[p].ch[0]);
		if (!gr[p].leaf[1])
			printGr(gr[p].ch[1]);
		if (!gr[p].leaf[2])
			printGr(gr[p].ch[2]);
	}

}

class UserScanner {
	private InputStream in;
	private final byte[] buffer = new byte[1024];
	private int ptr = 0;
	private int buflen = 0;

	public UserScanner(InputStream inStream) {
		in = inStream;
	}

	private void read() {
		ptr = 0;
		try {
			buflen = in.read(buffer);
		} catch (IOException e) {
			e.printStackTrace();
			System.exit(9);
		}
	}

	private byte getByte() {
		if (ptr >= buflen)
			read();
		if (buflen < 0 || isCtlSpace(buffer[ptr])) {
			return -1;
		} else
			return buffer[ptr++];
	}

	private void skipCtlSpace() {
		for (; ptr < buflen; ptr++)
			if (!isCtlSpace(buffer[ptr]))
				return;
		read();
		skipCtlSpace();
	}

	private boolean isCtlSpace(byte b) {
		if (b <= ' ' || b > '~')
			return true;
		else
			return false;
	}

	public void close() {
		try {
			in.close();
		} catch (IOException e) {
			e.printStackTrace();
			System.exit(9);
		}
	}

	public String next() {
		skipCtlSpace();
		StringBuilder sb = new StringBuilder();
		byte b;
		while ((b = getByte()) != -1) {
			sb.appendCodePoint(b);
		}
		return sb.toString();
	}

	public int nextInt() {
		skipCtlSpace();
		int n = 0;
		boolean minus = false;
		byte b;
		while ((b = getByte()) != -1) {
			if (b == '-')
				minus = true;
			else {
				n *= 10;
				n += (b - '0');
			}
		}
		if (minus)
			return n * -1;
		else
			return n;
	}
}