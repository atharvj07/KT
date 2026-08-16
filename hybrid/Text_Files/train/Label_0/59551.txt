import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;


public class R673 {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(System.out);

		int t = sc.nextInt();
		while (t-- > 0) {
			int n = sc.nextInt();
			int k = sc.nextInt();
			int a[] = new int[n];
			HashMap<Integer, Integer> hm = new HashMap<>();
			HashMap<Integer, Integer> hm2 = new HashMap<>();

			for (int i = 0; i < n; i++) {
				a[i] = sc.nextInt();

			}
			int res[] = new int[n];
			for (int i = 0; i < n; i++) {
				if (hm.containsKey(k - a[i])) {
					if (k - a[i] == a[i]) {
						int c = hm.getOrDefault(a[i], 0);
						if (c % 2 == 0) {
							res[i] = 0;
						} else
							res[i] = 1;
					} else {
						res[i] =hm2.getOrDefault((a[i]),1);
					}
				} else {
					res[i] =0;
					hm2.put(a[i], 0);
					}

				hm.put(a[i], hm.getOrDefault(a[i], 0) + 1);
			}
			for (int i = 0; i < n; i++)
				pw.print(res[i] + " ");
			pw.println();
		}
		pw.flush();
	}

	static class Scanner {

		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream system) {
			br = new BufferedReader(new InputStreamReader(system));
		}

		public Scanner(String file) throws Exception {
			br = new BufferedReader(new FileReader(file));
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public String nextLine() throws IOException {
			return br.readLine();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		public char nextChar() throws IOException {
			return next().charAt(0);
		}

		public Long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public boolean ready() throws IOException {
			return br.ready();
		}

		public void waitForInput() throws InterruptedException {
			Thread.sleep(3000);
		}
	}

}