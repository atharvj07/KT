import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import static java.lang.Integer.parseInt;

/**
 * Swap Cipher
 */
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		String[] words;

		while ((line = br.readLine()) != null && !line.isEmpty()) {

			int N = parseInt(line);
			if (N == 0) break;

			char[] msg = br.readLine().toCharArray();

			int[][] swaps = new int[N][2];

			for (int i = 0; i < N; i++) {
				line = br.readLine();
				swaps[i][0] = parseInt(line.substring(0, line.indexOf(' '))) - 1; ;
				swaps[i][1] = parseInt(line.substring(line.indexOf(' ') + 1)) - 1; ;
			}

			for (int i = N - 1; i >= 0; i--) {
				int shift = swaps[i][1] - swaps[i][0];
				for (int j : swaps[i]) {
					msg[j] += shift;
					if (msg[j] > 'z') {
						msg[j] -= 'z' + 1;
						msg[j] %= 26;
						msg[j] += 'a';
					}
				}
				char tmp = msg[swaps[i][0]];
				msg[swaps[i][0]] = msg[swaps[i][1]];
				msg[swaps[i][1]] = tmp;
			}

			System.out.println(msg);
		}
	}
}