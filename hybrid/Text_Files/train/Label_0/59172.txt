import java.util.*;
import java.io.*;

public class Lv1100_Dungeon {

	public static void main(String[] args) {
		InputReader rd = new InputReader(System.in);
		int testcases = rd.nextInt();
		StringBuilder stb = new StringBuilder();
		for (; testcases > 0; testcases--) {
			int[] demons = new int[3];
			long total = 0;
			for (int i = 0; i < demons.length; i++) {
				demons[i] = rd.nextInt();
				total += demons[i];
			}
			Arrays.sort(demons);
			if (total % 9 == 0) {
				long avarage = total / 9;
				if (demons[0] < avarage) {
					stb.append("NO\n");
				} else {
					stb.append("YES\n");
				}
			} else {
				stb.append("NO\n");
			}

		}
		System.out.println(stb);
	}

	static class InputReader {
		StringTokenizer tokenizer;
		BufferedReader reader;
		String token;
		String temp;

		public InputReader(InputStream stream) {
			tokenizer = null;
			reader = new BufferedReader(new InputStreamReader(stream));
		}

		public InputReader(FileInputStream stream) {
			tokenizer = null;
			reader = new BufferedReader(new InputStreamReader(stream));
		}

		public String nextLine() throws IOException {
			return reader.readLine();
		}

		public String next() {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					if (temp != null) {
						tokenizer = new StringTokenizer(temp);
						temp = null;
					} else {
						tokenizer = new StringTokenizer(reader.readLine());
					}
				} catch (IOException e) {
				}
			}
			return tokenizer.nextToken();
		}

		public double nextDouble() {
			return Double.parseDouble(next());
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}

		public long nextLong() {
			return Long.parseLong(next());
		}
	}
}
