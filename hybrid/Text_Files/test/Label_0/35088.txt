import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Locale;
import java.util.StringTokenizer;

public class B {

	private void solve() throws IOException {
		int n = nextInt();
		int r = nextInt();
		int c = nextInt();
		
		String s = reader.readLine();
		String[] all = new String[n];
		StringTokenizer st = new StringTokenizer(s);
		for (int i = 0; i < n; i++) {
			all[i] = st.nextToken();
		}
		
		int[] start = new int[n];
		int[] finish = new int[n];
		int len = 0;
		for (int i = 0; i < n; i++) {
			start[i] = len;
			len += all[i].length();
			finish[i] = len - 1;
			len++;
		}
		
		char[] a = s.toCharArray();
		int[] wordIndex = new int[a.length];
		
		for (int i = 1; i < a.length; i++) {
			if (a[i] == ' ') {
				wordIndex[i] = wordIndex[i - 1] + 1;
			} else {
				wordIndex[i] = wordIndex[i - 1];
			}
		}
		for (int i = 0; i < a.length; i++) {
			if (a[i] == ' ') {
				wordIndex[i]--;
			}
		}
		
		int[] lines = new int[n];
		int[] words = new int[n];
		int[] onLine = new int[n];
		int[][] prevW = new int[20][n];
		
		for (int i = 0; i < n; i++) {
			int prev = finish[i] - c;
			int wordsOnLine = 0;

			if (prev < 0) {
				wordsOnLine = i + 1;
				lines[i] = 1;
				words[i] = wordsOnLine;
				onLine[i] = wordsOnLine;
				continue;
			} else {
				wordsOnLine = i - wordIndex[prev];
			}
			
			if (wordsOnLine == 0) {
				continue;
			}
			
			
			if (r == 1) {
				lines[i] = 1;
				words[i] = wordsOnLine;
				onLine[i] = wordsOnLine;
				continue;
			}
			
			int prevWord = wordIndex[prev];
			if (lines[prevWord] == r) {
				lines[i] = r;
				
				int begin = prevWord - words[prevWord] + 1;
				int d = r - 1;
				int p = prevWord;
				int t = 20;
				while (d != 0) {
					if ((1 << t) > d) {
						t--;
					} else {
						d -= 1 << t;
						p = prevW[t][p];
					}
				}
				
				int w = p - begin + 1;
				words[i] = words[prevWord] - w + wordsOnLine;
			} else {
				lines[i] = lines[prevWord] + 1;
				words[i] = words[prevWord] + wordsOnLine;
			}
			
			prevW[0][i] = prevWord;
			for (int j = 1; j < 20; j++) {
				prevW[j][i] = prevW[j - 1][prevW[j - 1][i]];
			}
			onLine[i] = wordsOnLine;
		}
		
		
		
		int ans = 0;
		for (int i = 1; i < n; i++) {
			if (words[i] > words[ans]) {
				ans = i;
			}
		}
		
		int p = ans;
		ArrayList<String> res = new ArrayList<String>();
		for (int i = 0; i < lines[ans]; i++) {
			StringBuilder sb = new StringBuilder();
			for (int j = p - onLine[p] + 1; j <= p; j++) {
				sb.append(all[j]);
				if (j < p) {
					sb.append(' ');
				}
			}
			
			res.add(sb.toString());
			p = prevW[0][p];
		}
		
		Collections.reverse(res);
		for (String t: res) {
			println(t);
		}
	}

	private String nextToken() throws IOException {
		while (tokenizer == null || !tokenizer.hasMoreTokens()) {
			tokenizer = new StringTokenizer(reader.readLine());
		}
		return tokenizer.nextToken();
	}

	private int nextInt() throws NumberFormatException, IOException {
		return Integer.parseInt(nextToken());
	}

	private double nextDouble() throws NumberFormatException, IOException {
		return Double.parseDouble(nextToken());
	}

	private long nextLong() throws IOException {
		return Long.parseLong(nextToken());
	}

	private void print(Object o) {
		writer.print(o);
	}

	private void println(Object o) {
		writer.println(o);
	}

	private void printf(String format, Object... o) {
		writer.printf(format, o);
	}

	public static void main(String[] args) {
		long time = System.currentTimeMillis();
		Locale.setDefault(Locale.US);
		new B().run();
		System.err.printf("%.3f\n", 1e-3 * (System.currentTimeMillis() - time));
	}

	BufferedReader reader;
	StringTokenizer tokenizer;
	PrintWriter writer;

	private void run() {
		try {
			reader = new BufferedReader(new InputStreamReader(System.in));
			writer = new PrintWriter(System.out);
			solve();
			reader.close();
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
			System.exit(13);
		}
	}
}