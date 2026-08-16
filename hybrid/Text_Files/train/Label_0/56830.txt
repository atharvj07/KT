import java.io.*;
import java.util.*;

public class C {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputReader in = new InputReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		Task solver = new Task();
		solver.solve(1, in, out);
		out.close();
	}

	static class Task {
		class Pair implements Comparable<Pair> {
			Integer l, r, id;

			public Pair(Integer id, Integer l, Integer r) {
				this.id = id;
				this.l = l;
				this.r = r;
			}

			@Override
			public int compareTo(Pair o) {
			    int lCmp = l.compareTo(o.l);
			    if (lCmp != 0)
			    	return lCmp;

			    return -r.compareTo(o.r);
			}
		}
		public void solve(int ntest, InputReader inp, PrintWriter out) {
			int nSegment = inp.nextInt();
			List<Pair> pairs = new ArrayList<>();

			for (int i = 0; i < nSegment; ++i) {
				int l = inp.nextInt(), r = inp.nextInt();
				pairs.add(new Pair(i + 1, l, r));
			}

			Collections.sort(pairs);

			for (int i = 1; i < nSegment; ++i) {
				if (pairs.get(i - 1).r >= pairs.get(i).r)	 {
					out.println(pairs.get(i).id + " " + pairs.get(i - 1).id);
					return;
				}
			}

			out.print("-1 -1");

		}
	}

	static class InputReader {
		public BufferedReader reader;
		public StringTokenizer tokenizer;

		public InputReader(InputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream), 32768);
			tokenizer = null;
		}

		public String next() {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(reader.readLine());
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return tokenizer.nextToken();
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}

		public long nextLong() {
			return Long.parseLong(next());
		}
	}
}
