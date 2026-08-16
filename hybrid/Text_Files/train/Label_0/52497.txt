import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.NoSuchElementException;

public class Main{
	int N,M;
	int[] union,rank;
	boolean[] used;

	public boolean same(int x,int y){
		return find(x) == find(y);
	}

	public int find(int x){
		if(union[x] == x)return x;
		return union[x] = find(union[x]);
	}

	public void unite(int x,int y){
		x = find(x);
		y = find(y);

		if(x == y)return;

		if(x < y){
			union[y] = x;
			rank[x] += rank[y];
		}else{
			union[x] = y;
			rank[y] += rank[x];
		}
	}

	public void solve() {
		N = nextInt();
		M = nextInt();

		union = new int[N];
		rank = new int[N];
		used = new boolean[N];
		for(int i = 0;i < N;i++)union[i] = i;
		Arrays.fill(rank, 1);


		for(int i = 0;i < M;i++){
			int a = nextInt()-1;
			int b = nextInt()-1;

			unite(a,b);
		}

		int big = 0;
		int small = 0;
		for(int i = 0;i < N;i++){
			int root = find(i);
			if(used[root])continue;
			used[root] = true;

			if(rank[root] == 1)small++;
			else big++;
		}

		out.println(Math.abs(big-small));
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