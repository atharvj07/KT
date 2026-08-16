import java.io.*;
import java.util.*;


public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Printer pr = new Printer(System.out);

		int n = sc.nextInt();
		int k = sc.nextInt();

		List<List<Integer>> edges = new ArrayList<>(n);
		for (int i = 0; i < n; i++) {
			edges.add(new ArrayList<Integer>());
		}

		int[] a = new int[n - 1];
		int[] b = new int[n - 1];
		for (int i = 0; i < n - 1; i++) {
			a[i] = sc.nextInt() - 1;
			b[i] = sc.nextInt() - 1;
			edges.get(a[i]).add(b[i]);
			edges.get(b[i]).add(a[i]);
		}

		int ret = Integer.MAX_VALUE;
		if (k % 2 == 0) {
			for (int i = 0; i < n; i++) {
				int root = i;
				int[] used = new int[n];
				Arrays.fill(used, -1);
				Deque<Integer> st = new ArrayDeque<>();
				st.push(root);
				used[root] = 0;
				int cnt = 0;
				while (!st.isEmpty()) {
					int e = st.pop();

					for (int ne : edges.get(e)) {
						if (used[ne] >= 0) {
							continue;
						}
						st.push(ne);
						used[ne] = used[e] + 1;
						if (used[ne] > k / 2) {
							cnt++;
						}
					}
				}
				ret = Math.min(ret, cnt);
			}
		} else {
			for (int i = 0; i < n - 1; i++) {
				int[] used = new int[n];
				Arrays.fill(used, -1);
				Deque<Integer> st = new ArrayDeque<>();
				st.push(a[i]);
				st.push(b[i]);
				used[a[i]] = 0;
				used[b[i]] = 0;
				int cnt = 0;
				while (!st.isEmpty()) {
					int e = st.pop();

					for (int ne : edges.get(e)) {
						if (used[ne] >= 0) {
							continue;
						}
						st.push(ne);
						used[ne] = used[e] + 1;
						if (used[ne] > k / 2) {
							cnt++;
						}
					}
				}
				ret = Math.min(ret, cnt);
			}
		}

		pr.println(ret);

		pr.close();
		sc.close();
	}

	@SuppressWarnings("unused")
	private static class Scanner {
		BufferedReader br;
		Iterator<String> it;

		Scanner (InputStream in) {
			br = new BufferedReader(new InputStreamReader(in));
		}

		String next() throws RuntimeException  {
			try {
				if (it == null || !it.hasNext()) {
//					it = Arrays.asList(br.readLine().split(" ")).iterator();
					it = Arrays.asList(br.readLine().split("\\p{javaWhitespace}+")).iterator();
				}
				return it.next();
			} catch (IOException e) {
				throw new IllegalStateException();
			}
		}

		int nextInt() throws RuntimeException {
			return Integer.parseInt(next());
		}

		long nextLong() throws RuntimeException {
			return Long.parseLong(next());
		}

		float nextFloat() throws RuntimeException {
			return Float.parseFloat(next());
		}

		double nextDouble() throws RuntimeException {
			return Double.parseDouble(next());
		}

		void close() {
			try {
				br.close();
			} catch (IOException e) {
//				throw new IllegalStateException();
			}
		}
	}

	private static class Printer extends PrintWriter {
		Printer(PrintStream out) {
			super(out);
		}
	}
}
