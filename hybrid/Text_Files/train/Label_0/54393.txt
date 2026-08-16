import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Jasper van Merle
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputReader in = new InputReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskA solver = new TaskA();
		solver.solve(1, in, out);
		out.close();
	}

	static class TaskA {
		public void solve(int testNumber, InputReader in, PrintWriter out) {
			String line = in.nextLine();
			boolean success = false;

			outer:
			for (int i = 0, iMax = line.length(); i < iMax; i++) {
				for (char c = 'a'; c <= 'z'; c++) {
					if (line.charAt(i) != c) {
						String word = line.substring(0, i) + c + line.substring(i + 1);
						if (word.equals(new StringBuilder(word).reverse().toString())) {
							out.println("YES");
							success = true;
							break outer;
						}
					}
				}
			}

			if (!success) out.println("NO");
		}

	}

	static class InputReader {
		public BufferedReader br;

		public InputReader(InputStream in) {
			br = new BufferedReader(new InputStreamReader(in));
		}

		public String nextLine() {
			String str;

			try {
				str = br.readLine();
			} catch (IOException e) {
				throw new RuntimeException(e);
			}

			return str;
		}

	}
}

