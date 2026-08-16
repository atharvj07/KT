import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.NoSuchElementException;

public class Main {
	int L,N;
	int[] x,w;
	ArrayList<Integer>[] list;
	@SuppressWarnings("unchecked")
	public void solve() {
		L = nextInt();
		N = nextInt();
		x = new int[N];
		w = new int[N];

		list = new ArrayList[2 * L + 1];
		for(int i = 0;i < 2 * L + 1;i++){
			list[i] = new ArrayList<Integer>();
		}
		for(int i = 0;i < N;i++){
			x[i] = nextInt();
			w[i] = nextInt();
			list[-x[i] + L].add(w[i]);
		}
		out.println(N);
		for(int i = 0;i < 2 * L + 1;i++){
			for(int weight : list[i]){
				out.println((i-L) + " " + weight);
			}
		}


	}
	public static void main(String[] args) {
		out.flush();
		new Main().solve();
		out.close();
	}

	/* Input */
	private static final InputStream in = System.in;
	private static final PrintWriter out = new PrintWriter(System.out);
	private final byte[] buffer = new byte[2048];
	private int p = 0;
	private int buflen = 0;

	private boolean hasNextByte() {
		if (p < buflen)
			return true;
		p = 0;
		try {
			buflen = in.read(buffer);
		} catch (IOException e) {
			e.printStackTrace();
		}
		if (buflen <= 0)
			return false;
		return true;
	}

	public boolean hasNext() {
		while (hasNextByte() && !isPrint(buffer[p])) {
			p++;
		}
		return hasNextByte();
	}

	private boolean isPrint(int ch) {
		if (ch >= '!' && ch <= '~')
			return true;
		return false;
	}

	private int nextByte() {
		if (!hasNextByte())
			return -1;
		return buffer[p++];
	}

	public String next() {
		if (!hasNext())
			throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = -1;
		while (isPrint((b = nextByte()))) {
			sb.appendCodePoint(b);
		}
		return sb.toString();
	}

	public int nextInt() {
		return Integer.parseInt(next());
	}

	public long nextLong() {
		return Long.parseLong(next());
	}

	public double nextDouble() {
		return Double.parseDouble(next());
	}
}