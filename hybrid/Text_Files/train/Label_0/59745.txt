import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class D {

	static class FastScanner {
		BufferedReader reader;
		StringTokenizer tokens;

		public FastScanner() {
			reader = new BufferedReader(new InputStreamReader(System.in));
		}

		public FastScanner(File f) throws FileNotFoundException {
			reader = new BufferedReader(new FileReader(f));
		}

		public String nextToken() {
			while (tokens == null || !tokens.hasMoreTokens()) {
				try {
					tokens = new StringTokenizer(reader.readLine());
				} catch (IOException e) {
					return null;
				}
			}
			return tokens.nextToken();
		}

		public int nextInt() {
			return Integer.parseInt(nextToken());
		}

		public double nextDouble() {
			return Double.parseDouble(nextToken());
		}

		public boolean hasNextToken() {
			while (tokens == null || !tokens.hasMoreTokens()) {
				try {
					tokens = new StringTokenizer(reader.readLine());
				} catch (Exception e) {
					return false;
				}
			}
			return true;
		}

		public void close() {
			try {
				reader.close();
			} catch (IOException e) {
			}
		}
	}

	public static class Tree {
		int[] array;

		public Tree(int n) {
			array = new int[n * 4];
			init(0, 0, n);
		}

		public void init(int i, int L, int R) {
			array[i] = Integer.MAX_VALUE;
			if (R - L > 1) {
				int M = (R + L) >> 1;
				init((i << 1) + 1, L, M);
				init((i << 1) + 2, M, R);
			}
		}

		public void set(int i, int L, int R, int index, int value) {
			if (R - L == 1) {
				array[i] = value;
				return;
			}
			int M = (R + L) >> 1;
			if (index < M) {
				set((i << 1) + 1, L, M, index, value);
			} else {
				set((i << 1) + 2, M, R, index, value);
			}
			array[i] = Math.min(array[(i << 1) + 1], array[(i << 1) + 2]);
		}

		public int get(int i, int L, int R, int a, int b) {
			if (R <= a || L >= b) {
				return Integer.MAX_VALUE;
			}
			if (a <= L && R <= b) {
				return array[i];
			}
			int M = (R + L) >> 1;
			return Math.min(get((i << 1) + 1, L, M, a, b),
					get((i << 1) + 2, M, R, a, b));
		}
	}

	public static class Event implements Comparable<Event> {
		int index, l, r;

		public Event(int index, int l, int r) {
			this.index = index;
			this.l = l;
			this.r = r;
		}

		@Override
		public int compareTo(Event o) {
			return r - o.r;
		}

	}

	public static void main(String[] args) throws FileNotFoundException {
		FastScanner in = new FastScanner();
		PrintWriter out = new PrintWriter(System.out);
		// FastScanner in = new FastScanner(new File("in.txt"));
		// PrintWriter out = new PrintWriter(new File("out.txt"));
		int n = in.nextInt();
		int m = in.nextInt();
		int[] a = new int[n];
		for (int i = 0; i < n; i++)
			a[i] = in.nextInt();
		Tree tree = new Tree(n);
		Event[] events = new Event[m];
		for (int i = 0; i < m; i++) {
			events[i] = new Event(i, in.nextInt() - 1, in.nextInt() - 1);
		}
		Arrays.sort(events);
		HashMap<Integer, Integer> lastIndex = new HashMap<>();
		Integer last;
		int eventIndex = 0, ans;
		int[] answers = new int[m];
		for (int i = 0; i < n; i++) {
			last = lastIndex.get(a[i]);
			if (last != null)
				tree.set(0, 0, n, last, i - last);
			lastIndex.put(a[i], i);
			for (; eventIndex < m; eventIndex++) {
				if (events[eventIndex].r != i)
					break;
				ans = tree.get(0, 0, n, events[eventIndex].l,
						events[eventIndex].r);
				answers[events[eventIndex].index] = ans;
			}
		}
		for (int i = 0; i < m; i++)
			out.println(answers[i] == Integer.MAX_VALUE ? -1 : answers[i]);
		out.close();
	}
}
