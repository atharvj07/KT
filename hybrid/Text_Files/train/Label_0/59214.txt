import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class TVSubscriptions {
	public static void main(String[] args) throws IOException {
		InputReader r = new InputReader(System.in);
		int t = r.nextInt();
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		while (t-- > 0) {
			int x = solve(r);
			out.append(x + "\n");
		}
		out.flush();
		out.close();
	}

	static int[] cnt = new int[1000005];

	private static int solve(TVSubscriptions.InputReader r) {
		int n = r.nextInt();
		int k = r.nextInt();
		int d = r.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = r.nextInt();
		}
		int curr = 0;
		for (int i = 0; i < d; i++) {
			cnt[arr[i]]++;
			if (cnt[arr[i]] == 1)
				curr++;
		}
		int res = curr;
		for (int i = d; i < n; i++) {
			cnt[arr[i - d]]--;
			if (cnt[arr[i - d]] == 0)
				curr--;
			cnt[arr[i]]++;
			if (cnt[arr[i]] == 1)
				curr++;
			res = Math.min(res, curr);
		}
		for (int i = n - d; i < n; i++)
			cnt[arr[i]]--;
		return res;

	}

	static class InputReader {
		private BufferedReader reader;
		private StringTokenizer tokenizer;

		public InputReader(InputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream));
			tokenizer = null;
		}

		public InputReader(FileReader stream) {
			reader = new BufferedReader(stream);
			tokenizer = null;
		}

		public String nextLine() {
			try {
				return reader.readLine();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				return null;
			}
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

		public double nextDouble() {
			return Double.parseDouble(next());
		}
	}
}
