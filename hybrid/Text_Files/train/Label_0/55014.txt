import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {
	public static void main(String[] args) throws IOException {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;

		// InputStream inputStream = new FileInputStream("joke.in");
		// OutputStream outputStream = new FileOutputStream("joke.out");

		InputReader in = new InputReader(inputStream);
		OutputWriter out = new OutputWriter(outputStream);

		TaskB solver = new TaskB();
		solver.solve(in, out);

		out.close();
	}
}

class TaskB {

	public void solve(InputReader in, OutputWriter out) {

		n = in.nextInt();
		k = in.nextInt();
		a = in.nextInt();
		int m = in.nextInt();

		int cnt = f(n);
		TreeSet<Segment> set = new TreeSet<Segment>();
		set.add(new Segment(1, n));

		for (int i = 0; i < m; i++) {
			int x = in.nextInt();
			Segment s = new Segment(x, x);
			Segment seg = set.floor(s);
			
			//if(seg==null) continue;
			cnt -= f(seg.r - seg.l + 1);
			set.remove(seg);
			if (seg.l < x) {
				cnt += f(x - seg.l);
				set.add(new Segment(seg.l, x - 1));
			}

			if (seg.r > x) {
				cnt += f(seg.r - x);
				set.add(new Segment(x + 1, seg.r));
			}
			if(cnt<k){
				out.write(i+1);
				return;
			}
		}
		
		out.write(-1);
	}

	int n, k, a;

	int f(int len) {
		int ans = len / (a + 1);
		if (len % (a + 1) == a)
			ans++;

		return ans;
	}

}

class Segment implements Comparable<Segment> {

	public Segment(int l, int r) {
		this.l = l;
		this.r = r;
	}

	public int compareTo(Segment s) {
		return l-s.l;
	}

	int l, r;
}

class InputReader {

	BufferedReader reader;
	StringTokenizer tokenizer;

	public InputReader(InputStream stream) {
		tokenizer = null;
		reader = new BufferedReader(new InputStreamReader(stream));
	}

	public String next() {
		while (tokenizer == null || !tokenizer.hasMoreTokens()) {
			try {
				tokenizer = new StringTokenizer(reader.readLine());
			} catch (IOException e) {
				throw new RuntimeException();
			}
		}

		return tokenizer.nextToken();
	}

	public String nextLine() {
		tokenizer = null;
		try {
			return reader.readLine();
		} catch (IOException e) {
			throw new RuntimeException();
		}
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

	public int[] nextIntArray(int n) {
		int[] res = new int[n];
		for (int i = 0; i < n; i++)
			res[i] = nextInt();

		return res;
	}

}

class OutputWriter {

	PrintWriter out;

	public OutputWriter(OutputStream stream) {
		out = new PrintWriter(
				new BufferedWriter(new OutputStreamWriter(stream)));
	}

	public void write(Object... o) {
		for (Object cur : o)
			out.print(cur);
	}

	public void writeln(Object... o) {
		write(o);
		out.println();
	}

	public void flush() {
		out.flush();
	}

	public void close() {
		out.close();
	}

}
