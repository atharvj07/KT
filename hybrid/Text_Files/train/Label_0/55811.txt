import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	void solve() throws IOException {
		int n = nextInt();
		int[] a = new int[n];
		Integer[] b = new Integer[n];
		for (int i = 0; i < n; ++i) {
			a[i] = nextInt();
			b[i] = a[i];
		}
		Arrays.sort(b);
		int cnt = 0;
		for (int i = 0; i < n; ++i)
			if (a[i] != b[i])
				++cnt;
		if (cnt <= 2)
			writer.println("YES");
		else
			writer.println("NO");
	}

	BufferedReader reader;
	PrintWriter writer;
	StringTokenizer tokenizer;

	String nextToken() throws IOException {
		while (tokenizer == null || !tokenizer.hasMoreTokens())
			tokenizer = new StringTokenizer(reader.readLine());
		return tokenizer.nextToken();
	}

	int nextInt() throws IOException {
		return Integer.parseInt(nextToken());
	}

	public void run() {
		try {
			reader = new BufferedReader(new InputStreamReader(System.in));
			tokenizer = null;
			writer = new PrintWriter(new OutputStreamWriter(System.out));
			solve();
			reader.close();
			writer.close();
		} catch (Exception e) {
			e.printStackTrace();
			System.exit(1);
		}
	}

	public static void main(String[] args) throws IOException {
		new Main().run();
	}
}