import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Test {
	static BufferedReader reader;
	static StringTokenizer tokenizer;
	static PrintWriter writer;

	static int nextInt() throws IOException {
		return Integer.parseInt(nextToken());
	}

	static long nextLong() throws IOException {
		return Long.parseLong(nextToken());
	}

	static double nextDouble() throws IOException {
		return Double.parseDouble(nextToken());
	}

	static String nextToken() throws IOException {
		while (tokenizer == null || !tokenizer.hasMoreTokens()) {
			tokenizer = new StringTokenizer(reader.readLine());
		}
		return tokenizer.nextToken();
	}

	public static void main(String[] args) throws IOException {
		reader = new BufferedReader(new InputStreamReader(System.in));
		tokenizer = null;
		writer = new PrintWriter(System.out);
		solve();
		reader.close();
		writer.close();
	}

	private static void solve() throws IOException {
		int n;
		n = nextInt();
		int pref[][] = new int[n + 1][n + 1];
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++)
				pref[i][j] = nextInt();
		}
		int[] alex = new int[n + 1];
		int[] pos = new int[n + 1];
		for (int i = 1; i <= n; i++) {
			alex[i] = nextInt();
			pos[alex[i]] = i;
		}
		
		boolean win=false;
		for (int i = 1; i <= n; i++) {
			win=false;
			for (int j = 1; j <= n; j++) {
				if(pref[i][j]==i)
					continue;
				if(win==true)
					break;
				int posit = 10000;
				int best=-1;
				for (int t = 1; t <= n; t++) {
					if(t==i)
						continue;
					if (pos[t] < posit) {
						best = t;
						posit=pos[t];
						if (pref[i][j] == best) {
							win=true;
							writer.print(pref[i][j] + " ");
							break;
						}
					}
				}
			}
		}
	}
}