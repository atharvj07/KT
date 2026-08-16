import java.util.*;
import java.io.*;

public class B{
	public static void main(String[] args) {
		InputReader in = new InputReader(System.in);
		PrintWriter out = new PrintWriter(System.out);
		Solver solver = new Solver();
		solver.solve(in, out);
		out.close();
	}

	static class Solver{
		public void solve(InputReader in, PrintWriter out) {
			int n = in.nextInt();
			int[] a = new int[n+1], ans = new int[n+1];
			for (int i = 1; i <= n; ++ i) a[i] = in.nextInt();

			boolean[] v = new boolean[n+1];
			LinkedList<Integer> q = new LinkedList<>();
			int path = 0;
			
			q.add(1);
			v[1] = true;
			while (! q.isEmpty()) {
				int size = q.size();
				for (int i = 0; i < size; ++ i) {
					int node = q.poll();
					ans[node] = path;
					if (node-1 > 0 && !v[node-1]) {
						q.add(node-1);
						v[node-1] = true;
					}
					if (node+1 <= n && !v[node+1]) {
						q.add(node+1);
						v[node+1] = true;
					}
					if (!v[a[node]]) {
						q.add(a[node]);
						v[a[node]] = true;
					}
				}
				++path;
			}
			for (int i = 1; i <= n; ++ i) out.print(ans[i] + " ");
			out.println();
		}
	}

	static class InputReader{
		BufferedReader reader;
		StringTokenizer tokenizer;

		public InputReader(InputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream));
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
	}
}